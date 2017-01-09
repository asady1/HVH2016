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

parser.add_option('--T2', '--Selection', metavar='T32', type='string', dest='tightpre', default = "jet2_puppi_msoftdrop_raw > 105 & jet2_puppi_msoftdrop_raw < 135 & jet2bbtag > 0.3 & (!(jet2bbtag > 0.8 & jet1bbtag > 0.8))")
parser.add_option('--T1', '--Cut', metavar='T13', type='float', dest='tightcut', default = 0.3)

parser.add_option('--N', '--name', metavar='Name', type='string', dest='name', default="test")
parser.add_option('--L', '--lumi', metavar='Name', type='float', dest='lumi', default="27000")

parser.add_option("--data", action="store_true", dest="isData", default=True)
parser.add_option("--qcd", action="store_false", dest="isData")

parser.add_option("--quad", action="store_false", dest="Linear", default=False)
parser.add_option("--lin", action="store_true", dest="Linear")

parser.add_option("--blind", action="store_false", dest="Truth", default=False)
parser.add_option("--unblind", action="store_true", dest="Truth")

parser.add_option("--finebins", action="store_false", dest="finebins", default=True)
parser.add_option("--dijetbins", action="store_true", dest="finsbines")

parser.add_option("--log", action="store_true", dest="log", default=False)
parser.add_option("--nolog", action="store_false", dest="log")

parser.add_option("--sig", action="store_true", dest="Sig", default=True)
parser.add_option("--nosig", action="store_false", dest="Sig")

parser.add_option('-I', '--inject', metavar='Inj', type='string', dest='inject', default="none")

parser.add_option('--workspace', metavar='WSPC', type='string', dest='workspace', default="alphabet")
(Options, args) = parser.parse_args()

preselection    =       "&(vtype==-1||vtype==4)&jet2pt>300&json==1&jet1pt>300&abs(jet1eta-jet2eta)<1.3&jet1_puppi_tau21<0.6&jet2_puppi_tau21<0.6&dijetmass_softdrop_corr>750&jet2ID==1&jet1ID==1&abs(jet1eta)<2.4&abs(jet2eta)<2.4"
#preselection	= 	"&vtype==-1&jet2pt>250&json==1&jet1pt>250&etadiff<1.3&jet1tau21<0.6&dijetmass_corr>800&jet2ID==1&jet1ID==1&abs(jet1eta)<2.4&abs(jet2eta)<2.4&HLT_PFHT800_v==1"
TightPre 		=	Options.tightpre + preselection
TightAT                 =       TightPre + "&jet1_puppi_msoftdrop_raw_TheaCorr>105&jet1_puppi_msoftdrop_raw_TheaCorr<135&(jet1bbtag<"+str(Options.tightcut)+")"
#TightAT 		=	TightPre + "&jet1pmass>105&jet1pmass<135&(jet1bbtag<"+str(Options.tightcut)+")"
TightT          =       TightPre + "&jet1_puppi_msoftdrop_raw_TheaCorr>105&jet1_puppi_msoftdrop_raw_TheaCorr<135&(jet1bbtag>"+str(Options.tightcut)+")"
#TightT 		=	TightPre + "&jet1pmass>105&jet1pmass<135&(jet1bbtag>"+str(Options.tightcut)+")"
TightT2         = "jet2bbtag > 0.8 & jet2_puppi_msoftdrop_raw*jet2_puppi_TheaCorr > 105 & jet2_puppi_msoftdrop_raw*jet2_puppi_TheaCorr < 135  &(vtype==-1||vtype==4)&jet2pt>250&json==1&jet1pt>250&abs(jet1eta-jet2eta)<1.3&jet1_puppi_tau21<0.6&jet2_puppi_tau21<0.6&dijetmass_softdrop_corr>750&jet2ID==1&jet1ID==1&abs(jet1eta)<2.4&abs(jet2eta)<2.4&jet1_puppi_msoftdrop_raw*jet1_puppi_TheaCorr>105&jet1_puppi_msoftdrop_raw*jet1_puppi_TheaCorr<135&(jet1bbtag>0.8)&(HLT_PFHT800_v==1||HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v==1||HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v==1||HLT_AK8PFJet360_V==1||HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v==1)"
#TightT2         = "jet2bbtag > 0.3 & jet2_puppi_msoftdrop_raw*jet2_puppi_TheaCorr > 110 & jet2_puppi_msoftdrop_raw*jet2_puppi_TheaCorr < 140  & (!( jet1bbtag > 0.8 & jet2bbtag > 0.8))&(vtype==-1||vtype==4)&jet2_puppi_pt>200&json==1&jet1_puppi_pt>200&abs(jet1_puppi_eta-jet2_puppi_eta)<1.3&jet1_puppi_tau21<0.6&dijetmass_TLpuppi_SubsoftdropTheaCorr>800&jet2ID==1&jet1ID==1&abs(jet1_puppi_eta)<2.4&abs(jet2_puppi_eta)<2.4&jet1_puppi_msoftdrop_raw*jet1_puppi_TheaCorr>110&jet1_puppi_msoftdrop_raw*jet1_puppi_TheaCorr<140&(jet1bbtag>0.3)"


