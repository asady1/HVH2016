#!/usr/bin/env python

### PDF4LHC recommendations for LHC Run II: http://arxiv.org/abs/1510.03865

import os, sys, ROOT
import math
from ROOT import *
from math import *
import glob
import FWCore.ParameterSet.Config as cms
from DataFormats.FWLite import Events, Handle
from array import *
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-o", "--outName", dest="outName",
                  help="output file name")
parser.add_option("-m", "--mass", dest="mass",
                  help="mass")
(options, args) = parser.parse_args()
outputfilename = options.outName


idxpdfs=range(1,1+101)
nwts=len(idxpdfs)

allevt   = 0
allevtup = [] 
allevtlo = [] 

passevt   = 0
passevtup = []
passevtlo = []

f = ROOT.TFile.Open(sys.argv[1], "READ")
f2 =  ROOT.TFile(outputfilename, 'recreate')
f2.cd()
mychain = f.Get("tree")
entries=mychain.GetEntriesFast()

mynewTree = ROOT.TTree('mynewTree', 'mynewTree')
pdfNum = array('f', [-100.0])
allEvt = array('f', [-100.0])
allEvtUp = array('f', [-100.0])
allEvtLo = array('f', [-100.0])
passEvt = array('f', [-100.0])
passEvtUp = array('f', [-100.0])
passEvtLo = array('f', [-100.0])
mynewTree.Branch("pdfNum", pdfNum, "pdfNum")
mynewTree.Branch("allEvt", allEvt, "allEvt")
mynewTree.Branch("allEvtUp", allEvtUp, "allEvtUp")
mynewTree.Branch("allEvtLo", allEvtLo, "allEvtLo")
mynewTree.Branch("passEvt", passEvt, "passEvt")
mynewTree.Branch("passEvtUp", passEvtUp, "passEvtUp")
mynewTree.Branch("passEvtLo", passEvtLo, "passEvtLo")

for i in idxpdfs:

    evtwt=0
    evtwtpdfUp=0
    evtwtpdfLo=0
    passevtwt=0
    passevtwtpdfUp=0
    passevtwtpdfLo=0

    evts=200
    ievt = 0
    #for each event
    totalEv = 0
    passEv = 0
    for event in mychain:
      ievt = ievt+1
      if ievt > evts: break
      
      totalEv += 1

      #get this variable
      lhewts = event.LHE_weights_pdf_wgt
      lhewtcentral = float(lhewts[idxpdfs[0]])

      #total lhewtcentral for all events
      evtwt+=lhewtcentral

      happy = 0
      if ievt%2 == 0:
        happy = 1
      #for the ith PDF, get the lhewts and determine whether it's an up or down, calculate total for all events
      lhewt = lhewts[i-1]
      if i%2 == 0:
        evtwtpdfUp += float(lhewt) 
      elif i%2 == 1:
        evtwtpdfLo += float(lhewt)
    
      #event selection goes here

#      if ( event.LeadingDiJets_minv_leading2hjets > 1100 and \
#          event.LeadingDiJets_deta_leading2hjets < 1.3 and \
#          event.AK8Jets_Pt[0] > 300 and event.AK8Jets_Pt[1] > 300 and \
#          abs(event.AK8Jets_Eta[0]) < 2.4 and abs(event.AK8Jets_Eta[1]) < 2.4 and \
#          (105. < event.AK8Jets_MassSoftDrop[0] < 135.) and (105. < event.AK8Jets_MassSoftDrop[1] < 135.) and \
#          (event.AK8Jets_tau2[0]/event.AK8Jets_tau1[0] < 0.55) and (event.AK8Jets_tau2[1]/event.AK8Jets_tau1[1] < #0.55) ) :

 #       passTT = event.AK8Jets_doublesv[0] > 0.8 and event.AK8Jets_doublesv[1] > 0.8
 #       passLL = event.AK8Jets_doublesv[0] > 0.3 and event.AK8Jets_doublesv[1] > 0.3
