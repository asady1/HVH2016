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
(options, args) = parser.parse_args()
outputfilename = options.outName

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
TT = array('f', [-100.0])
v1 = array('f', [-100.0])
fatjetPT = array('f', [-100.0])
fatjetETA = array('f', [-100.0])
fatjetPHI = array('f', [-100.0])
fatjetM = array('f', [-100.0])
bjet1PT = array('f', [-100.0])
bjet1ETA = array('f', [-100.0])
bjet1PHI = array('f', [-100.0])
bjet1M = array('f', [-100.0])
bjet2PT = array('f', [-100.0])
bjet2ETA = array('f', [-100.0])
bjet2PHI = array('f', [-100.0])
bjet2M = array('f', [-100.0])
HT = array('f', [-100.0])
ak4btag1 = array('f', [-100.0])
ak4btag2 = array('f', [-100.0])
#trigger1 = array('f', [-100.0])
#trigger2 = array('f', [-100.0])
#trigger3 = array('f', [-100.0])
#trigger_pre = array('f', [-100.0])
    
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
mynewTree.Branch("TT", TT, "TT")
mynewTree.Branch("resolved", v1, "resolved")
mynewTree.Branch("fatjetPT", fatjetPT, "fatjetPT")
mynewTree.Branch("fatjetETA", fatjetETA, "fatjetETA")
mynewTree.Branch("fatjetPHI", fatjetPHI, "fatjetPHI")
mynewTree.Branch("fatjetM", fatjetM, "fatjetM")
mynewTree.Branch("bjet1PT", bjet1PT, "bjet1PT")
mynewTree.Branch("bjet1ETA", bjet1ETA, "bjet1ETA")
mynewTree.Branch("bjet1PHI", bjet1PHI, "bjet1PHI")
mynewTree.Branch("bjet1M", bjet1M, "bjet1M")
mynewTree.Branch("bjet2PT", bjet2PT, "bjet2PT")
mynewTree.Branch("bjet2ETA", bjet2ETA, "bjet2ETA")
mynewTree.Branch("bjet2PHI", bjet2PHI, "bjet2PHI")
mynewTree.Branch("bjet2M", bjet2M, "bjet2M")
mynewTree.Branch("HT", HT, "HT")
mynewTree.Branch("ak4btag1", ak4btag1, "ak4btag1")
mynewTree.Branch("ak4btag2", ak4btag2, "ak4btag2")

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
    
    ak4jets1Pre = []
    ak4jets2Pre = []
    ak4jets1csv = []
    ak4jets2csv = []
    ak4jet1ID = []
    ak4jet2ID = []
    for j in range(len(treeMine.ak4jet_pt)):
        j_p4=TLorentzVector()
        j_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[j], treeMine.ak4jet_eta[j], treeMine.ak4jet_phi[j], treeMine.ak4jet_mass[j])
        deltaR1=j_p4.DeltaR(ak8Jet1)
        deltaR2=j_p4.DeltaR(ak8Jet2)
        if deltaR1 > 0.8 and treeMine.ak4jetCSV[j] > 0.5426:
            ak4jets1Pre.append(j_p4)
            ak4jets1csv.append(treeMine.ak4jetCSV[j])
            ak4jet1ID.append(j)
        if deltaR2 > 0.8 and treeMine.ak4jetCSV[j] > 0.5426:
            ak4jets2Pre.append(j_p4)
            ak4jets2csv.append(treeMine.ak4jetCSV[j])
            ak4jet2ID.append(j)

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
                        ak4jet2 = ak4jets1Pre[l]
                        ak4jet2btag = ak4jets1csv[l]
                        ak4jet2i = ak4jet1ID[l]
                        b_min = b_add
    if b_min == 0 and len(ak4jets2Pre) > 1 and ak8Jet2.Pt() > 250 and treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr > 40:
        fatjet = ak8Jet2
        pmass = treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr
        bbtag = treeMine.jet2bbtag
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
                        ak4jet2 = ak4jets2Pre[l]
                        ak4jet2btag= ak4jets2csv[l]
                        ak4jet2i = ak4jet2ID[l]
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
    if (treeMine.HLT_PFHT800_v > 0 or treeMine.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v > 0 or treeMine.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v > 0 or treeMine.HLT_AK8PFJet360_TrimMass30_v > 0 or treeMine.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v > 0) and (treeMine.jet1pt > 300 and treeMine.jet2pt > 300 and abs(treeMine.jet1eta) < 2.4 and abs(treeMine.jet2eta) < 2.4) and (abs(treeMine.jet1eta - treeMine.jet2eta) < 1.3) and (treeMine.jet1ID == 1 and treeMine.jet2ID == 1) and (dijetmass_softdrop_corr > 750) and (105 < treeMine.jet1_puppi_msoftdrop_raw*treeMine.jet1_puppi_TheaCorr < 135) and (105 < treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr) and (treeMine.jet1_puppi_tau21 < 0.6 and treeMine.jet2_puppi_tau21 < 0.6):
        u1[0] = 1.
        if (treeMine.jet1bbtag > 0.8 and treeMine.jet2bbtag > 0.8):
            TT[0] = 1.
        if (treeMine.jet1bbtag > 0.3 and treeMine.jet1bbtag > 0.3 and treeMine.jet1bbtag < 0.8 and treeMine.jet2bbtag < 0.8):
            LL[0] = 1.
    else:
        u1[0] = 0.
        LL[0] = 0.
        TT[0] = 0.
    v1[0]=treeMine.passesResolved
    if options.ttbar == "True":
        ttHT[0] = treeMine.topHT
    fatjetPT[0] = fatjet.Pt()
    fatjetETA[0] = fatjet.Eta()
    fatjetPHI[0] = fatjet.Phi()
    fatjetM[0] = fatjet.M()
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
        if fatjetPT[0] > 250 and fatjetPT[0] < 300:
            SF[0] = 1.05 
            SFup[0] = 1.11
            SFdown[0] = 0.97
        elif fatjetPT[0] > 300 and fatjetPT[0] < 350:
            SF[0] = 0.9
            SFup[0] = 0.97
            SFdown[0] = 0.83
        elif fatjetPT[0] > 350 and fatjetPT[0] < 400:
            SF[0] = 0.95
            SFup[0] = 1.0
            SFdown[0] = 0.9
        elif fatjetPT[0] > 400 and fatjetPT[0] < 500:
            SF[0] = 0.96
            SFup[0] = 1.01
            SFdown[0] = 0.92
        elif fatjetPT[0] > 500:
            SF[0] = 0.89
            SFup[0] = 0.96
            SFdown[0] = 0.82

        ak4btag1SF[0] = treeMine.ak4jetCSVMSF[ak4jet1i]
        ak4btag1SFup[0] = treeMine.ak4jetCSVMSF_up[ak4jet1i]
        ak4btag1SFdown[0] = treeMine.ak4jetCSVMSF_Down[ak4jet1i]
        ak4btag2SF[0] = treeMine.ak4jetCSVMSF[ak4jet2i]
        ak4btag2SFup[0] = treeMine.ak4jetCSVMSF_up[ak4jet2i]
        ak4btag2SFdown[0] = treeMine.ak4jetCSVMSF_Down[ak4jet2i]

    if options.saveTrig == 'True':
        HLT2_HT800[0]= treeMine.HLT_PFHT800_v
        HLT2_Quad_Triple[0] = treeMine.HLT_QuadJet45_TripleBTagCSV_p087_v
        HLT2_Double_Triple[0] = treeMine.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
        
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


