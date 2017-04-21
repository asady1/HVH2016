import os
#import numpy
import glob
import math    

import ROOT 
#ROOT.gROOT.Macro("rootlogon.C")
from ROOT import *

import FWCore.ParameterSet.Config as cms

import sys
from DataFormats.FWLite import Events, Handle

from array import *

from optparse import OptionParser
parser = OptionParser()

parser.add_option("-o", "--outName", dest="outName",
                  help="output file name")
parser.add_option("-t", "--saveTrig", dest="saveTrig",
                  help="trigger info saved")
parser.add_option("-b", "--ttbar", dest="ttbar",
                  help="isttbar")
parser.add_option("-d", "--data", dest="data",
                  help="isdata")
(options, args) = parser.parse_args()
outputfilename = options.outName

#AK4 btag SF calculation loaded here
ROOT.gSystem.Load('libCondFormatsBTauObjects') 
ROOT.gSystem.Load('libCondToolsBTau') 
calib = ROOT.BTagCalibration('DeepCSV', 'DeepCSV_Moriond17_B_H.csv')
v_sys = getattr(ROOT, 'vector<string>')()
v_sys.push_back('up')
v_sys.push_back('down')
readerb = ROOT.BTagCalibrationReader(
    1,             
    "central",      
    v_sys,          
)
readerb.load(
    calib, 
    0,          
    "comb"     
)
readerc = ROOT.BTagCalibrationReader(
    1,             
    "central",      
    v_sys,          
)
readerc.load(
    calib, 
    1,          
    "comb"     
)
readerl = ROOT.BTagCalibrationReader(
    1,             
    "central",      
    v_sys,          
)
readerl.load(
    calib, 
    2,          
    "incl"     
)

#numberLimit = float(sys.argv[1])

f = ROOT.TFile.Open(sys.argv[1],"READ")

f2 =  ROOT.TFile(outputfilename, 'recreate')
#print outputfilename
f2.cd()

treeMine  = f.Get('myTree')

mynewTree = ROOT.TTree('mynewTree', 'mynewTree')

f1 = array('f', [-100.0])
g1 = array('f', [-100.0])
h1 = array('f', [-100.0])
i1 = array('f', [-100.0])
l1 = array('f', [-100.0])
o1 = array('f', [-100.0])
u1 = array('f', [-100.0])
LL = array('f', [-100.0])
LT = array('f', [-100.0])
TT = array('f', [-100.0])
v1 = array('f', [-100.0])
fatjetPT = array('f', [-100.0])
fatjetETA = array('f', [-100.0])
fatjetPHI = array('f', [-100.0])
fatjetM = array('f', [-100.0])
ak4nfatjetPT = array('f', [-100.0])
ak4nfatjetETA = array('f', [-100.0])
ak4nfatjetPHI = array('f', [-100.0])
ak4nfatjetM = array('f', [-100.0])
sak4nfatjetPT = array('f', [-100.0])
sak4nfatjetETA = array('f', [-100.0])
sak4nfatjetPHI = array('f', [-100.0])
sak4nfatjetM = array('f', [-100.0])
fatjetl1l2l3 = array('f', [-100.0])
fatjetl2l3 = array('f', [-100.0])
fatjetJER = array('f', [-100.0])
fatjetMatchedHadW = array('f', [-100.0])
fatjettau32 = array('f', [-100.0])
fatjettau21 = array('f', [-100.0])
fatjetptau21 = array('f', [-100.0])
fatjettau31 = array('f', [-100.0])
fatjetAKCAratio = array('f', [-100.0])
fatjetCAPT = array('f', [-100.0])
fatjetCAETA = array('f', [-100.0])
fatjetCAPHI = array('f', [-100.0])
fatjetCAM = array('f', [-100.0])
bjet1PT = array('f', [-100.0])
bjet1ETA = array('f', [-100.0])
bjet1PHI = array('f', [-100.0])
bjet1M = array('f', [-100.0])
bjet2PT = array('f', [-100.0])
bjet2ETA = array('f', [-100.0])
bjet2PHI = array('f', [-100.0])
bjet2M = array('f', [-100.0])
ak4nbjet1PT = array('f', [-100.0])
ak4nbjet1ETA = array('f', [-100.0])
ak4nbjet1PHI = array('f', [-100.0])
ak4nbjet1M = array('f', [-100.0])
ak4nbjet2PT = array('f', [-100.0])
ak4nbjet2ETA = array('f', [-100.0])
ak4nbjet2PHI = array('f', [-100.0])
ak4nbjet2M = array('f', [-100.0])
HT = array('f', [-100.0])
nAK4 = array('f', [-100.0])
nAK4near1 = array('f', [-100.0])
nAK4near2 = array('f', [-100.0])
ak4btag1 = array('f', [-100.0])
ak4btag2 = array('f', [-100.0])
#trigger1 = array('f', [-100.0])
#trigger2 = array('f', [-100.0])
#trigger3 = array('f', [-100.0])
#trigger_pre = array('f', [-100.0])
ak4jetCorr1 = array('f', [-100.0])
ak4jetCorr2 = array('f', [-100.0])
ak4jetCorrJECUp1 = array('f', [-100.0])
ak4jetCorrJECUp2 = array('f', [-100.0])
ak4jetCorrJECDown1 = array('f', [-100.0])
ak4jetCorrJECDown2 = array('f', [-100.0])
ak4jetCorrJER1 = array('f', [-100.0])
ak4jetCorrJER2 = array('f', [-100.0])
ak4jetCorrJERUp1 = array('f', [-100.0])
ak4jetCorrJERUp2 = array('f', [-100.0])
ak4jetCorrJERDown1 = array('f', [-100.0])
ak4jetCorrJERDown2 = array('f', [-100.0])    
ak4jetflav1 = array('f', [-100.0])
ak4jetflav2 = array('f', [-100.0])

if options.ttbar == "True":
    ttHT = array('f', [-100.0])
