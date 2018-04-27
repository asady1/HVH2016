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

parser.add_option("--sig", action="store_true", dest="Sig", default=False)
parser.add_option("--nosig", action="store_false", dest="Sig")

parser.add_option('-I', '--inject', metavar='Inj', type='string', dest='inject', default="none")

parser.add_option('--workspace', metavar='WSPC', type='string', dest='workspace', default="alphabet")
(Options, args) = parser.parse_args()

presel    =   Options.pre
tag = presel + "&(fatjet_mass<135&fatjet_mass>105)&(fatjet_hbb>"+str(Options.cut)+")"
atag = presel + "&(fatjet_mass<135&fatjet_mass>105)&(fatjet_hbb<"+str(Options.cut)+")"
#tag = presel + "&(fatjet_mass<210&fatjet_mass>110)&(fatjet_hbb>"+str(Options.cut)+")"
#atag = presel + "&(fatjet_mass<210&fatjet_mass>110)&(fatjet_hbb<"+str(Options.cut)+")"
#tag = presel + "&(fatjet_mass<135&fatjet_mass>105)&(fatjetptau21<"+str(Options.cut)+")" 
#atag = presel + "&(fatjet_mass<135&fatjet_mass>105)&(fatjetptau21>"+str(Options.cut)+")" 

if Options.finebins:
	binBoundaries=[]
	for i in range(0,1700):	
		binBoundaries.append(450+i*1)
else:
#	binBoundaries =[300,350,400,450, 499, 548, 596, 644, 692, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132]
#	binBoundaries =[450, 499, 548, 596, 644, 692, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132] 
	binBoundaries = [750, 800, 852, 906, 962, 1020, 1080, 1142, 1206, 1272, 1340, 1410, 1482,2100]
#	binBoundaries = [750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250]#, 1300, 1350, 1400, 1450, 1500]
#	binBoundaries = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,95,100,105,110,115,120]
#	binBoundaries = [450, 500, 550,  600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1880, 1960, 2040, 2120]
#	binBoundaries =[450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150]

variable = "Red_mass"
#variable = "fatjetPT"

sigpath = "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/input/"

