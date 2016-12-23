import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy
import pdb

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

def GetNom(file_string):
	tempFile = TFile(file_string)
	tempHist = tempFile.Get("CountWeighted")
	norm = tempHist.GetBinContent(1)
	tempFile.Close()
	return norm

from optparse import OptionParser
parser = OptionParser()

parser.add_option('--B', '--binsize', metavar='Bin', type='string', dest='bin', default="15")

parser.add_option('--T2', '--Selection', metavar='T32', type='string', dest='pre')
parser.add_option('--T1', '--Cut', metavar='T13', type='float', dest='cut', default = 0.8)

parser.add_option('--N', '--name', metavar='Name', type='string', dest='name', default="test")
parser.add_option('--L', '--lumi', metavar='Name', type='float', dest='lumi', default="27200")

parser.add_option("--data", action="store_true", dest="isData", default=True)
parser.add_option("--qcd", action="store_false", dest="isData")

parser.add_option("--quad", action="store_false", dest="Linear", default=False)
parser.add_option("--lin", action="store_true", dest="Linear")

parser.add_option("--blind", action="store_false", dest="Truth", default=True)
parser.add_option("--unblind", action="store_true", dest="Truth")

parser.add_option("--finebins", action="store_false", dest="finebins", default=False)
parser.add_option("--dijetbins", action="store_true", dest="finebins")

parser.add_option("--log", action="store_true", dest="log", default=False)
parser.add_option("--nolog", action="store_false", dest="log")

parser.add_option("--sig", action="store_true", dest="Sig", default=False)
parser.add_option("--nosig", action="store_false", dest="Sig")

parser.add_option('-I', '--inject', metavar='Inj', type='string', dest='inject', default="none")

parser.add_option('--workspace', metavar='WSPC', type='string', dest='workspace', default="alphabet")
(Options, args) = parser.parse_args()

presel    =   Options.pre
tag = presel + "&(fatjet_mass<135&fatjet_mass>105)&(fatjet_hbb>"+str(Options.cut)+")"
atag = presel + "&(fatjet_mass<135&fatjet_mass>105)&(fatjet_hbb<"+str(Options.cut)+")"

if Options.finebins:
	binBoundaries=[]
	for i in range(0,1700):	
		binBoundaries.append(450+i*1)
else:
	binBoundaries =[450, 499, 548, 596, 644, 692, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132]
#	binBoundaries = [450, 500, 550,  600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1880, 1960, 2040, 2120]
#	binBoundaries =[450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150]

variable = "Inv_mass"

############# DATASETS: #################
QCD1 = DIST("DATA1", "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/QCDHH/QCD_300to500_pruned_cmva.root","mynewTree",str(Options.lumi)+"*347700./16762990")
QCD2 = DIST("DATA2", "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/QCDHH/QCD_500to700_pruned_cmva.root","mynewTree",str(Options.lumi)+"*32100./19199090")
QCD3 = DIST("DATA2", "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/QCDHH/QCD_700to1000_pruned_cmva.root","mynewTree",str(Options.lumi)+"*6831./15621630")
QCD4 = DIST("DATA3", "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/QCDHH/QCD_1000to1500_pruned_cmva.root","mynewTree",str(Options.lumi)+"*1207./4980387")
QCD5 = DIST("DATA5", "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/QCDHH/QCD_1500to2000_pruned_cmva.root","mynewTree",str(Options.lumi)+"*119.9/3754452")
QCD6 = DIST("DATA6", "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/QCDHH/QCD_2000toInf_pruned_cmva.root","mynewTree",str(Options.lumi)+"*25.24/1960245")
#TTBar = DIST("TTBar", "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/TT_SFs.root", "mynewTree", "(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)*"+str(Options.lumi)+"*831.76/75176620")
TTBar = DIST("TTBar", "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/TT_CSV.root", "mynewTree", "(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)*2.71828^(0.0615-0.0005*ttHT/2)*"+str(Options.lumi)+"*831.76/75176620")
JetHT = DIST("JetHT", "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/JetHT_CSV.root","mynewTree", "(HLT2_HT800>0)")
BTag = DIST("BTag","/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/BTag_CSV.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")

