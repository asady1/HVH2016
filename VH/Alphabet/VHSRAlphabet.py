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

parser.add_option('--T2', '--Selection', metavar='T32', type='string', dest='tightpre')
parser.add_option('--T1', '--Cut', metavar='T13', type='float', dest='tightcut', default = 0.8)

parser.add_option('--N', '--name', metavar='Name', type='string', dest='name', default="test")
parser.add_option('--L', '--lumi', metavar='Name', type='float', dest='lumi', default="27200")

parser.add_option("--data", action="store_true", dest="isData", default=True)
parser.add_option("--qcd", action="store_false", dest="isData")

parser.add_option("--quad", action="store_false", dest="Linear", default=False)
parser.add_option("--lin", action="store_true", dest="Linear")

parser.add_option("--blind", action="store_false", dest="Truth", default=False)
parser.add_option("--unblind", action="store_true", dest="Truth")

parser.add_option("--finebins", action="store_false", dest="finebins", default=False)
parser.add_option("--dijetbins", action="store_true", dest="finsbines")

parser.add_option("--log", action="store_true", dest="log", default=False)
parser.add_option("--nolog", action="store_false", dest="log")

parser.add_option("--sig", action="store_true", dest="Sig", default=True)
parser.add_option("--nosig", action="store_false", dest="Sig")

parser.add_option('-I', '--inject', metavar='Inj', type='string', dest='inject', default="none")

parser.add_option('--workspace', metavar='WSPC', type='string', dest='workspace', default="alphabet")
(Options, args) = parser.parse_args()

preselection    =       "&vtype==-1&jetVpt>200&json==1&jetHpt>200&abs(jetVeta-jetHeta)<1.3&jetVtau21<0.6&jetHtau21<0.6&dijetmass_puppi>800&jetVID==1&jetHID==1&abs(jetVeta)<2.4&abs(jetHeta)<2.4&HLT_PFHT800_v==1"
#preselection	= 	"&vtype==-1&jet2pt>250&json==1&jet1pt>250&etadiff<1.3&jet1tau21<0.6&dijetmass_corr>800&jet2ID==1&jet1ID==1&abs(jet1eta)<2.4&abs(jet2eta)<2.4&HLT_PFHT800_v==1"
TightPre 		=	Options.tightpre + preselection
TightAT                 =       TightPre + "&jetH_puppi_msoftdrop_TheaCorr>110&jetH_puppi_msoftdrop_TheaCorr<140&(jetHbbtag<"+str(Options.tightcut)+")"
#TightAT 		=	TightPre + "&jet1pmass>105&jet1pmass<135&(jet1bbtag<"+str(Options.tightcut)+")"
TightT          =       TightPre + "&jetH_puppi_msoftdrop_TheaCorr>110&jetH_puppi_msoftdrop_TheaCorr<140&(jetHbbtag>"+str(Options.tightcut)+")"
#TightT 		=	TightPre + "&jet1pmass>105&jet1pmass<135&(jet1bbtag>"+str(Options.tightcut)+")"
#TightT2         = "jetV_puppi_msoftdrop_raw_TheaCorr > 65 & jetV_puppi_msoftdrop_raw_TheaCorr < 105  &vtype==-1&jetVpt>200&json==1&jetHpt>200&abs(jetVeta-jetHeta)<1.3&jetHtau21<0.6&dijetmass_puppi_raw>800&jetVID==1&jetHID==1&abs(jetHeta)<2.4&abs(jetVeta)<2.4&jetH_puppi_msoftdrop_raw_TheaCorr>110&_puppi_msoftdrop_raw_TheaCorr<140&(jetHbbtag>0.8)"
TightT2         = "jetV_puppi_msoftdrop_raw_TheaCorr > 65 & jetV_puppi_msoftdrop_raw_TheaCorr< 105  &  jetHbbtag < 0.8 &vtype==-1&jetVpt>200&json==1&jetHpt>200&abs(jetHeta-jetVeta)<1.3&jetHtau21<0.6&dijetmass_puppi_raw>800&jetVID==1&jetHID==1&abs(jetHeta)<2.4&abs(jetVeta)<2.4&jetH_puppi_msoftdrop_raw_TheaCorr>110&jetH_puppi_msoftdrop_raw_TheaCorr<140&(jetHbbtag>0.3)&HLT_PFHT800_v==1"