SF = array('f', [-100.0])
SFup = array('f', [-100.0])
SFdown = array('f', [-100.0])
    
ak4btag1SF = array('f', [-100.0])
ak4btag1SFup = array('f', [-100.0])
ak4btag1SFdown = array('f', [-100.0])
ak4btag2SF = array('f', [-100.0])
ak4btag2SFup = array('f', [-100.0])
ak4btag2SFdown = array('f', [-100.0])
    
puW_up = array('f', [-100.0])
puW_down = array('f', [-100.0])
 
if options.saveTrig == 'True':
    HLT2_HT800 = array('f', [-100.0])  
    HLT2_Quad_Triple = array('f', [-100.0])
    HLT2_Double_Triple = array('f', [-100.0])
    HLT2_DiPFJet280 = array('f', [-100.0])
    HLT2_AK8PFHT650 = array('f', [-100.0])
    HLT2_AK8PFJet360 = array('f', [-100.0])
    HLT2_PFHT650 = array('f', [-100.0])
    HLT2_PFHT900 = array('f', [-100.0])
    HLT2_AK8PFHT700 = array('f', [-100.0])  
    trigger800 = array('f', [-100.0])
    triggerBtag = array('f', [-100.0])

mynewTree.Branch("Inv_mass", f1, "Invariant mass")
mynewTree.Branch("dijet_mass", g1, "dijet_mass")
mynewTree.Branch("fatjet_mass", h1, "fatjet_mass")
mynewTree.Branch("cross_section", i1, "cross_section")
mynewTree.Branch("fatjet_hbb", l1, "fatjet_hbb")
mynewTree.Branch("puWeight", o1, "puWeight")
mynewTree.Branch("boosted", u1, "boosted")
mynewTree.Branch("LL", LL, "LL")
mynewTree.Branch("LT", LT, "LT")
mynewTree.Branch("TT", TT, "TT")
mynewTree.Branch("resolved", v1, "resolved")
mynewTree.Branch("ak4nfatjetPT", ak4nfatjetPT, "ak4nfatjetPT")
mynewTree.Branch("ak4nfatjetETA", ak4nfatjetETA, "ak4nfatjetETA")
mynewTree.Branch("ak4nfatjetPHI", ak4nfatjetPHI, "ak4nfatjetPHI")
mynewTree.Branch("ak4nfatjetM", ak4nfatjetM, "ak4nfatjetM")
mynewTree.Branch("sak4nfatjetPT", sak4nfatjetPT, "sak4nfatjetPT")
mynewTree.Branch("sak4nfatjetETA", sak4nfatjetETA, "sak4nfatjetETA")
mynewTree.Branch("sak4nfatjetPHI", sak4nfatjetPHI, "sak4nfatjetPHI")
mynewTree.Branch("sak4nfatjetM", sak4nfatjetM, "sak4nfatjetM")
mynewTree.Branch("fatjetPT", fatjetPT, "fatjetPT")
mynewTree.Branch("fatjetETA", fatjetETA, "fatjetETA")
mynewTree.Branch("fatjetPHI", fatjetPHI, "fatjetPHI")
mynewTree.Branch("fatjetM", fatjetM, "fatjetM")
mynewTree.Branch("fatjetl1l2l3", fatjetl1l2l3, "fatjetl1l2l3")
mynewTree.Branch("fatjetl2l3", fatjetl2l3, "fatjetl2l3")
mynewTree.Branch("fatjetJER", fatjetJER, "fatjetJER")
mynewTree.Branch("fatjetMatchedHadW", fatjetMatchedHadW, "fatjetMatchedHadW")
mynewTree.Branch("fatjettau32", fatjettau32, "fatjettau32")
mynewTree.Branch("fatjettau21", fatjettau21, "fatjettau21")
mynewTree.Branch("fatjetptau21", fatjetptau21, "fatjetptau21")
mynewTree.Branch("fatjettau31", fatjettau31, "fatjettau31")
mynewTree.Branch("fatjetAKCAratio", fatjetAKCAratio, "fatjetAKCAratio")
mynewTree.Branch("fatjetCAPT", fatjetCAPT, "fatjetCAPT")
mynewTree.Branch("fatjetCAETA", fatjetCAETA, "fatjetCAETA")
mynewTree.Branch("fatjetCAPHI", fatjetCAPHI, "fatjetCAPHI")
mynewTree.Branch("fatjetCAM", fatjetCAM, "fatjetCAM")
mynewTree.Branch("nAK4", nAK4, "nAK4")
mynewTree.Branch("nAK4near1", nAK4near1, "nAK4near1")
mynewTree.Branch("nAK4near2", nAK4near2, "nAK4near2")
mynewTree.Branch("bjet1PT", bjet1PT, "bjet1PT")
mynewTree.Branch("bjet1ETA", bjet1ETA, "bjet1ETA")
mynewTree.Branch("bjet1PHI", bjet1PHI, "bjet1PHI")
mynewTree.Branch("bjet1M", bjet1M, "bjet1M")
mynewTree.Branch("bjet2PT", bjet2PT, "bjet2PT")
mynewTree.Branch("bjet2ETA", bjet2ETA, "bjet2ETA")
mynewTree.Branch("bjet2PHI", bjet2PHI, "bjet2PHI")
mynewTree.Branch("bjet2M", bjet2M, "bjet2M")
mynewTree.Branch("ak4nbjet1PT", ak4nbjet1PT, "ak4nbjet1PT")
mynewTree.Branch("ak4nbjet1ETA", ak4nbjet1ETA, "ak4nbjet1ETA")
mynewTree.Branch("ak4nbjet1PHI", ak4nbjet1PHI, "ak4nbjet1PHI")
mynewTree.Branch("ak4nbjet1M", ak4nbjet1M, "ak4nbjet1M")
mynewTree.Branch("ak4nbjet2PT", ak4nbjet2PT, "ak4nbjet2PT")
mynewTree.Branch("ak4nbjet2ETA", ak4nbjet2ETA, "ak4nbjet2ETA")
mynewTree.Branch("ak4nbjet2PHI", ak4nbjet2PHI, "ak4nbjet2PHI")
mynewTree.Branch("ak4nbjet2M", ak4nbjet2M, "ak4nbjet2M")
mynewTree.Branch("HT", HT, "HT")
mynewTree.Branch("ak4btag1", ak4btag1, "ak4btag1")
mynewTree.Branch("ak4btag2", ak4btag2, "ak4btag2")
mynewTree.Branch("ak4jetCorr1", ak4jetCorr1, "ak4jetCorr1")
mynewTree.Branch("ak4jetCorr2", ak4jetCorr2, "ak4jetCorr2")
mynewTree.Branch("ak4jetCorrJECUp1", ak4jetCorrJECUp1, "ak4jetCorrJECUp1")
mynewTree.Branch("ak4jetCorrJECUp2", ak4jetCorrJECUp2, "ak4jetCorrJECUp2")
mynewTree.Branch("ak4jetCorrJECDown1", ak4jetCorrJECDown1, "ak4jetCorrJECDown1")
mynewTree.Branch("ak4jetCorrJECDown2", ak4jetCorrJECDown2, "ak4jetCorrJECDown2")
mynewTree.Branch("ak4jetCorrJER1", ak4jetCorrJER1, "ak4jetCorrJER1")
mynewTree.Branch("ak4jetCorrJER2", ak4jetCorrJER2, "ak4jetCorrJER2")
mynewTree.Branch("ak4jetCorrJERUp1", ak4jetCorrJERUp1, "ak4jetCorrJERUp1")
mynewTree.Branch("ak4jetCorrJERUp2", ak4jetCorrJERUp2, "ak4jetCorrJERUp2")
mynewTree.Branch("ak4jetCorrJERDown1", ak4jetCorrJERDown1, "ak4jetCorrJERDown1")
mynewTree.Branch("ak4jetCorrJERDown2", ak4jetCorrJERDown2, "ak4jetCorrJERDown2")
mynewTree.Branch("ak4jetflav1", ak4jetflav1, "ak4jetflav1")
mynewTree.Branch("ak4jetflav2", ak4jetflav2, "ak4jetflav2")

