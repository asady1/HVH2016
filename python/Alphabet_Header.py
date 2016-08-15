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


#RooDataHist pred("pred", "Prediction from SB", RooArgList( x ), h_SR_Prediction);
#RooFitResult * r_bg=bg.fitTo(pred, RooFit::Range(SR_lo, SR_hi), RooFit::Save());
#RooPlot *aC_plot=x.frame();
#pred.plotOn(aC_plot, RooFit::MarkerColor(kPink+2));
#bg.plotOn(aC_plot, RooFit::VisualizeError(* r_bg, 1), RooFit::FillColor(kGray+1),   RooFit::FillStyle(3001));
#bg.plotOn(aC_plot, RooFit::LineColor(kBlack));
#pred.plotOn(aC_plot, RooFit::LineColor(kBlack), RooFit::MarkerColor(kBlack));
