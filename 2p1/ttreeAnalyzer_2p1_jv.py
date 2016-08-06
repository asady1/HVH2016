import os, numpy
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
(options, args) = parser.parse_args()
outputfilename = options.outName

#numberLimit = float(sys.argv[1])

f = ROOT.TFile(sys.argv[1])

f2 =  ROOT.TFile(outputfilename, 'recreate')
#print outputfilename
f2.cd()

treeMine  = f.Get('myTree')

mynewTree = ROOT.TTree('mynewTree', 'mynewTree')


jet1Branch = array('f', [-1.0, -100, -100, -1.0])
jet2Branch = array('f', [-1.0, -100, -100, -1.0])
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
treeMine.SetBranchAddress('jet1', jet1Branch)
treeMine.SetBranchAddress('jet2', jet2Branch)
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
treeMine.SetBranchAddress('genJet1Pt', genJet1PtB)
treeMine.SetBranchAddress('genJet1Phi', genJet1PhiB)
treeMine.SetBranchAddress('genJet1Eta', genJet1EtaB)
treeMine.SetBranchAddress('genJet1Mass', genJet1MassB)
treeMine.SetBranchAddress('genJet1ID', genJet1IDB)
treeMine.SetBranchAddress('genJet2Pt', genJet2PtB)
treeMine.SetBranchAddress('genJet2Phi', genJet2PhiB)
treeMine.SetBranchAddress('genJet2Eta', genJet2EtaB)
treeMine.SetBranchAddress('genJet2Mass', genJet2MassB)
treeMine.SetBranchAddress('genJet2ID', genJet2IDB)
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
treeMine.SetBranchAddress('tPtSum', tPtSumB)
#transition region variables

f1 = array('f', [-100.0])
g1 = array('f', [-100.0])
h1 = array('f', [-100.0])
i1 = array('f', [-100.0])
l1 = array('f', [-100.0])
m1 = array('f', [-100.0])
q1 = array('f', [-100.0])
o1 = array('f', [-100.0])
p1 = array('f', [-100.0])
r1 = array('f', [-100.0])
s1 = array('f', [-100.0])
t1 = array('f', [-100.0])
u1 = array('f', [-100.0])
v1 = array('f', [-100.0])
fatjetPT = array('f', [-100.0])
bjet1PT = array('f', [-100.0])
bjet2PT = array('f', [-100.0])
HT = array('f', [-100.0])
#trigger1 = array('f', [-100.0])
#trigger2 = array('f', [-100.0])
#trigger3 = array('f', [-100.0])
#trigger_pre = array('f', [-100.0])
    
SF = array('f', [-100.0])
SFup = array('f', [-100.0])
SFdown = array('f', [-100.0])
    
cmvaSF = array('f', [-100.0])
cmvaSFup = array('f', [-100.0])
cmvaSFdown = array('f', [-100.0])
cmvaSF2 = array('f', [-100.0])
cmvaSFup2 = array('f', [-100.0])
cmvaSFdown2 = array('f', [-100.0])
    
puW_up = array('f', [-100.0])
puW_down = array('f', [-100.0])

HLT2_Jet250 = array('f', [-100.0])
HLT2_Jet280 = array('f', [-100.0])
HLT2_HT600 = array('f', [-100.0])
HLT2_HT650 = array('f', [-100.0])
HLT2_HT700 = array('f', [-100.0])
HLT2_HT800 = array('f', [-100.0])  

mynewTree.Branch("Inv_mass", f1, "Invariant mass")
mynewTree.Branch("dijet_mass", g1, "dijet_mass")
mynewTree.Branch("fatjet_mass", h1, "fatjet_mass")
mynewTree.Branch("cross_section", i1, "cross_section")
mynewTree.Branch("fatjet_hbb", l1, "fatjet_hbb")
mynewTree.Branch("isCR", m1, "isCR")#
mynewTree.Branch("Vtype", q1, "Vtype")
mynewTree.Branch("puWeight", o1, "puWeight")
mynewTree.Branch("norm", p1, "norm")
mynewTree.Branch("n_OkJets", r1, "n_OkJets")
mynewTree.Branch("n_OkFj", s1, "n_OkFj")
mynewTree.Branch("evt", t1, "evt")
mynewTree.Branch("boosted", u1, "boosted")
mynewTree.Branch("resolved", v1, "resolved")
mynewTree.Branch("fatjetPT", fatjetPT, "fatjetPT")
mynewTree.Branch("bjet1PT", bjet1PT, "bjet1PT")
mynewTree.Branch("bjet2PT", bjet2PT, "bjet2PT")
mynewTree.Branch("HT", HT, "HT")