if Options.finebins:
	binBoundaries=[]
	for i in range(0,1300):	
		binBoundaries.append(1200+i*1)
else:
	binBoundaries =[800, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509]

variable = "dijetmass_puppi"
variable2 = "dijetmass_puppi_raw"
#variable = "dijetmass_corr"

############# DATASETS: #################
QCD1 = DIST("DATA1", "/eos/uscms/store/user/mkrohn/HHTo4b/V23/miniTrees_80X_ICHEP/QCD_HT500To700.root","myTree",str(Options.lumi)+"*31630./19665695")
QCD2 = DIST("DATA2", "/eos/uscms/store/user/mkrohn/HHTo4b/V23/miniTrees_80X_ICHEP/QCD_HT700To1000.root","myTree",str(Options.lumi)+"*6802./15547962")
QCD3 = DIST("DATA3", "/eos/uscms/store/user/mkrohn/HHTo4b/V23/miniTrees_80X_ICHEP/QCD_HT1000To1500.root","myTree",str(Options.lumi)+"*1206./5049267")
QCD4 = DIST("DATA4", "/eos/uscms/store/user/mkrohn/HHTo4b/V23/miniTrees_80X_ICHEP/QCD_HT1500To2000.root","myTree",str(Options.lumi)+"*120.4/3939077")
QCD5 = DIST("DATA5", "/eos/uscms/store/user/mkrohn/HHTo4b/V23/miniTrees_80X_ICHEP/QCD_HT2000ToInf.root","myTree",str(Options.lumi)+"*25.25/1981228")
DATA = DIST("DATA", "/uscms_data/d3/mkrohn/CMSSW_8_0_12/src/HH2016/SlimMiniTrees/JetHT_VH.root","mynewTree","1.")
#DATA = DIST("DATA", "/eos/uscms/store/user/mkrohn/HHHHTo4b/V24/JetHT.root","myTree","1.")
if Options.isData:
	DistsWeWantToEstimate = [DATA]
	whichdataorQCD = "Data"
else:
	DistsWeWantToEstimate = [QCD1,QCD2,QCD3,QCD4,QCD5]
	whichdataorQCD = "QCD"

sigpath = "/eos/uscms/store/user/mkrohn/HHHHTo4b/V24/Wprime/VH/"
if Options.inject != "none":
	normI = GetNom(sigpath+"Wprime"+Options.inject+".root")
	INJ = DIST("INJ", sigpath+"Wprime"+Options.inject+".root","mynewTree",str(Options.lumi)+"*0.01*puWeights*SF/"+str(normI))
	whichdataorQCD = "QCD w/ Injected Signal"
	DistsWeWantToEstimate.append(INJ)
#### SOME SIGNALS WE'LL USE:
norm0= GetNom(sigpath+"Wprime3500.root")
norm1 = GetNom(sigpath+"Wprime1800.root")
norm2 = GetNom(sigpath+"Wprime2500.root")

