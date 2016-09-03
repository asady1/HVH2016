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

(options, args) = parser.parse_args()
outputfilename = options.outName

#numberLimit = float(sys.argv[1])

f = ROOT.TFile.Open(sys.argv[1],"READ")

f2 =  ROOT.TFile(outputfilename, 'recreate')
#print outputfilename
f2.cd()

treeMine  = f.Get('myTree')

mynewTree = ROOT.TTree('mynewTree', 'mynewTree')

#miniTree variables
#jet1Branch = array('f', [-1.0, -100, -100, -1.0])
#jet2Branch = array('f', [-1.0, -100, -100, -1.0])
jet1IDB = array('f', [-100.0])
jet2IDB = array('f', [-100.0])
jet1tau21B = array('f', [-100.0])
jet2tau21B = array('f', [-100.0])
jet1pmassB = array('f', [-100.0])
jet2pmassB = array('f', [-100.0])
jet1pmassuncB = array('f', [-100.0])
jet2pmassuncB = array('f', [-100.0])
jet1bbtagB = array('f', [-100.0])
jet2bbtagB = array('f', [-100.0])
jet1s1csvB = array('f', [-100.0])
jet1s2csvB = array('f', [-100.0])
jet2s1csvB = array('f', [-100.0])
jet2s2csvB = array('f', [-100.0])
#triggerpassB = array('f', [-100.0])
#triggerHT800passB = array('f', [-100.0])
nHiggsTagsB = array('f', [-100.0])
nTrueIntB = array('f', [-100])
#sPUWeight B = array('f', [-100.0])
vtypeB = array('f', [-100.0])
isDataB = array('f', [-100.0])
jet1nbHadronB = array('f', [-100.0])
jet2nbHadronB = array('f', [-100.0])
jet1flavorB = array('f', [-100.0])
jet2flavorB = array('f', [-100.0])
jet1ncHadronB = array('f', [-100.0])
jet2ncHadronB = array('f', [-100.0])
genJet1PtB = array('f', [-100.0])
genJet1PhiB = array('f', [-100.0])
genJet1EtaB = array('f', [-100.0])
genJet1MassB = array('f', [-100.0])
genJet1IDB = array('f', [-100.0])
genJet2PtB = array('f', [-100.0])
genJet2PhiB = array('f', [-100.0])
genJet2EtaB = array('f', [-100.0])
genJet2MassB = array('f', [-100.0])
genJet2IDB = array('f', [-100.0])
jet1l1l2l3B = array('f', [-100.0])
jet2l1l2l3B = array('f', [-100.0])
jet1l2l3B = array('f', [-100.0])
jet2l2l3B = array('f', [-100.0])
jet1JERB = array('f', [-100.0])
jet2JERB = array('f', [-100.0])
puWeightsB = array('f', [-100.0])
puWeightsUpB = array('f', [-100.0])
puWeightsDownB = array('f', [-100.0])
bbtag1SFB = array('f', [-100.0])
bbtag2SFB = array('f', [-100.0])
bbtag1SFUpB = array('f', [-100.0])
bbtag2SFUpB = array('f', [-100.0])
bbtag1SFDownB = array('f', [-100.0])
bbtag2SFDownB = array('f', [-100.0])
passesBoostedB = array('f', [-100.0])
passesResolvedB = array('f', [-100.0])
jsonB = array('f', [-100.0])
normB = array('f', [-100.0])
evtB = array('f', [-100.0])
htB = array('f', [-100.0])
xsecB = array('f', [-100.0])
tPtSumB = array('f', [-100.0])
#treeMine.SetBranchAddress('jet1', jet1Array, 'pt/F:eta/F:phi/F:mass/F')
#treeMine.SetBranchAddress('jet2', jet2Array, 'pt/F:eta/F:phi/F:mass/F')
#treeMine.SetBranchAddress('jet1', jet1Branch)
#treeMine.SetBranchAddress('jet2', jet2Branch)
treeMine.SetBranchAddress('jet1tau21', jet1tau21B)
treeMine.SetBranchAddress('jet2tau21', jet2tau21B)
treeMine.SetBranchAddress('jet1pmass', jet1pmassB)
treeMine.SetBranchAddress('jet2pmass', jet2pmassB)
treeMine.SetBranchAddress('jet1pmassunc', jet1pmassuncB)
treeMine.SetBranchAddress('jet2pmassunc', jet2pmassuncB)
treeMine.SetBranchAddress('jet1bbtag', jet1bbtagB)
treeMine.SetBranchAddress('jet2bbtag', jet2bbtagB)
treeMine.SetBranchAddress('jet1s1csv', jet1s1csvB)
treeMine.SetBranchAddress('jet1s2csv', jet1s2csvB)
treeMine.SetBranchAddress('jet2s1csv', jet2s1csvB)
treeMine.SetBranchAddress('jet2s2csv', jet2s2csvB)
treeMine.SetBranchAddress('nHiggsTags', nHiggsTagsB)
#treeMine.SetBranchAddress('triggerpass', triggerpassB)
#treeMine.SetBranchAddress('triggerHT800pass', triggerHT800passB)
treeMine.SetBranchAddress('nTrueInt',nTrueIntB)
#treeMine.SetBranchAddress('PUWeight',PUWeight,'PUWeight/F')
treeMine.SetBranchAddress('jet1ID', jet1IDB)
treeMine.SetBranchAddress('jet2ID', jet2IDB)
treeMine.SetBranchAddress('vtype', vtypeB) 
treeMine.SetBranchAddress('isData', isDataB) 
treeMine.SetBranchAddress('jet1nbHadron', jet1nbHadronB)
treeMine.SetBranchAddress('jet2nbHadron', jet2nbHadronB)
treeMine.SetBranchAddress('jet1flavor', jet1flavorB) 
treeMine.SetBranchAddress('jet2flavor', jet2flavorB) 
treeMine.SetBranchAddress('jet1ncHadron', jet1ncHadronB)
treeMine.SetBranchAddress('jet2ncHadron', jet2ncHadronB)
treeMine.SetBranchAddress('gen1Pt', genJet1PtB)
treeMine.SetBranchAddress('gen1phi', genJet1PhiB)
treeMine.SetBranchAddress('gen1Eta', genJet1EtaB)
treeMine.SetBranchAddress('gen1Mass', genJet1MassB)
treeMine.SetBranchAddress('gen1ID', genJet1IDB)
treeMine.SetBranchAddress('gen2Pt', genJet2PtB)
treeMine.SetBranchAddress('gen2Phi', genJet2PhiB)
treeMine.SetBranchAddress('gen2Eta', genJet2EtaB)
treeMine.SetBranchAddress('gen2Mass', genJet2MassB)
treeMine.SetBranchAddress('gen2ID', genJet2IDB)
treeMine.SetBranchAddress('jet1l1l2l3', jet1l1l2l3B) 
treeMine.SetBranchAddress('jet2l1l2l3', jet2l1l2l3B) 
treeMine.SetBranchAddress('jet1l2l3', jet1l2l3B)
treeMine.SetBranchAddress('jet2l2l3', jet2l2l3B)
treeMine.SetBranchAddress('jet1JER', jet1JERB) 
treeMine.SetBranchAddress('jet2JER', jet2JERB) 
treeMine.SetBranchAddress('puWeights', puWeightsB)
treeMine.SetBranchAddress('puWeightsUp', puWeightsUpB)
treeMine.SetBranchAddress('puWeightsDown', puWeightsDownB)
treeMine.SetBranchAddress('bbtag1SF', bbtag1SFB)
treeMine.SetBranchAddress('bbtag2SF', bbtag2SFB)
treeMine.SetBranchAddress('bbtag1SFUp', bbtag1SFUpB)
treeMine.SetBranchAddress('bbtag2SFUp', bbtag2SFUpB)
treeMine.SetBranchAddress('bbtag1SFDown', bbtag1SFDownB)
treeMine.SetBranchAddress('bbtag2SFDown', bbtag2SFDownB)
treeMine.SetBranchAddress('json', jsonB)
treeMine.SetBranchAddress('norm', normB)
treeMine.SetBranchAddress('evt', evtB)
treeMine.SetBranchAddress('ht', htB)
treeMine.SetBranchAddress('xsec', xsecB)
treeMine.SetBranchAddress('passesBoosted', passesBoostedB)
treeMine.SetBranchAddress('passesResolved', passesResolvedB)
treeMine.SetBranchAddress('tPtsum', tPtSumB)

