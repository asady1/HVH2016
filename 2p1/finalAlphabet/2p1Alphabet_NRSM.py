import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy
import pdb
import CMS_lumi, tdrstyle
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
parser.add_option('--X', '--leghead', metavar='Name', type='string', dest='leghead', default="leg")
parser.add_option('--L', '--lumi', metavar='Name', type='float', dest='lumi', default="35876")

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

parser.add_option("--sig", action="store_true", dest="Sig", default=True)
parser.add_option("--nosig", action="store_false", dest="Sig")

parser.add_option('-I', '--inject', metavar='Inj', type='string', dest='inject', default="none")

parser.add_option('--workspace', metavar='WSPC', type='string', dest='workspace', default="alphabet")
(Options, args) = parser.parse_args()

presel    =   Options.pre
tag = presel + "&(fatjet_mass<135&fatjet_mass>105)&(fatjet_hbb>"+str(Options.cut)+")"
atag = presel + "&(fatjet_mass<135&fatjet_mass>105)&(fatjet_hbb<"+str(Options.cut)+")"

CMS_lumi.lumi_13TeV = "35.9 fb^{-1} (2016)"
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.12

iPeriod =4


if Options.finebins:
	binBoundaries=[]
	for i in range(0,1700):	
		binBoundaries.append(450+i*1)
else:
#	binBoundaries =[450, 499, 548, 596, 644, 692, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132]
#	binBoundaries = [750, 798, 850, 904, 960, 1018, 1078, 1140, 1204, 1270, 1338, 1408, 1480, 2000]
	binBoundaries = [750, 800, 852, 906, 962, 1020, 1080, 1142, 1206, 1272, 1340, 1410, 1482,2100]
#	binBoundaries = [450, 500, 550,  600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1880, 1960, 2040, 2120]
#	binBoundaries =[450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150]

variable = "Red_mass"

sigpath = "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/input/"