if Options.isData:
	DistsWeWantToEstimate = [JetHT,BTag]
	whichdataorQCD = "Data"
else:
	DistsWeWantToEstimate = [QCD1,QCD2,QCD3,QCD4,QCD5,QCD6]
	whichdataorQCD = "QCD"

sigpath = "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/input/"
#if Options.inject != "none":
#	normI = GetNom(sigpath+"Wprime"+Options.inject+".root")
#	INJ = DIST("INJ", sigpath+"Wprime"+Options.inject+".root","mynewTree",str(Options.lumi)+"*0.01*puWeights*SF/"+str(normI))
#	whichdataorQCD = "QCD w/ Injected Signal"
#	DistsWeWantToEstimate.append(INJ)
#### SOME SIGNALS WE'LL USE:
#norm0= GetNom(sigpath+"tree_500.root")
#norm1 = GetNom(sigpath+"tree_550.root")
#norm2 = GetNom(sigpath+"tree_600.root")
#norm3 = GetNom(sigpath+"tree_650.root")
#norm4 = GetNom(sigpath+"tree_700.root")
#norm5 = GetNom(sigpath+"tree_750.root")
#norm6 = GetNom(sigpath+"tree_800.root")
#norm7 = GetNom(sigpath+"tree_900.root")
#norm8 = GetNom(sigpath+"tree_1000.root")
#norm9 = GetNom(sigpath+"tree_1200.root")
#norm10 = GetNom(sigpath+"tree_1400.root")
#norm11 = GetNom(sigpath+"tree_1600.root")
#norm12 = GetNom(sigpath+"tree_1800.root")
#norm13 = GetNom(sigpath+"tree_2000.root")
norm0 = 46000.
norm1 = 100000.
norm2 = 98000.
norm3 = 100000.
norm4 = 100000.
norm5 = 95600.
norm6 = 95800.
norm7 = 2000.
norm8 = 50000.
norm9 = 50000.
norm10 = 50000.
norm11 = 50000.
norm12 = 50000.
norm13 = 50000.