#new tree variables
Inv_mass = array('f', [-100.0])
dijet_mass_fj_1 = array('f', [-100.0])
dijet_mass_fj_2 = array('f', [-100.0])
dijet_mass_12 = array('f', [-100.0])
fatjet_mass = array('f', [-100.0])
i1 = array('f', [-100.0])
fatjet_hbb = array('f', [-100.0])
q1 = array('f', [-100.0])
o1 = array('f', [-100.0])
p1 = array('f', [-100.0])
t1 = array('f', [-100.0])
u1 = array('f', [-100.0])
v1 = array('f', [-100.0])
fatjetPT = array('f', [-100.0])
bjet1PT = array('f', [-100.0])
bjet2PT = array('f', [-100.0])
fatjetETA = array('f', [-100.0])
bjet1ETA = array('f', [-100.0])
bjet2ETA = array('f', [-100.0])
fatjetPHI = array('f', [-100.0])
bjet1PHI = array('f', [-100.0])
bjet2PHI = array('f', [-100.0])
fatjetMASS = array('f', [-100.0])
bjet1MASS = array('f', [-100.0])
bjet2MASS = array('f', [-100.0])
pt_all = array('f', [-100.0])
pt_fj_1 = array('f', [-100.0])
pt_fj_2 = array('f', [-100.0])
pt_12 = array('f', [-100.0])
dR_fj_1 = array('f', [-100.0])
dR_fj_2 = array('f', [-100.0])
dR_12 = array('f', [-100.0])
HT = array('f', [-100.0])
cmva1 = array('f', [-100.0])
cmva2 = array('f', [-100.0])
   