#
#        if (cat=="LL" and passLL and not passTT) or (cat=="TT" and passTT) : 
    
        #if you pass event selection
      if len(event.FatjetAK08ungroomed_pt) > 0 and len(event.Jet_pt) > 3:
        AK8 = ROOT.TLorentzVector()
        AK8.SetPtEtaPhiM(event.FatjetAK08ungroomed_pt[0], event.FatjetAK08ungroomed_eta[0], event.FatjetAK08ungroomed_phi[0], event.FatjetAK08ungroomed_mass[0])
        AK40j = ROOT.TLorentzVector()
        AK40j.SetPtEtaPhiM(event.Jet_pt[0], event.Jet_eta[0], event.Jet_phi[0], event.Jet_mass[0])
        AK41j = ROOT.TLorentzVector()
        AK41j.SetPtEtaPhiM(event.Jet_pt[1], event.Jet_eta[1], event.Jet_phi[1], event.Jet_mass[1])
        AK42j = ROOT.TLorentzVector()
        AK42j.SetPtEtaPhiM(event.Jet_pt[2], event.Jet_eta[2], event.Jet_phi[2], event.Jet_mass[2])
        AK43j = ROOT.TLorentzVector()
        AK43j.SetPtEtaPhiM(event.Jet_pt[3], event.Jet_eta[3], event.Jet_phi[3], event.Jet_mass[3])
        if len(event.Jet_pt) > 4:
          AK44j = ROOT.TLorentzVector()
          AK44j.SetPtEtaPhiM(event.Jet_pt[4], event.Jet_eta[4], event.Jet_phi[4], event.Jet_mass[4])
          if len(event.Jet_pt) > 5:
            AK45j = ROOT.TLorentzVector()
            AK45j.SetPtEtaPhiM(event.Jet_pt[5], event.Jet_eta[5], event.Jet_phi[5], event.Jet_mass[5])
        AK41 = ROOT.TLorentzVector()
        AK42 = ROOT.TLorentzVector()
        AK43 = ROOT.TLorentzVector()
        AK41.SetPtEtaPhiM(-1.,-100.,-100.,-1.)
        AK42.SetPtEtaPhiM(-1.,-100.,-100.,-1.)
        AK43.SetPtEtaPhiM(-1.,-100.,-100.,-1.)
        dCSV1 = 0
        dCSV2 = 0
        if AK8.DeltaR(AK40j) > 0.8:
          AK41 = AK40j
          dCSV1 = (event.Jet_btagDeepCSVb[0] + event.Jet_btagDeepCSVbb[0])
          if AK8.DeltaR(AK41j) > 0.8:
            AK42 = AK41j
            dCSV2 = (event.Jet_btagDeepCSVb[1] + event.Jet_btagDeepCSVbb[1])
          else:
            if AK8.DeltaR(AK42j) > 0.8:
              AK42 = AK42j
              AK43 = AK43j
              dCSV2 = (event.Jet_btagDeepCSVb[2] + event.Jet_btagDeepCSVbb[2]) 
            else:
              if AK8.DeltaR(AK43j) > 0.8:
                AK42 = AK43j
                AK43 = AK44j
                dCSV2 = (event.Jet_btagDeepCSVb[3] + event.Jet_btagDeepCSVbb[3])
              else:
                if len(event.Jet_pt) > 4:
                  if AK8.DeltaR(AK44j) > 0.8:
                    AK42 = AK44j
                    dCSV2 = (event.Jet_btagDeepCSVb[4] + event.Jet_btagDeepCSVbb[4])
                    if AK8.DeltaR(AK45j) > 0.8:
                      AK43 = AK45j
        else:
          if AK8.DeltaR(AK41j) > 0.8:
            AK41 = AK41j
            dCSV1 = (event.Jet_btagDeepCSVb[1] + event.Jet_btagDeepCSVbb[1])
            if AK8.DeltaR(AK42j) > 0.8:
              AK42 = AK42j
              AK43 = AK43j
              dCSV2 = (event.Jet_btagDeepCSVb[2] + event.Jet_btagDeepCSVbb[2])
            else:
              if AK8.DeltaR(AK43j) > 0.8:
                AK42 = AK43j
                dCSV2 = (event.Jet_btagDeepCSVb[3] + event.Jet_btagDeepCSVbb[3])
                if len(event.Jet_pt) > 4:
                  AK43 = AK44j
              else:
                if len(event.Jet_pt) > 4:
                  if AK8.DeltaR(AK44j) > 0.8:
                    AK42 = AK44j
                    dCSV2 = (event.Jet_btagDeepCSVb[4] + event.Jet_btagDeepCSVbb[4])
                    if AK8.DeltaR(AK45j) > 0.8:
                       AK43 = AK45j
          else:
            if AK8.DeltaR(AK42j) > 0.8:
              AK41 = AK42j
              dCSV1 = (event.Jet_btagDeepCSVb[2] + event.Jet_btagDeepCSVbb[2])
              if AK8.DeltaR(AK43j) > 0.8:
                AK42 = AK43j
                dCSV2 = (event.Jet_btagDeepCSVb[3] + event.Jet_btagDeepCSVbb[3])
                AK43 = AK44j
              else:
                if len(event.Jet_pt) > 4:
                  if AK8.DeltaR(AK44j) > 0.8:
                    AK42 = AK44j
                    dCSV2 = (event.Jet_btagDeepCSVb[4] + event.Jet_btagDeepCSVbb[4])
                    if AK8.DeltaR(AK45j) > 0.8:
                      AK43 = AK45j
            else:
              if AK8.DeltaR(AK43j) > 0.8:
                AK41 = AK43j
                dCSV1 = (event.Jet_btagDeepCSVb[3] + event.Jet_btagDeepCSVbb[3])
                if len(event.Jet_pt) > 4:
                  AK42 = AK44j
                  dCSV2 = (event.Jet_btagDeepCSVb[4] + event.Jet_btagDeepCSVbb[4])
                  if AK8.DeltaR(AK45j) > 0.8:
                    AK43 = AK45j
                     
        dRAK8J1 = AK8.DeltaR(AK41)
        dRAK8J2 = AK8.DeltaR(AK42)
        dRAK4 = AK41.DeltaR(AK42)
        dEta = abs((AK41+AK42).Eta() - AK8.Eta())
        djm = (AK41+AK42).M()
        if event.FatjetAK08ungroomed_puppi_tau1[0] > 0:
          tau21 = event.FatjetAK08ungroomed_puppi_tau2[0]/event.FatjetAK08ungroomed_puppi_tau1[0]
        else:
          tau21 = 1.
        passv = 0
        if event.Vtype == -1:
          passv = 1
        if event.Vtype == 4:
          passv = 1

        if (event.FatjetAK08ungroomed_pt[0] > 300 and abs(event.FatjetAK08ungroomed_eta[0]) < 2.4 and AK41.Pt() > 30 and AK42.Pt() > 30 and abs(AK41.Eta()) < 2.4 and abs(AK42.Eta()) < 2.4 and dCSV1 > 0.6324 and dCSV2 > 0.6324 and dRAK8J1 > 0.8 and dRAK8J2 > 0.8 and dRAK4 < 1.5 and event.FatjetAK08ungroomed_puppi_msoftdrop_raw[0] > 105 and event.FatjetAK08ungroomed_puppi_msoftdrop_raw[0] < 135 and tau21 < 0.55 and event.FatjetAK08ungroomed_bbtag[0] > 0.8 and djm > 90 and djm < 140 and (AK41+AK42+AK43).M() > 200 and dEta < 2.0 and (AK41 + AK42 + AK8).M() > 700 and passv > 0): 
          passEv += 1
        #total lhewtcentral for all passing events
          passevtwt+=lhewtcentral
          #for the ith PDF, get the lhewts and determine whether it's an up or down, calculate total for passed events
          if i%2 == 0:
            passevtwtpdfUp += float(lhewt) 
          elif i%2 == 1:
            passevtwtpdfLo += float(lhewt)

    pdfNum[0] = i
    allEvt[0] = evtwt
    allEvtUp[0] = evtwtpdfUp
    allEvtLo[0] = evtwtpdfLo
    passEvt[0] = passevtwt
    passEvtUp[0] = passevtwtpdfUp
    passEvtLo[0] = passevtwtpdfLo
    mynewTree.Fill()
    allevt=evtwt
    allevtup.append(evtwtpdfUp)
    allevtlo.append(evtwtpdfLo)

    passevt=passevtwt
    passevtup.append(passevtwtpdfUp)
    passevtlo.append(passevtwtpdfLo)