SIG0 = TH1F("Signal3500", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG1 = TH1F("Signal1800", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG2 = TH1F("Signal2500", "", len(binBoundaries)-1, array('d',binBoundaries))

quickplot(sigpath+"Wprime3500.root", "mynewTree", SIG0, variable2, TightT2, "puWeights*SF/1.")
quickplot(sigpath+"Wprime1800.root", "mynewTree", SIG1, variable2, TightT2, "puWeights*SF/1.")
quickplot(sigpath+"Wprime2500.root", "mynewTree", SIG2, variable2, TightT2, "puWeights*SF/1.")

SIG0.Scale(Options.lumi*0.01/norm0)
SIG1.Scale(Options.lumi*0.01/norm1)
SIG2.Scale(Options.lumi*0.01/norm2)

SIG0.SetLineColor(kRed-3)
SIG1.SetLineColor(kRed)
SIG2.SetLineColor(kRed+3)

var_array = ["jetH_puppi_msoftdrop_TheaCorr", "jetHbbtag", 60,50,200, 100, -1., 1.]
#var_array = ["jet1pmass", "jet1bbtag", 60,50,200, 100, -1., 1.]

Hbb = Alphabetizer(Options.name, DistsWeWantToEstimate, [])
Hbb.SetRegions(var_array, TightPre)

bins = binCalc(50,200,110,140,Options.bin)
if Options.Linear:
	F = LinearFit([0.0,0.0], -75, 85, "linfit", "EMRNSQ")
else:
	F = QuadraticFit([0.1,0.1,0.1], -75, 85, "quadfit", "EMRFNEX0")
Hbb.GetRates([Options.tightcut, ">"], bins[0], bins[1], 125., F)


Hbb.TwoDPlot.SetStats(0)
C1 = TCanvas("C1", "", 800, 600)
C1.cd()
Hbb.TwoDPlot.Draw("COLZ")
Hbb.TwoDPlot.GetXaxis().SetTitle("jet mass (GeV)")
Hbb.TwoDPlot.GetYaxis().SetTitle("bb-tag")
C1.SaveAs("outputs/VHSR_2D_"+Options.name+".pdf")

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
plotforplotting.GetYaxis().SetRangeUser(0.,0.35)
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
NU = TH1F("est_up", "", len(binBoundaries)-1, array('d',binBoundaries)) 
ND = TH1F("est_down", "", len(binBoundaries)-1, array('d',binBoundaries))
A =  TH1F("antitag", "", len(binBoundaries)-1, array('d',binBoundaries)) 

PULL = FillPlots(Hbb, D, N, NU, ND, A, variable, binBoundaries, TightAT, TightT)

Pull = PULL[0]
maxy = PULL[1]
Boxes = PULL[2]
sBoxes = PULL[3]
pBoxes = PULL[4]

vartitle = "m_{X} (GeV)"

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
N.SetLineColor(kBlue)

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

leg2 = TLegend(0.6,0.6,0.89,0.89)
leg2.SetLineColor(0)
leg2.SetFillColor(0)
leg2.AddEntry(D, whichdataorQCD, "PL")
leg2.AddEntry(N, "background prediction", "LF")
leg2.AddEntry(Boxes[0], "total uncertainty", "F")
leg2.AddEntry(sBoxes[0], "background statistical component", "F")
if Options.Sig:
	leg2.AddEntry(SIG0, "Wprime (3500 GeV, 27 fb)", "F")
	leg2.AddEntry(SIG1, "Wprime (1800 GeV, 27 fb)", "F")
	leg2.AddEntry(SIG2, "Wprime (2500 GeV, 27 fb)", "F")

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

C4 = TCanvas("C4", "", 800, 600)
plot = TPad("pad1", "The pad 80% of the height",0,0.15,1,1)
pull = TPad("pad2", "The pad 20% of the height",0,0,1.0,0.15)
plot.Draw()
pull.Draw()
plot.cd()
N.Draw("Hist")
if Options.Truth:
	D.Draw("same E0")
for i in Boxes:
	i.Draw("same")
for i in sBoxes:
	i.Draw("same")
if Options.Sig:
	SIG0.Draw("same hist")
	SIG1.Draw("same hist")
	SIG2.Draw("same hist")
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
C4.SaveAs("outputs/VHSR_Plot_"+Options.name+".pdf")

if Options.workspace == "alphabet":
	print "creating workspace and datacard: ALPHABET"

	mass=[800,1600,1800,2000,2500, 3000,3500,4000,4500]
	for m in mass:
		print str(m)
		SF_tau21 =1.
		UD = ['Up','Down']

		output_file = TFile("outputs/datacards/VH_mX_%s_"%(m)+Options.name+"_13TeV.root", "RECREATE")
		vh=output_file.mkdir("vh")
		vh.cd()

		Signal_mX = TH1F("Signal_mX_%s_"%(m)+Options.name, "", len(binBoundaries)-1, array('d',binBoundaries))
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

		quickplot(sigpath+"Wprime%s.root"%(m), "mynewTree", Signal_mX, variable2, TightT2+"&HLT_PFHT800_v>0", "puWeights*SF/1.")
		quickplot(sigpath+"Wprime%s.root"%(m), "mynewTree", Signal_mX_btag_up, variable2, TightT2+"&HLT_PFHT800_v>0", "puWeights*SFup/1.")
		quickplot(sigpath+"Wprime%s.root"%(m), "mynewTree", Signal_mX_btag_down, variable2, TightT2+"&HLT_PFHT800_v>0", "puWeights*SFdown/1.")
		quickplot(sigpath+"Wprime%s.root"%(m), "mynewTree", Signal_mX_trig_up, variable2, TightT2, "trigWeightUp*puWeights*SF/1.")
		quickplot(sigpath+"Wprime%s.root"%(m), "mynewTree", Signal_mX_trig_down, variable2, TightT2, "trigWeightDown*puWeights*SF/1.")
		quickplot(sigpath+"Wprime%s.root"%(m), "mynewTree", Signal_mX_pu_up, variable2, TightT2+"&HLT_PFHT800_v>0", "puWeightsUp*SF/1.")
		quickplot(sigpath+"Wprime%s.root"%(m), "mynewTree", Signal_mX_pu_down, variable2, TightT2+"&HLT_PFHT800_v>0", "puWeightsDown*SF/1.")

		norm = GetNom(sigpath+"Wprime%s.root"%(m))

		btaglnN= 1.+ abs(Signal_mX_btag_up.GetSumOfWeights()-Signal_mX_btag_down.GetSumOfWeights())/(2.*Signal_mX_btag_up.GetSumOfWeights())
		PUlnN= 1.+ abs(Signal_mX_pu_up.GetSumOfWeights()-Signal_mX_pu_down.GetSumOfWeights())/(2.*Signal_mX.GetSumOfWeights())

		Signal_mX.Scale(SF_tau21*Options.lumi*0.01/norm)
		Signal_mX_btag_up.Scale(SF_tau21*Options.lumi*0.01/norm)
		Signal_mX_btag_down.Scale(SF_tau21*Options.lumi*0.01/norm)
		Signal_mX_trig_up.Scale(SF_tau21*0.01*Options.lumi/norm)
		Signal_mX_trig_down.Scale(SF_tau21*0.01*Options.lumi/norm)
		Signal_mX_pu_up.Scale(Options.lumi*SF_tau21*0.01/norm)
		Signal_mX_pu_down.Scale(Options.lumi*SF_tau21*0.01/norm)


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
		Signal_mX_trig_up.Write()
		Signal_mX_trig_down.Write()
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
	
		text_file.write("CMS_eff_tau21_sf lnN                    1.027       -\n") #(0.028/0.979)
		#text_file.write("CMS_eff_Htag_sf lnN                    1.1       -\n")   
		text_file.write("CMS_JEC lnN 		     %f        -\n"%(FJEClnN)) 	
		text_file.write("CMS_massJEC lnN                 %f        -\n"%(MJEClnN))
		text_file.write("CMS_eff_bbtag_sf lnN                    %f       -\n"%(btaglnN))
		text_file.write("CMS_JER lnN                    %f        -\n"%(FJERlnN))
		text_file.write("CMS_PU lnN                    %f        -\n"%(PUlnN))
		text_file.write("CMS_eff_trig shapeN2           1.0   -\n")
	 	
		text_file.write("CMS_scale"+Options.name+"_13TeV shapeN2                           -       1.000\n")
		text_file.write("CMS_PDF_Scales lnN   1.02 -       \n")

		for bin in range(0,len(binBoundaries)-1):
			text_file.write("CMS_stat"+Options.name+"_13TeV_bin%s shapeN2                           -       1.000\n"%(bin))


		text_file.close()

if Options.workspace == "fit":
	print "creating workspace and datacard: ALPHABET ASSISTED FIT"