SF = array('f', [-100.0])
SFup= array('f', [-100.0])
SFdown = array('f', [-100.0])
cmvaSF1 = array('f', [-100.0])
cmvaSF1up = array('f', [-100.0])
cmvaSF1down = array('f', [-100.0]) 
cmvaSF2 = array('f', [-100.0])
cmvaSF2up = array('f', [-100.0])
cmvaSF2down = array('f', [-100.0])
    
puW_up = array('f', [-100.0])
puW_down= array('f', [-100.0])

if options.saveTrig == 'True':
    HLT2_Jet250 = array('f', [-100.0])
    HLT2_Jet280 = array('f', [-100.0])
#HLT2_HT600 = array('f', [-100.0])
#HLT2_HT650 = array('f', [-100.0])
    HLT2_HT700 = array('f', [-100.0])
    HLT2_HT800 = array('f', [-100.0])  
    HLT2_Jet360 = array('f', [-100.0])  
    HLT2_HT650_MJJ900 = array('f', [-100.0])   
    HLT2_HT650_MJJ950 = array('f', [-100.0])
    HLT2_Quad_Triple = array('f', [-100.0])
    HLT2_Double_Triple = array('f', [-100.0])  

mynewTree.Branch("Inv_mass", Inv_mass, "Inv_mass/F")
mynewTree.Branch("dijet_mass_fj_1", dijet_mass_fj_1, "dijet_mass_fj_1/F")
mynewTree.Branch("dijet_mass_fj_2", dijet_mass_fj_2, "dijet_mass_fj_2/F")
mynewTree.Branch("dijet_mass_12", dijet_mass_12, "dijet_mass_12/F")
mynewTree.Branch("fatjet_mass", fatjet_mass, "fatjet_mass/F")
mynewTree.Branch("cross_section", i1, "cross_section")
mynewTree.Branch("fatjet_hbb", fatjet_hbb, "fatjet_hbb")
mynewTree.Branch("Vtype", q1, "Vtype")
mynewTree.Branch("puWeight", o1, "puWeight")
mynewTree.Branch("norm", p1, "norm")
mynewTree.Branch("evt", t1, "evt")
mynewTree.Branch("boosted", u1, "boosted")
mynewTree.Branch("resolved", v1, "resolved")
mynewTree.Branch("fatjetPT", fatjetPT, "fatjetPT")
mynewTree.Branch("bjet1PT", bjet1PT, "bjet1PT")
mynewTree.Branch("bjet2PT", bjet2PT, "bjet2PT")
mynewTree.Branch("fatjetETA", fatjetETA, "fatjetETA")
mynewTree.Branch("bjet1ETA", bjet1ETA, "bjet1ETA")
mynewTree.Branch("bjet2ETA", bjet2ETA, "bjet2ETA")
mynewTree.Branch("fatjetPHI", fatjetPHI, "fatjetPHI")
mynewTree.Branch("bjet1PHI", bjet1PHI, "bjet1PHI")
mynewTree.Branch("bjet2PHI", bjet2PHI, "bjet2PHI")
mynewTree.Branch("fatjetMASS", fatjetMASS, "fatjetMASS")
mynewTree.Branch("bjet1MASS", bjet1MASS, "bjet1MASS")
mynewTree.Branch("bjet2MASS", bjet2MASS, "bjet2MASS")
mynewTree.Branch("pt_all", pt_all, "pt_all/F")
mynewTree.Branch("pt_fj_1", pt_fj_1, "pt_fj_1")
mynewTree.Branch("pt_fj_2", pt_fj_2, "pt_fj_2")
mynewTree.Branch("pt_12", pt_12, "pt_12")
mynewTree.Branch("dR_fj_1", dR_fj_1, "dR_fj_1")
mynewTree.Branch("dR_fj_2", dR_fj_2, "dR_fj_2")
mynewTree.Branch("dR_12", dR_12, "dR_12")
mynewTree.Branch("HT", HT, "HT")
mynewTree.Branch("cmva1", cmva1, "cmva1")
mynewTree.Branch("cmva2", cmva2, "cmva2")
    
