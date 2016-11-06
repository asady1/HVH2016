#
import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy

import Converters
from Converters import *

def binCalc(start,end,blindstart,blindend,binsize):
	B = []
	TB = []
	thisstart = start
	thisend = start
	while thisend < blindstart:
		thisstart = thisend
		thisend = thisend + int(binsize)
		if thisend > blindstart:
			thisend = blindstart
		B.append([thisstart,thisend])
	while thisend < blindend:
		thisstart = thisend
		thisend = thisend + int(binsize)
		if thisend > blindend:
			thisend = blindend
		TB.append([thisstart,thisend])
	while thisend < end:
		thisstart = thisend
		thisend = thisend + int(binsize)
		B.append([thisstart,thisend])
	print str(B)
	print str(TB)
	return [B, TB]

def AlphabetSlicer(plot, bins, cut, which, center): # Takes a 2D plot and measures the Pass/Fail ratios in given bins
	# plot = 2D plot to perform the measurment on
	# bins = list of bins to measure the P/F ratio in (each bin will yield a A/B point
	# cut = Value to differentiate pass from fail. Should be on the y-axis of plot
	# which = ">" or "<", to tell you which way the cut goes
	# center = the x-var is recentered about the middle of the blinded region. This tells you where. You can leave it as 0 if you want.
        x = []
        y = []
        exl = []
        eyl = []
        exh = []
        eyh = []  # ALL OF THESE ARE THE COMPONENTS OF A TGraphAsymmErrors object.
        hx = []
        hy = []
        ehx = []
        ehy = []
	print str(bins)
        for b in bins: # loop through the bins (bins are along the mass axis and should contain a gap for the sigreg)
		print str(b)
                passed = 0
                failed = 0
                for i in range(plot.GetNbinsX()):  # Get pass/failed
                        for j in range(plot.GetNbinsY()):
                                if plot.GetXaxis().GetBinCenter(i) < b[1] and plot.GetXaxis().GetBinCenter(i) > b[0]:
				    if which == ">":
                                        if plot.GetYaxis().GetBinCenter(j) < cut:
                                                failed = failed + plot.GetBinContent(i,j)
                                        else:
                                                passed = passed + plot.GetBinContent(i,j)
				    if which == "<":
                                        if plot.GetYaxis().GetBinCenter(j) > cut:
                                                failed = failed + plot.GetBinContent(i,j)
                                        else:
                                                passed = passed + plot.GetBinContent(i,j)
                if passed < 0:
                        passed = 0
                if failed < 0:
                        failed = 0
		print str(passed) + " pass"
		print str(failed) + " fail"
                ep = math.sqrt(passed)
                ef = math.sqrt(failed)
		if (float((b[0]+b[1])/2.)-center) > 100 and (failed == 0 or passed/failed < 0.02):
			print "bin not filled CONDITION 1"
	                continue
                if passed < 0.06 or failed == 0:
			print "bin not filled CONDITION 2"
	                continue
                err = (passed/(failed))*((ep/passed)+(ef/failed))
                if err > 4.:
			print "bin not filled CONDITION 3"
	                continue
                x.append((float((b[0]+b[1])/2.)-center))  # do the math in these steps (calculate error)
                exl.append(float((b[1]-b[0])/2.))
                exh.append(float((b[1]-b[0])/2.))
                y.append(passed/(failed))      # NOTE: negative bins are not corrected, if you're getting negative values your bins are too fine.
                eyh.append(err)
                if (passed/failed) - err > 0.:
                        eyl.append(err)
                else:
                        eyl.append(passed/failed)
	if len(x) > 0:
       		G = TGraphAsymmErrors(len(x), scipy.array(x), scipy.array(y), scipy.array(exl), scipy.array(exh), scipy.array
(eyl), scipy.array(eyh))
	else:
		G = TGraphAsymmErrors()
        return G  # Returns a TGAE which you can fit or plot.


