#
import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy

# Our functions:
import Alphabet_Header
from Alphabet_Header import *
import Plotting_Header
from Plotting_Header import *
import Converters
from Converters import *
import Distribution_Header
from Distribution_Header import *
import Alphabet
from Alphabet import *

DATA = DIST("DATA", "/uscms_data/d3/osherson/Ana80X/CMSSW_8_0_2/data/JetsHT_0.root","myTree","1.")
DistsWeWantToEstiamte = [DATA]
Hbb = Alphabetizer("AnaBLIND", DistsWeWantToEstiamte, [])

presel = "jet2pmass>105&jet2pmass<135&jet2tau21<0.6&jet2bbtag>0.6&vtype==-1&triggerpassbb==1&jet2pt>200&json==1&jet1pt>200&etadiff<1.3&jet1tau21<0.6&dijetmass_corr>800&jet2ID==1&jet1ID==1"
tag = presel + "&(jet1pmass<135&jet1pmass>105)&(jet1bbtag>0.6)"
antitag = presel + "&(jet1pmass<135&jet1pmass>105)&(jet1bbtag<0.6)"

var_array = ["jet1pmass", "jet1bbtag", 60,50,200, 200, -1.1, 1.1]
Hbb.SetRegions(var_array, presel) # make the 2D plot
Hbb.TwoDPlot.SetStats(0)
C1 = TCanvas("C1", "", 800, 600)
C1.cd()
Hbb.TwoDPlot.Draw("COLZ")
Hbb.TwoDPlot.GetXaxis().SetTitle("jet mass (GeV)")
Hbb.TwoDPlot.GetYaxis().SetTitle("bb-tag")
C1.SaveAs("outputs/HHSR_2D.root")


cut = [0.6, ">"]
bins = [[50,65],[65,75],[75,90],[90,105],[135,150],[150,165],[165,185],[185,200]]
truthbins = [[105,120],[120,135]]
center = 120.
F = QuadraticFit([0.1,0.1,0.1], -75, 75, "quadfit", "EMRFNEX0")
Hbb.GetRates(cut, bins, truthbins, center, F)
leg = TLegend(0.11,0.11,0.4,0.4)
leg.SetLineColor(0)
leg.SetFillColor(4001)
leg.SetTextSize(0.03)
leg.AddEntry(Hbb.G, "events used in fit", "PLE")
#leg.AddEntry(Hbb.truthG, "signal region (blind)", "PLE")
leg.AddEntry(Hbb.Fit.fit, "fit", "L")
leg.AddEntry(Hbb.Fit.ErrUp, "fit errors", "L")
C2 = TCanvas("C2", "", 800, 800)
C2.cd()
Hbb.G.SetTitle("")
Hbb.G.Draw("AP")
Hbb.G.GetXaxis().SetTitle("m_{J} - m_{H} (GeV)")
Hbb.G.GetYaxis().SetTitle("R_{p/f}")
Hbb.G.GetYaxis().SetTitleOffset(1.3)
Hbb.truthG.SetLineColor(kBlue)
Hbb.truthG.SetLineWidth(2)
#Hbb.truthG.Draw("P same") # TURN ON FOR TRUTH BINS
Hbb.Fit.fit.Draw("same")
Hbb.Fit.ErrUp.SetLineStyle(2)
Hbb.Fit.ErrUp.Draw("same")
Hbb.Fit.ErrDn.SetLineStyle(2)
Hbb.Fit.ErrDn.Draw("same")
leg.Draw()
C2.SaveAs("outputs/HHSR_Fit.pdf")


variable = "dijetmass_corr"

binBoundaries = [800, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687,
        1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509]


Hbb.MakeEstVariable(variable, binBoundaries, antitag, tag)
FILE = TFile("HHSR.root", "RECREATE")
FILE.cd()
V = TH1F("data_obs", "", len(binBoundaries)-1, array('d',binBoundaries))
for i in Hbb.hists_MSR:
	V.Add(i,1.)
# the estimate is the sum of the histograms in self.hists_EST and self.hist_MSR_SUB
N = TH1F("EST", "", len(binBoundaries)-1, array('d',binBoundaries))
for i in Hbb.hists_EST:
	N.Add(i,1.)
# We can do the same thing for the Up and Down shapes:
NU = TH1F("EST_CMS_scale_13TeVUp", "", len(binBoundaries)-1, array('d',binBoundaries)) 
for i in Hbb.hists_EST_UP:
	NU.Add(i,1.)
ND = TH1F("EST_CMS_scale_13TeVDown", "", len(binBoundaries)-1, array('d',binBoundaries)) 
for i in Hbb.hists_EST_DN:
	ND.Add(i,1.)