mynewTree.Branch("SF", SF, "SF")
mynewTree.Branch("SFup", SFup, "SFup")
mynewTree.Branch("SFdown", SFdown, "SFdown")
mynewTree.Branch("cmvaSF1", cmvaSF1, "cmvaSF1")
mynewTree.Branch("cmvaSF1up", cmvaSF1up, "cmvaSF1up")
mynewTree.Branch("cmvaSF1down", cmvaSF1down, "cmvaSF1down") 
mynewTree.Branch("cmvaSF2", cmvaSF2, "cmvaSF2")
mynewTree.Branch("cmvaSF2up", cmvaSF2up, "cmvaSF2up")
mynewTree.Branch("cmvaSF2down", cmvaSF2down, "cmvaSF2down")
    
mynewTree.Branch("puWeightUp", puW_up, "puWeightUp")
mynewTree.Branch("puWeightDown", puW_down, "puWeightDown")

if options.saveTrig == 'True':
    mynewTree.Branch("HLT2_Jet250", HLT2_Jet250, "HLT2_Jet250/F")
    mynewTree.Branch("HLT2_Jet280", HLT2_Jet280, "HLT2_Jet280/F")
#mynewTree.Branch("HLT2_HT600", HLT2_HT600, "HLT2_HT600/F")
#mynewTree.Branch("HLT2_HT650", HLT2_HT650, "HLT2_HT650/F")
    mynewTree.Branch("HLT2_HT700", HLT2_HT700, "HLT2_HT700/F")
    mynewTree.Branch('HLT2_HT800', HLT2_HT800, 'HLT2_HT800/F')
    mynewTree.Branch('HLT2_Jet360', HLT2_Jet360, 'HLT2_Jet360/F')
    mynewTree.Branch('HLT2_HT650_MJJ900', HLT2_HT650_MJJ900, 'HLT2_HT650_MJJ900/F')
    mynewTree.Branch('HLT2_HT650_MJJ950', HLT2_HT650_MJJ950, 'HLT2_HT650_MJJ950/F')
    mynewTree.Branch('HLT2_Quad_Triple', HLT2_Quad_Triple, 'HLT2_Quad_Triple/F')
    mynewTree.Branch('HLT2_Double_Triple', HLT2_Double_Triple, 'HLT2_Double_Triple/F')