Options.finebins = True
if Options.finebins:
	binBoundaries=[]
	for i in range(0,1300):	
		binBoundaries.append(1200+i*1)
	print (" 1 GeV bins ...")
	
else:
	binBoundaries =[800, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4681, 4853, 5025]

variable = "dijetmass_softdrop_corr"
variable2 = "dijetmass_softdrop_corr"
#variable = "dijetmass_corr"

############# DATASETS: #################
QCD1 = DIST("DATA1", "/eos/uscms/store/user/mkrohn/HHHHTo4b/V24b/MCvsData/QCD_HT500To700.root","mynewTree",str(Options.lumi)+"*31630./16563300.")
QCD2 = DIST("DATA2", "/eos/uscms/store/user/mkrohn/HHHHTo4b/V24b/MCvsData/QCD_HT700To1000.root","mynewTree",str(Options.lumi)+"*6802./10206600.")
QCD3 = DIST("DATA3", "/eos/uscms/store/user/mkrohn/HHHHTo4b/V24b/MCvsData/QCD_HT1000To1500.root","mynewTree",str(Options.lumi)+"*1206./3407530.")
QCD4 = DIST("DATA4", "/eos/uscms/store/user/mkrohn/HHHHTo4b/V24b/MCvsData/QCD_HT1500To2000.root","mynewTree",str(Options.lumi)+"*120.4/3161430.")
QCD5 = DIST("DATA5", "/eos/uscms/store/user/mkrohn/HHHHTo4b/V24b/MCvsData/QCD_HT2000ToInf.root","mynewTree",str(Options.lumi)+"*25.25/3234700.")
DATA = DIST("DATA", "/uscms_data/d3/mkrohn/CMSSW_8_0_12/src/HH2016/SlimMiniTrees/JetHT.root","mynewTree","1.")
#DATA = DIST("DATA", "/eos/uscms/store/user/mkrohn/HHHHTo4b/V24/JetHT.root","myTree","1.")
if Options.isData:
	DistsWeWantToEstimate = [DATA]
	whichdataorQCD = "Data"
else:
	DistsWeWantToEstimate = [QCD1,QCD2,QCD3,QCD4,QCD5]
	whichdataorQCD = "QCD"

sigpath = "/uscms_data/d3/mkrohn/CMSSW_8_0_12/src/HH2016/SlimMiniTrees/"

#sigpath = "/eos/uscms/store/user/mkrohn/HHHHTo4b/V24/BulkGrav_Correct/Alphabet/"
if Options.inject != "none":
	normI = GetNom(sigpath+"BulkGrav_M-"+Options.inject+"_0.root")
	INJ = DIST("INJ", sigpath+"BulkGrav_M-"+Options.inject+"_0.root","mynewTree",str(Options.lumi)+"*0.01*puWeights*SFTight/"+str(normI))
	whichdataorQCD = "QCD w/ Injected Signal"
	DistsWeWantToEstimate.append(INJ)
#### SOME SIGNALS WE'LL USE:
norm0= GetNom(sigpath+"BulkGrav_M-1200_0.root")
norm1 = GetNom(sigpath+"BulkGrav_M-1800_0.root")
norm2 = GetNom(sigpath+"BulkGrav_M-2500_0.root")