#mynewTree.Branch("HLT_ht800", trigger1, "HLT_ht800")
#mynewTree.Branch("HLT_AK08", trigger2, "HLT_AK08")
#mynewTree.Branch("HLT_HH4b", trigger3, "HLT_HH4b")
#mynewTree.Branch("HLT_ht350", trigger_pre, "HLT_ht350")
    
mynewTree.Branch("SF", SF, "SF")
mynewTree.Branch("SFup", SFup, "SFup")
mynewTree.Branch("SFdown", SFdown, "SFdown")
mynewTree.Branch("cmvaSF", cmvaSF, "cmvaSF")
mynewTree.Branch("cmvaSFup", cmvaSFup, "cmvaSFup")
mynewTree.Branch("cmvaSFdown", cmvaSFdown, "cmvaSFdown")
mynewTree.Branch("cmvaSF2", cmvaSF2, "cmvaSF2")
mynewTree.Branch("cmvaSFup2", cmvaSFup2, "cmvaSFup2")
mynewTree.Branch("cmvaSFdown2", cmvaSFdown2, "cmvaSFdown2")
    
mynewTree.Branch("puWeightUp", puW_up, "puWeightUp")
mynewTree.Branch("puWeightDown", puW_down, "puWeightDown")

mynewTree.Branch("HLT2_Jet250", HLT2_Jet250, "HLT2_Jet250/F")
mynewTree.Branch("HLT2_Jet280", HLT2_Jet280, "HLT2_Jet280/F")
mynewTree.Branch("HLT2_HT600", HLT2_HT600, "HLT2_HT600/F")
mynewTree.Branch("HLT2_HT650", HLT2_HT650, "HLT2_HT650/F")
mynewTree.Branch("HLT2_HT700", HLT2_HT700, "HLT2_HT700/F")
mynewTree.Branch('HLT2_HT800', HLT2_HT800, 'HLT2_HT800/F')

nevent = treeMine.GetEntries();

tpo3 = ROOT.TH1F("tpo3", "After v-type cut", 8, -2.5, 5.5)
tpo4 = ROOT.TH1F("tpo4", "After fatjet btag and mass", 8, -2.5, 5.5)
tpo5 = ROOT.TH1F("tpo5", "After subjet btag and deltaR", 8, -2.5, 5.5)
tpo6 = ROOT.TH1F("tpo6", "After pass HH", 8, -2.5, 5.5)
tpo7 = ROOT.TH1F("tpo7", "After mass cut", 8, -2.5, 5.5)

counter = 0
for i in range(0, nevent) :
    counter = counter + 1
    treeMine.GetEntry(i)

    count_fatjets = 0
    count_jets1outsidef=0
    count_jets1outsidef_atag=0
    count_jets2outsidef=0
    count_jets2outsidef_atag=0
    save_index=[]
    save_indexCR=[]
    save_jet1_index=[]
    save_atag_jet1_index=[]
    save_jet2_index=[]
    save_atag_jet2_index=[]

    passHH = 0
    passHHCR = 0
    passHH1 = 0
    passHH2 = 0
    passHHCR1 = 0
    passHHCR2 = 0
    
    if vtypeB[0] == -1 or vtypeB[0] == 4:
        tpo3.Fill(vtypeB[0])
        passfj = 0
        if jet1bbtagB[0] > 0.9 and jet1pmassB[0] > 40:
            passfj += 1
        if jet2bbtagB[0] > 0.9 and jet2pmassB[0] > 40:
            passfj += 1
        if passfj > 0:
            tpo4.Fill(vtypeB[0])
        if jet1bbtagB[0] > 0.9 and jet1pmassB[0] > 40:
#        if jet1pmassB[0] > 40:
            count_fatjets += 1
            fj_p4 = TLorentzVector()
            fj_p4.SetPtEtaPhiM(jet1Branch[0], jet1Branch[1], jet1Branch[2], jet1Branch[3])
            for j in range(len(treeMine.ak4jet_pt)):
                j_p4=TLorentzVector()
                j_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[j], treeMine.ak4jet_eta[j], treeMine.ak4jet_phi[j], treeMine.ak4jet_mass[j])
                deltaR=j_p4.DeltaR(fj_p4)
                if treeMine.ak4jetCMVA[j] > 0.185 and deltaR > 1.5:
#                if deltaR > 1.5:
                    count_jets1outsidef+=1
                    save_jet1_index.append(j)
                if treeMine.ak4jetCMVA[j] < 0.185 and deltaR > 1.5:
#                if deltaR > 1.5:
                    count_jets1outsidef_atag+=1
                    save_atag_jet1_index.append(j)
       
            if count_jets1outsidef>1:
                save_index.append(0)
            if count_jets1outsidef>0:
                save_indexCR.append(0)

        if jet2bbtagB[0] > 0.9 and jet2pmassB[0] > 40:
#        if jet2pmassB[0] > 40:
            count_fatjets += 1
            fj2_p4 = TLorentzVector()
            fj2_p4.SetPtEtaPhiM(jet2Branch[0], jet2Branch[1], jet2Branch[2], jet2Branch[3])
            for j in range(len(treeMine.ak4jet_pt)):
                j_p4=TLorentzVector()
                j_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[j], treeMine.ak4jet_eta[j], treeMine.ak4jet_phi[j], treeMine.ak4jet_mass[j])
                deltaR=j_p4.DeltaR(fj2_p4)
                if treeMine.ak4jetCMVA[j] > 0.185 and deltaR > 1.5:
#                if deltaR > 1.5:
                    count_jets2outsidef+=1
                    save_jet2_index.append(j)
                if treeMine.ak4jetCMVA[j] < 0.185 and deltaR > 1.5:
#                if deltaR > 1.5:
                    count_jets2outsidef_atag+=1
                    save_atag_jet2_index.append(j)
                    
            if count_jets2outsidef>1:
                save_index.append(1)

            if count_jets2outsidef>0:
                save_indexCR.append(1)
                               
        if (count_jets1outsidef>=2 and count_fatjets>=1):
            m_max = 50.
            jet3_p4=TLorentzVector()
            jet4_p4=TLorentzVector()
            for k in save_jet1_index:
                jet3_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[k], treeMine.ak4jet_eta[k], treeMine.ak4jet_phi[k], treeMine.ak4jet_mass[k])
                for l in save_jet1_index:
                    if (l!=k):
                        jet4_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[l], treeMine.ak4jet_eta[l], treeMine.ak4jet_phi[l], treeMine.ak4jet_mass[l])
                        deltaRfat3=jet3_p4.DeltaR(fj_p4)
                        deltaRfat4=jet4_p4.DeltaR(fj_p4)                                        
                        deltaR2=jet3_p4.DeltaR(jet4_p4) 
                        m_diff1=abs(jet1pmassB[0] - (jet3_p4+jet4_p4).M())
                        if m_diff1 < m_max and deltaRfat3>1.5 and deltaRfat4>1.5 and deltaR2<1.5:
                            passHH1 = 1
                            h21jet1 = k
                            h21jet2 = l
                            m_max = m_diff1
                           
        if (count_jets2outsidef>=2 and count_fatjets>=1):
            m_max2 = 50.
            jet23_p4=TLorentzVector()
            jet24_p4=TLorentzVector()
            for k in save_jet2_index:
                jet23_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[k], treeMine.ak4jet_eta[k], treeMine.ak4jet_phi[k], treeMine.ak4jet_mass[k])
                for l in save_jet2_index:
                    if (l!=k):
                        jet24_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[l], treeMine.ak4jet_eta[l], treeMine.ak4jet_phi[l], treeMine.ak4jet_mass[l])
                        deltaR2fat3=jet23_p4.DeltaR(fj2_p4)
                        deltaR2fat4=jet24_p4.DeltaR(fj2_p4)                                        
                        deltaR22=jet23_p4.DeltaR(jet24_p4) 
                        m_diff2=abs(jet2pmassB[0] - (jet23_p4+jet24_p4).M())
                        if m_diff2 < m_max2 and deltaR2fat3>1.5 and deltaR2fat4>1.5 and deltaR22<1.5:
                            passHH2 = 2
                            h22jet1 = k
                            h22jet2 = l
                            m_max2 = m_diff2
                           
        if (count_jets1outsidef==1 and count_jets1outsidef_atag>1 and count_fatjets>=1):
            tpo5.Fill(vtypeB[0])
            m_max = 50.
            jet3_p4=TLorentzVector()
            jet4_p4=TLorentzVector()
            for k in save_atag_jet1_index:
                jet3_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[k], treeMine.ak4jet_eta[k], treeMine.ak4jet_phi[k], treeMine.ak4jet_mass[k])
                for l in save_atag_jet1_index:
                    if (l!=k):
                        jet4_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[l], treeMine.ak4jet_eta[l], treeMine.ak4jet_phi[l], treeMine.ak4jet_mass[l])
                        deltaRfat3=jet3_p4.DeltaR(fj_p4)
                        deltaRfat4=jet4_p4.DeltaR(fj_p4)                                        
                        deltaR2=jet3_p4.DeltaR(jet4_p4) 
                        m_diffCR1=abs(jet1pmassB[0] - (jet3_p4+jet4_p4).M())
                        if m_diffCR1 < m_max and deltaRfat3>1.5 and deltaRfat4>1.5 and deltaR2<1.5:
                            passHHCR1 = 1
                            h21jet1 = k
                            h21jet2 = l
                            m_max = m_diffCR1

        if (count_jets2outsidef==1 and count_jets2outsidef_atag>1 and count_fatjets>=1):
            m_max2 = 50.
            jet23_p4=TLorentzVector()
            jet24_p4=TLorentzVector()
            for k in save_atag_jet2_index:
                jet23_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[k], treeMine.ak4jet_eta[k], treeMine.ak4jet_phi[k], treeMine.ak4jet_mass[k])
                for l in save_atag_jet2_index:
                    if (l!=k):
                        jet24_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[l], treeMine.ak4jet_eta[l], treeMine.ak4jet_phi[l], treeMine.ak4jet_mass[l])
                        deltaR2fat3=jet23_p4.DeltaR(fj2_p4)
                        deltaR2fat4=jet24_p4.DeltaR(fj2_p4)                                        
                        deltaR22=jet23_p4.DeltaR(jet24_p4) 
                        m_diffCR2=abs(jet2pmassB[0] - (jet23_p4+jet24_p4).M())
                        if m_diffCR2 < m_max2 and deltaR2fat3>1.5 and deltaR2fat4>1.5 and deltaR22<1.5:
                            passHHCR2 = 2
                            h22jet1 = k
                            h22jet2 = l
                            m_max2 = m_diffCR2

    passHH = passHH1 + passHH2

    if passHH > 0:
            tpo6.Fill(vtypeB[0])
    if passHH < 1:
        continue
    if passHH == 3: 
        if m_diff1 < m_diff2:
            passHH = 1
        else:
            passHH = 2

    if passHH == 1:
            fatjet = TLorentzVector()
            ak4jet1 = TLorentzVector()
            ak4jet2 = TLorentzVector()
            fatjet.SetPtEtaPhiM(jet1Branch[0], jet1Branch[1], jet1Branch[2], jet1Branch[3])
            ak4jet1.SetPtEtaPhiM(treeMine.ak4jet_pt[h21jet1], treeMine.ak4jet_eta[h21jet1], treeMine.ak4jet_phi[h21jet1], treeMine.ak4jet_mass[h21jet1])
            ak4jet2.SetPtEtaPhiM(treeMine.ak4jet_pt[h21jet2], treeMine.ak4jet_eta[h21jet2], treeMine.ak4jet_phi[h21jet2], treeMine.ak4jet_mass[h21jet2])
            pmass = jet1pmassB[0]
            bbtag = jet1bbtagB[0]
            bjet1 = h21jet1
            bjet2 = h21jet2

    if passHH == 2:
            fatjet = TLorentzVector()
            ak4jet1 = TLorentzVector()
            ak4jet2 = TLorentzVector()
            fatjet.SetPtEtaPhiM(jet2Branch[0], jet2Branch[1], jet2Branch[2], jet2Branch[3])
            ak4jet1.SetPtEtaPhiM(treeMine.ak4jet_pt[h22jet1], treeMine.ak4jet_eta[h22jet1], treeMine.ak4jet_phi[h22jet1], treeMine.ak4jet_mass[h22jet1])
            ak4jet2.SetPtEtaPhiM(treeMine.ak4jet_pt[h22jet2], treeMine.ak4jet_eta[h22jet2], treeMine.ak4jet_phi[h22jet2], treeMine.ak4jet_mass[h22jet2])
            pmass = jet2pmassB[0]
            bbtag = jet2bbtagB[0]
            bjet1 = h22jet1
            bjet2 = h22jet2

    if passHH > 0:
            pTH1=(fatjet).Pt()
            pTH2=(ak4jet1+ak4jet2).Pt()
            mH1=pmass
            mH2=(ak4jet1+ak4jet2).M()
            
            if 105 < mH1 < 135 and 105 < mH2 < 135:
                tpo7.Fill(vtypeB[0])

            f1[0]=(ak4jet1+ak4jet2+fatjet).M()
            g1[0]=mH2
            h1[0]=mH1
            i1[0]=treeMine.xsec
            l1[0]=bbtag
            q1[0]=treeMine.vtype
            o1[0]=treeMine.puWeights
            p1[0]=treeMine.norm
            r1[0]=count_jets1outsidef + count_jets2outsidef
            s1[0]=count_fatjets
            m1[0]=0.
            t1[0]=treeMine.evt
            u1[0]=treeMine.passesBoosted
            v1[0]=treeMine.passesResolved
            fatjetPT[0] = fatjet.Pt()
            bjet1PT[0] = ak4jet1.Pt()
            bjet2PT[0] = ak4jet2.Pt()
            HT[0] = treeMine.ht
            HLT2_Jet250[0] = treeMine.HLT_Jet250
            HLT2_Jet280[0] = treeMine.HLT_Jet280
            HLT2_HT600[0] = treeMine.HLT_HT600
            HLT2_HT650[0] = treeMine.HLT_HT650 
            HLT2_HT700[0] = treeMine.HLT_HT700 
            HLT2_HT800[0] = treeMine.triggerHT800pass
           # trigger1[0]=treeMine.HLT_ht800
           # trigger2[0]=treeMine.HLT_AK08
           # trigger3[0]=treeMine.HLT_HH4b
           # trigger_pre[0]=treeMine.HLT_ht350
 
            if pTH1<300:
                sf=0.9135
                sfup=sf+0.15
                sfd=sf-0.15
            elif pTH1<400:
                sf=0.913
                sfup=sf+0.088
                sfd=sf-0.088
            elif pTH1<500:
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
                        
                cmvaSF[0]=treeMine.ak4jetCMVAMSF[bjet1]
                cmvaSFup[0]=treeMine.ak4jetCMVAMSF_Up[bjet1]
                cmvaSFdown[0]=treeMine.ak4jetCMVAMSF_Down[bjet1]
                cmvaSF2[0]=treeMine.ak4jetCMVAMSF[bjet2]
                cmvaSFup2[0]=treeMine.ak4jetCMVAMSF_Up[bjet2]
                cmvaSFdown2[0]=treeMine.ak4jetCMVAMSF_Down[bjet2]
                        
                        
                puW_up[0]=treeMine.puWeightsUp
                puW_down[0]=treeMine.puWeightsDown

    passHHCR = passHHCR1 + passHHCR2
    if passHHCR > 0:
        continue
      #  print "passHHCR: " + str(passHHCR)
    if passHHCR == 3: 
        if m_diffCR1 < m_diffCR2:
            passHHCR = 1
        else:
            passHHCR = 2

    if passHHCR == 1:
            fatjet = TLorentzVector()
            ak4jet1 = TLorentzVector()
            ak4jet2 = TLorentzVector()
            fatjet.SetPtEtaPhiM(jet1Branch[0], jet1Branch[1], jet1Branch[2], jet1Branch[3])
            ak4jet1.SetPtEtaPhiM(treeMine.ak4jet_pt[h21jet1], treeMine.ak4jet_eta[h21jet1], treeMine.ak4jet_phi[h21jet1], treeMine.ak4jet_mass[h21jet1])
            ak4jet2.SetPtEtaPhiM(treeMine.ak4jet_pt[h21jet2], treeMine.ak4jet_eta[h21jet2], treeMine.ak4jet_phi[h21jet2], treeMine.ak4jet_mass[h21jet2])
            pmass = jet1pmassB[0]
            bbtag = jet1bbtagB[0]
            bjet1 = h21jet1
            bjet2 = h21jet2

    if passHHCR == 2:
            fatjet = TLorentzVector()
            ak4jet1 = TLorentzVector()
            ak4jet2 = TLorentzVector()
            fatjet.SetPtEtaPhiM(jet2Branch[0], jet2Branch[1], jet2Branch[2], jet2Branch[3])
            ak4jet1.SetPtEtaPhiM(treeMine.ak4jet_pt[h22jet1], treeMine.ak4jet_eta[h22jet1], treeMine.ak4jet_phi[h22jet1], treeMine.ak4jet_mass[h22jet1])
            ak4jet2.SetPtEtaPhiM(treeMine.ak4jet_pt[h22jet2], treeMine.ak4jet_eta[h22jet2], treeMine.ak4jet_phi[h22jet2], treeMine.ak4jet_mass[h22jet2])
            pmass = jet2pmassB[0]
            bbtag = jet2bbtagB[0]
            bjet1 = h22jet1
            bjet2 = h22jet2

    if passHHCR > 0:
            pTH1=(fatjet).Pt()
            pTH2=(ak4jet1+ak4jet2).Pt()
            mH1=pmass
            mH2=(ak4jet1+ak4jet2).M()

            f1[0]=(ak4jet1+ak4jet2+fatjet).M()
            g1[0]=mH2
            h1[0]=mH1
            i1[0]=treeMine.xsec
            l1[0]=bbtag
            q1[0]=treeMine.vtype
            o1[0]=treeMine.puWeights
            p1[0]=treeMine.norm
            r1[0]=count_jets1outsidef + count_jets2outsidef
            s1[0]=count_fatjets
            m1[0]=1.
            t1[0]=treeMine.evt
            u1[0]=treeMine.passesBoosted
            v1[0]=treeMine.passesResolved
           # trigger1[0]=treeMine.HLT_ht800
           # trigger2[0]=treeMine.HLT_AK08
           # trigger3[0]=treeMine.HLT_HH4b
           # trigger_pre[0]=treeMine.HLT_ht350
                        
            if pTH1<300:
                sf=0.9135
                sfup=sf+0.15
                sfd=sf-0.15
            elif pTH1<400:
                sf=0.913
                sfup=sf+0.088
                sfd=sf-0.088
            elif pTH1<500:
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
                        
                cmvaSF[0]=treeMine.ak4jetCMVAMSF[bjet1]
                cmvaSFup[0]=treeMine.ak4jetCMVAMSF_Up[bjet1]
                cmvaSFdown[0]=treeMine.ak4jetCMVAMSF_Down[bjet1]
                cmvaSF2[0]=treeMine.ak4jetCMVAMSF[bjet2]
                cmvaSFup2[0]=treeMine.ak4jetCMVAMSF_Up[bjet2]
                cmvaSFdown2[0]=treeMine.ak4jetCMVAMSF_Down[bjet2]
                        
                        
                puW_up[0]=treeMine.puWeightsUp
                puW_down[0]=treeMine.puWeightsDown

    mynewTree.Fill()

print "Done with " + outputfilename

f2.cd()
f2.Write()
f2.Close()

f.Close()