SIG0 = TH1F("Signal_500", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG1 = TH1F("Signal_550", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG2 = TH1F("Signal_600", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG3 = TH1F("Signal_650", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG4 = TH1F("Signal_700", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG5 = TH1F("Signal_750", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG6 = TH1F("Signal_800", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG7 = TH1F("Signal_900", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG8 = TH1F("Signal_1000", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG9 = TH1F("Signal_1200", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG10 = TH1F("Signal_1400", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG11 = TH1F("Signal_1600", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG12 = TH1F("Signal_1800", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG13 = TH1F("Signal_2000", "", len(binBoundaries)-1, array('d',binBoundaries))

quickplot(sigpath+"tree_500.root", "mynewTree", SIG0, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_550.root", "mynewTree", SIG1, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_600.root", "mynewTree", SIG2, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_650.root", "mynewTree", SIG3, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_700.root", "mynewTree", SIG4, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_750.root", "mynewTree", SIG5, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_800.root", "mynewTree", SIG6, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_900.root", "mynewTree", SIG7, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_1000.root", "mynewTree", SIG8, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_1200.root", "mynewTree", SIG9, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_1400.root", "mynewTree", SIG10, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_1600.root", "mynewTree", SIG11, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_1800.root", "mynewTree", SIG12, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")
quickplot(sigpath+"tree_2000.root", "mynewTree", SIG13, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "1.")

SIG0.Scale(Options.lumi*0.01/norm0)
SIG1.Scale(Options.lumi*0.01/norm1)
SIG2.Scale(Options.lumi*0.01/norm2)
SIG3.Scale(Options.lumi*0.01/norm3)
SIG4.Scale(Options.lumi*0.01/norm4)
SIG5.Scale(Options.lumi*0.01/norm5)
SIG6.Scale(Options.lumi*0.01/norm6)
SIG7.Scale(Options.lumi*0.01/norm7)
SIG8.Scale(Options.lumi*0.01/norm8)
SIG9.Scale(Options.lumi*0.01/norm9)
SIG10.Scale(Options.lumi*0.01/norm10)
SIG11.Scale(Options.lumi*0.01/norm11)
SIG12.Scale(Options.lumi*0.01/norm12)
SIG13.Scale(Options.lumi*0.01/norm13)

SIG0.SetLineColor(kMagenta - 9)
SIG1.SetLineColor(kMagenta - 6)
SIG2.SetLineColor(kMagenta - 3)
SIG3.SetLineColor(kMagenta)
SIG4.SetLineColor(kPink + 8) 
SIG5.SetLineColor(kPink + 7)
SIG6.SetLineColor(kPink + 3)
SIG7.SetLineColor(kPink - 6)
SIG8.SetLineColor(kPink - 4)
SIG9.SetLineColor(kRed - 7)
SIG10.SetLineColor(kRed - 3)
SIG11.SetLineColor(kRed)
SIG12.SetLineColor(kRed + 2)
SIG13.SetLineColor(kRed + 3)

var_array = ["fatjet_mass", "fatjet_hbb", 60,50,200, 100, -1., 1.]
#var_array = ["jet1pmass", "jet1bbtag", 60,50,200, 100, -1., 1.]

Hbb = Alphabetizer(Options.name, DistsWeWantToEstimate, [TTBar])
Hbb.SetRegions(var_array, presel)

bins = binCalc(50,200,105,135,Options.bin)
if Options.Linear:
	F = LinearFit([0.0,0.0], -75, 85, "linfit", "EMRNSQ")
else:
	print "quad"
	F = QuadraticFit([0.1,0.1,0.1], -75, 75, "quadfit", "EMRFNEX0")
Hbb.TwoDPlot.Draw("COLZ")
Hbb.GetRates([Options.cut, ">"], bins[0], bins[1], 120., F)
print bins[0]
print bins[1]
#Hbb.TwoDPlot.Draw("COLZ")

Hbb.TwoDPlot.SetStats(0)
C1 = TCanvas("C1", "", 800, 600)
C1.cd()
Hbb.TwoDPlot.Draw("COLZ")
Hbb.TwoDPlot.GetXaxis().SetTitle("jet mass (GeV)")
Hbb.TwoDPlot.GetYaxis().SetTitle("bb-tag")
C1.SaveAs("outputs/VHSR_2D_"+Options.name+".pdf")

leg = TLegend(0.65,0.65,0.89,0.89)
leg.SetLineColor(0)
leg.SetFillColor(4001)
leg.SetTextSize(0.03)
leg.AddEntry(Hbb.G, "events used in fit", "PLE")
if Options.Truth:
	leg.AddEntry(Hbb.truthG, "signal region (blind)", "PLE")
leg.AddEntry(Hbb.Fit.fit, "fit", "L")
leg.AddEntry(Hbb.Fit.ErrUp, "fit errors", "L")
plotforplotting = TH1F("empty_"+Options.name, "", 24, -75, 75)
plotforplotting.SetStats(0)
plotforplotting.GetYaxis().SetRangeUser(-0.1,0.1)
plotforplotting.GetXaxis().SetTitle("m_{J} - m_{H} (GeV)")
plotforplotting.GetYaxis().SetTitle("R_{p/f}")
plotforplotting.GetYaxis().SetTitleOffset(1.5)

C2 = TCanvas("C2", "", 800, 600)
C2.cd()
Hbb.G.SetTitle("")
plotforplotting.Draw()
Hbb.G.Draw("P same")
Hbb.truthG.SetLineColor(kBlue)
Hbb.truthG.SetLineWidth(2)
if Options.Truth:
	Hbb.truthG.Draw("P same") # TURN ON FOR TRUTH BINS
Hbb.Fit.fit.Draw("same")
Hbb.Fit.ErrUp.SetLineStyle(2)
Hbb.Fit.ErrUp.Draw("same")
Hbb.Fit.ErrDn.SetLineStyle(2)
Hbb.Fit.ErrDn.Draw("same")
leg.Draw()
C2.SaveAs("outputs/VHSR_Fit_"+Options.name+".pdf")


D = TH1F("data", "", len(binBoundaries)-1, array('d',binBoundaries))
N = TH1F("est", "", len(binBoundaries)-1, array('d',binBoundaries))
TTNom = TH1F("TT", "", len(binBoundaries)-1, array('d',binBoundaries))
NU = TH1F("est_up", "", len(binBoundaries)-1, array('d',binBoundaries)) 
ND = TH1F("est_down", "", len(binBoundaries)-1, array('d',binBoundaries))
A =  TH1F("antitag", "", len(binBoundaries)-1, array('d',binBoundaries)) 

PULL = FillPlots(Hbb, D, N, NU, ND, A, variable, binBoundaries, atag, tag, 1., TTNom)

print "D info"
D.Print("all")
print "N info"
N.Print("all")
print "NU info"
NU.Print("all")
print "ND info"
ND.Print("all")
print "A info"
A.Print("all")

C3 = TCanvas("C3", "", 800, 600)
N.Draw()
C5 = TCanvas("C5", "", 800, 600)
A.Draw()
C6 = TCanvas("C6", "", 800, 600)
NU.Draw()
C7 = TCanvas("C7", "", 800, 600)
ND.Draw()

Pull = PULL[0]
C8 = TCanvas("C8", "", 800, 600)
Pull.Draw()
maxy = PULL[1]
Boxes = PULL[2]
sBoxes = PULL[3]
pBoxes = PULL[4]

print "MAXY " + str(maxy)

vartitle = "m_{X} (GeV)"

NU.SetLineColor(kBlack)
ND.SetLineColor(kBlack)
NU.SetLineStyle(2)
ND.SetLineStyle(2)
N.SetLineColor(kBlack)
N.SetFillColor(kAzure+10)
TTNom.SetLineColor(kRed+2)
TTNom.SetFillColor(kRed+2)

D.SetStats(0)
D.Sumw2()
D.SetLineColor(1)
D.SetFillColor(0)
D.SetMarkerColor(1)
D.SetMarkerStyle(20)
N.GetYaxis().SetTitle("events")
N.GetXaxis().SetTitle(vartitle)

if Options.log:
#        N.GetYaxis().SetRangeUser(0.05,maxy*1.5)
	N.GetYaxis().SetRangeUser(0.01,maxy*1.5)
else:
	N.GetYaxis().SetRangeUser(0.,maxy*1.2)

Pull.GetXaxis().SetTitle("")
Pull.SetStats(0)
Pull.SetLineColor(1)
Pull.SetFillColor(0)
if Options.Truth:
	Pull.SetMarkerColor(1)
	Pull.SetLineColor(1)
else:
	Pull.SetMarkerColor(0)
	Pull.SetLineColor(0)
Pull.SetMarkerStyle(20)
Pull.GetXaxis().SetNdivisions(0)
Pull.GetYaxis().SetNdivisions(4)
Pull.GetYaxis().SetTitle("#frac{Data - Bkg}{#sigma_{data}}")
Pull.GetYaxis().SetLabelSize(85/15*Pull.GetYaxis().GetLabelSize())
Pull.GetYaxis().SetTitleSize(4.2*Pull.GetYaxis().GetTitleSize())
Pull.GetYaxis().SetTitleOffset(0.175)
Pull.GetYaxis().SetRangeUser(-3.,3.)

SIG6.SetFillColor(kPink+3)
SIG6.SetFillStyle(3244)
SIG8.SetFillColor(kPink-4)
SIG8.SetFillStyle(3244)
SIG2.SetFillColor(kMagenta-3)
SIG2.SetFillStyle(3244)

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
leg2.AddEntry(D, whichdataorQCD, "PL")
leg2.AddEntry(N, "background prediction", "F")
leg2.AddEntry(Boxes[0], "total uncertainty", "F")
leg2.AddEntry(sBoxes[0], "background statistical component", "F")
leg2.AddEntry(TTNom, "ttbar", "F")
if Options.Sig:
	leg2.AddEntry(SIG2, "Bulk Grav (600 GeV, 27 fb)", "F")
	leg2.AddEntry(SIG6, "Bulk Grav (800 GeV, 27 fb)", "F")
	leg2.AddEntry(SIG8, "Bulk Grav (1000 GeV, 27 fb)", "F")

T0 = TLine(450,0.,2120,0.)
T0.SetLineColor(kBlue)
T2 = TLine(450,2.,2120,2.)
T2.SetLineColor(kBlue)
T2.SetLineStyle(2)
Tm2 = TLine(450,-2.,2120,-2.)
Tm2.SetLineColor(kBlue)
Tm2.SetLineStyle(2)
T1 = TLine(450,1.,2120,1.)
T1.SetLineColor(kBlue)
T1.SetLineStyle(3)
Tm1 = TLine(450,-1.,2120,-1.)
Tm1.SetLineColor(kBlue)
Tm1.SetLineStyle(3)

N.SetStats(0)

C4 = TCanvas("C4", "", 800, 600)
plot = TPad("pad1", "The pad 80% of the height",0,0.15,1,1)
pull = TPad("pad2", "The pad 20% of the height",0,0,1.0,0.15)
plot.Draw()
if Options.Truth:
	pull.Draw()
plot.cd()
N.Draw("Hist")
TTNom.Draw("same Hist")
if Options.Truth:
	D.Draw("same E0")
for i in Boxes:
	i.Draw("same")
for i in sBoxes:
	i.Draw("same")
if Options.Sig:
	SIG2.Draw("same hist")
	SIG6.Draw("same hist")
	SIG8.Draw("same hist")
#N.Draw("Hist same")
if Options.log:
	plot.SetLogy()
leg2.Draw()
pull.cd()
Pull.Draw("")
for i in pBoxes:
	i.Draw("same")
if not Options.finebins:
	T0.Draw("same")
	T2.Draw("same")
	Tm2.Draw("same")
	T1.Draw("same")
	Tm1.Draw("same")
	Pull.Draw("same")
C4.SaveAs("outputs/VH_Plot_"+Options.name+".pdf")

if Options.workspace == "alphabet":
	print "creating workspace and datacard: ALPHABET"

	mass=[500,550,600,650,700,750,800,900,1000,1200,1400,1600,1800,2000]
	i = 0
	signorm = [46000., 100000., 98000., 100000., 100000., 95600., 95800., 2000., 50000., 50000., 50000., 50000., 50000., 50000.]
	for m in mass:
		print str(m)
	        UD = ['Up','Down']

		output_file = TFile("outputs/datacards/VH_mX_%s_"%(m)+Options.name+"_13TeV.root", "RECREATE")
		vh=output_file.mkdir("vh")
		vh.cd()

#missing CMVA SF
		Signal_mX = TH1F("Signal_mX_%s_"%(m)+Options.name, "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_csv_up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_csvUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_csv_down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_csvDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_btag_up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_btagUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_btag_down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_btagDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_pu_up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_puUp", "", len(binBoundaries)-1, array('d',binBoundaries))
	 	Signal_mX_pu_down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_puDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_FJEC_Up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_JECUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_FJEC_Down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_JECDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_FJER_Up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_JERUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_FJER_Down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_JERDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_MJEC_Up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_massJECUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_MJEC_Down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_massJECDown", "", len(binBoundaries)-1, array('d',binBoundaries))

		quickplot(sigpath+"tree_%s.root"%(m), "mynewTree", Signal_mX, variable, tag+ "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "puWeight*SF*csvLSF*csvLSF2/1.")
		quickplot(sigpath+"tree_%s.root"%(m), "mynewTree", Signal_mX_btag_up, variable, tag +"&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "puWeight*SFup*csvLSF*csvLSF2/1.")
		quickplot(sigpath+"tree_%s.root"%(m), "mynewTree", Signal_mX_btag_down, variable, tag+ "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "puWeight*SFdown*csvLSF*csvLSF2/1.")
		quickplot(sigpath+"tree_%s.root"%(m), "mynewTree", Signal_mX_csv_up, variable, tag+ "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "puWeight*SF*csvLSFup*csvLSFup2/1.")
		quickplot(sigpath+"tree_%s.root"%(m), "mynewTree", Signal_mX_csv_down, variable, tag+ "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "puWeight*SF*csvLSFdown*csvLSFdown2/1.")
		quickplot(sigpath+"tree_%s.root"%(m), "mynewTree", Signal_mX_pu_up, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "puWeightUp*SF*csvLSF*csvLSF2/1.")
		quickplot(sigpath+"tree_%s.root"%(m), "mynewTree", Signal_mX_pu_down, variable, tag + "&(HLT2_HT800>0||HLT2_Quad_Triple>0||HLT2_Double_Triple>0)", "puWeightDown*SF*csvLSF*csvLSF2/1.")

#		norm = GetNom(sigpath+"tree_%s.root"%(m))
		norm = signorm[i]
		i += 1
		btaglnN= 1.+ abs(Signal_mX_btag_up.GetSumOfWeights()-Signal_mX_btag_down.GetSumOfWeights())/(2.*Signal_mX_btag_up.GetSumOfWeights())
		csvlnN= 1. +  abs(Signal_mX_csv_up.GetSumOfWeights()-Signal_mX_csv_down.GetSumOfWeights())/(2.*Signal_mX_csv_up.GetSumOfWeights())
		PUlnN= 1.+ abs(Signal_mX_pu_up.GetSumOfWeights()-Signal_mX_pu_down.GetSumOfWeights())/(2.*Signal_mX.GetSumOfWeights())

		Signal_mX.Scale(Options.lumi*0.01/norm)
		Signal_mX_btag_up.Scale(Options.lumi*0.01/norm)
		Signal_mX_btag_down.Scale(Options.lumi*0.01/norm)
		Signal_mX_csv_up.Scale(0.01*Options.lumi/norm)
		Signal_mX_csv_down.Scale(0.01*Options.lumi/norm)
		Signal_mX_pu_up.Scale(Options.lumi*0.01/norm)
		Signal_mX_pu_down.Scale(Options.lumi*0.01/norm)


		MJEClnN= 1.02 ## add variation from ntuples
		FJEClnN= 1.02
		FJERlnN= 1.02

		signal_integral = Signal_mX.Integral()

		qcd_integral = N.Integral()
		qcd = N.Clone(Options.name+"EST")
		qcd_antitag = A.Clone(Options.name+"EST_Antitag")
		qcd_up = NU.Clone(Options.name+"EST_CMS_scale"+Options.name+"_13TeVUp")
		qcd_down = ND.Clone(Options.name+"EST_CMS_scale"+Options.name+"_13TeVDown")
		data_obs = D.Clone("data_obs")
		data_integral = data_obs.Integral() 
	
		for bin in range(0,len(binBoundaries)-1):
		    for Q in UD:
		        qcd_syst =TH1F("%s_bin%s%s"%(Options.name+"EST_CMS_stat"+Options.name+"_13TeV",bin,Q),"",len(binBoundaries)-1, array('d',binBoundaries))
	 		bin_stat = qcd.GetBinContent(bin+1)
			for bin1 in range(0,len(binBoundaries)-1):
				bin_stat1 = qcd.GetBinContent(bin1+1)
				qcd_syst.SetBinContent(bin1+1,bin_stat1)
			#if bin_stat==0 :	
			#	bin_stat = 1.5
			bin_at = qcd_antitag.GetBinContent(bin+1)
			if bin_at < 1 and bin_at >0:  
				bin_at=1.
		        if Q == 'Up':
				if bin_at >0 :
		                       qcd_syst.SetBinContent(bin+1,bin_stat+qcd_antitag.GetBinError(bin+1)/bin_at*bin_stat)
				else : 
					qcd_syst.SetBinContent(bin+1,bin_stat)
				
		        if Q == 'Down':
				if bin_at >0 :
					if ( bin_stat-qcd_antitag.GetBinError(bin+1)/bin_at*bin_stat >0 ):
		                		qcd_syst.SetBinContent(bin+1,bin_stat-qcd_antitag.GetBinError(bin+1)/bin_at*bin_stat)
					else :
						qcd_syst.SetBinContent(bin+1, 0.1)
				else : 	
					qcd_syst.SetBinContent(bin+1,bin_stat)
			output_file.cd()
			vh.cd()
			qcd_syst.Write()
		

		#qcd_trigger_up.Write()
		#qcd_trigger_low.Write()
		qcd.Write()
		qcd_up.Write()
		qcd_down.Write()
		Signal_mX.Write()
		Signal_mX_btag_up.Write()
		Signal_mX_btag_down.Write()
		Signal_mX_csv_up.Write()
		Signal_mX_csv_down.Write()
		data_obs.Write()
		vh.Write()
		output_file.Write()
		output_file.Close()

		text_file = open("outputs/datacards/VH_mX_%s_"%(m)+Options.name+"_13TeV.txt", "w")


		text_file.write("max    1     number of categories\n")
		text_file.write("jmax   1     number of samples minus one\n")
		text_file.write("kmax    *     number of nuisance parameters\n")
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("shapes * * VH_mX_%s_"%(m)+Options.name+"_13TeV.root vh/$PROCESS vh/$PROCESS_$SYSTEMATIC\n")
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("bin                                            vh4b\n")
		text_file.write("observation                                    %f\n"%(data_integral))
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("bin                                             vh4b            vh4b\n")
		text_file.write("process                                          0      1\n")
		text_file.write("process                                         Signal_mX_%s_"%(m)+Options.name+"  "+Options.name+"EST\n")
		text_file.write("rate                                            %f  %f\n"%(signal_integral,qcd_integral))
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("lumi_13TeV lnN                          1.027       -\n")	
	
#		text_file.write("CMS_eff_tau21_sf lnN                    1.027       -\n") #(0.028/0.979)
		#text_file.write("CMS_eff_Htag_sf lnN                    1.1       -\n")   
		text_file.write("CMS_JEC lnN 		     %f        -\n"%(FJEClnN)) 	
		text_file.write("CMS_massJEC lnN                 %f        -\n"%(MJEClnN))
		text_file.write("CMS_eff_bbtag_sf lnN                    %f       -\n"%(btaglnN))
		text_file.write("CMS_eff_csv_sf lnN                    %f       -\n"%(csvlnN))
		text_file.write("CMS_JER lnN                    %f        -\n"%(FJERlnN))
		text_file.write("CMS_PU lnN                    %f        -\n"%(PUlnN))
#		text_file.write("CMS_eff_trig shapeN2           1.0   -\n")
	 	
		text_file.write("CMS_scale"+Options.name+"_13TeV shapeN2                           -       1.000\n")
		text_file.write("CMS_PDF_Scales lnN   1.02 -       \n")

		for bin in range(0,len(binBoundaries)-1):
			text_file.write("CMS_stat"+Options.name+"_13TeV_bin%s shapeN2                           -       1.000\n"%(bin))


		text_file.close()

if Options.workspace == "fit":
	print "creating workspace and datacard: ALPHABET ASSISTED FIT"