#mynewTree.Branch("HLT_ht800", trigger1, "HLT_ht800")
#mynewTree.Branch("HLT_AK08", trigger2, "HLT_AK08")
#mynewTree.Branch("HLT_HH4b", trigger3, "HLT_HH4b")
#mynewTree.Branch("HLT_ht350", trigger_pre, "HLT_ht350")

if options.ttbar == "True":
    mynewTree.Branch("ttHT", ttHT, "ttHT")
mynewTree.Branch("SF", SF, "SF")
mynewTree.Branch("SFup", SFup, "SFup")
mynewTree.Branch("SFdown", SFdown, "SFdown")
mynewTree.Branch("ak4btag1SF", ak4btag1SF, "ak4btag1SF")
mynewTree.Branch("ak4btag1SFup", ak4btag1SFup, "ak4btag1upSF")
mynewTree.Branch("ak4btag1SFdown", ak4btag1SFdown, "ak4btag1downSF")
mynewTree.Branch("ak4btag2SF", ak4btag2SF, "ak4btag2SF")
mynewTree.Branch("ak4btag2SFup", ak4btag2SFup, "ak4btag2SFup")
mynewTree.Branch("ak4btag2SFdown", ak4btag2SFdown, "ak4btag2SFdown")
    
mynewTree.Branch("puWeightUp", puW_up, "puWeightUp")
mynewTree.Branch("puWeightDown", puW_down, "puWeightDown")

if options.saveTrig == 'True':
    mynewTree.Branch('HLT2_HT800', HLT2_HT800, 'HLT2_HT800/F')
    mynewTree.Branch('HLT2_Quad_Triple', HLT2_Quad_Triple, 'HLT2_Quad_Triple/F')
    mynewTree.Branch('HLT2_Double_Triple', HLT2_Double_Triple, 'HLT2_Double_Triple/F')
    mynewTree.Branch('trigger800', trigger800, 'trigger800/F')
    mynewTree.Branch('triggerBtag', triggerBtag, 'triggerBtag/F')
    mynewTree.Branch("HLT2_DiPFJet280", HLT2_DiPFJet280, "HLT2_DiPFJet280")
    mynewTree.Branch("HLT2_AK8PFHT650", HLT2_AK8PFHT650, "HLT2_AK8PFHT650")
    mynewTree.Branch("HLT2_AK8PFJet360", HLT2_AK8PFJet360, "HLT2_AK8PFJet360")
    mynewTree.Branch("HLT2_PFHT650", HLT2_PFHT650, "HLT2_PFHT650")
    mynewTree.Branch("HLT2_PFHT900", HLT2_PFHT900, "HLT2_PFHT900")
    mynewTree.Branch("HLT2_AK8PFHT700", HLT2_AK8PFHT700, "HLT2_AK8PFHT700")

    
nevent = treeMine.GetEntries();

tpo1 = ROOT.TH1F("tpo1", "After jet kinematic cuts", 8,-1, 7)
tpo2 = ROOT.TH1F("tpo2", "After trigger", 8, -1, 7)
tpo3 = ROOT.TH1F("tpo3", "After v-type cut", 8, -1, 7)
tpo4 = ROOT.TH1F("tpo4", "After 1 fatjet + 2 AK4 b tagged dR(fj) jets", 8, -1, 7)
tpo5 = ROOT.TH1F("tpo5", "After fatjet pt, mass, AK4 jets dR", 8, -1, 7)
tpo6 = ROOT.TH1F("tpo6", "After mass cuts", 8, -1, 7)
tpo7 = ROOT.TH1F("tpo7", "After double b 0.8", 8, -1, 7)
tpo8 = ROOT.TH1F("tpo8", "After double b 0.9", 8, -1, 7) 
tpo9 = ROOT.TH1F("tpo9", "After double b 0.6", 8, -1, 7)
if options.data == "False":
    CountWeightedmc = ROOT.TH1F("CountWeighted","Count with sign(gen weight) and pu weight",1,0,2)
    CountWeightedmc.Add(f.Get("CountWeighted"))