A =  TH1F("EST_Antitag", "", len(binBoundaries)-1, array('d',binBoundaries)) 
for i in Hbb.hists_ATAG:
	    A.Add(i,1.)

for bin in range(0,len(binBoundaries)-1):
	if not A.GetBinContent(bin+1) > 0.:
		print A.GetBinError(bin+1)
		A.SetBinError(bin+1, 2.0)
		A.SetBinContent(bin+1, 0.001)
		N.SetBinContent(bin+1,0.0001)
		ND.SetBinContent(bin+1,0.00001)
		NU.SetBinContent(bin+1,0.001)

FILE.Write()
FILE.Save()

vartitle = "m_{X} (GeV)"

NU.SetLineColor(kBlack)
ND.SetLineColor(kBlack)
NU.SetLineStyle(2)
ND.SetLineStyle(2)
N.SetLineColor(kBlack)
N.SetFillColor(kPink+3)



V.SetStats(0)
V.Sumw2()
V.SetLineColor(1)
V.SetFillColor(0)
V.SetMarkerColor(1)
V.SetMarkerStyle(20)
N.GetYaxis().SetTitle("events")
N.GetXaxis().SetTitle(vartitle)

FindAndSetMax([V,N, NU, ND])
Pull = V.Clone("Pull")
Pull.Add(N, -1.)

Boxes = []
sBoxes = []
pBoxes = []
maxy = 0.
for i in range(1, N.GetNbinsX()+1):
	P = Pull.GetBinContent(i)
	Ve = V.GetBinError(i)
	if Ve > 1.:
		Pull.SetBinContent(i, P/Ve)
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

Pull.GetXaxis().SetTitle("")
Pull.SetStats(0)
Pull.SetLineColor(1)
Pull.SetFillColor(0)
Pull.SetMarkerColor(1)
Pull.SetMarkerStyle(20)
Pull.GetXaxis().SetNdivisions(0)
Pull.GetYaxis().SetNdivisions(4)
Pull.GetYaxis().SetTitle("#frac{Data - Bkg}{#sigma_{data}}")
Pull.GetYaxis().SetLabelSize(85/15*Pull.GetYaxis().GetLabelSize())
Pull.GetYaxis().SetTitleSize(4.2*Pull.GetYaxis().GetTitleSize())
Pull.GetYaxis().SetTitleOffset(0.175)
Pull.GetYaxis().SetRangeUser(-3.,3.)

for i in Boxes:
	i.SetFillColor(12)
	i.SetFillStyle(3244)
for i in pBoxes:
	i.SetFillColor(12)
	i.SetFillStyle(3144)
for i in sBoxes:
	i.SetFillColor(38)
	i.SetFillStyle(3002)

leg2 = TLegend(0.6,0.6,0.89,0.89)
leg2.SetLineColor(0)
leg2.SetFillColor(0)
leg2.AddEntry(V, "Data", "PL")
leg2.AddEntry(N, "background prediction", "F")
leg2.AddEntry(Boxes[0], "total uncertainty", "F")
leg2.AddEntry(sBoxes[0], "background statistical component", "F")


T0 = TLine(800,0.,4509,0.)
T0.SetLineColor(kBlue)
T2 = TLine(800,2.,4509,2.)
T2.SetLineColor(kBlue)
T2.SetLineStyle(2)
Tm2 = TLine(800,-2.,4509,-2.)
Tm2.SetLineColor(kBlue)
Tm2.SetLineStyle(2)

T1 = TLine(800,1.,4509,1.)
T1.SetLineColor(kBlue)
T1.SetLineStyle(3)
Tm1 = TLine(800,-1.,4509,-1.)
Tm1.SetLineColor(kBlue)
Tm1.SetLineStyle(3)

C4 = TCanvas("C4", "", 800, 800)
#draw the lumi text on the canvas

plot = TPad("pad1", "The pad 80% of the height",0,0.15,1,1)
pull = TPad("pad2", "The pad 20% of the height",0,0,1.0,0.15)
plot.Draw()
pull.Draw()
plot.cd()
N.Draw("Hist")
#V.Draw("same E0")
for i in Boxes:
	i.Draw("same")
for i in sBoxes:
	i.Draw("same")
leg2.Draw()
pull.cd()
#Pull.Draw("")
for i in pBoxes:
	i.Draw("same")
T0.Draw("same")
T2.Draw("same")
Tm2.Draw("same")
T1.Draw("same")
Tm1.Draw("same")
Pull.Draw("same")
C4.SaveAs("outputs/HHSR_Plot.pdf")

print str(N.Integral())
print str(V.Integral())