def AlphabetFitter(G, F): # Linear fit to output of above function, fitting with form F
	# Want an arbitrary F: Need to provide conversion from Fit to the Error: use Converter.
	G.Fit(F.fit, F.Opt)
	fitter = TVirtualFitter.GetFitter()
	F.Converter(fitter)

def FillPlots(Alphabet, V, N, NU, ND, A, variable, binBoundaries, AT, T):
	Alphabet.MakeEstVariable(variable, binBoundaries, AT, T)
	for i in Alphabet.hists_MSR:
		V.Add(i,1.)
	for i in Alphabet.hists_EST:
		N.Add(i,1.)
	for i in Alphabet.hists_EST_UP:
		NU.Add(i,1.)
	for i in Alphabet.hists_EST_DN:
		ND.Add(i,1.)
	for i in Alphabet.hists_ATAG:
		    A.Add(i,1.)

	for bin in range(0,len(binBoundaries)-1):
		if not A.GetBinContent(bin+1) > 0.:
			A.SetBinError(bin+1, 2.0)
			A.SetBinContent(bin+1, 0.001)
			N.SetBinContent(bin+1,0.0001)
			ND.SetBinContent(bin+1,0.00001)
			NU.SetBinContent(bin+1,0.001)

	Boxes = []
	sBoxes = []
	pBoxes = []
	maxy = 0.
	Pull = V.Clone("Pull")
	Pull.Add(N, -1.)
	for i in range(1, N.GetNbinsX()+1):
		P = Pull.GetBinContent(i)
		Ve = V.GetBinError(i)
		if Ve > 1.:
			Pull.SetBinContent(i, P/Ve)
		else:
			Pull.SetBinContent(i, P/1.2)
		
		Pull.SetBinError(i, 1.)
		a = A.GetBinError(i)*N.GetBinContent(i)/A.GetBinContent(i)
		u = NU.GetBinContent(i) - N.GetBinContent(i)
		d = N.GetBinContent(i) - ND.GetBinContent(i)
		x1 = Pull.GetBinCenter(i) - (0.5*Pull.GetBinWidth(i))
		y1 = N.GetBinContent(i) - math.sqrt((d*d) + (a*a))
		s1 = N.GetBinContent(i) - a
		if y1 < 0.:
			y1 = 0
		if s1 < 0:
			s1 = 0
		x2 = Pull.GetBinCenter(i) + (0.5*Pull.GetBinWidth(i))
		y2 = N.GetBinContent(i) + math.sqrt((u*u) + (a*a))
		s2 = N.GetBinContent(i) + a
		if maxy < y2:
			maxy = y2
		if Ve > 1.:
			yP1 = -math.sqrt((d*d) + (a*a))/Ve
			yP2 = math.sqrt((u*u) + (a*a))/Ve
		else:
			yP1 = -math.sqrt((d*d) + (a*a))
			yP2 = math.sqrt((u*u) + (a*a))
		tempbox = TBox(x1,y1,x2,y2)
		temppbox = TBox(x1,yP1,x2,yP2)
		tempsbox = TBox(x1,s1,x2,s2)
		Boxes.append(tempbox)
		sBoxes.append(tempsbox)
		pBoxes.append(temppbox)
	return [Pull, maxy, Boxes, sBoxes, pBoxes]


#RooDataHist pred("pred", "Prediction from SB", RooArgList( x ), h_SR_Prediction);
#RooFitResult * r_bg=bg.fitTo(pred, RooFit::Range(SR_lo, SR_hi), RooFit::Save());
#RooPlot *aC_plot=x.frame();
#pred.plotOn(aC_plot, RooFit::MarkerColor(kPink+2));
#bg.plotOn(aC_plot, RooFit::VisualizeError(* r_bg, 1), RooFit::FillColor(kGray+1),   RooFit::FillStyle(3001));
#bg.plotOn(aC_plot, RooFit::LineColor(kBlack));
#pred.plotOn(aC_plot, RooFit::LineColor(kBlack), RooFit::MarkerColor(kBlack));