counter = 0
for i in range(0, nevent) :
    counter = counter + 1
    treeMine.GetEntry(i)
    triggerpass = 1
    if options.saveTrig == 'True':
        triggerpass = treeMine.HLT_PFHT800_v + treeMine.HLT_QuadJet45_TripleBTagCSV_p087_v + treeMine.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
        btagtrigs = treeMine.HLT_QuadJet45_TripleBTagCSV_p087_v + treeMine.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
        value800 = 0
        valuebtag = 0
        if treeMine.HLT_PFHT800_v > 0 and btagtrigs < 1:
            value800 = 1
        if treeMine.HLT_PFHT800_v < 1 and btagtrigs > 0:
            valuebtag = 1
        trigger800[0] = value800
        triggerBtag[0] = valuebtag

    tpo1.Fill(triggerpass)
    if triggerpass > 0:
        tpo2.Fill(triggerpass) 

    passesVtype = 0
    if treeMine.vtype == -1 or treeMine.vtype == 4:
        passesVtype = 1

    if passesVtype < 1:
        continue
    if triggerpass > 0:
        tpo3.Fill(triggerpass)

    ak8Jet1 = TLorentzVector()
    ak8Jet1.SetPtEtaPhiM(treeMine.jet1pt, treeMine.jet1eta, treeMine.jet1phi, treeMine.jet1mass)

    ak8Jet2 = TLorentzVector()
    ak8Jet2.SetPtEtaPhiM(treeMine.jet2pt, treeMine.jet2eta, treeMine.jet2phi, treeMine.jet2mass)

    ca15Jet1 = TLorentzVector()
    ca15Jet1.SetPtEtaPhiM(treeMine.CA15jet1pt, treeMine.CA15jet1eta, treeMine.CA15jet1phi, treeMine.CA15jet1mass)

    ca15Jet2 = TLorentzVector()
    ca15Jet2.SetPtEtaPhiM(treeMine.CA15jet2pt, treeMine.CA15jet2eta, treeMine.CA15jet2phi, treeMine.CA15jet2mass)
    
    ak4jets1Pre = []
    ak4jets2Pre = []
    ak4jets1csv = []
    ak4jets2csv = []
    ak4jet1ID = []
    ak4jet2ID = []
    ak4corr1 = []
    ak4jecup1 = []
    ak4jecdown1 = []
    ak4jer1 = []
    ak4jerup1 = []
    ak4jerdown1 = []
    ak4flav1 = []
    ak4corr2 = []
    ak4jecup2 = []
    ak4jecdown2 = []
    ak4jer2 = []
    ak4jerup2 = []
    ak4jerdown2 = []
    ak4flav2 = []

    nAK4[0] = len(treeMine.ak4jet_pt)
    
    for j in range(len(treeMine.ak4jet_pt)):
        j_p4=TLorentzVector()
        j_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[j], treeMine.ak4jet_eta[j], treeMine.ak4jet_phi[j], treeMine.ak4jet_mass[j])
        deltaR1=j_p4.DeltaR(ak8Jet1)
        deltaR2=j_p4.DeltaR(ak8Jet2)
        deepCSV = treeMine.ak4jetDeepCSVb[j] + treeMine.ak4jetDeepCSVbb[j]
        if deltaR1 > 0.8 and deepCSV > 0.2219:
            ak4jets1Pre.append(j_p4)
            ak4jets1csv.append(deepCSV)
            ak4jet1ID.append(j)
            if treeMine.isData < 1:
                ak4corr1.append(treeMine.ak4jetCorr[j])
                ak4jecup1.append(treeMine.ak4jetCorrJECUp[j])
                ak4jecdown1.append(treeMine.ak4jetCorrJECDown[j])
                ak4jer1.append(treeMine.ak4jetCorrJER[j])
                ak4jerup1.append(treeMine.ak4jetCorrJERUp[j])
                ak4jerdown1.append(treeMine.ak4jetCorrJERDown[j])
                ak4flav1.append(treeMine.ak4jetMCflavour[j])
        if deltaR2 > 0.8 and deepCSV > 0.2219:
            ak4jets2Pre.append(j_p4)
            ak4jets2csv.append(deepCSV)
            ak4jet2ID.append(j)
            if treeMine.isData < 1:
                ak4corr2.append(treeMine.ak4jetCorr[j])
                ak4jecup2.append(treeMine.ak4jetCorrJECUp[j])
                ak4jecdown2.append(treeMine.ak4jetCorrJECDown[j])
                ak4jer2.append(treeMine.ak4jetCorrJER[j])
                ak4jerup2.append(treeMine.ak4jetCorrJERUp[j])
                ak4jerdown2.append(treeMine.ak4jetCorrJERDown[j])
                ak4flav2.append(treeMine.ak4jetMCflavour[j])

    ak4jet1 = TLorentzVector()
    ak4jet2 = TLorentzVector()

    fatjet = TLorentzVector()
    if len(ak4jets1Pre) < 2 and len(ak4jets2Pre) < 2:
        continue

    if triggerpass > 0:
        tpo4.Fill(triggerpass)

    b_min = 0
    if len(ak4jets1Pre) > 1 and ak8Jet1.Pt() > 250 and treeMine.jet1_puppi_msoftdrop_raw*treeMine.jet1_puppi_TheaCorr > 40:
        fatjet = ak8Jet1
        pmass = treeMine.jet1_puppi_msoftdrop_raw*treeMine.jet1_puppi_TheaCorr
        bbtag = treeMine.jet1bbtag
        if treeMine.jet1tau2 > 0:
            fatjet32 = treeMine.jet1tau3/treeMine.jet1tau2
        else:
            fatjet32 = -100.
        fatjetp21 = treeMine.jet1_puppi_tau21    
        if treeMine.jet1tau1 > 0:
            fatjet21 = treeMine.jet1tau2/treeMine.jet1tau1
            fatjet31 = treeMine.jet1tau3/treeMine.jet1tau1
        else:
            fatjet21 = -100.
            fatjet31 = -100.
        fatjetptCA = treeMine.CA15jet1pt
        fatjetetaCA = treeMine.CA15jet1eta
        fatjetphiCA = treeMine.CA15jet1phi
        fatjetmCA = treeMine.CA15jet1mass
        if treeMine.CA15jet1pt > 0:
            fatjetAKCA = fatjet.Pt()/treeMine.CA15jet1pt
        else:
            fatjetAKCA = -100.
        if treeMine.isData < 1:
            l1l2l3 = treeMine.jet1l1l2l3
            l2l3 = treeMine.jet1l2l3
            ak8jer = treeMine.jet1JER
            hadw = treeMine.LeadingAK8Jet_MatchedHadW
        jet3_p4=TLorentzVector()
        jet4_p4=TLorentzVector()
        for k in range(len(ak4jets1Pre)):
            jet3_p4.SetPtEtaPhiM(ak4jets1Pre[k].Pt(), ak4jets1Pre[k].Eta(), ak4jets1Pre[k].Phi(), ak4jets1Pre[k].M())
            for l in range(len(ak4jets1Pre)):
                if (l!=k):
                    jet4_p4.SetPtEtaPhiM(ak4jets1Pre[l].Pt(), ak4jets1Pre[l].Eta(), ak4jets1Pre[l].Phi(), ak4jets1Pre[l].M())
                    deltaRak4=jet3_p4.DeltaR(jet4_p4)
                    b_add = ak4jets1csv[k] + ak4jets1csv[l]
                    if b_min < b_add and deltaRak4 < 1.5:
                        ak4jet1 = ak4jets1Pre[k]
                        ak4jet1btag = ak4jets1csv[k]
                        ak4jet1i = ak4jet1ID[k]
                        if treeMine.isData < 1:
                            ak4jet1corr = ak4corr1[k]
                            ak4jet1jecup = ak4jecup1[k]
                            ak4jet1jecdown = ak4jecdown1[k]
                            ak4jet1jer = ak4jer1[k]
                            ak4jet1jerup = ak4jerup1[k]
                            ak4jet1jerdown = ak4jerdown1[k]
                            ak4jet1flav = ak4flav1[k]
                        ak4jet2 = ak4jets1Pre[l]
                        ak4jet2btag = ak4jets1csv[l]
                        ak4jet2i = ak4jet1ID[l]
                        if treeMine.isData < 1:
                            ak4jet2corr = ak4corr1[l]
                            ak4jet2jecup = ak4jecup1[l]
                            ak4jet2jecdown = ak4jecdown1[l]
                            ak4jet2jer = ak4jer1[l]
                            ak4jet2jerup = ak4jerup1[l]
                            ak4jet2jerdown = ak4jerdown1[l]
                            ak4jet2flav = ak4flav1[l]
                        b_min = b_add
    if b_min == 0 and len(ak4jets2Pre) > 1 and ak8Jet2.Pt() > 250 and treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr > 40:
        fatjet = ak8Jet2
        pmass = treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr
        bbtag = treeMine.jet2bbtag
        if treeMine.jet2tau2 > 0:
            fatjet32 = treeMine.jet2tau3/treeMine.jet2tau2
        else:
            fatjet32 = -100.
        fatjetp21 = treeMine.jet2_puppi_tau21
        if treeMine.jet2tau1 > 0:
            fatjet21 = treeMine.jet2tau2/treeMine.jet2tau1
            fatjet31 = treeMine.jet2tau3/treeMine.jet2tau1
        else:
            fatjet21 = -100.
            fatjet31 = -100.
        fatjetptCA = treeMine.CA15jet2pt
        fatjetetaCA = treeMine.CA15jet2eta
        fatjetphiCA = treeMine.CA15jet2phi
        fatjetmCA = treeMine.CA15jet2mass
        if treeMine.CA15jet2pt > 0:
            fatjetAKCA = fatjet.Pt()/treeMine.CA15jet2pt
        else:
            fatjetAKCA = -100.
        if treeMine.isData < 1:
            l1l2l3 = treeMine.jet2l1l2l3
            l2l3 = treeMine.jet2l2l3
            ak8jer = treeMine.jet2JER
            hadw = -1.
        b_min = 0.
        jet3_p4=TLorentzVector()
        jet4_p4=TLorentzVector()
        for k in range(len(ak4jets2Pre)):
            jet3_p4.SetPtEtaPhiM(ak4jets2Pre[k].Pt(), ak4jets2Pre[k].Eta(), ak4jets2Pre[k].Phi(), ak4jets2Pre[k].M())
            for l in range(len(ak4jets2Pre)):
                if (l!=k):
                    jet4_p4.SetPtEtaPhiM(ak4jets2Pre[l].Pt(), ak4jets2Pre[l].Eta(), ak4jets2Pre[l].Phi(), ak4jets2Pre[l].M())
                    deltaRak4=jet3_p4.DeltaR(jet4_p4)
                    b_add = ak4jets2csv[k] + ak4jets2csv[l]
                    if b_min < b_add and deltaRak4 < 1.5:
                        ak4jet1 = ak4jets2Pre[k]
                        ak4jet1btag= ak4jets2csv[k]
                        ak4jet1i = ak4jet2ID[k]
                        if treeMine.isData < 1:
                            ak4jet1corr = ak4corr2[k]
                            ak4jet1jecup = ak4jecup2[k]
                            ak4jet1jecdown = ak4jecdown2[k]
                            ak4jet1jer = ak4jer2[k]
                            ak4jet1jerup = ak4jerup2[k]
                            ak4jet1jerdown = ak4jerdown2[k]
                            ak4jet1flav = ak4flav2[k]
                        ak4jet2 = ak4jets2Pre[l]
                        ak4jet2btag= ak4jets2csv[l]
                        ak4jet2i = ak4jet2ID[l]
                        if treeMine.isData < 1:
                            ak4jet2corr = ak4corr2[l]
                            ak4jet2jecup = ak4jecup2[l]
                            ak4jet2jecdown = ak4jecdown2[l]
                            ak4jet2jer = ak4jer2[l]
                            ak4jet2jerup = ak4jerup2[l]
                            ak4jet2jerdown = ak4jerdown2[l]
                            ak4jet2flav = ak4flav2[l]
                        b_min = b_add
    if b_min == 0:
        continue
    
    if triggerpass > 0:
        tpo5.Fill(triggerpass)

    pTH1=(fatjet).Pt()
    pTH2=(ak4jet1+ak4jet2).Pt()
    mH1=pmass
    mH2=(ak4jet1+ak4jet2).M()
    f1[0]=(ak4jet1+ak4jet2+fatjet).M()
    g1[0]=mH2
    h1[0]=mH1
    i1[0]=treeMine.xsec
    l1[0]=bbtag
    o1[0]=treeMine.puWeights
    puW_up[0] = treeMine.puWeightsUp
    puW_down[0] = treeMine.puWeightsDown
    jet1_ungroomed_TL = ROOT.TLorentzVector()
    jet2_ungroomed_TL = ROOT.TLorentzVector()
    jet1_ungroomed_TL.SetPtEtaPhiM(treeMine.jet1pt, treeMine.jet1eta, treeMine.jet1phi, treeMine.jet1mass)
    jet2_ungroomed_TL.SetPtEtaPhiM(treeMine.jet2pt, treeMine.jet2eta, treeMine.jet2phi, treeMine.jet2mass)
    dijetmass_softdrop_corr = (jet1_ungroomed_TL + jet2_ungroomed_TL).M() - (treeMine.jet1_puppi_msoftdrop_raw*treeMine.jet1_puppi_TheaCorr - 125) - (treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr - 125)
    if (treeMine.HLT_PFHT900_v==1 or treeMine.HLT_PFHT800_v==1 or treeMine.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v==1 or treeMine.HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v==1 or treeMine.HLT_AK8PFJet360_TrimMass30_v==1 or treeMine.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v==1 or treeMine.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v==1) and (treeMine.jet1pt > 300 and treeMine.jet2pt > 300 and abs(treeMine.jet1eta) < 2.4 and abs(treeMine.jet2eta) < 2.4) and (abs(treeMine.jet1eta - treeMine.jet2eta) < 1.3) and (treeMine.jet1ID == 1 and treeMine.jet2ID == 1) and (dijetmass_softdrop_corr > 750) and (105 < treeMine.jet1_puppi_msoftdrop_raw*treeMine.jet1_puppi_TheaCorr < 135) and (105 < treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr < 135) and (treeMine.jet1_puppi_tau21 < 0.55 and treeMine.jet2_puppi_tau21 < 0.55):
        u1[0] = 1.
        if (treeMine.jet1bbtag > 0.8 and treeMine.jet2bbtag > 0.8):
            TT[0] = 1.
        if (treeMine.jet1bbtag > 0.3 and treeMine.jet2bbtag > 0.3 and treeMine.jet1bbtag < 0.8 and treeMine.jet2bbtag < 0.8):
            LL[0] = 1.
        if (treeMine.jet1bbtag > 0.8 and treeMine.jet2bbtag > 0.3 and treeMine.jet2bbtag < 0.8):
            LT[0] = 1.
        if (treeMine.jet1bbtag > 0.3 and treeMine.jet1bbtag < 0.8 and treeMine.jet2bbtag > 0.8):
            LT[0] = 1.
    else:
        u1[0] = 0.
        LL[0] = 0.
        TT[0] = 0.
        LT[0] = 0.
    ak4res = []
    chi2_old = 200
    foundRes = False
    v1[0] = 0
    for j in range(len(treeMine.ak4jet_pt)):
        if (treeMine.ak4jetDeepCSVb[j] + treeMine.ak4jetDeepCSVbb[j]) > 0.6324:
            j_p4=TLorentzVector()
            j_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[j], treeMine.ak4jet_eta[j], treeMine.ak4jet_phi[j], treeMine.ak4jet_mass[j])
            ak4res.append(j_p4)
            if len(ak4res) > 3:
                    jet1=TLorentzVector()
                    jet2=TLorentzVector()
                    jet3=TLorentzVector()
                    jet4=TLorentzVector()
                    for l in range(len(ak4res)):
                        jet1.SetPtEtaPhiM(ak4res[l].Pt(), ak4res[l].Eta(), ak4res[l].Phi(), ak4res[l].M())
                        for m in range(len(ak4res)):
                            if m!=l:
                                jet2.SetPtEtaPhiM(ak4res[m].Pt(), ak4res[m].Eta(), ak4res[m].Phi(),ak4res[m].M())
                                for n in range(len(ak4res)):
                                    if (n!=l and n!=m):
                                        jet3.SetPtEtaPhiM(ak4res[n].Pt(), ak4res[n].Eta(), ak4res[n].Phi(),ak4res[n].M())
                                        for k in range(len(ak4res)):
                                            if (k!=l and k!=m and k!=n):
                                                jet4.SetPtEtaPhiM(ak4res[k].Pt(),ak4res[k].Eta(), ak4res[k].Phi(),ak4res[k].M())

                                                dijet1=jet1+jet2
                                                dijet2=jet3+jet4
                                            
                                                deltar1=jet1.DeltaR(jet2)
                                                deltar2=jet3.DeltaR(jet4)
                                        
                                                mHig1=dijet1.M()
                                                mHig2=dijet2.M()
                                            
                                                chi2=((mHig1-120)/20)**2+((mHig2-120)/20)**2
                                        
                                                if (chi2<chi2_old and deltar1<1.5 and deltar2<1.5):
                                                    chi2_old=chi2
                                                    foundRes=True

    if foundRes:
        chi=chi2_old**0.5
        if chi<1:
            v1[0] = 1

    fjak4 = 1000
    ak1ak4 = 1000
    ak2ak4 = 1000
    fjak4s = 1000
    n1 = 0
    n2 = 0
    fjak4spt = -100.
    fjak4seta = -100.
    fjak4sphi = -100.
    fjak4sm = -100.
    for j in range(len(treeMine.ak4jet_pt)):
        j_p4=TLorentzVector()
        j_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[j], treeMine.ak4jet_eta[j], treeMine.ak4jet_phi[j], treeMine.ak4jet_mass[j])
        deltaRFJ = fatjet.DeltaR(j_p4)
        if deltaRFJ < fjak4:
            fjak4 = deltaRFJ
            fjak4pt = j_p4.Pt()
            fjak4eta = j_p4.Eta()
            fjak4phi = j_p4.Phi()
            fjak4m = j_p4.M()
            fjak4index = j
        deltaRFJs = fatjet.DeltaR(j_p4)
        if (deltaRFJs < fjak4s) and (deltaRFJs > 0.8) and (j != ak4jet1i) and (j != ak4jet2i):
            fjak4s = deltaRFJs
            fjak4spt = j_p4.Pt()
            fjak4seta = j_p4.Eta()
            fjak4sphi = j_p4.Phi()
            fjak4sm = j_p4.M()
        deltaRAK1 = ak4jet1.DeltaR(j_p4)
        if deltaRAK1 < 1.5 and (j != ak4jet1i):
            n1 += 1
        if (deltaRAK1 < ak1ak4) and (j != ak4jet1i) and (j != ak4jet2i):
            ak1ak4 = deltaRAK1
            ak1ak4pt = j_p4.Pt()
            ak1ak4eta = j_p4.Eta()
            ak1ak4phi = j_p4.Phi()
            ak1ak4m = j_p4.M()
        deltaRAK2 = ak4jet2.DeltaR(j_p4)
        if deltaRAK2 < 1.5 and (j != ak4jet2i):
            n2 += 1
        if (deltaRAK2 < ak2ak4) and (j != ak4jet1i) and (j != ak4jet2i):
            ak2ak4 = deltaRAK2
            ak2ak4pt = j_p4.Pt()
            ak2ak4eta = j_p4.Eta()
            ak2ak4phi = j_p4.Phi()
            ak2ak4m = j_p4.M()
    
    nAK4near1[0] = n1
    nAK4near2[0] = n2
    ak4nfatjetPT[0] = fjak4pt
    ak4nfatjetETA[0] = fjak4eta
    ak4nfatjetPHI[0] = fjak4phi
    ak4nfatjetM[0] = fjak4m
    sak4nfatjetPT[0] = fjak4spt
    sak4nfatjetETA[0] = fjak4seta
    sak4nfatjetPHI[0] = fjak4sphi
    sak4nfatjetM[0] = fjak4sm
    ak4nbjet1PT[0] = ak1ak4pt
    ak4nbjet1ETA[0] = ak1ak4eta
    ak4nbjet1PHI[0] = ak1ak4phi
    ak4nbjet1M[0] = ak1ak4m
    ak4nbjet2PT[0] = ak2ak4pt
    ak4nbjet2ETA[0] = ak2ak4eta
    ak4nbjet2PHI[0] = ak2ak4phi
    ak4nbjet2M[0] = ak2ak4m

    if options.ttbar == "True":
        ttHT[0] = treeMine.tPtsum
    fatjetPT[0] = fatjet.Pt()
    fatjetETA[0] = fatjet.Eta()
    fatjetPHI[0] = fatjet.Phi()
    fatjetM[0] = fatjet.M()
    if treeMine.isData < 1:
        fatjetl1l2l3[0] = l1l2l3
        fatjetl2l3[0] = l2l3
        fatjetJER[0] = ak8jer
        fatjetMatchedHadW[0] = hadw
    fatjettau32[0] = fatjet32
    fatjettau21[0] = fatjet21
    fatjetptau21[0] = fatjetp21
    fatjettau31[0] = fatjet31
    fatjetAKCAratio[0] = fatjetAKCA
    fatjetCAPT[0] = fatjetptCA
    fatjetCAETA[0] = fatjetetaCA
    fatjetCAPHI[0] = fatjetphiCA
    fatjetCAM[0] = fatjetmCA
    bjet1PT[0] = ak4jet1.Pt()
    bjet1ETA[0] = ak4jet1.Eta()
    bjet1PHI[0] = ak4jet1.Phi()
    bjet1M[0] = ak4jet1.M()
    bjet2PT[0] = ak4jet2.Pt()
    bjet2ETA[0] = ak4jet2.Eta()
    bjet2PHI[0] = ak4jet2.Phi()
    bjet2M[0] = ak4jet2.M()
    HT[0] = treeMine.ht
    ak4btag1[0] = ak4jet1btag
    ak4btag2[0] = ak4jet2btag
    if treeMine.isData < 1:
        ak4jetCorr1[0] = ak4jet1corr
        ak4jetCorrJECUp1[0] = ak4jet1jecup 
        ak4jetCorrJECDown1[0] = ak4jet1jecdown
        ak4jetCorrJER1[0] = ak4jet1jer
        ak4jetCorrJERUp1[0] = ak4jet1jerup
        ak4jetCorrJERDown1[0] = ak4jet1jerdown
        ak4jetflav1[0] = ak4jet1flav
        ak4jetCorr2[0] = ak4jet2corr
        ak4jetCorrJECUp2[0] = ak4jet2jecup 
        ak4jetCorrJECDown2[0] = ak4jet2jecdown
        ak4jetCorrJER2[0] = ak4jet2jer
        ak4jetCorrJERUp2[0] = ak4jet2jerup
        ak4jetCorrJERDown2[0] = ak4jet2jerdown
        ak4jetflav2[0] = ak4jet2flav

    if treeMine.isData < 1:
        if fatjetPT[0] <= 250:
            SF[0] = 0.92
            SFup[0] = 0.98
            SFdown[0] = 0.86
        elif fatjetPT[0] > 250 and fatjetPT[0] <= 350:
            SF[0] = 0.92 
            SFup[0] = 0.95
            SFdown[0] = 0.89
        elif fatjetPT[0] > 350 and fatjetPT[0] <= 430:
            SF[0] = 1.01
            SFup[0] = 1.04
            SFdown[0] = 0.97
        elif fatjetPT[0] > 430 and fatjetPT[0] <= 840:
            SF[0] = 0.92
            SFup[0] = 0.95
            SFdown[0] = 0.87
        elif fatjetPT[0] > 840:
            SF[0] = 0.92
            SFup[0] = 0.98
            SFdown[0] = 0.82

        if abs(ak4jetflav1[0]) == 5:
            ak4jet1sf = readerb.eval_auto_bounds(
                'central',      
                0,             
                bjet1ETA[0],           
                bjet1PT[0]            
                )
            ak4jet1sfup = readerb.eval_auto_bounds(
                'up',
                0,
                bjet1ETA[0],
                bjet1PT[0]
                )
            ak4jet1sfdown = readerb.eval_auto_bounds(
                'down',
                0,
                bjet1ETA[0],
                bjet1PT[0]
                )
        elif abs(ak4jetflav1[0]) == 4:
            ak4jet1sf = readerc.eval_auto_bounds(
                'central',      
                1,             
                bjet1ETA[0],           
                bjet1PT[0]            
                )
            ak4jet1sfup = readerc.eval_auto_bounds(
                'up',
                1,
                bjet1ETA[0],
                bjet1PT[0]
                )
            ak4jet1sfdown = readerc.eval_auto_bounds(
                'down',
                1,
                bjet1ETA[0],
                bjet1PT[0]
                )
        else:
            ak4jet1sf = readerl.eval_auto_bounds(
                'central',      
                2,             
                bjet1ETA[0],           
                bjet1PT[0]            
                )
            ak4jet1sfup = readerl.eval_auto_bounds(
                'up',
                2,
                bjet1ETA[0],
                bjet1PT[0]
                )
            ak4jet1sfdown = readerl.eval_auto_bounds(
                'down',
                2,
                bjet1ETA[0],
                bjet1PT[0]
                )
        if abs(ak4jetflav2[0]) == 5:
            ak4jet2sf = readerb.eval_auto_bounds(
                'central',      
                0,             
                bjet2ETA[0],           
                bjet2PT[0]            
                )
            ak4jet2sfup = readerb.eval_auto_bounds(
                'up',
                0,
                bjet2ETA[0],
                bjet2PT[0]
                )
            ak4jet2sfdown = readerb.eval_auto_bounds(
                'down',
                0,
                bjet2ETA[0],
                bjet2PT[0]
                )
        elif abs(ak4jetflav2[0]) == 4:
            ak4jet2sf = readerc.eval_auto_bounds(
                'central',      
                1,             
                bjet2ETA[0],           
                bjet2PT[0]            
                )
            ak4jet2sfup = readerc.eval_auto_bounds(
                'up',
                1,
                bjet2ETA[0],
                bjet2PT[0]
                )
            ak4jet2sfdown = readerc.eval_auto_bounds(
                'down',
                1,
                bjet2ETA[0],
                bjet2PT[0]
                )
        else:
            ak4jet2sf = readerl.eval_auto_bounds(
                'central',      
                2,             
                bjet2ETA[0],           
                bjet2PT[0]            
                )
            ak4jet2sfup = readerl.eval_auto_bounds(
                'up',
                2,
                bjet2ETA[0],
                bjet2PT[0]
                )
            ak4jet2sfdown = readerl.eval_auto_bounds(
                'down',
                2,
                bjet2ETA[0],
                bjet2PT[0]
                )
        ak4btag1SF[0] = ak4jet1sf
        ak4btag1SFup[0] = ak4jet1sfup
        ak4btag1SFdown[0] = ak4jet1sfdown
        ak4btag2SF[0] = ak4jet2sf
        ak4btag2SFup[0] = ak4jet2sfup
        ak4btag2SFdown[0] = ak4jet2sfdown

    if options.saveTrig == 'True':
        HLT2_HT800[0]= treeMine.HLT_PFHT800_v
        HLT2_Quad_Triple[0] = treeMine.HLT_QuadJet45_TripleBTagCSV_p087_v
        HLT2_Double_Triple[0] = treeMine.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
        HLT2_DiPFJet280[0] = treeMine.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v
        HLT2_AK8PFHT650[0] = treeMine.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v
        HLT2_AK8PFJet360[0] = treeMine.HLT_AK8PFJet360_TrimMass30_v
        HLT2_PFHT650[0] = treeMine.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v
        HLT2_PFHT900[0] = treeMine.HLT_PFHT900_v
        HLT2_AK8PFHT700[0] = treeMine.HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v
        
    if triggerpass > 0 and 105 < mH1 < 135 and 105 < mH2 < 135:
        tpo6.Fill(triggerpass)

    if triggerpass > 0 and 105 < mH1 < 135 and 105 < mH2 < 135 and bbtag > 0.8:
        tpo7.Fill(triggerpass) 

    if triggerpass > 0 and 105 < mH1 < 135 and 105 < mH2 < 135 and bbtag > 0.9:
        tpo8.Fill(triggerpass) 

    if triggerpass > 0 and 105 < mH1 < 135 and 105 < mH2 < 135 and bbtag > 0.6:
        tpo9.Fill(triggerpass) 


    mynewTree.Fill()

f2.cd()
f2.Write()
f2.Close()

f.Close()