SIG0 = TH1F("Signal1200", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG1 = TH1F("Signal1800", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG2 = TH1F("Signal2500", "", len(binBoundaries)-1, array('d',binBoundaries))

quickplot(sigpath+"BulkGrav_M-1200_0.root", "mynewTree", SIG0, variable2, TightT2, "puWeights*SFTight/1.")
quickplot(sigpath+"BulkGrav_M-1800_0.root", "mynewTree", SIG1, variable2, TightT2, "puWeights*SFTight/1.")
quickplot(sigpath+"BulkGrav_M-2500_0.root", "mynewTree", SIG2, variable2, TightT2, "puWeights*SFTight/1.")

SIG0.Scale(Options.lumi*0.01/norm0)
SIG1.Scale(Options.lumi*0.01/norm1)
SIG2.Scale(Options.lumi*0.01/norm2)

SIG0.SetLineColor(kRed-3)
SIG1.SetLineColor(kRed)
SIG2.SetLineColor(kRed+3)

var_array = ["jet1_puppi_msoftdrop_raw_TheaCorr", "jet1bbtag", 60,50,200, 100, -1., 1.]
#var_array = ["jet1pmass", "jet1bbtag", 60,50,200, 100, -1., 1.]

Hbb = Alphabetizer(Options.name, DistsWeWantToEstimate, [])
Hbb.SetRegions(var_array, TightPre)

bins = binCalc(50,200,105,135,Options.bin)
if Options.Linear:
	F = LinearFit([0.0,0.0], -75, 85, "linfit", "W")
else:
	F = QuadraticFit([0.1,0.1,0.1], -75, 85, "quadfit", "EMRFNEX0")
Hbb.GetRates([Options.tightcut, ">"], bins[0], bins[1], 120., F)


leg = TLegend(0.6,0.6,0.89,0.89)
leg.SetLineColor(0)
leg.SetFillColor(4001)
leg.SetTextSize(0.03)
leg.AddEntry(Hbb.G, "events used in fit", "PLE")
if Options.Truth:
	leg.AddEntry(Hbb.truthG, "signal region (blind)", "PLE")
leg.AddEntry(Hbb.Fit.fit, "fit", "L")
leg.AddEntry(Hbb.Fit.ErrUp, "fit errors", "L")
plotforplotting = TH1F("empty_"+Options.name, "", 24, -75, 80)
plotforplotting.SetStats(0)
plotforplotting.GetYaxis().SetRangeUser(0.00,0.25)
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

FunctionChiSquared = Hbb.Fit.fit.GetChisquare()

THILABL = TLatex()
THILABL.SetNDC()
THILABL.SetTextSize(0.04)
THILABL.DrawLatex(0.651,0.91,"#chi^{2} = %s"%(FunctionChiSquared))

Hbb.Fit.ErrUp.SetLineStyle(2)
Hbb.Fit.ErrUp.Draw("same")
Hbb.Fit.ErrDn.SetLineStyle(2)
Hbb.Fit.ErrDn.Draw("same")
leg.Draw()
C2.SaveAs("outputs/HHSR_Fit_"+Options.name+".pdf")


FILE = TFile("outputs/HHSR_TT.root", "RECREATE")
FILE.cd()

D = TH1F("data", "", len(binBoundaries)-1, array('d',binBoundaries))
N = TH1F("est", "", len(binBoundaries)-1, array('d',binBoundaries))
NU = TH1F("est_up", "", len(binBoundaries)-1, array('d',binBoundaries)) 
ND = TH1F("est_down", "", len(binBoundaries)-1, array('d',binBoundaries))
A =  TH1F("antitag", "", len(binBoundaries)-1, array('d',binBoundaries)) 

PULL = FillPlots(Hbb, D, N, NU, ND, A, variable, binBoundaries, TightAT, TightT)


FILE.Write()
FILE.Save()


Pull = PULL[0]
maxy = PULL[1]
Boxes = PULL[2]
sBoxes = PULL[3]
pBoxes = PULL[4]
#fBoxes = PULL[5]

vartitle = "m_{X} (GeV)"

D.SetStats(0)
D.Sumw2()
D.SetLineColor(1)
D.SetFillColor(0)
D.SetMarkerColor(1)
D.SetMarkerStyle(20)
N.GetYaxis().SetTitle("events")
N.GetXaxis().SetTitle(vartitle)
A.GetYaxis().SetTitle("events")
A.GetXaxis().SetTitle(vartitle)
if Options.log:
#        N.GetYaxis().SetRangeUser(0.05,maxy*1.5)
	A.GetYaxis().SetRangeUser(0.000005,maxy*30)
else:
	N.GetYaxis().SetRangeUser(0.,maxy*1.2)
N.SetLineColor(kBlue)
A.SetLineColor(kGreen + 2)

Pull.GetXaxis().SetTitle("")
Pull.SetStats(0)
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

SIG0.SetFillColor(kRed-3)
SIG0.SetFillStyle(3244)
SIG1.SetFillColor(kRed)
SIG1.SetFillStyle(3244)
SIG2.SetFillColor(kRed+3)
SIG2.SetFillStyle(3244)

for i in Boxes:
	i.SetFillColor(9)
for i in pBoxes:
	i.SetFillColor(12)
	i.SetFillStyle(3144)
for i in sBoxes:
	i.SetFillColor(41)
	i.SetFillStyle(3344)
#for i in fBoxes:
#        i.SetFillColor(46)
#        i.SetFillStyle(3444)

leg2 = TLegend(0.6,0.6,0.89,0.89)
leg2.SetLineColor(0)
leg2.SetFillColor(0)
leg2.AddEntry(D, whichdataorQCD, "PL")
leg2.AddEntry(N, "background prediction", "LF")
#leg2.AddEntry(Boxes[0], "total uncertainty", "F")
leg2.AddEntry(sBoxes[0], "background statistical component", "F")
#leg2.AddEntry(fBoxes[0], "alphabet fit component", "F")
leg2.AddEntry(A, "anti-tag", "LF")
#if Options.Sig:
#	leg2.AddEntry(SIG0, "Bulk Graviton (1200 GeV, 27 fb)", "F")
#	leg2.AddEntry(SIG1, "Bulk Graviton (1800 GeV, 27 fb)", "F")
#	leg2.AddEntry(SIG2, "Bulk Graviton (2500 GeV, 27 fb)", "F")

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

N.SetStats(0)
A.SetStats(0)

C4 = TCanvas("C4", "", 800, 600)
plot = TPad("pad1", "The pad 80% of the height",0,0.15,1,1)
pull = TPad("pad2", "The pad 20% of the height",0,0,1.0,0.15)
plot.Draw()
pull.Draw()
plot.cd()
A.Draw("Hist")
N.Draw("Hist SAME")
if Options.Truth:
	D.Draw("same E0")
#for i in Boxes:
#	i.Draw("same")
for i in sBoxes:
	i.Draw("same")
#for i in fBoxes:
#        i.Draw("same")
#if Options.Sig:
#	SIG0.Draw("same hist")
#	SIG1.Draw("same hist")
#	SIG2.Draw("same hist")
N.Draw("Hist same")
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
C4.SaveAs("outputs/HHSR_Plot_"+Options.name+".pdf")

if Options.workspace == "alphabet":
	print "creating workspace and datacard: ALPHABET"

	mass=[750,800,1000,1200,1400,1600,1800,2000,2500, 3000, 4000, 4500]
	for m in mass:
		print str(m)
		SF_tau21 = 1.03*1.03
		UD = ['Up','Down']

		output_file = TFile("outputs/datacards/HH_mX_%s_"%(m)+Options.name+"_13TeV.root", "RECREATE")
		vh=output_file.mkdir("vh")
		vh.cd()

		Signal_mX = TH1F("Signal_mX_%s_"%(m)+Options.name, "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_antitag = TH1F("Signal_mX_antitag_%s"%(m)+Options.name, "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_trig_up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_trigUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_trig_down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_trigDown", "", len(binBoundaries)-1, array('d',binBoundaries))
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

		quickplot(sigpath+"BulkGrav_M-%s_0.root"%(m), "mynewTree", Signal_mX, variable2, TightT2+"&(HLT_PFHT800_v==1||HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v==1||HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v==1||HLT_AK8PFJet360_V==1||HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v==1)", "puWeights*SFTight/1.")
		quickplot(sigpath+"BulkGrav_M-%s_0.root"%(m), "mynewTree", Signal_mX_antitag, variable2, TightAT+"&(HLT_PFHT800_v==1||HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v==1||HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v==1||HLT_AK8PFJet360_V==1||HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v==1)", "puWeights*(1.-SFTight)/1.")
		quickplot(sigpath+"BulkGrav_M-%s_0.root"%(m), "mynewTree", Signal_mX_btag_up, variable2, TightT2+"&(HLT_PFHT800_v==1||HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v==1||HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v==1||HLT_AK8PFJet360_V==1||HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v==1)", "puWeights*SFTightup/1.")
		quickplot(sigpath+"BulkGrav_M-%s_0.root"%(m), "mynewTree", Signal_mX_btag_down, variable2, TightT2+"&(HLT_PFHT800_v==1||HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v==1||HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v==1||HLT_AK8PFJet360_V==1||HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v==1)", "puWeights*SFTightdown/1.")
		quickplot(sigpath+"BulkGrav_M-%s_0.root"%(m), "mynewTree", Signal_mX_trig_up, variable2, TightT2, "trigWeightUp*puWeights*SFTight/1.")
		quickplot(sigpath+"BulkGrav_M-%s_0.root"%(m), "mynewTree", Signal_mX_trig_down, variable2, TightT2, "trigWeightDown*puWeights*SFTight/1.")
		quickplot(sigpath+"BulkGrav_M-%s_0.root"%(m), "mynewTree", Signal_mX_pu_up, variable2, TightT2+"&(HLT_PFHT800_v==1||HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v==1||HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v==1||HLT_AK8PFJet360_V==1||HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v==1)", "puWeightsUp*SFTight/1.")
		quickplot(sigpath+"BulkGrav_M-%s_0.root"%(m), "mynewTree", Signal_mX_pu_down, variable2, TightT2+"&(HLT_PFHT800_v==1||HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v==1||HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v==1||HLT_AK8PFJet360_V==1||HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v==1)", "puWeightsDown*SFTight/1.")

		norm = GetNom(sigpath+"BulkGrav_M-%s_0.root"%(m))
		print(norm)
		print("norm")
		print(Signal_mX_btag_up.GetSumOfWeights())
		btaglnN= 1.#+ abs(Signal_mX_btag_up.GetSumOfWeights()-Signal_mX_btag_down.GetSumOfWeights())/(2.*Signal_mX_btag_up.GetSumOfWeights())
		PUlnN= 1.#+ abs(Signal_mX_pu_up.GetSumOfWeights()-Signal_mX_pu_down.GetSumOfWeights())/(2.*Signal_mX.GetSumOfWeights())

		Signal_mX.Scale(SF_tau21*Options.lumi*0.01/norm)
		Signal_mX_antitag.Scale(SF_tau21*Options.lumi*0.01/norm)
		Signal_mX_btag_up.Scale(SF_tau21*Options.lumi*0.01/norm)
		Signal_mX_btag_down.Scale(SF_tau21*Options.lumi*0.01/norm)
		Signal_mX_trig_up.Scale(SF_tau21*0.01*Options.lumi/norm)
		Signal_mX_trig_down.Scale(SF_tau21*0.01*Options.lumi/norm)
		Signal_mX_pu_up.Scale(Options.lumi*SF_tau21*0.01/norm)
		Signal_mX_pu_down.Scale(Options.lumi*SF_tau21*0.01/norm)


		MJEClnN= 1.02 ## add variation from ntuples
		FJEClnN= 1.02
		FJERlnN= 1.02

		signal_integral = Signal_mX.Integral(Signal_mX.FindBin(1200),Signal_mX.FindBin(2500))
		print(signal_integral)
		print("signal_integral")
		signal_integral_anti = Signal_mX_antitag.Integral(Signal_mX_antitag.FindBin(1200),Signal_mX_antitag.FindBin(2500))
		print(signal_integral_anti)
		print("signal_integral_anti")

		#Getting R parameter for card:
		AntitagIntegral = A.Integral(Signal_mX.FindBin(1200),Signal_mX.FindBin(2500))
		AverageRate = N.Integral(Signal_mX.FindBin(1200),Signal_mX.FindBin(2500))/AntitagIntegral 
		AverageErrorRate = NU.Integral(Signal_mX.FindBin(1200),Signal_mX.FindBin(2500))/AntitagIntegral 
		AverageError = math.fabs(AverageErrorRate - AverageRate)

		qcd_integral = N.Integral(N.FindBin(1200),N.FindBin(2500))
		qcd = N.Clone(Options.name+"EST")
		qcd_antitag = A.Clone(Options.name+"EST_antitag")
		qcd_up = NU.Clone(Options.name+"EST_CMS_scale"+Options.name+"_13TeVUp")
		qcd_down = ND.Clone(Options.name+"EST_CMS_scale"+Options.name+"_13TeVDown")
		data_obs = D.Clone("data_obs")
		data_integral = data_obs.Integral(data_obs.FindBin(1200),data_obs.FindBin(2500)) 
	
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
		Signal_mX.Write()
		Signal_mX_btag_up.Write()
		Signal_mX_btag_down.Write()
		Signal_mX_trig_up.Write()
		Signal_mX_trig_down.Write()
		data_obs.Write()
		vh.Write()
		output_file.Write()
		output_file.Close()

		text_file = open("outputs/datacards/HH_mX_%s_"%(m)+Options.name+"_13TeV_pass.txt", "w")

		text_file.write("imax    1     number of categories\n")
		text_file.write("jmax    1     number of samples minus one\n")
		text_file.write("kmax    *     number of nuisance parameters\n")
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("shapes * * HH_mX_%s_"%(m)+Options.name+"_13TeV.root vh/$PROCESS vh/$PROCESS_$SYSTEMATIC\n")
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("bin                                            vh4b_pass			\n")
		text_file.write("observation                                    -1.0				\n")
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("bin                                             vh4b_pass            vh4b_pass	\n")
		text_file.write("process                                         Signal_mX_%s_"%(m)+Options.name+"  "+Options.name+"EST\n")#	Signal_mX_antitag_%s_"%(m)+Options.name+"  "+Options.name+"EST_antitag
		text_file.write("process                                          -1      0	\n")
		text_file.write("rate                                            %f 	1.0000	\n"%(signal_integral))#,signal_integral_anti))
		text_file.write("-------------------------------------------------------------------------------\n")
		#text_file.write("bgSB_norm rateParam vh4b_fail "+Options.name+"EST_antitag "+str(AntitagIntegral)+"\n")
		text_file.write("R param "+str(AverageRate)+" "+str(AverageError)+"\n")
		text_file.write("n_exp_binHH4b_proc_EST_ EST rateParam vh4b_pass "+Options.name+"EST @0*@1 bgSB_norm,R\n")

		text_file.close()
		
		text_filea = open("outputs/datacards/HH_mX_%s_"%(m)+Options.name+"_13TeV_fail.txt", "w")

		text_filea.write("imax    1     number of categories\n")
		text_filea.write("jmax    1     number of samples minus one\n")
		text_filea.write("kmax    *     number of nuisance parameters\n")
		text_filea.write("-------------------------------------------------------------------------------\n")
		text_filea.write("shapes * * HH_mX_%s_"%(m)+Options.name+"_13TeV.root vh/$PROCESS vh/$PROCESS_$SYSTEMATIC\n")
		text_filea.write("-------------------------------------------------------------------------------\n")
		text_filea.write("bin                                            vh4b_fail			\n")
		text_filea.write("observation                                    -1.0				\n")
		text_filea.write("-------------------------------------------------------------------------------\n")
		text_filea.write("bin                                             vh4b_fail            vh4b_fail	\n")
		text_filea.write("process                                         Signal_mX_antitag_%s_"%(m)+Options.name+"  "+Options.name+"EST_antitag\n")
		text_filea.write("process                                          -1      0	\n")
		text_filea.write("rate                                            %f 	1.0000	\n"%(signal_integral_anti))
		text_filea.write("-------------------------------------------------------------------------------\n")
		text_filea.write("bgSB_norm rateParam vh4b_fail "+Options.name+"EST_antitag "+str(AntitagIntegral)+"\n")
		#text_file.write("R param "+str(AverageRate)+" "+str(AverageError)+"\n")
		#text_file.write("n_exp_binHH4b_proc_EST_ EST rateParam vh4b_pass "+Options.name+"EST @0*@1 bgSB_norm,R\n")

		text_file.close()	

if Options.workspace == "fit":
	print "creating workspace and datacard: ALPHABET ASSISTED FIT"