nevent = treeMine.GetEntries();

tpo3 = ROOT.TH1F("tpo3", "After fatjet mass cut", 8, -2.5, 5.5)
tpo4 = ROOT.TH1F("tpo4", "After vtype cut", 8, -2.5, 5.5)

counter = 0
for i in range(0, nevent) :
    counter = counter + 1
    treeMine.GetEntry(i)

    #pick a fatjet with highest pt that has pruned mass > 40
    if jet1pmassB[0] > 40: 
        fj_p4 = TLorentzVector()
        fj_p4.SetPtEtaPhiM(treeMine.jet1pt, treeMine.jet1eta, treeMine.jet1phi, treeMine.jet1mass)
        pmass = jet1pmassB[0]
        btag = jet1bbtagB[0]
    elif jet2pmassB[0] > 40:
        fj_p4 = TLorentzVector()
        fj_p4.SetPtEtaPhiM(treeMine.jet2pt, treeMine.jet2eta, treeMine.jet2phi, treeMine.jet2mass)
        pmass = jet2pmassB[0]
        btag = jet2bbtagB[0]
    elif (jet1pmassB[0] < 40 and jet2pmassB[0] < 40):
        continue
    tpo3.Fill(vtypeB[0])
    #cutting on vtype
    vtypeGood = 0
    if vtypeB[0] == -1 or vtypeB[0] == 4:
        vtypeGood = 1
    if vtypeGood < 1:
        continue
    tpo4.Fill(vtypeB[0])
    #selecting ak4 jets
    bjetArray = []
    bjetCMVA = []
    bjetCMVASF = []
    bjetCMVASFUp = []
    bjetCMVASFDown = []
    for j in range(len(treeMine.ak4jet_pt)):
        j_p4=TLorentzVector()
        j_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[j], treeMine.ak4jet_eta[j], treeMine.ak4jet_phi[j], treeMine.ak4jet_mass[j])
        deltaR=j_p4.DeltaR(fj_p4)
        if deltaR > 0.8:
            bjetArray.append(j)
            bjetCMVA.append(treeMine.ak4jetCMVA[j])
            if isDataB[0] < 1:
                bjetCMVASF.append(treeMine.ak4jetCMVAMSF[j])
                bjetCMVASFUp.append(treeMine.ak4jetCMVAMSF_Up[j])
                bjetCMVASFDown.append(treeMine.ak4jetCMVAMSF_Down[j])
    if len(bjetArray) < 2:
        continue
    bji1 = bjetArray[0]
    bji2 = bjetArray[1]
    bjet1 = TLorentzVector()
    bjet1.SetPtEtaPhiM(treeMine.ak4jet_pt[bji1], treeMine.ak4jet_eta[bji1], treeMine.ak4jet_phi[bji1], treeMine.ak4jet_mass[bji1])
    bjet2 = TLorentzVector()
    bjet2.SetPtEtaPhiM(treeMine.ak4jet_pt[bji2], treeMine.ak4jet_eta[bji2], treeMine.ak4jet_phi[bji2], treeMine.ak4jet_mass[bji2])
                               
    #saving variables
    Inv_mass[0] = (fj_p4 + bjet1 + bjet2).M()
    dijet_mass_fj_1[0] = (bjet1 + fj_p4).M()
    dijet_mass_fj_2[0] = (bjet2 + fj_p4).M()
    dijet_mass_12[0] = (bjet1 + bjet2).M()
    fatjet_mass[0] = pmass
    i1[0] = treeMine.xsec
    fatjet_hbb[0] = btag
    q1[0]=treeMine.vtype
    o1[0]=treeMine.puWeights
    p1[0]=treeMine.norm
    t1[0]=treeMine.evt
    u1[0]=treeMine.passesBoosted
    v1[0]=treeMine.passesResolved
    fatjetPT[0] = fj_p4.Pt()
    bjet1PT[0] = bjet1.Pt()
    bjet2PT[0] = bjet2.Pt()
    fatjetETA[0] = fj_p4.Eta()
    bjet1ETA[0] = bjet1.Eta()
    bjet2ETA[0] = bjet2.Eta()
    fatjetPHI[0] = fj_p4.Phi()
    bjet1PHI[0] = bjet1.Phi()
    bjet2PHI[0] = bjet2.Phi()
    fatjetMASS[0] = fj_p4.M()
    bjet1MASS[0] = bjet1.M()
    bjet2MASS[0] = bjet2.M()
    pt_all[0] = (fj_p4 + bjet1 + bjet2).Pt()
    pt_fj_1[0] = (fj_p4 + bjet1).Pt()
    pt_fj_2[0] = (fj_p4 + bjet2).Pt()
    pt_12[0] = (bjet1 + bjet2).Pt()
    dR_fj_1[0] = fj_p4.DeltaR(bjet1)
    dR_fj_2[0] = fj_p4.DeltaR(bjet2)
    dR_12[0] = bjet1.DeltaR(bjet2)
    HT[0] = treeMine.ht
    cmva1[0] = bjetCMVA[0]
    cmva2[0] = bjetCMVA[1]

    if options.saveTrig == 'True':
        HLT2_Jet250[0] = treeMine.HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v 
        HLT2_Jet280[0] = treeMine.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v
        HLT2_HT700[0] = treeMine.HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v 
        HLT2_HT800[0] = treeMine.HLT_PFHT800_v
        HLT2_Jet360[0] = treeMine.HLT_AK8PFJet360_V  
        HLT2_HT650_MJJ900[0] = treeMine.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v
        HLT2_HT650_MJJ950[0] = treeMine.HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v
        HLT2_Quad_Triple[0] = treeMine.HLT_QuadJet45_TripleBTagCSV_p087_v
        HLT2_Double_Triple[0] = treeMine.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
    if fj_p4.Pt() <300:
        sf=0.9135
        sfup=sf+0.15
        sfd=sf-0.15
    elif fj_p4.Pt() <400:
        sf=0.913
        sfup=sf+0.088
        sfd=sf-0.088
    elif fj_p4.Pt() <500:
        sf=0.914
        sfup=sf+0.141
        sfd=sf-0.141
    else:
        sf=0.9135
        sfup=sf+0.15
        sfd=sf-0.15
    if isDataB[0] < 1:
        SF[0]=sf
        SFup[0]=sfup
        SFdown[0]=sfd                      
        cmvaSF1[0]=bjetCMVASF[0]
        cmvaSF1up[0]=bjetCMVASFUp[0]
        cmvaSF1down[0]=bjetCMVASFDown[0]
        cmvaSF2[0]=bjetCMVASF[1]
        cmvaSF2up[0]=bjetCMVASFUp[1]
        cmvaSF2down[0]=bjetCMVASFDown[1]
        puW_up[0]=treeMine.puWeightsUp
        puW_down[0]=treeMine.puWeightsDown

    mynewTree.Fill()

print "Done with " + outputfilename

f2.cd()
f2.Write()
f2.Close()

f.Close()