############# DATASETS: #################
QCD1 = DIST("DATA1", "../V25miniTrees/QCD_300_backEst.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*"+str(Options.lumi)+"*347700./39598300")
QCD2 = DIST("DATA2", "../V25miniTrees/QCD500_backEst.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*"+str(Options.lumi)+"*32100./42837570")
QCD3 = DIST("DATA2", "../V25miniTrees/QCD700_backEst.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*"+str(Options.lumi)+"*6831./44384120")
QCD4 = DIST("DATA3", "../V25miniTrees/QCD1000_backEst.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*"+str(Options.lumi)+"*1207./14977450")
QCD5 = DIST("DATA5", "../V25miniTrees/QCD1500_backEst.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*"+str(Options.lumi)+"*119.9/11777410")
QCD6 = DIST("DATA6", "../V25miniTrees/QCD2000_backEst.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*"+str(Options.lumi)+"*25.24/5740311")
#TTBar = DIST("TTBar", "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/TT_SFs.root", "mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0|dcsvBtag/_|HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*"+str(Options.lumi)+"*831.76/75176620")
#TTBar = DIST("TTBar", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*2.71828^(0.0615-0.0005*ttHT/2)*"+str(Options.lumi)+"*831.8/71480770")
TTBar = DIST("TTBar", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*1.*"+str(Options.lumi)+"*831.8/71480770")
JetHTB = DIST("JetHTB", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_B_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagB = DIST("BTagB","root://cmsxrootd.fnal.gov//store/user/asady1/V25/finally/BTag_B_tree_finally.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTC = DIST("JetHTC", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_C_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagC = DIST("BTagC","root://cmsxrootd.fnal.gov//store/user/asady1/V25/finally/BTag_C_tree_finally.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTD = DIST("JetHTD", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_D_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagD = DIST("BTagD","root://cmsxrootd.fnal.gov//store/user/asady1/V25/finally/BTag_D_tree_finally.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTE = DIST("JetHTE", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_E_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagE = DIST("BTagE","root://cmsxrootd.fnal.gov//store/user/asady1/V25/finally/BTag_E_tree_finally.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTF = DIST("JetHTF", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_F_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagF = DIST("BTagF","root://cmsxrootd.fnal.gov//store/user/asady1/V25/finally/BTag_F_tree_finally.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTG = DIST("JetHTG", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_G_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagG = DIST("BTagG","root://cmsxrootd.fnal.gov//store/user/asady1/V25/finally/BTag_G_tree_finally.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTH = DIST("JetHTH", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_H_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagH = DIST("BTagH","root://cmsxrootd.fnal.gov//store/user/asady1/V25/add/BTag_H_tree_add.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")

if Options.isData:
#	DistsWeWantToEstimate = [JetHTB,BTagB,JetHTC,BTagC,JetHTD,BTagD,JetHTE,BTagE,JetHTF,BTagF,BTagG,JetHTH,BTagH,JetHTG]
	DistsWeWantToEstimate = [JetHTB, JetHTC, JetHTD, JetHTE, JetHTF, JetHTG, JetHTH]
#	DistsWeWantToEstimate = [BTagB, BTagC, BTagD, BTagE, BTagF, BTagG, BTagH]
	whichdataorQCD = "Data"
else:
	DistsWeWantToEstimate = [QCD1,QCD2,QCD3,QCD4,QCD5,QCD6]
	whichdataorQCD = "QCD"

#sigpath = "root://cmsxrootd.fnal.gov//store/user/asady1/V25/"
#if Options.inject != "none":
#	normI = GetNom(sigpath+"Wprime"+Options.inject+".root")
#	INJ = DIST("INJ", sigpath+"Wprime"+Options.inject+".root","mynewTree",str(Options.lumi)+"*0.01*puWeights*SF/"+str(normI))
#	whichdataorQCD = "QCD w/ Injected Signal"
#	DistsWeWantToEstimate.append(INJ)
#### SOME SIGNALS WE'LL USE:
#norm0= GetNom(sigpath+"tree_500.root")
#norm1 = GetNom(sigpath+"tree_550.root")
norm2 = 50344.
norm3 = 100000.
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
norm0 = 50000.
norm1 = 100000.
#norm2 = 100000.
#norm3 = 49200.
#norm4 = 100000.
norm5 = 50000.
norm6 = 100000.
norm7 = 50000.
norm8 = 49200.
norm9 = 50000.
#norm10 = 50000.
norm11 = 50000.
#norm12 = 50000.
norm13 = 50000.

SIG0 = TH1F("Signal_500", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG1 = TH1F("Signal_550", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG2 = TH1F("NonResv1 node2", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG3 = TH1F("Bulk Graviton 800", "", len(binBoundaries)-1, array('d',binBoundaries))
#SIG4 = TH1F("Signal_700", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG5 = TH1F("Signal_750", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG6 = TH1F("Signal_800", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG7 = TH1F("Signal_900", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG8 = TH1F("Signal_1000", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG9 = TH1F("Signal_1200", "", len(binBoundaries)-1, array('d',binBoundaries))
#SIG10 = TH1F("Signal_1400", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG11 = TH1F("Signal_1600", "", len(binBoundaries)-1, array('d',binBoundaries))
#SIG12 = TH1F("Signal_1800", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG13 = TH1F("Signal_2000", "", len(binBoundaries)-1, array('d',binBoundaries))

#quickplot(sigpath+"BG_500_tree_finally.root", "mynewTree", SIG0, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_550_tree_finally.root", "mynewTree", SIG1, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
quickplot(sigpath+"NRv1_node2_tree_bfinallyb.root", "mynewTree", SIG2, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
quickplot(sigpath+"BG_1000_tree_bfinallyb.root", "mynewTree", SIG3, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
#quickplot(sigpath+"BG_700_tree_finally.root", "mynewTree", SIG4, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_750_tree_finally.root", "mynewTree", SIG5, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_800_tree_finally.root", "mynewTree", SIG6, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_900_tree_finally.root", "mynewTree", SIG7, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_1000_tree_finally.root", "mynewTree", SIG8, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_1200_tree_finally.root", "mynewTree", SIG9, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_1400_tree_finally.root", "mynewTree", SIG10, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_1600_tree_finally.root", "mynewTree", SIG11, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_1800_tree_finally.root", "mynewTree", SIG12, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_2000_tree_finally.root", "mynewTree", SIG13, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")



#SIG0.Scale(Options.lumi*0.01/norm0)
#SIG1.Scale(Options.lumi*0.01/norm1)
SIG2.Scale(Options.lumi*0.01/norm2)
SIG3.Scale(Options.lumi*0.01/norm3)
##SIG4.Scale(Options.lumi*0.01/norm4)
#SIG5.Scale(Options.lumi*0.01/norm5)
#SIG6.Scale(Options.lumi*0.01/norm6)
#SIG7.Scale(Options.lumi*0.01/norm7)
#SIG8.Scale(Options.lumi*0.01/norm8)
#SIG9.Scale(Options.lumi*0.01/norm9)
##SIG10.Scale(Options.lumi*0.01/norm10)
#SIG11.Scale(Options.lumi*0.01/norm11)
##SIG12.Scale(Options.lumi*0.01/norm12)
#SIG13.Scale(Options.lumi*0.01/norm13)

#SIG0.SetLineColor(kMagenta - 9)
#SIG1.SetLineColor(kMagenta - 6)
SIG2.SetLineColor(kBlue+2)
SIG3.SetLineColor(kBlack)
SIG3.SetLineStyle(9)
SIG2.SetLineWidth(2)
SIG3.SetLineWidth(2)
##SIG4.SetLineColor(kPink + 8) 
#SIG5.SetLineColor(kPink + 7)
#SIG6.SetLineColor(kPink + 3)
#SIG7.SetLineColor(kPink - 6)
#SIG8.SetLineColor(kPink - 4)
#SIG9.SetLineColor(kRed - 7)
##SIG10.SetLineColor(kRed - 3)
#SIG11.SetLineColor(kRed)
##SIG12.SetLineColor(kRed + 2)
#SIG13.SetLineColor(kRed + 3)

var_array = ["fatjet_mass", "fatjet_hbb", 60,45,195, 100, -1., 1.]
#var_array = ["jet1pmass", "jet1bbtag", 60,50,200, 100, -1., 1.]

Hbb = Alphabetizer(Options.name, DistsWeWantToEstimate, [TTBar])
Hbb.SetRegions(var_array, presel)

bins = binCalc(45,195,105,135,Options.bin)
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
Hbb.TwoDPlot.GetYaxis().SetTitle("double b-tagger")
C1.SaveAs("outputs/HH4b2p1SR_2D_"+Options.name+".pdf")

leg = TLegend(0.65,0.65,0.89,0.89)
leg.SetLineColor(0)
leg.SetFillColor(4001)
leg.SetTextSize(0.03)
leg.SetHeader(Options.leghead)
leg.AddEntry(Hbb.G, "events used in fit", "PLE")
if Options.Truth:
	leg.AddEntry(Hbb.truthG, "signal region", "PLE")
leg.AddEntry(Hbb.Fit.fit, "fit", "L")
leg.AddEntry(Hbb.Fit.ErrUp, "fit errors", "L")
plotforplotting = TH1F("empty_"+Options.name, "", 24, -75, 75)
plotforplotting.SetStats(0)
plotforplotting.GetYaxis().SetRangeUser(0.,1.)
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
CMS_lumi.CMS_lumi(C2, iPeriod, iPos)
C2.SaveAs("outputs/HH4b2p1SR_Fit_"+Options.name+".pdf")
C2.SaveAs("outputs/HH4b2p1SR_Fit_"+Options.name+".C")


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
#SIG2.SetFillColor(kMagenta-3)
#SIG2.SetFillStyle(3244)

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
leg2.SetHeader(Options.leghead)
leg2.AddEntry(D, whichdataorQCD, "PL")
leg2.AddEntry(N, "background prediction", "F")
leg2.AddEntry(Boxes[0], "total uncertainty", "F")
leg2.AddEntry(sBoxes[0], "background statistical component", "F")
leg2.AddEntry(TTNom, "ttbar", "F")
if Options.Sig:
	leg2.AddEntry(SIG3, "Bulk Grav (1000 GeV, 36 fb)", "l")
	leg2.AddEntry(SIG2, "NonResv1 (node 2, 36 fb)", "l")
#	leg2.AddEntry(SIG8, "Bulk Grav (1000 GeV, 27 fb)", "F")

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
if Options.Truth:
	D.Draw("E0")
N.Draw("same Hist")
TTNom.Draw("same Hist")
if Options.Truth:
	D.Draw("same E0")
for i in Boxes:
	i.Draw("same")
for i in sBoxes:
	i.Draw("same")
if Options.Sig:
	SIG2.Draw("same hist")
	SIG3.Draw("same hist")
#	SIG6.Draw("same hist")
#	SIG8.Draw("same hist")
#N.Draw("Hist same")
if Options.log:
	plot.SetLogy()
leg2.Draw()
CMS_lumi.CMS_lumi(C4, iPeriod, iPos)
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
C4.SaveAs("outputs/HH4b2p1_Plot_"+Options.name+".pdf")
C4.SaveAs("outputs/HH4b2p1_Plot_"+Options.name+".C")

if Options.workspace == "alphabet":
	print "creating workspace and datacard: ALPHABET"

#	mass=[500,550,600,650,750,800,900,1000,1200,1600,2000]
#	mass=[1,2,3,4,5,6,7,8,9,10,11,12,100]
	mass = [1,2,3,4,5,6,7,8,9,10,11,12,100]
	i = 0
#	signorm = [50000., 100000., 100000., 49200., 50000., 100000., 50000., 49200., 50000., 50000., 50000.]
	pdfup = [1.037,1.061,0.923,0.931,0.978,1.034,0.976,0.960,1.034,0.979,1.034,1.042,0.987]
	pdfdown = [1.039,1.065,0.918,0.926,0.976,1.037,0.979,0.960,1.037,0.977,1.037,1.038,0.991]
	pdfsup = [1.001,1.000,1.001,1.001,1.001,1.001,1.002,1.001,1.001,1.002,1.001,1.001,1.001]
	pdfsdown = [1.003,1.002,1.003,1.004,1.003,1.004,1.005,1.004,1.003,1.005,1.004,1.004,1.003]
#	signorm = [ 0.411053092815, 0.438148829154,0.308863407832,0.25856900425,0.259906321536,0.289594874935, 0.125299801629,0.135470964857,0.362598978651,0.200083293881,0.289594874935,0.175763135754,0.26]
#	signorm = [299800.,299600., 299800., 265200., 258000., 300000., 192434., 294000., 263400., 16800., 300000., 226200., 300000., 154600.]
	signorm = [111746.,50344.,139492.,220012.,254388.,105680.,231132.,77421.,90457.,194295.,72522.,211670.,299800.]
#	pdfup = [1.0,1.0]
#	pdfdown = [1.0,1.0]
	for m in mass:
		print str(m)
	        UD = ['Up','Down']
	
		output_file = TFile("outputs/datacards/HH4b_semiBoosted_mX_%s_"%(m)+Options.name+"_13TeV.root", "RECREATE")
		vh=output_file.mkdir("vh")
		vh.cd()
		print "made output file"
		ggHH_hbbhbb_mX = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name, "", len(binBoundaries)-1, array('d',binBoundaries))
		ggHH_hbbhbb_mX_htag = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_htag", "", len(binBoundaries)-1, array('d',binBoundaries))
#		ggHH_hbbhbb_mX_csv_up = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_csvUp", "", len(binBoundaries)-1, array('d',binBoundaries))
#		ggHH_hbbhbb_mX_csv_down = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_csvDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		ggHH_hbbhbb_mX_btag_up = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_btagUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		ggHH_hbbhbb_mX_btag_down = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_btagDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		ggHH_hbbhbb_mX_pu_up = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_puUp", "", len(binBoundaries)-1, array('d',binBoundaries))
	 	ggHH_hbbhbb_mX_pu_down = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_puDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		ggHH_hbbhbb_mX_JEC_Up = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_JECUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		ggHH_hbbhbb_mX_JEC_Down = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_JECDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		ggHH_hbbhbb_mX_JER_Up = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_JERUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		ggHH_hbbhbb_mX_JER_Down = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_JERDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		ggHH_hbbhbb_mX_trig_up = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_trigUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		ggHH_hbbhbb_mX_trig_down = TH1F("ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"_CMS_eff_trigDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb.root"%(m), "mynewTree", ggHH_hbbhbb_mX, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb.root"%(m), "mynewTree", ggHH_hbbhbb_mX_htag, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*(1. - 2.71828^(-0.125052 + 32.5054/(fatjetPT))+ 1)")
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb.root"%(m), "mynewTree", ggHH_hbbhbb_mX_btag_up, variable, tag +"&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SFup*ak4btag1SFup*ak4btag2SFup*trigWeight*1.03/1.")
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb.root"%(m), "mynewTree", ggHH_hbbhbb_mX_btag_down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SFdown*ak4btag1SFdown*ak4btag2SFdown*trigWeight*1.03/1.")
#		quickplot(sigpath+"NRv1_node%s_tree_finallyb.root"%(m), "mynewTree", ggHH_hbbhbb_mX_csv_up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SFup*ak4btag2SFup*trigWeight*1.03/1.")
#		quickplot(sigpath+"NRv1_node%s_tree_finallyb.root"%(m), "mynewTree", ggHH_hbbhbb_mX_csv_down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SFdown*ak4btag2SFdown*trigWeight*1.03/1.")
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb.root"%(m), "mynewTree", ggHH_hbbhbb_mX_pu_up, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeightUp*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb.root"%(m), "mynewTree", ggHH_hbbhbb_mX_pu_down, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeightDown*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb.root"%(m), "mynewTree", ggHH_hbbhbb_mX_trig_up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeightUp*1.03/1.")
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb.root"%(m), "mynewTree", ggHH_hbbhbb_mX_trig_down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeightDown*1.03/1.")
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb_JECUp.root"%(m), "mynewTree", ggHH_hbbhbb_mX_JEC_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb_JECDown.root"%(m), "mynewTree", ggHH_hbbhbb_mX_JEC_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb_JERUp.root"%(m), "mynewTree", ggHH_hbbhbb_mX_JER_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"NRv1_node%s_tree_bfinallyb_JERDown.root"%(m), "mynewTree", ggHH_hbbhbb_mX_JER_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		print "made sig plots"
		ttbar = TH1F("ttbar", "", len(binBoundaries)-1, array('d',binBoundaries))
#		ttbar_csv_up = TH1F("ttbar_CMS_eff_csvUp", "", len(binBoundaries)-1, array('d',binBoundaries))
#		ttbar_csv_down = TH1F("ttbar_CMS_eff_csvDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		ttbar_btag_up = TH1F("ttbar_CMS_eff_btagUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		ttbar_btag_down = TH1F("ttbar_CMS_eff_btagDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		ttbar_pu_up = TH1F("ttbar_CMS_eff_puUp", "", len(binBoundaries)-1, array('d',binBoundaries))
	 	ttbar_pu_down = TH1F("ttbar_CMS_eff_puDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		ttbar_JEC_Up = TH1F("ttbar_CMS_eff_JECUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		ttbar_JEC_Down = TH1F("ttbar_CMS_eff_JECDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		ttbar_JER_Up = TH1F("ttbar_CMS_eff_JERUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		ttbar_JER_Down = TH1F("ttbar_CMS_eff_JERDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		ttbar_trig_up = TH1F("ttbar_CMS_eff_trigUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		ttbar_trig_down = TH1F("ttbar_CMS_eff_trigDown", "", len(binBoundaries)-1, array('d',binBoundaries))
	#	ttbar_ptNorm_Up = TH1F("ttbar_CMS_eff_ptNormUp", "", len(binBoundaries)-1, array('d',binBoundaries))
#		ttbar_ptNorm_Down = TH1F("ttbar_CMS_eff_ptNormDown", "", len(binBoundaries)-1, array('d',binBoundaries))
#		ttbar_ptAlpha_Up = TH1F("ttbar_CMS_eff_ptAlphaUp", "", len(binBoundaries)-1, array('d',binBoundaries))
#		ttbar_ptAlpha_Down = TH1F("ttbar_CMS_eff_ptAlphaDown", "", len(binBoundaries)-1, array('d',binBoundaries))

		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_btag_up, variable, tag +"&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeight*SFup*ak4btag1SFup*ak4btag2SFup*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_btag_down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeight*SFdown*ak4btag1SFdown*ak4btag2SFdown*trigWeight*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_csv_up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeight*SF*ak4btag1SFup*ak4btag2SFup*trigWeight*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_csv_down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeight*SF*ak4btag1SFdown*ak4btag2SFdown*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_pu_up, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeightUp*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_pu_down, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeightDown*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_trig_up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeightUp*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_trig_down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeightDown*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_ptNorm_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","2.71828^(0.076875-0.0005*ttHT/2)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_ptNorm_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","2.71828^(0.046125-0.0005*ttHT/2)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
#	      	quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_ptAlpha_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","2.71828^(0.0615-0.000625*ttHT/2)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_ptAlpha_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","2.71828^(0.0615-0.000375*ttHT/2)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF_JECUp.root", "mynewTree", ttbar_JEC_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF_JECDown.root", "mynewTree", ttbar_JEC_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF_JERUp.root", "mynewTree", ttbar_JER_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF_JERDown.root", "mynewTree", ttbar_JER_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		print "made ttbar plots"
#		norm = GetNom(sigpath+"tree_%s.root"%(m))
		norm = signorm[i]
		HTaggingUnc = 1. + abs(ggHH_hbbhbb_mX_htag.GetSumOfWeights()-ggHH_hbbhbb_mX.GetSumOfWeights())/(ggHH_hbbhbb_mX.GetSumOfWeights())
		btaglnN= 1.+ abs(ggHH_hbbhbb_mX_btag_up.GetSumOfWeights()-ggHH_hbbhbb_mX_btag_down.GetSumOfWeights())/(2.*ggHH_hbbhbb_mX.GetSumOfWeights())
#		csvlnN= 1. +  abs(ggHH_hbbhbb_mX_csv_up.GetSumOfWeights()-ggHH_hbbhbb_mX_csv_down.GetSumOfWeights())/(2.*ggHH_hbbhbb_mX.GetSumOfWeights())
		PUlnN= 1.+ abs(ggHH_hbbhbb_mX_pu_up.GetSumOfWeights()-ggHH_hbbhbb_mX_pu_down.GetSumOfWeights())/(2.*ggHH_hbbhbb_mX.GetSumOfWeights())
		triglnN = 1. + abs(ggHH_hbbhbb_mX_trig_up.GetSumOfWeights()-ggHH_hbbhbb_mX_trig_down.GetSumOfWeights())/(2.*ggHH_hbbhbb_mX.GetSumOfWeights())
		JEClnN= 1. + abs(ggHH_hbbhbb_mX_JEC_Up.GetSumOfWeights()-ggHH_hbbhbb_mX_JEC_Down.GetSumOfWeights())/(2.*ggHH_hbbhbb_mX.GetSumOfWeights())
		JERlnN= 1. + abs(ggHH_hbbhbb_mX_JER_Up.GetSumOfWeights()-ggHH_hbbhbb_mX_JER_Down.GetSumOfWeights())/(2.*ggHH_hbbhbb_mX.GetSumOfWeights())
		print "trig Er Sig"
		print triglnN
		btaglnN_ttbar= 1.+ abs(ttbar_btag_up.GetSumOfWeights()-ttbar_btag_down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
#		csvlnN_ttbar= 1. +  abs(ttbar_csv_up.GetSumOfWeights()-ttbar_csv_down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
		PUlnN_ttbar= 1.+ abs(ttbar_pu_up.GetSumOfWeights()-ttbar_pu_down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
		triglnN_ttbar= 1.+ abs(ttbar_trig_up.GetSumOfWeights()-ttbar_trig_down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
#		ptnormlnN_ttbar= 1.+ abs(ttbar_ptNorm_Up.GetSumOfWeights()-ttbar_ptNorm_Down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
#		ptalphalnN_ttbar= 1. + abs(ttbar_ptAlpha_Up.GetSumOfWeights()-ttbar_ptAlpha_Down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
		print "trig Er Top"
		print triglnN_ttbar
		JEClnN_ttbar = 1. + abs(ttbar_JEC_Up.GetSumOfWeights()-ttbar_JEC_Down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
		JERlnN_ttbar = 1. + abs(ttbar_JER_Up.GetSumOfWeights()-ttbar_JER_Down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
		print "defined ln"
		ggHH_hbbhbb_mX.Scale(Options.lumi*0.01/norm)
		ggHH_hbbhbb_mX_htag.Scale(Options.lumi*0.01/norm)
		ggHH_hbbhbb_mX_btag_up.Scale(Options.lumi*0.01/norm)
		ggHH_hbbhbb_mX_btag_down.Scale(Options.lumi*0.01/norm)
		#ggHH_hbbhbb_mX_csv_up.Scale(Options.lumi*0.01/norm)
		#ggHH_hbbhbb_mX_csv_down.Scale(Options.lumi*0.01/norm)
		ggHH_hbbhbb_mX_pu_up.Scale(Options.lumi*0.01/norm)
		ggHH_hbbhbb_mX_pu_down.Scale(Options.lumi*0.01/norm)
		ggHH_hbbhbb_mX_trig_up.Scale(Options.lumi*0.01/norm)
		ggHH_hbbhbb_mX_trig_down.Scale(Options.lumi*0.01/norm)
		ggHH_hbbhbb_mX_JEC_Up.Scale(Options.lumi*0.01/norm)
		ggHH_hbbhbb_mX_JEC_Down.Scale(Options.lumi*0.01/norm)
		ggHH_hbbhbb_mX_JER_Up.Scale(Options.lumi*0.01/norm)
		ggHH_hbbhbb_mX_JER_Down.Scale(Options.lumi*0.01/norm)

		ttbar.Scale(Options.lumi*831.8/71480770)
		ttbar_btag_up.Scale(Options.lumi*831.8/71480770)
		ttbar_btag_down.Scale(Options.lumi*831.8/71480770)
		#ttbar_csv_up.Scale(Options.lumi*831.8/71480770)
		#ttbar_csv_down.Scale(Options.lumi*831.8/71480770)
		ttbar_pu_up.Scale(Options.lumi*831.8/71480770)
		ttbar_pu_down.Scale(Options.lumi*831.8/71480770)
		ttbar_trig_up.Scale(Options.lumi*831.8/71480770)
		ttbar_trig_down.Scale(Options.lumi*831.8/71480770)
#		ttbar_ptNorm_Up.Scale(Options.lumi*831.8/71480770)
#	#	ttbar_ptNorm_Down.Scale(Options.lumi*831.8/71480770)
	#	ttbar_ptAlpha_Up.Scale(Options.lumi*831.8/71480770)
	#	ttbar_ptAlpha_Down.Scale(Options.lumi*831.8/71480770)
		ttbar_JEC_Up.Scale(Options.lumi*831.8/71480770)
		ttbar_JEC_Down.Scale(Options.lumi*831.8/71480770)
		ttbar_JER_Up.Scale(Options.lumi*831.8/71480770)
		ttbar_JER_Down.Scale(Options.lumi*831.8/71480770)
		print "scaled"
#		HTaggingUnc = (1. - math.exp(-0.125052 + 32.5054/(float(m)/2)))+ 1.
#		HTaggingUnc_ttbar = (1. - math.exp(-0.125052 + 32.5054/(float(m)/2)))+ 1.
#		FJEClnN= 1.02
#		JEClnN = 1.02
#		FJERlnN= 1.02
#		JERlnN = 1.02
#		FJEClnN_ttbar= 1.02
#		FJERlnN_ttbar= 1.02
#		JEClnN_ttbar= 1.02
#		JERlnN_ttbar= 1.02
	
		signal_integral = ggHH_hbbhbb_mX.Integral()

		ttbar_integral = ttbar.Integral()

		PDFup = pdfup[i]
		PDFdown = pdfdown[i]
		PDFsup = pdfsup[i]
		PDFsdown = pdfsdown[i]
		PDFup_ttbar = 1.00037
		PDFdown_ttbar = 1.00036
		PDFsup_ttbar = 0.98785
		PDFsdown_ttbar = 1.00015

		qcd_integral = N.Integral()
		qcd = N.Clone(Options.name+"EST")
		qcd_antitag = A.Clone(Options.name+"EST_Antitag")
		qcd_up = NU.Clone(Options.name+"EST_CMS_scale"+Options.name+"_13TeVUp")
		qcd_down = ND.Clone(Options.name+"EST_CMS_scale"+Options.name+"_13TeVDown")
		data_obs = D.Clone("data_obs")
		data_integral = data_obs.Integral() 

		i += 1
	
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
		ggHH_hbbhbb_mX.Write()
		ggHH_hbbhbb_mX_btag_up.Write()
		ggHH_hbbhbb_mX_btag_down.Write()
		#ggHH_hbbhbb_mX_csv_up.Write()
		#ggHH_hbbhbb_mX_csv_down.Write()
		ggHH_hbbhbb_mX_pu_up.Write()
		ggHH_hbbhbb_mX_pu_down.Write()
		ggHH_hbbhbb_mX_trig_up.Write()
		ggHH_hbbhbb_mX_trig_down.Write()
		ggHH_hbbhbb_mX_JEC_Up.Write()
		ggHH_hbbhbb_mX_JEC_Down.Write()
		ggHH_hbbhbb_mX_JER_Up.Write()
		ggHH_hbbhbb_mX_JER_Down.Write()
		ttbar.Write()
		ttbar_btag_up.Write()
		ttbar_btag_down.Write()
		#ttbar_csv_up.Write()
		#ttbar_csv_down.Write()
		ttbar_pu_up.Write()
		ttbar_pu_down.Write()
		ttbar_trig_up.Write()
		ttbar_trig_down.Write()
#		ttbar_ptNorm_Up.Write()
#		ttbar_ptNorm_Down.Write()
#		ttbar_ptAlpha_Up.Write()
#		ttbar_ptAlpha_Down.Write()
		ttbar_JEC_Up.Write()
		ttbar_JEC_Down.Write()
		ttbar_JER_Up.Write()
		ttbar_JER_Down.Write()
		data_obs.Write()
		vh.Write()
		output_file.Write()
		output_file.Close()
		print "wrote"
		text_file = open("outputs/datacards/HH4b_semiBoosted_mX_%s_"%(m)+Options.name+"_13TeV.txt", "w")


		text_file.write("max    1     number of categories\n")
		text_file.write("jmax   2     number of samples minus one\n")
		text_file.write("kmax    *     number of nuisance parameters\n")
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("shapes * * HH4b_semiBoosted_mX_%s_"%(m)+Options.name+"_13TeV.root vh/$PROCESS vh/$PROCESS_$SYSTEMATIC\n")
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("bin                                            hh4b\n")
		text_file.write("observation                                    %f\n"%(data_integral))
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("bin                                             hh4b              hh4b       hh4b\n")
		text_file.write("process                                          0                 1          2  \n")
		text_file.write("process                                 ggHH_hbbhbb_mX_%s_"%(m)+Options.name+"   "+Options.name+"EST    ttbar\n")
		text_file.write("rate                                             %f                %f         %f\n"%(signal_integral,qcd_integral,ttbar_integral))
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("lumi_13TeV lnN                                   1.025             -          1.025\n")	
		text_file.write("ttbar_xsec lnN                                   -                 -           1.048/0.945\n")
		text_file.write("AK4_invariant_mass lnN                           1.005             -          1.005\n") 
		text_file.write("CMS_eff_tau21_sf lnN                             1.136/0.864       -          1.136/0.864\n")
#		text_file.write("CMS_eff_JMS lnN                                  1.0094/0.9906     -          1.0094/0.9906\n")
#		text_file.write("CMS_eff_JMR lnN                                  1.20/0.80         -          1.20/0.80\n")
		text_file.write("CMS_eff_Htag lnN                              %f                -          - \n"%(HTaggingUnc))     
#		text_file.write("CMS_scale_j lnN 		                          %f                -          %f\n"%(JEClnN,JEClnN_ttbar)) 	
		text_file.write("CMS_scale_j lnN 		                          %f                -          %f\n"%(JEClnN,JEClnN_ttbar)) 	
                text_file.write("CMS_massJEC lnN                                  1.02              -        1.02\n")
#		text_file.write("CMS_AK4JEC lnN 		                          %f                -          %f\n"%(JEClnN,JEClnN_ttbar)) 	
		text_file.write("CMS_btag_comb lnN                             %f                -          %f\n"%(btaglnN, btaglnN_ttbar))
#		text_file.write("CMS_eff_csv_sf lnN                               %f                -          %f\n"%(csvlnN, csvlnN_ttbar))
		text_file.write("CMS_res_j lnN                                      %f                -          %f\n"%(JERlnN, JERlnN_ttbar)) 
#		text_file.write("CMS_AK4JER lnN                                      %f                -          %f\n"%(JERlnN, JERlnN_ttbar))
		text_file.write("CMS_PU lnN                                       %f                -          %f\n"%(PUlnN, PUlnN_ttbar))
#		text_file.write("CMS_TRIG lnN                                     %f                -          %f\n"%(triglnN, triglnN_ttbar))
#		text_file.write("CMS_ptnorm lnN                                   -                 -          %f\n"%(ptnormlnN_ttbar))
#		text_file.write("CMS_ptalpha lnN                                  -                 -          %f\n"%(ptalphalnN_ttbar))
		text_file.write("CMS_eff_trig shapeN2                             1.000             -         1.000\n")
		text_file.write("CMS_scale"+Options.name+"_13TeV shapeN2          -                 1.000      -\n")
#		text_file.write("CMS_PDF_Scales lnN                            1.01/0.99         -          -\n")
#		text_file.write("CMS_PDF_HHgg lnN                                1.03              -          -\n")
#		text_file.write("QCDscale_ggHH lnN                               %.6f/%.6f         -         %.6f/%.6f\n"%(PDFsup,PDFsdown,PDFsup_ttbar,PDFsdown_ttbar))
		text_file.write("CMS_PDF_Scales lnN                               %.6f/%.6f         -         %.6f/%.6f\n"%(PDFsup,PDFsdown,PDFsup_ttbar,PDFsdown_ttbar))
		text_file.write("CMS_PDF_HHgg lnN                               %.6f/%.6f         -         %.6f/%.6f\n"%(PDFup,PDFdown,PDFup_ttbar,PDFdown_ttbar))  
#		text_file.write("pdf_ggHH lnN                               %.6f/%.6f         -         %.6f/%.6f\n"%(PDFup,PDFdown, PDFup_ttbar#,PDFdown_ttbar))

		for bin in range(0,len(binBoundaries)-1):
			text_file.write("CMS_stat"+Options.name+"_13TeV_bin%s shapeN2      -       1.000      -\n"%(bin))


		text_file.close()
		print "wrote txt file"
if Options.workspace == "fit":
	print "creating workspace and datacard: ALPHABET ASSISTED FIT"