############# DATASETS: #################
QCD1 = DIST("DATA1", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_300_tree_finally.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*"+str(Options.lumi)+"*347700./39598300")
QCD2 = DIST("DATA2", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_500_tree_finally.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*"+str(Options.lumi)+"*32100./42837570")
QCD3 = DIST("DATA2", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_700_tree_finally.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*"+str(Options.lumi)+"*6831./44384120")
QCD4 = DIST("DATA3", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_1000_tree_finally.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*"+str(Options.lumi)+"*1207./14977450")
QCD5 = DIST("DATA5", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_1500_tree_finally.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*"+str(Options.lumi)+"*119.9/11777410")
QCD6 = DIST("DATA6", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_2000_tree_finally.root","mynewTree","(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*"+str(Options.lumi)+"*25.24/5740311")
#TTBar = DIST("TTBar", "/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/TT_SFs.root", "mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0|dcsvBtag/_|HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*"+str(Options.lumi)+"*831.76/75176620")
#TTBar = DIST("TTBar", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*2.71828^(0.0615-0.0005*ttHT/2)*"+str(Options.lumi)+"*831.8/71480770")
TTBar = DIST("TTBar", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*1.*"+str(Options.lumi)+"*831.8/71480770")
#TTBar = DIST("TTBar", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallyb.root", "mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*0.427638716963*2.71828^(-0.000437930802173*ttHT)*"+str(Options.lumi)+"*831.8/71480770")
#TTBarD = DIST("TTBarD", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_final.root", "mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.*1.*"+str(Options.lumi)+"*831.8/71480770")
JetHTB = DIST("JetHTB", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_B_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagB = DIST("BTagB","root://cmsxrootd.fnal.gov//store/user/asady1/V25/add/BTag_B_tree_add.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTC = DIST("JetHTC", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_C_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagC = DIST("BTagC","root://cmsxrootd.fnal.gov//store/user/asady1/V25/dcsv/BTag_C_tree_dcsv.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTD = DIST("JetHTD", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_D_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagD = DIST("BTagD","root://cmsxrootd.fnal.gov//store/user/asady1/V25/dcsv/BTag_D_tree_dcsv.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTE = DIST("JetHTE", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_E_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagE = DIST("BTagE","root://cmsxrootd.fnal.gov//store/user/asady1/V25/dcsv/BTag_E_tree_dcsv.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTF = DIST("JetHTF", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_F_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagF = DIST("BTagF","root://cmsxrootd.fnal.gov//store/user/asady1/V25/dcsv/BTag_F_tree_dcsv.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTG = DIST("JetHTG", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_G_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagG = DIST("BTagG","root://cmsxrootd.fnal.gov//store/user/asady1/V25/dcsv/BTag_G_tree_dcsv.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")
JetHTH = DIST("JetHTH", "root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_H_tree_finally1p1b.root","mynewTree", "(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)")
#BTagH = DIST("BTagH","root://cmsxrootd.fnal.gov//store/user/asady1/V25/dcsv/BTag_H_tree_dcsv.root", "mynewTree", "((HLT2_HT800==0)&&((HLT2_Quad_Triple>0)||(HLT2_Double_Triple>0)))")

if Options.isData:
#	DistsWeWantToEstimate = [JetHTB,BTagB,JetHTC,BTagC,JetHTD,BTagD,JetHTE,BTagE,JetHTF,BTagF,BTagG,JetHTH,BTagH,JetHTG]
	DistsWeWantToEstimate = [JetHTB, JetHTC, JetHTD, JetHTE, JetHTF, JetHTG, JetHTH]
#	DistsWeWantToEstimate = [QCD1,QCD2,QCD3,QCD4,QCD5,QCD6,TTBar]
#	DistsWeWantToEstimate = [BTagB, BTagC, BTagD, BTagE, BTagF, BTagG, BTagH]
	whichdataorQCD = "Data"
else:
	DistsWeWantToEstimate = [QCD1,QCD2,QCD3,QCD4,QCD5,QCD6,TTBar]
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
norm0 = 50000.
norm1 = 100000.
norm2 = 100000.
norm3 = 49200.
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
SIG2 = TH1F("Signal_600", "", len(binBoundaries)-1, array('d',binBoundaries))
SIG3 = TH1F("Signal_650", "", len(binBoundaries)-1, array('d',binBoundaries))
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

quickplot(sigpath+"BG_500_tree_finally.root", "mynewTree", SIG0, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
quickplot(sigpath+"BG_550_tree_finally.root", "mynewTree", SIG1, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
quickplot(sigpath+"BG_600_tree_finally.root", "mynewTree", SIG2, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
quickplot(sigpath+"BG_650_tree_finally.root", "mynewTree", SIG3, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_700_tree_finally.root", "mynewTree", SIG4, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
quickplot(sigpath+"BG_750_tree_finally.root", "mynewTree", SIG5, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
quickplot(sigpath+"BG_800_tree_finally.root", "mynewTree", SIG6, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
quickplot(sigpath+"BG_900_tree_finally.root", "mynewTree", SIG7, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
quickplot(sigpath+"BG_1000_tree_finally.root", "mynewTree", SIG8, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
quickplot(sigpath+"BG_1200_tree_finally.root", "mynewTree", SIG9, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_1400_tree_finally.root", "mynewTree", SIG10, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
quickplot(sigpath+"BG_1600_tree_finally.root", "mynewTree", SIG11, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
#quickplot(sigpath+"BG_1800_tree_finally.root", "mynewTree", SIG12, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")
quickplot(sigpath+"BG_2000_tree_finally.root", "mynewTree", SIG13, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "1.")

SIG0.Scale(Options.lumi*0.01/norm0)
SIG1.Scale(Options.lumi*0.01/norm1)
SIG2.Scale(Options.lumi*0.01/norm2)
SIG3.Scale(Options.lumi*0.01/norm3)
#SIG4.Scale(Options.lumi*0.01/norm4)
SIG5.Scale(Options.lumi*0.01/norm5)
SIG6.Scale(Options.lumi*0.01/norm6)
SIG7.Scale(Options.lumi*0.01/norm7)
SIG8.Scale(Options.lumi*0.01/norm8)
SIG9.Scale(Options.lumi*0.01/norm9)
#SIG10.Scale(Options.lumi*0.01/norm10)
SIG11.Scale(Options.lumi*0.01/norm11)
#SIG12.Scale(Options.lumi*0.01/norm12)
SIG13.Scale(Options.lumi*0.01/norm13)

SIG0.SetLineColor(kMagenta - 9)
SIG1.SetLineColor(kMagenta - 6)
SIG2.SetLineColor(kMagenta - 3)
SIG3.SetLineColor(kMagenta)
#SIG4.SetLineColor(kPink + 8) 
SIG5.SetLineColor(kPink + 7)
SIG6.SetLineColor(kPink + 3)
SIG7.SetLineColor(kPink - 6)
SIG8.SetLineColor(kPink - 4)
SIG9.SetLineColor(kRed - 7)
#SIG10.SetLineColor(kRed - 3)
SIG11.SetLineColor(kRed)
#SIG12.SetLineColor(kRed + 2)
SIG13.SetLineColor(kRed + 3)

var_array = ["fatjet_mass", "fatjet_hbb", 50,45,195, 100, -1., 1.]
#var_array = ["fatjetat_mass", "fatjetptau21", 60,50,200, 100, 0, 1.]
#var_array = ["jet1pmass", "jet1bbtag", 60,50,200, 100, -1., 1.]

Hbb = Alphabetizer(Options.name, DistsWeWantToEstimate, [TTBar])
Hbb.SetRegions(var_array, presel)

bins = binCalc(45,195,105,135,Options.bin)
if Options.Linear:
	print "linear"
	#F = LinearFit([0.0,0.0], -75, 85, "linfit", "EMRNSQ")
	F = CubicFit([0.1,0.1,0.1,0.1], -75, 85, "linfit", "EMRFNEX0")
else:
	print "quad"
	F = QuadraticFit([0.1,0.1,0.1], -75, 75, "quadfit", "EMRFNEX0")
#	F = LinearFit([0.0,0.0], -75, 85, "linfit", "EMRNSQ")
#	F = CubicFit([0.1,0.1,0.1,0.1], -75, 85, "quadfit", "EMRFNEX0")
Hbb.TwoDPlot.Draw("COLZ")
Hbb.GetRates([Options.cut, ">"], bins[0], bins[1], 120., F)
print bins[0]
print bins[1]
#Hbb.TwoDPlot.Draw("COLZ")

Hbb.TwoDPlot.SetStats(0)
C1 = TCanvas("C1", "", 800, 600)
C1.cd()
Hbb.TwoDPlot.Draw("COLZ")
#tpf = Hbb.TwoDPlot.ProfileX("pfx",0,100)
#tpf.SetLineWidth(6)
#tpf.SetLineColor(1)
#tpf.Draw("same")
Hbb.TwoDPlot.GetXaxis().SetTitle("jet mass (GeV)")
Hbb.TwoDPlot.GetYaxis().SetTitle("double b-tagger")
C1.SaveAs("outputs/HH4b2p1SR_2D_"+Options.name+".pdf")
C1.SaveAs("outputs/HH4b2p1SR_2D_"+Options.name+".C")

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
plotforplotting.GetYaxis().SetRangeUser(0,0.1)
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

vartitle = "m_{X}^{red} (GeV)"
#vartitle = "AK8 Jet p_{T} (GeV)"

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

for c in range(1, N.GetNbinsX()+1):
	print "ALICE LOOK HERE"
	print c
	print N.GetBinContent(c)
	print D.GetBinContent(c)

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
print "ALICE: up " + str(NU.Integral())
print "ALice: down " + str(ND.Integral())
print "ALice: norm " + str(N.Integral())
if Options.Truth:
	D.Draw("E0")
#	D.GetYaxis().SetRangeUser(0,80)
N.Draw("same Hist")
TTNom.Draw("same Hist")
for i in Boxes:
	i.Draw("same")
for i in sBoxes:
	i.Draw("same")
if Options.Sig:
	SIG2.Draw("same hist")
	SIG6.Draw("same hist")
	SIG8.Draw("same hist")
if Options.Truth:
        D.Draw("same E0")
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
#C4.SaveAs("outputs/HH4b2p1_Plot_"+Options.name+".pdf")
C4.SaveAs("outputs/HH4b2p1_Plot_"+Options.name+".pdf")
C4.SaveAs("outputs/HH4b2p1_Plot_"+Options.name+".C")

if Options.workspace == "alphabet":
	print "creating workspace and datacard: ALPHABET"

	mass=[750,800,900,1000,1200,1600,2000]
	i = 0
	signorm = [50000., 100000., 50000., 49200., 50000., 50000., 50000.]
	pdfup = [0.997, 0.996, 0.996, 0.995, 0.993, 0.993, 0.972]
	pdfdown = [0.995, 0.995, 0.994, 0.993, 0.991, 0.992, 0.969]
	for m in mass:
		print str(m)
	        UD = ['Up','Down']
	
		output_file = TFile("outputs/datacards/HH4b2p1_BG_mX_%s_"%(m)+Options.name+"_13TeV.root", "RECREATE")
		vh=output_file.mkdir("vh")
		vh.cd()
		print "made output file"
		Signal_mX = TH1F("Signal_mX_%s_"%(m)+Options.name, "", len(binBoundaries)-1, array('d',binBoundaries))
		#Signal_mX_csv_up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_csvUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		#Signal_mX_csv_down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_csvDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_btag_up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_btagUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_btag_down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_btagDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_pu_up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_puUp", "", len(binBoundaries)-1, array('d',binBoundaries))
	 	Signal_mX_pu_down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_puDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_JEC_Up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_JECUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_JEC_Down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_JECDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_JER_Up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_JERUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_JER_Down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_JERDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_trig_Up = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_trigUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		Signal_mX_trig_Down = TH1F("Signal_mX_%s_"%(m)+Options.name+"_CMS_eff_trigDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		
		quickplot(sigpath+"BG_%s_tree_bfinallyb.root"%(m), "mynewTree", Signal_mX, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"BG_%s_tree_bfinallyb.root"%(m), "mynewTree", Signal_mX_btag_up, variable, tag +"&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SFup*ak4btag1SFup*ak4btag2SFup*trigWeight*1.03/1.")
		quickplot(sigpath+"BG_%s_tree_bfinallyb.root"%(m), "mynewTree", Signal_mX_btag_down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SFdown*ak4btag1SFdown*ak4btag2SFdown*trigWeight*1.03/1.")
#		quickplot(sigpath+"BG_%s_tree_finallyb.root"%(m), "mynewTree", Signal_mX_csv_up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SFup*ak4btag2SFup*trigWeight*1.03/1.")
#		quickplot(sigpath+"BG_%s_tree_finallyb.root"%(m), "mynewTree", Signal_mX_csv_down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SFdown*ak4btag2SFdown*trigWeight*1.03/1.")
		quickplot(sigpath+"BG_%s_tree_bfinallyb.root"%(m), "mynewTree", Signal_mX_pu_up, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeightUp*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"BG_%s_tree_bfinallyb.root"%(m), "mynewTree", Signal_mX_pu_down, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeightDown*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"BG_%s_tree_bfinallyb.root"%(m), "mynewTree", Signal_mX_trig_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeightUp*1.03/1.")
		quickplot(sigpath+"BG_%s_tree_bfinallyb.root"%(m), "mynewTree", Signal_mX_trig_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeightDown*1.03/1.")
		quickplot(sigpath+"BG_%s_tree_bfinallyb__JECUp.root"%(m), "mynewTree", Signal_mX_JEC_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"BG_%s_tree_bfinallyb__JECDown.root"%(m), "mynewTree", Signal_mX_JEC_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"BG_%s_tree_bfinallyb__JERUp.root"%(m), "mynewTree", Signal_mX_JER_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot(sigpath+"BG_%s_tree_bfinallyb__JERDown.root"%(m), "mynewTree", Signal_mX_JER_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)", "puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
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
		ttbar_trig_Up = TH1F("ttbar_CMS_eff_trigUp", "", len(binBoundaries)-1, array('d',binBoundaries))
		ttbar_trig_Down = TH1F("ttbar_CMS_eff_trigDown", "", len(binBoundaries)-1, array('d',binBoundaries))
		#ttbar_xsec_Down = TH1F("ttbar_xsec_Down", "", len(binBoundaries)-1, array('d',binBoundaries))
		#ttbar_xsec_Up= TH1F("ttbar_xsec_Up", "", len(binBoundaries)-1, array('d',binBoundaries))
#		ttbar_ptNorm_Up = TH1F("ttbar_CMS_eff_ptNormUp", "", len(binBoundaries)-1, array('d',binBoundaries))
#		ttbar_ptNorm_Down = TH1F("ttbar_CMS_eff_ptNormDown", "", len(binBoundaries)-1, array('d',binBoundaries))
#		ttbar_ptAlpha_Up = TH1F("ttbar_CMS_eff_ptAlphaUp", "", len(binBoundaries)-1, array('d',binBoundaries))
#		ttbar_ptAlpha_Down = TH1F("ttbar_CMS_eff_ptAlphaDown", "", len(binBoundaries)-1, array('d',binBoundaries))

		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_btag_up, variable, tag +"&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SFup*ak4btag1SFup*ak4btag2SFup*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_btag_down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SFdown*ak4btag1SFdown*ak4btag2SFdown*trigWeight*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_csv_up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SF*ak4btag1SFup*ak4btag2SFup*trigWeight*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_csv_down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SF*ak4btag1SFdown*ak4btag2SFdown*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_pu_up, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeightUp*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_pu_down, variable, tag + "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeightDown*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_trig_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeightUp*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF.root", "mynewTree", ttbar_trig_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeightDown*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_xsec_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SF*ak4btag1SF*ak4btag2SF*0.945*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_xsec_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SF*ak4btag1SF*ak4btag2SF*1.048*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_ptNorm_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*2.71828^(0.076875-0.0005*ttHT/2)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_ptNorm_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*2.71828^(0.046125-0.0005*ttHT/2)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
#	      	quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_ptAlpha_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*2.71828^(0.0615-0.000625*ttHT/2)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
#		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_finallybSF.root", "mynewTree", ttbar_ptAlpha_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*2.71828^(0.0615-0.000375*ttHT/2)*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF_JECUp.root", "mynewTree", ttbar_JEC_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF_JECDown.root", "mynewTree", ttbar_JEC_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF_JERUp.root", "mynewTree", ttbar_JER_Up, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		quickplot("root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinallybSF_JERDown.root", "mynewTree", ttbar_JER_Down, variable, tag+ "&(HLT2_HT800>0||HLT2_DiPFJet280>0||HLT2_AK8PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_AK8PFJet360>0||HLT2_PFHT650>0||HLT2_PFHT900>0||HLT2_AK8PFHT700>0)","1.*1.*puWeight*SF*ak4btag1SF*ak4btag2SF*trigWeight*1.03/1.")
		print "made ttbar plots"
#		norm = GetNom(sigpath+"tree_%s.root"%(m))
		norm = signorm[i]
		btaglnN= 1.+ abs(Signal_mX_btag_up.GetSumOfWeights()-Signal_mX_btag_down.GetSumOfWeights())/(2.*Signal_mX.GetSumOfWeights())
#		csvlnN= 1. +  abs(Signal_mX_csv_up.GetSumOfWeights()-Signal_mX_csv_down.GetSumOfWeights())/(2.*Signal_mX.GetSumOfWeights())
		PUlnN= 1.+ abs(Signal_mX_pu_up.GetSumOfWeights()-Signal_mX_pu_down.GetSumOfWeights())/(2.*Signal_mX.GetSumOfWeights())
		triglnN = 1. + abs(Signal_mX_trig_Up.GetSumOfWeights()-Signal_mX_trig_Down.GetSumOfWeights())/(2.*Signal_mX.GetSumOfWeights())
		JEClnN= 1. + abs(Signal_mX_JEC_Up.GetSumOfWeights()-Signal_mX_JEC_Down.GetSumOfWeights())/(2.*Signal_mX.GetSumOfWeights())
		JERlnN= 1. + abs(Signal_mX_JER_Up.GetSumOfWeights()-Signal_mX_JER_Down.GetSumOfWeights())/(2.*Signal_mX.GetSumOfWeights())

		btaglnN_ttbar= 1.+ abs(ttbar_btag_up.GetSumOfWeights()-ttbar_btag_down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
#		csvlnN_ttbar= 1. +  abs(ttbar_csv_up.GetSumOfWeights()-ttbar_csv_down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
		PUlnN_ttbar= 1.+ abs(ttbar_pu_up.GetSumOfWeights()-ttbar_pu_down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
		triglnN_ttbar= 1.+ abs(ttbar_trig_Up.GetSumOfWeights()-ttbar_trig_Down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
	#	ptnormlnN_ttbar= 1.+ abs(ttbar_ptNorm_Up.GetSumOfWeights()-ttbar_ptNorm_Down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
	#	ptalphalnN_ttbar= 1. + abs(ttbar_ptAlpha_Up.GetSumOfWeights()-ttbar_ptAlpha_Down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
		JEClnN_ttbar = 1. + abs(ttbar_JEC_Up.GetSumOfWeights()-ttbar_JEC_Down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
		JERlnN_ttbar = 1. + abs(ttbar_JER_Up.GetSumOfWeights()-ttbar_JER_Down.GetSumOfWeights())/(2.*ttbar.GetSumOfWeights())
		print "defined ln"
		Signal_mX.Scale(Options.lumi*0.01/norm)
		Signal_mX_btag_up.Scale(Options.lumi*0.01/norm)
		Signal_mX_btag_down.Scale(Options.lumi*0.01/norm)
#		Signal_mX_csv_up.Scale(0.01*Options.lumi/norm)
#		Signal_mX_csv_down.Scale(0.01*Options.lumi/norm)
		Signal_mX_pu_up.Scale(Options.lumi*0.01/norm)
		Signal_mX_pu_down.Scale(Options.lumi*0.01/norm)
		Signal_mX_trig_Up.Scale(Options.lumi*0.01/norm)
		Signal_mX_trig_Down.Scale(Options.lumi*0.01/norm)
		Signal_mX_JEC_Up.Scale(Options.lumi*0.01/norm)
		Signal_mX_JEC_Down.Scale(Options.lumi*0.01/norm)
		Signal_mX_JER_Up.Scale(Options.lumi*0.01/norm)
		Signal_mX_JER_Down.Scale(Options.lumi*0.01/norm)

		ttbar.Scale(Options.lumi*831.8/71480770)
		ttbar_btag_up.Scale(Options.lumi*831.8/71480770)
		ttbar_btag_down.Scale(Options.lumi*831.8/71480770)
#		ttbar_csv_up.Scale(Options.lumi*831.8/71480770)
#		ttbar_csv_down.Scale(Options.lumi*831.8/71480770)
		ttbar_pu_up.Scale(Options.lumi*831.8/71480770)
		ttbar_pu_down.Scale(Options.lumi*831.8/71480770)
		ttbar_trig_Up.Scale(Options.lumi*831.8/71480770)
		ttbar_trig_Down.Scale(Options.lumi*831.8/71480770)
		#ttbar_ptNorm_Up.Scale(Options.lumi*831.8/71480770)
		#ttbar_ptNorm_Down.Scale(Options.lumi*831.8/71480770)
		#ttbar_ptAlpha_Up.Scale(Options.lumi*831.8/71480770)
		#ttbar_ptAlpha_Down.Scale(Options.lumi*831.8/71480770)
		#ttbar_xsec_Down.Scale(Options.lumi*831.8/71480770)
		#ttbar_xsec_Up.Scale(Options.lumi*831.8/71480770)
		ttbar_JEC_Up.Scale(Options.lumi*831.8/71480770)
		ttbar_JEC_Down.Scale(Options.lumi*831.8/71480770)
		ttbar_JER_Up.Scale(Options.lumi*831.8/71480770)
		ttbar_JER_Down.Scale(Options.lumi*831.8/71480770)
		print "scaled"
		HTaggingUnc = (1. - math.exp(-0.125052 + 32.5054/(float(m)/2)))+ 1.
#		HTaggingUnc_ttbar = (1. - math.exp(-0.125052 + 32.5054/(float(m)/2)))+ 1.
#		FJEClnN= 1.02
#		JEClnN = 1.02
#		FJERlnN= 1.02
#		JERlnN = 1.02
#		FJEClnN_ttbar= 1.02
#		FJERlnN_ttbar= 1.02
#		JEClnN_ttbar= 1.02
#		JERlnN_ttbar= 1.02
	
		signal_integral = Signal_mX.Integral()

		ttbar_integral = ttbar.Integral()

		PDFup = pdfup[i]
		PDFdown = pdfdown[i]
		PDFup_ttbar = 0.987857078733
		PDFdown_ttbar = 1.00015458763


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
		Signal_mX.Write()
		Signal_mX_btag_up.Write()
		Signal_mX_btag_down.Write()
#		Signal_mX_csv_up.Write()
#		Signal_mX_csv_down.Write()
		Signal_mX_pu_up.Write()
		Signal_mX_pu_down.Write()
		Signal_mX_trig_Up.Write()
		Signal_mX_trig_Down.Write()
		Signal_mX_JEC_Up.Write()
		Signal_mX_JEC_Down.Write()
		Signal_mX_JER_Up.Write()
		Signal_mX_JER_Down.Write()
		ttbar.Write()
		ttbar_btag_up.Write()
		ttbar_btag_down.Write()
#		ttbar_csv_up.Write()
#		ttbar_csv_down.Write()
		ttbar_pu_up.Write()
		ttbar_pu_down.Write()
		ttbar_trig_Up.Write()
		ttbar_trig_Down.Write()
		#ttbar_xsec_Down.Write()
		#ttbar_xsec_Up.Write()
		#ttbar_ptNorm_Up.Write()
		#ttbar_ptNorm_Down.Write()
		#ttbar_ptAlpha_Up.Write()
		#ttbar_ptAlpha_Down.Write()
		ttbar_JEC_Up.Write()
		ttbar_JEC_Down.Write()
		ttbar_JER_Up.Write()
		ttbar_JER_Down.Write()
		data_obs.Write()
		vh.Write()
		output_file.Write()
		output_file.Close()
		print "wrote"
		text_file = open("outputs/datacards/HH4b2p1_BG_mX_%s_"%(m)+Options.name+"_13TeV.txt", "w")


		text_file.write("max    1     number of categories\n")
		text_file.write("jmax   2     number of samples minus one\n")
		text_file.write("kmax    *     number of nuisance parameters\n")
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("shapes * * HH4b2p1_BG_mX_%s_"%(m)+Options.name+"_13TeV.root vh/$PROCESS vh/$PROCESS_$SYSTEMATIC\n")
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("bin                                            vh4b\n")
		text_file.write("observation                                    %f\n"%(data_integral))
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("bin                                             vh4b              vh4b       vh4b\n")
		text_file.write("process                                          0                 1          2  \n")
		text_file.write("process                                 Signal_mX_%s_"%(m)+Options.name+"   "+Options.name+"EST    ttbar\n")
		text_file.write("rate                                             %f                %f         %f\n"%(signal_integral,qcd_integral,ttbar_integral))
		text_file.write("-------------------------------------------------------------------------------\n")
		text_file.write("lumi_13TeV lnN                                   1.025             -          1.025\n")	
		text_file.write("ttbar_xsec lnN                                   -                 -           1.048/0.945\n")
		text_file.write("AK4_invariant_mass lnN                           1.005             -          1.005\n") 
		text_file.write("CMS_eff_tau21_sf lnN                             1.136/0.864       -          1.136/0.864\n")
#		text_file.write("CMS_eff_JMS lnN                                  1.0094/0.9906     -          1.0094/0.9906\n")
#		text_file.write("CMS_eff_JMR lnN                                  1.20/0.80         -          1.20/0.80\n")
		text_file.write("CMS_eff_Htag lnN                              %f                -          - \n"%(HTaggingUnc))     
		text_file.write("CMS_JEC lnN 		                          %f                -          %f\n"%(JEClnN,JEClnN_ttbar)) 	
                text_file.write("CMS_massJEC lnN                                  1.02              -        1.02\n")
#		text_file.write("CMS_AK4JEC lnN 		                          %f                -          %f\n"%(JEClnN,JEClnN_ttbar)) 	
		text_file.write("CMS_eff_bbtag_sf lnN                             %f                -          %f\n"%(btaglnN, btaglnN_ttbar))
#		text_file.write("CMS_eff_csv_sf lnN                               %f                -          %f\n"%(csvlnN, csvN_ttbar))
		text_file.write("CMS_JER lnN                                      %f                -          %f\n"%(JERlnN, JERlnN_ttbar))
#		text_file.write("CMS_AK4JER lnN                                      %f                -          %f\n"%(JERlnN, JERlnN_ttbar))
		text_file.write("CMS_PU lnN                                       %f                -          %f\n"%(PUlnN, PUlnN_ttbar))
#		text_file.write("CMS_TRIG lnN                                     %f                -          %f\n"%(triglnN, triglnN_ttbar))
		#text_file.write("CMS_ptnorm lnN                                   -                 -          %f\n"%(ptnormlnN_ttbar))
		#text_file.write("CMS_ptalpha lnN                                  -                 -          %f\n"%(ptalphalnN_ttbar))
		text_file.write("CMS_eff_trig shapeN2                             1.000             -         1.000\n")
		text_file.write("CMS_scale"+Options.name+"_13TeV shapeN2          -                 1.000      -\n")
		text_file.write("CMS_PDF_Scales lnN                               %.6f/%.6f         -         %.6f/%.6f\n"%(PDFup,PDFdown, PDFup_ttbar,PDFdown_ttbar))

		for bin in range(0,len(binBoundaries)-1):
			text_file.write("CMS_stat"+Options.name+"_13TeV_bin%s shapeN2      -       1.000      -\n"%(bin))


		text_file.close()
		print "wrote txt file"
if Options.workspace == "fit":
	print "creating workspace and datacard: ALPHABET ASSISTED FIT"