#    print i
#    print allevt
#    print passevt

#print allevtup
#print allevtlo

#print passevtup
#print passevtlo
  #evtwt passing/ all evt wt
aenominal = passevt/allevt
  
allevtup_sum=0
for k in allevtup:
    allevtup_sum += pow(k - allevt,2.)
allevtup_sum = math.sqrt(allevtup_sum/100)

passevtup_sum=0
for k in passevtup:
    passevtup_sum += pow(k - passevt,2.)
passevtup_sum = math.sqrt(passevtup_sum/100)

  #total pdf up passing / total pdf up all
aepdfup = passevtup_sum/allevtup_sum

allevtlo_sum=0
for k in allevtlo:
    allevtlo_sum += pow(k - allevt,2.)
allevtlo_sum = math.sqrt(allevtlo_sum/100)

passevtlo_sum=0
for k in passevtlo:
    passevtlo_sum += pow(k - passevt,2.)
passevtlo_sum = math.sqrt(passevtlo_sum/100)

  #total pdf down passing / total pdf down all
aepdflo = passevtlo_sum/allevtlo_sum

#print " aenominal %f aepdfup %f aepdflo %f" % (aenominal, aepdfup, aepdflo)

#print aepdfup/aenominal
#print aepdflo/aenominal
#  print passEv
#  print totalEv

#  return aepdfup/aenominal, aepdflo/aenominal

#from glob import glob

#fs = glob("/afs/cern.ch/user/d/devdatta/afswork/CMSREL/Analysis/CMSSW_8_0_20/src/Analysis/VLQAna/test/HH4bTrees_15Mar2017/*/output/hh4b_0.root")


#for f in fs:
#  mass = f.split("/")[-3]
#  print mass
#  out = open("pdfuncert%s.log" % mass,"w")
#  upLL, downLL = getPDFUncert(f,"LL")
#up, down = getPDFUncert("/eos/uscms/store/user/lpchbb/HeppyNtuples/V25b/GluGluToHHTo4B_node_2_13TeV-madgraph/VHBB_HEPPY_V25c_GluGluToHHTo4B_node_2_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170523_042327/0000/tree_8.root")
#mass = options.mass
#up, down = getPDFUncert()
#txtfile = open(outputfilename,"w")
#txtfile.write(
#txtfile.write("%s CMS_PDF_Scales lnN %1.3f/%1.3f  -\n" % (mass, up, down)) 
#up, down = getPDFUncert("root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node10_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node10_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033031/0000/tree_1.root")
#  out.write("%s CMS_PDF_Scales lnN %1.3f/%1.3f  -  %1.3f/%1.3f  -\n" % (mass, upLL, downLL, upTT, downTT))
#out.close()
f2.cd()
f2.Write()
f2.Close()
