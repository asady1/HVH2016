#! /usr/bin/env python
# Analytical reweighting implementation for H->4b
# This file is part of https://github.com/cms-hh/HHStatAnalysis
#from optparse import OptionParser
#import ROOT
#from ROOT import *
#import numpy as np
#from HHStatAnalysis.AnalyticalModels.python.NonResonantModel i# python nonResonant_test_v0.py --kl 1 --kt 1 
# compiling
#import os
#import glob
#import math
#from array import *
import os
#import numpy
import glob
import math    
from math import *

import ROOT 
#ROOT.gROOT.Macro("rootlogon.C")
from ROOT import *

import FWCore.ParameterSet.Config as cms

import sys
from DataFormats.FWLite import Events, Handle

from array import *

from optparse import OptionParser


import NonResonantModel
from NonResonantModel import *

parser = OptionParser()
parser.add_option("--kl", type="float", dest="kll", help="Multiplicative factor in the H trilinear wrt to SM")
parser.add_option("--kt", type="float", dest="ktt", help="Multiplicative factor in the H top Yukawa wrt to SM")

parser.add_option("--c2", type="float", dest="c22", help="ttHH with triangle loop", default=0)
parser.add_option("--cg", type="float", dest="cgg", help="HGG contact", default=0)
parser.add_option("--c2g", type="float", dest="c2gg", help="HHGG contact", default=0)
parser.add_option("--doPlot", action='store_true', default=False, dest='doPlot', 
                    help='calculate the limit in the benchmark poin specified')
parser.add_option("-o", "--outName", dest="outName",help="output file name")

(options, args) = parser.parse_args()
print " "
kl = options.kll
kt = options.ktt
c2 = options.c22
cg = options.cgg
c2g = options.c2gg
outputfilename = options.outName


#print "events for V0 (the same of the fullsim version of Moriond 2016) \n We sum SM + box + the benchmarks from 2-13"
#if c2 != 0 or cg != 0 or c2g != 0 :  print "The analytical function is not yet implemented"

###########################################################
# read events and apply weight
###########################################################
def main():
  #if 1 > 0 :
  # declare the 2D ===> should be global variable
  model = NonResonantModel()
  # obtaining BSM/SM coeficients
  #dumb = model.ReadCoefficients("../data/coefficientsByBin_A1A3A7.txt") 
  dumb = model.ReadCoefficients("../data/coefficientsByBin_extended_3M_costHHSim_19-4.txt") 
  #dumb = model.ReadCoefficients("../data/coefficientsByBin_extended_3M.txt") 
  counteventSM=0
  sumWeight=0
  # now loop over events, calculate weights using the coeffitients and  plot histograms
  # We sum SM + box + the benchmarks from 2-13 
  # read the 2D histo referent to the sum of events
  #fileHH=ROOT.TFile("../../../Analysis/Support/NonResonant/Hist2DSum_V0_SM_box.root")
  #sumHAnalyticalBin = fileHH.Get("SumV0_AnalyticalBin")
  histfilename="/uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/V25miniTrees/nodeHisto.root"
  #histtitle= "SumV0_AnalyticalBinExt" #
  histtitle= "hist2D" #
  fileHH=ROOT.TFile(histfilename)
  sumHAnalyticalBin = fileHH.Get(histtitle)
  calcSumOfWeights = model.getNormalization(kl, kt,c2,cg,c2g,histfilename,histtitle)  # this input is flexible, tatabb may have only the SM
  # print "sum of weights calculated" , calcSumOfWeights 
  # read the events
#  pathBenchEvents="/eos/user/a/acarvalh/asciiHH_tofit/GF_HH_BSM/" #"/eos/user/a/acarvalh/asciiHH_tofit/GF_HH_BSM/" # events to reweight   
  file=ROOT.TFile.Open("/eos/uscms/store/user/asady1/V25/NR_nodehadd.root","READ")

  f2 =  ROOT.TFile(outputfilename, 'recreate')
  f2.cd()

  tree=file.Get("myTree")
  nev = tree.GetEntries()

  theTree = ROOT.TTree('myTree', 'myTree')

  CountWeightedmc = ROOT.TH1F("CountWeighted","Count with sign(gen weight) and pu weight",1,0,2)
  CountWeightedmc.Add(file.Get("CountWeighted"))

#  mhh = array('f', [-100.0])
#  costhetast = array('f', [-100.0])
  weightSig = array('f', [-100.0])
#  ak4jet_pt = vector('double')()


#  theTree.Branch('mhh', mhh, 'mhh/F')
#  theTree.Branch('costhetast', costhetast, 'costhetast/F')
  theTree.Branch('weightSig', weightSig, 'weightSig/F')
#  theTree.Branch('ak4jet_pt',ak4jet_pt)


  regressedJetpT_0 = array('f', [-100.0])
  regressedJetpT_1 = array('f', [-100.0])
  jet1pt = array('f', [-100.0])
  jet2pt = array('f', [-100.0])
  jet1pt_reg = array('f', [-100.0])
  jet2pt_reg = array('f', [-100.0])
  jet1mass_reg = array('f', [-100.0])
  jet2mass_reg = array('f', [-100.0])
  jet1mass_reg_noL2L3 = array('f', [-100.0])
  jet2mass_reg_noL2L3 = array('f', [-100.0])

#  jet1NearbyJetcsvArray = array('f', [-100.0, -100.0, -100.0, -100.0])
#  jet2NearbyJetcsvArray = array('f', [-100.0, -100.0, -100.0, -100.0])
#  jet1NearbyJetcmvaArray = array('f', [-100.0, -100.0, -100.0, -100.0])
#  jet2NearbyJetcmvaArray = array('f', [-100.0, -100.0, -100.0, -100.0])
  jet1NJcsv = array('f', [-100.0])
  jet2NJcsv = array('f', [-100.0])
  jet1NJcmva = array('f', [-100.0])
  jet2NJcmva = array('f', [-100.0])
  jet1ID = array('f', [-100.0])
  jet2ID = array('f', [-100.0])
  jet1eta = array('f', [-100.0])
  jet2eta = array('f', [-100.0])
  jet1phi = array('f', [-100.0])
  jet2phi = array('f', [-100.0])
  jet1mass = array('f', [-100.0])
  jet2mass = array('f', [-100.0])
  etadiff = array('f', [-100.0])
  dijetmass = array('f', [-100.0])
  dijetmass_corr = array('f', [-100.0])
  dijetmass_reg = array('f', [-100.0])
  dijetmass_corr_punc = array('f', [-100.0])
  jet1tau21 = array('f', [-100.0])
  jet1tau1 = array('f', [-100.0])
  jet1tau2 = array('f', [-100.0])
  jet1tau3 = array('f', [-100.0])
  jet2tau21 = array('f', [-100.0])
  jet2tau1 = array('f', [-100.0])
  jet2tau2 = array('f', [-100.0])
  jet2tau3 = array('f', [-100.0])
  jet1pmass = array('f', [-100.0])
  jet2pmass = array('f', [-100.0])
  jet1pmass_noL2L3 = array('f', [-100.0])
  jet1pmass_CA15 = array('f', [-100.0])
  jet1pmassunc = array('f', [-100.0])
  jet2pmassunc = array('f', [-100.0])
  jet1bbtag = array('f', [-100.0])
  jet2bbtag = array('f', [-100.0])
  jet1s1csv = array('f', [-100.0])
  jet2s1csv = array('f', [-100.0])
  jet1s2csv = array('f', [-100.0])
  jet2s2csv = array('f', [-100.0])

  mhh = array('f', [-100.0])
  costhetast = array('f', [-100.0])

  jet1_puppi_pt = array('f', [-100.0])
  jet2_puppi_pt = array('f', [-100.0])
  jet1_puppi_eta = array('f', [-100.0])
  jet2_puppi_eta = array('f', [-100.0])
  jet1_puppi_phi = array('f', [-100.0])
  jet2_puppi_phi = array('f', [-100.0])
  jet1_puppi_mass = array('f', [-100.0])
  jet2_puppi_mass = array('f', [-100.0])
  jet1_puppi_tau21 = array('f', [-100.0])
  jet2_puppi_tau21 = array('f', [-100.0])
  jet1_puppi_msoftdrop = array('f', [-100.0])
  jet2_puppi_msoftdrop = array('f', [-100.0])
  jet1_puppi_msoftdrop_corrL2L3 = array('f', [-100.0])
  jet2_puppi_msoftdrop_corrL2L3 = array('f', [-100.0])
  jet1_puppi_TheaCorr = array('f', [-100.0])
  jet2_puppi_TheaCorr = array('f', [-100.0])
  jet1_puppi_msoftdrop_raw = array('f', [-100.0])
  jet2_puppi_msoftdrop_raw = array('f', [-100.0])

  jetSJfla = array('f', [-100.0]*4)
  jetSJpt =  array('f', [-100.0]*4)
  jetSJcsv = array('f', [-100.0]*4)
  jetSJeta = array('f', [-100.0]*4)
  triggerpassbb = array('f', [-100.0])
  nHiggsTags = array('f', [-100.0])
  nTrueInt = array('f', [-100])
  vtype = array('f', [-100.0])
  nPVs = array('f', [-100.0])
  isData = array('f', [100.0])
  jet1nbHadron = array('f', [-100.0])
  jet2nbHadron = array('f', [-100.0])
  jet1flavor = array('f', [-100.0])
  jet2flavor = array('f', [-100.0])
  jet1ncHadron = array('f', [-100.0])
  jet2ncHadron = array('f', [-100.0])
  gen1Pt = array('f', [-100.0])
  gen1phi = array('f', [-100.0])
  gen1Eta = array('f', [-100.0])
  gen1Mass = array('f', [-100.0])
  gen1ID = array('f', [-100.0])
  gen2Pt = array('f', [-100.0])
  gen2Phi = array('f', [-100.0])
  gen2Eta = array('f', [-100.0])
  gen2Mass = array('f', [-100.0])
  gen2ID = array('f', [-100.0])
  CA15jet1pt = array('f', [-100.0])
  CA15jet2pt = array('f', [-100.0])
  CA15jet1eta = array('f', [-100.0])
  CA15jet2eta = array('f', [-100.0])
  CA15jet1phi = array('f', [-100.0])
  CA15jet2phi = array('f', [-100.0])
  CA15jet1mass = array('f', [-100.0])
  CA15jet2mass = array('f', [-100.0])
  jet1l1l2l3 = array('f', [-100.0])
  jet1l2l3 = array('f', [-100.0])
  jet2l1l2l3 = array('f', [-100.0])
  jet2l2l3 = array('f', [-100.0])
  jet1l1l2l3Unc = array('f', [-100.0])
  jet1l2l3Unc = array('f', [-100.0])
  jet2l1l2l3Unc = array('f', [-100.0])
  jet2l2l3Unc = array('f', [-100.0])
  jet1JER = array('f', [-100.0])
  jet2JER = array('f', [-100.0])
  puWeights = array('f', [-100.0])
  puWeightsUp = array('f', [-100.0])
  puWeightsDown = array('f', [-100.0])
  json = array('f', [-100.0])

  bbtag1SFTight = array('f', [-100.0])
  bbtag2SFTight = array('f', [-100.0])
  bbtag1SFTightUp = array('f', [-100.0])
  bbtag2SFTightUp = array('f', [-100.0])
  bbtag1SFTightDown = array('f', [-100.0])
  bbtag2SFTightDown = array('f', [-100.0])
  bbtag1SFLoose = array('f', [-100.0])
  bbtag2SFLoose = array('f', [-100.0])
  bbtag1SFLooseUp = array('f', [-100.0])
  bbtag2SFLooseUp = array('f', [-100.0])
  bbtag1SFLooseDown = array('f', [-100.0])
  bbtag2SFLooseDown = array('f', [-100.0])
  passesBoosted = array('f', [-100.0])
  passesResolved = array('f', [-100.0])
  SFTight = array('f', [-100.0])
  SFTightup = array('f', [-100.0])
  SFTightdown = array('f', [-100.0])
  SFLoose = array('f', [-100.0])
  SFLooseup = array('f', [-100.0])
  SFLoosedown = array('f', [-100.0])
  SF4sj = array('f', [-100.0])
  SF4sjUp = array('f', [-100.0])
  SF4sjDown = array('f', [-100.0])
  SF3sj = array('f', [-100.0])
  SF3sjUp = array('f', [-100.0])
  SF3sjDown = array('f', [-100.0])
  trigWeight = array('f', [-100.0])
  trigWeightUp = array('f', [-100.0])
  trigWeightDown = array('f', [-100.0])
  trigWeight2Up = array('f', [-100.0])
  trigWeight2Down = array('f', [-100.0])

  evt = array('f', [-100.0])
  ht = array('f', [-100.0])
  htJet30 = array('f', [-100.0])
  xsec = array('f', [-100.0])
  sjSF = array('f', [-100.0])
  sjSFup = array('f', [-100.0])
  sjSFdown = array('f', [-100.0])
  genJet1BH = array('f', [-100.0])
  genjet2BH = array('f', [-100.0])
  genjet1CH = array('f', [-100.0])
  genjet2CH = array('f', [-100.0])
  MET = array('f', [-100.0])
  nAK08Jets = array('f', [-100.0])
  nAK04Jets = array('f', [-100.0])
  DeltaPhi1 = array('f', [-100.0])
  DeltaPhi2 = array('f', [-100.0])
  DeltaPhi3 = array('f', [-100.0])
  DeltaPhi4 = array('f', [-100.0])
  nAK04btagsMWP = array('f', [-100.0])
  nTightEle = array('f', [-100.0])
  nTightMu = array('f', [-100.0])
  nLooseEle = array('f', [-100.0])
  nLooseMu = array('f', [-100.0])
  tPtsum = array('f', [-100.0])

  LeadingAK8Jet_MatchedHadW = array('f', [-100.0])

  aLeptons_pT = vector('double')()
  aLeptons_eta = vector('double')()
  aLeptons_phi = vector('double')()
  aLeptons_mass = vector('double')()
  vLeptons_pT = vector('double')()
  vLeptons_eta = vector('double')()
  vLeptons_phi = vector('double')()
  vLeptons_mass = vector('double')()

  ak4jet_pt = vector('double')()
  ak4jet_eta = vector('double')()
  ak4jet_phi = vector('double')()
  ak4jet_mass = vector('double')()
  ak4jetID = vector('double')()
  ak4jetHeppyFlavour = vector('double')()
  ak4jetMCflavour = vector('double')()
  ak4jetPartonFlavour = vector('double')()
  ak4jetHadronFlavour = vector('double')()
  ak4jetCSVLSF = vector('double')()
  ak4jetCSVLSF_Up = vector('double')()
  ak4jetCSVLSF_Down = vector('double')()
  ak4jetCSVMSF = vector('double')()
  ak4jetCSVMSF_up = vector('double')()
  ak4jetCSVMSF_Down = vector('double')()
  ak4jetCSVTSF = vector('double')()
  ak4jetCSVTSF_Up = vector('double')()
  ak4jetCSVTSF_Down = vector('double')()
  ak4jetCMVALSF = vector('double')()
  ak4jetCMVALSF_Up = vector('double')()
  ak4jetCMVALSF_Down = vector('double')()
  ak4jetCMVAMSF = vector('double')()
  ak4jetCMVAMSF_Up = vector('double')()
  ak4jetCMVAMSF_Down = vector('double')()
  ak4jetCMVATSF = vector('double')()
  ak4jetCMVATSF_Up = vector('double')()
  ak4jetCMVATSF_Down = vector('double')()
  ak4jetCSV = vector('double')()
  ak4jetDeepCSVb = vector('double')()
  ak4jetDeepCSVbb = vector('double')()
  ak4jetCMVA = vector('double')()
  ak4jetCorr = vector('double')()
  ak4jetCorrJECUp = vector('double')()
  ak4jetCorrJECDown = vector('double')()
  ak4jetCorrJER = vector('double')()
  ak4jetCorrJERUp = vector('double')()
  ak4jetCorrJERDown = vector('double')()
  ak4genJetPt = vector('double')()
  ak4genJetPhi = vector('double')()
  ak4genJetEta = vector('double')()
  ak4genJetMass = vector('double')()
  ak4genJetID = vector('double')()
  HLT_PFHT900_v = array('f', [-100.0])
  HLT_PFHT800_v = array('f', [-100.0])
  HLT_PFJet80_v = array('f', [-100.0])
  HLT_QuadJet45_TripleBTagCSV_p087_v = array('f', [-100.0])
  HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v = array('f', [-100.0])
  HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v = array('f', [-100.0])
  HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v = array('f', [-100.0])
  HLT_AK8PFJet360_TrimMass30_v = array('f', [-100.0])
  HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
  HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
  HLT_PFJet140_v = array('f', [-100.0])
  HLT_PFJet200_v = array('f', [-100.0])
  HLT_PFJet260_v = array('f', [-100.0])
  HLT_Mu24_eta2p1_v = array('f', [-100.0])
  HLT_Mu27_v = array('f', [-100.0])
  HLT_Ele105_CaloIdVT_GsfTrkIdT_v = array('f', [-100.0])


        #creating the tree branches we need
  theTree.Branch('regressedJetpT_0', regressedJetpT_0, 'regressedJetpT_0/F')
  theTree.Branch('regressedJetpT_1', regressedJetpT_1, 'regressedJetpT_1/F')
  theTree.Branch('jet1pt', jet1pt, 'jet1pt/F')
  theTree.Branch('jet2pt', jet2pt, 'jet2pt/F')
  theTree.Branch('jet1pt_reg', jet1pt_reg, 'jet1pt_reg/F')
  theTree.Branch('jet2pt_reg', jet2pt_reg, 'jet2pt_reg/F')
  theTree.Branch('jet1mass_reg', jet1mass_reg, 'jet1mass_reg/F')
  theTree.Branch('jet2mass_reg', jet2mass_reg, 'jet2mass_reg/F')
  theTree.Branch('jet1mass_reg_noL2L3', jet1mass_reg_noL2L3, 'jet1mass_reg_noL2L3/F')
  theTree.Branch('jet2mass_reg_noL2L3', jet2mass_reg_noL2L3, 'jet2mass_reg_noL2L3/F')
#  theTree.Branch('jet1NearbyJetcsv', jet1NearbyJetcsvArray, 'pt/F:eta/F:phi/F:mass/F')
#  theTree.Branch('jet2NearbyJetcsv', jet2NearbyJetcsvArray, 'pt/F:eta/F:phi/F:mass/F')
#  theTree.Branch('jet1NearbyJetcmva', jet1NearbyJetcmvaArray, 'pt/F:eta/F:phi/F:mass/F')
#  theTree.Branch('jet2NearbyJetcmva', jet2NearbyJetcmvaArray, 'pt/F:eta/F:phi/F:mass/F')
  theTree.Branch('jet1NJcsv', jet1NJcsv, 'jet1NJcsv')
  theTree.Branch('jet2NJcsv', jet2NJcsv, 'jet2NJcsv')
  theTree.Branch('jet1NJcmva', jet1NJcmva, 'jet1NJcmva')
  theTree.Branch('jet2NJcmva', jet2NJcmva, 'jet2NJcmva')
  theTree.Branch('jet1eta', jet1eta, 'jet1eta/F')
  theTree.Branch('jet2eta', jet2eta, 'jet2eta/F')
  theTree.Branch('jet1phi', jet1phi, 'jet1phi/F')
  theTree.Branch('jet2phi', jet2phi, 'jet2phi/F')
  theTree.Branch('jet1mass', jet1mass, 'jet1mass/F')
  theTree.Branch('jet2mass', jet2mass, 'jet2mass/F')
  theTree.Branch('etadiff', etadiff, 'etadiff/F')
  theTree.Branch('dijetmass', dijetmass, 'dijetmass/F')
  theTree.Branch('dijetmass_corr', dijetmass_corr, 'dijetmass_corr/F')
  theTree.Branch('dijetmass_reg', dijetmass_reg, 'dijetmass_reg/F')
  theTree.Branch('dijetmass_corr_punc', dijetmass_corr_punc, 'dijetmass_corr_punc/F')
  theTree.Branch('jet1tau21', jet1tau21, 'jet1tau21/F')
  theTree.Branch('jet1tau1', jet1tau1, 'jet1tau1/F')
  theTree.Branch('jet1tau2', jet1tau2, 'jet1tau2/F')
  theTree.Branch('jet1tau3', jet1tau3, 'jet1tau3/F')
  theTree.Branch('jet2tau21', jet2tau21, 'jet2tau21/F')
  theTree.Branch('jet2tau1', jet2tau1, 'jet2tau1/F')
  theTree.Branch('jet2tau2', jet2tau2, 'jet2tau2/F')
  theTree.Branch('jet2tau3', jet2tau3, 'jet2tau3/F')
  theTree.Branch('jet1pmass', jet1pmass, 'jet1pmass/F')
  theTree.Branch('jet2pmass', jet2pmass, 'jet2pmass/F')
  theTree.Branch('jet1pmass_noL2L3', jet1pmass_noL2L3, 'jet1pmass_noL2L3/F')
  theTree.Branch('jet1pmass_CA15', jet1pmass_CA15, 'jet1pmass_CA15/F')
  theTree.Branch('jet1pmassunc', jet1pmassunc, 'jet1pmassunc/F')
  theTree.Branch('jet2pmassunc', jet2pmassunc, 'jet2pmassunc/F')
  theTree.Branch('jet1bbtag', jet1bbtag, 'jet1bbtag/F')
  theTree.Branch('jet2bbtag', jet2bbtag, 'jet2bbtag/F')
  theTree.Branch('jet1s1csv', jet1s1csv, 'jet1s1csv/F')
  theTree.Branch('jet2s1csv', jet2s1csv, 'jet2s1csv/F')
  theTree.Branch('jet1s2csv', jet1s2csv, 'jet1s2csv/F')
  theTree.Branch('jet2s2csv', jet2s2csv, 'jet2s2csv/F')

  theTree.Branch('jet1_puppi_pt', jet1_puppi_pt, 'jet1_puppi_pt/F')
  theTree.Branch('jet2_puppi_pt', jet2_puppi_pt, 'jet2_puppi_pt/F')
  theTree.Branch('jet1_puppi_eta', jet1_puppi_eta, 'jet1_puppi_eta/F')
  theTree.Branch('jet2_puppi_eta', jet2_puppi_eta, 'jet2_puppi_eta/F')
  theTree.Branch('jet1_puppi_phi', jet1_puppi_phi, 'jet1_puppi_phi/F')
  theTree.Branch('jet2_puppi_phi', jet2_puppi_phi, 'jet2_puppi_phi/F')
  theTree.Branch('jet1_puppi_mass', jet1_puppi_mass, 'jet1_puppi_mass/F')
  theTree.Branch('jet2_puppi_mass', jet2_puppi_mass, 'jet2_puppi_mass/F')
  theTree.Branch('jet1_puppi_tau21', jet1_puppi_tau21, 'jet1_puppi_tau21/F')
  theTree.Branch('jet2_puppi_tau21', jet2_puppi_tau21, 'jet2_puppi_tau21/F')
  theTree.Branch('jet1_puppi_msoftdrop', jet1_puppi_msoftdrop, 'jet1_puppi_msoftdrop/F')
  theTree.Branch('jet2_puppi_msoftdrop', jet2_puppi_msoftdrop, 'jet2_puppi_msoftdrop/F')
  theTree.Branch('jet1_puppi_msoftdrop_corrL2L3', jet1_puppi_msoftdrop_corrL2L3, 'jet1_puppi_msoftdrop_corrL2L3/F')
  theTree.Branch('jet2_puppi_msoftdrop_corrL2L3', jet2_puppi_msoftdrop_corrL2L3, 'jet2_puppi_msoftdrop_corrL2L3/F')
  theTree.Branch('jet1_puppi_TheaCorr', jet1_puppi_TheaCorr, 'jet1_puppi_TheaCorr/F')
  theTree.Branch('jet2_puppi_TheaCorr', jet2_puppi_TheaCorr, 'jet2_puppi_TheaCorr/F')
  theTree.Branch('jet1_puppi_msoftdrop_raw', jet1_puppi_msoftdrop_raw, 'jet1_puppi_msoftdrop_raw/F')
  theTree.Branch('jet2_puppi_msoftdrop_raw', jet2_puppi_msoftdrop_raw, 'jet2_puppi_msoftdrop_raw/F')

  theTree.Branch('mhh', mhh, 'mhh/F')
  theTree.Branch('costhetast', costhetast, 'costhetast/F')

  theTree.Branch('nAK08Jets', nAK08Jets, 'nAK08Jets/F')
  theTree.Branch('nAK04Jets', nAK04Jets, 'nAK04Jets/F')
  theTree.Branch('nAK04btagsMWP', nAK04btagsMWP, 'nAK04btagsMWP/F')
  theTree.Branch('nHiggsTags', nHiggsTags, 'nHiggsTags/F')
  theTree.Branch('triggerpassbb', triggerpassbb, 'triggerpassbb/F')
  theTree.Branch('nTrueInt',nTrueInt,'nTrueInt/F')
  theTree.Branch('puWeights',puWeights,'puWeights/F')
  theTree.Branch('puWeightsUp',puWeightsUp,'puWeightsUp/F')
  theTree.Branch('puWeightsDown',puWeightsDown,'puWeightsDown/F')
  theTree.Branch('jet1ID', jet1ID, 'jet1ID/F')
  theTree.Branch('jet2ID', jet2ID, 'jet2ID/F')
  theTree.Branch('vtype', vtype, 'vtype/F')
  theTree.Branch('nPVs', nPVs, 'nPVs/F')
  theTree.Branch('isData', isData, 'isData/F')
  theTree.Branch('jet1nbHadron', jet1nbHadron, 'jet1nbHadron/F')
  theTree.Branch('jet2nbHadron', jet2nbHadron, 'jet2nbHadron/F')
  theTree.Branch('jet1flavor', jet1flavor, 'jet1flavor/F')
  theTree.Branch('jet2flavor', jet2flavor, 'jet2flavor/F')
  theTree.Branch('jet1ncHadron', jet1ncHadron, 'jet1ncHadron/F')
  theTree.Branch('jet2ncHadron', jet2ncHadron, 'jet2ncHadron/F')
  theTree.Branch('gen1Pt', gen1Pt, 'gen1Pt/F')
  theTree.Branch('gen1phi', gen1phi, 'gen1phi/F')
  theTree.Branch('gen1Eta', gen1Eta, 'gen1Eta/F')
  theTree.Branch('gen1Mass', gen1Mass, 'gen1Mass/F')
  theTree.Branch('gen1ID', gen1ID, 'gen1ID/F')
  theTree.Branch('gen2Pt', gen2Pt, 'gen2Pt/F')
  theTree.Branch('gen2Phi', gen2Phi, 'gen2Phi/F')
  theTree.Branch('gen2Eta', gen2Eta, 'gen2Eta/F')
  theTree.Branch('gen2Mass', gen2Mass, 'gen2Mass/F')
  theTree.Branch('gen2ID', gen2ID, 'gen2ID/F')
  theTree.Branch('CA15jet1pt', CA15jet1pt,'CA15jet1pt/F')
  theTree.Branch('CA15jet1eta', CA15jet1eta,'CA15jet1eta/F')
  theTree.Branch('CA15jet1phi', CA15jet1phi,'CA15jet1phi/F')
  theTree.Branch('CA15jet1mass', CA15jet1mass,'CA15jet1mass/F')
  theTree.Branch('CA15jet2pt', CA15jet2pt,'CA15jet2pt/F')
  theTree.Branch('CA15jet2eta', CA15jet2eta,'CA15jet2eta/F')
  theTree.Branch('CA15jet2phi', CA15jet2phi,'CA15jet2phi/F')
  theTree.Branch('CA15jet2mass', CA15jet2mass,'CA15jet2mass/F')
  theTree.Branch('jet1l1l2l3', jet1l1l2l3, 'jet1l1l2l3/F')
  theTree.Branch('jet1l2l3', jet1l2l3, 'jet1l2l3/F')
  theTree.Branch('jet2l1l2l3', jet2l1l2l3, 'jet2l1l2l3/F')
  theTree.Branch('jet2l2l3', jet2l2l3, 'jet2l2l3/F')
  theTree.Branch('jet1l1l2l3Unc', jet1l1l2l3Unc, 'jet1l1l2l3Unc/F')
  theTree.Branch('jet1l2l3Unc', jet1l2l3Unc, 'jet1l2l3Unc/F')
  theTree.Branch('jet2l1l2l3Unc', jet2l1l2l3Unc, 'jet2l1l2l3Unc/F')
  theTree.Branch('jet2l2l3Unc', jet2l2l3Unc, 'jet2l2l3Unc/F')
  theTree.Branch('jet1JER', jet1JER, 'jet1JER/F')
  theTree.Branch('jet2JER', jet2JER, 'jet2JER/F')
  theTree.Branch('json', json, 'json/F')
  theTree.Branch('DeltaPhi1', DeltaPhi1, 'DeltaPhi1/F')
  theTree.Branch('DeltaPhi2', DeltaPhi2, 'DeltaPhi2/F')
  theTree.Branch('DeltaPhi3', DeltaPhi3, 'DeltaPhi3/F')
  theTree.Branch('DeltaPhi4', DeltaPhi4, 'DeltaPhi4/F')

  theTree.Branch('bbtag1SFTight', bbtag1SFTight, 'bbtag1SFTight/F')
  theTree.Branch('bbtag2SFTight', bbtag2SFTight, 'bbtag2SFTight/F')
  theTree.Branch('bbtag1SFTightUp', bbtag1SFTightUp, 'bbtag1SFTightUp/F')
  theTree.Branch('bbtag2SFTightUp', bbtag2SFTightUp, 'bbtag2SFTightUp/F')
  theTree.Branch('bbtag1SFTightDown', bbtag1SFTightDown, 'bbtag1SFTightDown/F')
  theTree.Branch('bbtag2SFTightDown', bbtag2SFTightDown, 'bbtag2SFTightDown/F')
  theTree.Branch('bbtag1SFLoose', bbtag1SFLoose, 'bbtag1SFLoose/F')
  theTree.Branch('bbtag2SFLoose', bbtag2SFLoose, 'bbtag2SFLoose/F')
  theTree.Branch('bbtag1SFLooseUp', bbtag1SFLooseUp, 'bbtag1SFLooseUp/F')
  theTree.Branch('bbtag2SFLooseUp', bbtag2SFLooseUp, 'bbtag2SFLooseUp/F')
  theTree.Branch('bbtag1SFLooseDown', bbtag1SFLooseDown, 'bbtag1SFLooseDown/F')
  theTree.Branch('bbtag2SFLooseDown', bbtag2SFLooseDown, 'bbtag2SFLooseDown/F')

  theTree.Branch('passesBoosted', passesBoosted, 'passesBoosted/F')
  theTree.Branch('passesResolved', passesResolved, 'passesResolved/F')

  theTree.Branch('SFTight', SFTight, 'SFTight/F')
  theTree.Branch('SFTightup', SFTightup, 'SFTightup/F')
  theTree.Branch('SFTightdown', SFTightdown, 'SFTightdown/F')
  theTree.Branch('SFLoose', SFLoose, 'SFLoose/F')
  theTree.Branch('SFLooseup', SFLooseup, 'SFLooseup/F')
  theTree.Branch('SFLoosedown', SFLoosedown, 'SFLoosedown/F')
  theTree.Branch('SF4sj', SF4sj, 'SF4sj/F')
  theTree.Branch('SF4sjUp', SF4sjUp, 'SF4sjUp/F')
  theTree.Branch('SF4sjDown', SF4sjDown, 'SF4sjDown/F')
  theTree.Branch('SF3sj', SF3sj, 'SF3sj/F')
  theTree.Branch('SF3sjUp', SF3sjUp, 'SF3sjUp/F')
  theTree.Branch('SF3sjDown', SF3sjDown, 'SF3sjDown/F')
  theTree.Branch('tPtsum', tPtsum, 'tPtsum/F')
  theTree.Branch('trigWeight', trigWeight, 'trigWeight/F')
  theTree.Branch('trigWeightUp', trigWeightUp, 'trigWeightUp/F')
  theTree.Branch('trigWeightDown', trigWeightDown, 'trigWeightDown/F')
  theTree.Branch('trigWeight2Up', trigWeight2Up, 'trigWeight2Up/F')
  theTree.Branch('trigWeight2Down', trigWeight2Down, 'trigWeight2Down/F')
  theTree.Branch('LeadingAK8Jet_MatchedHadW', LeadingAK8Jet_MatchedHadW, 'LeadingAK8Jet_MatchedHadW/F')

  theTree.Branch('evt',evt,'evt/F')
  theTree.Branch('ht', ht, 'ht/F')
  theTree.Branch('htJet30', htJet30, 'htJet30/F')
  theTree.Branch('MET', MET, 'MET/F')
  theTree.Branch('xsec', xsec, 'xsec/F')
  theTree.Branch('sjSF', sjSF, 'sjSF/F')
  theTree.Branch('sjSFup', sjSFup, 'sjSFup/F')
  theTree.Branch('sjSFdown', sjSFdown, 'sjSFdown/F')
  theTree.Branch('jetSJfla',jetSJfla,'jetSJfla[4]/F')
  theTree.Branch('jetSJpt', jetSJpt,'jetSJpt[4]/F')
  theTree.Branch('jetSJcsv',jetSJcsv,'jetSJcsv[4]/F')
  theTree.Branch('jetSJeta',jetSJeta,'jetSJeta[4]/F')
  theTree.Branch('genJet1BH', genJet1BH, 'genJet1BH/F')
  theTree.Branch('genjet2BH', genjet2BH, 'genjet2BH/F')
  theTree.Branch('genjet1CH', genjet1CH, 'genjet1CH/F')
  theTree.Branch('genjet2CH', genjet2CH, 'genjet2CH/F')
  theTree.Branch('nTightEle', nTightEle, 'nTightEle/F')
  theTree.Branch('nTightMu', nTightMu, 'nTightMu/F')
  theTree.Branch('nLooseEle', nLooseEle, 'nLooseEle/F')
  theTree.Branch('nLooseMu', nLooseMu, 'nLooseMu/F')

  theTree.Branch('aLeptons_pT',aLeptons_pT)
  theTree.Branch('aLeptons_eta',aLeptons_eta)
  theTree.Branch('aLeptons_phi',aLeptons_phi)
  theTree.Branch('aLeptons_mass',aLeptons_mass)
  theTree.Branch('vLeptons_pT',vLeptons_pT)
  theTree.Branch('vLeptons_eta',vLeptons_eta)
  theTree.Branch('vLeptons_phi',vLeptons_phi)
  theTree.Branch('vLeptons_mass',vLeptons_mass)

  theTree.Branch('ak4jet_pt',ak4jet_pt)
  theTree.Branch('ak4jet_eta',ak4jet_eta)
  theTree.Branch('ak4jet_phi',ak4jet_phi)
  theTree.Branch('ak4jet_mass',ak4jet_mass)
  theTree.Branch('ak4jetID',ak4jetID)
  theTree.Branch('ak4jetHeppyFlavour', ak4jetHeppyFlavour)
  theTree.Branch('ak4jetMCflavour', ak4jetMCflavour)
  theTree.Branch('ak4jetPartonFlavour', ak4jetPartonFlavour)
  theTree.Branch('ak4jetHadronFlavour', ak4jetHadronFlavour)
  theTree.Branch('ak4jetCSVLSF', ak4jetCSVLSF)
  theTree.Branch('ak4jetCSVLSF_Up', ak4jetCSVLSF_Up)
  theTree.Branch('ak4jetCSVLSF_Down', ak4jetCSVLSF_Down)
  theTree.Branch('ak4jetCSVMSF', ak4jetCSVMSF)
  theTree.Branch('ak4jetCSVMSF_up', ak4jetCSVMSF_up)
  theTree.Branch('ak4jetCSVMSF_Down', ak4jetCSVMSF_Down)
  theTree.Branch('ak4jetCSVTSF', ak4jetCSVTSF)
  theTree.Branch('ak4jetCSVTSF_Up', ak4jetCSVTSF_Up)
  theTree.Branch('ak4jetCSVTSF_Down', ak4jetCSVTSF_Down)
  theTree.Branch('ak4jetCMVALSF', ak4jetCMVALSF)
  theTree.Branch('ak4jetCMVALSF_Up', ak4jetCMVALSF_Up)
  theTree.Branch('ak4jetCMVALSF_Down', ak4jetCMVALSF_Down)
  theTree.Branch('ak4jetCMVAMSF', ak4jetCMVAMSF)
  theTree.Branch('ak4jetCMVAMSF_Up', ak4jetCMVAMSF_Up)
  theTree.Branch('ak4jetCMVAMSF_Down', ak4jetCMVAMSF_Down)
  theTree.Branch('ak4jetCMVATSF', ak4jetCMVATSF)
  theTree.Branch('ak4jetCMVATSF_Up', ak4jetCMVATSF_Up)
  theTree.Branch('ak4jetCMVATSF_Down', ak4jetCMVATSF_Down)
  theTree.Branch('ak4jetCSV', ak4jetCSV)
  theTree.Branch('ak4jetDeepCSVb', ak4jetDeepCSVb)
  theTree.Branch('ak4jetDeepCSVbb', ak4jetDeepCSVbb)
  theTree.Branch('ak4jetCMVA', ak4jetCMVA)
  theTree.Branch('ak4jetCorr', ak4jetCorr)
  theTree.Branch('ak4jetCorrJECUp', ak4jetCorrJECUp)
  theTree.Branch('ak4jetCorrJECDown', ak4jetCorrJECDown)
  theTree.Branch('ak4jetCorrJER', ak4jetCorrJER)
  theTree.Branch('ak4jetCorrJERUp', ak4jetCorrJERUp)
  theTree.Branch('ak4jetCorrJERDown', ak4jetCorrJERDown)
  theTree.Branch('ak4genJetPt', ak4genJetPt)
  theTree.Branch('ak4genJetPhi', ak4genJetPhi)
  theTree.Branch('ak4genJetEta', ak4genJetEta)
  theTree.Branch('ak4genJetMass', ak4genJetMass)
  theTree.Branch('ak4genJetID', ak4genJetID)
  theTree.Branch('HLT_PFHT900_v', HLT_PFHT900_v, 'HLT_PFHT900_v/F')
  theTree.Branch('HLT_PFHT800_v', HLT_PFHT800_v, 'HLT_PFHT800_v/F')
  theTree.Branch('HLT_PFJet80_v', HLT_PFJet80_v, 'HLT_PFJet80_v/F')
  theTree.Branch('HLT_QuadJet45_TripleBTagCSV_p087_v', HLT_QuadJet45_TripleBTagCSV_p087_v, 'HLT_QuadJet45_TripleBTagCSV_p087_v/F')
  theTree.Branch('HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v', HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v, 'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v/F')
  theTree.Branch('HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v', HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v/F')
  theTree.Branch('HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v', HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v/F')
  theTree.Branch('HLT_AK8PFJet360_TrimMass30_v', HLT_AK8PFJet360_TrimMass30_v, 'HLT_AK8PFJet360_TrimMass30_v/F')
  theTree.Branch('HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v', HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v, 'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v/F')
  theTree.Branch('HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v', HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v, 'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v/F')
  theTree.Branch('HLT_PFJet140_v', HLT_PFJet140_v, 'HLT_PFJet140_v/F')
  theTree.Branch('HLT_PFJet200_v', HLT_PFJet200_v, 'HLT_PFJet200_v/F')
  theTree.Branch('HLT_PFJet260_v', HLT_PFJet260_v, 'HLT_PFJet260_v/F')
  theTree.Branch('HLT_Mu24_eta2p1_v', HLT_Mu24_eta2p1_v, 'HLT_Mu24_eta2p1_v/F')
  theTree.Branch('HLT_Mu27_v', HLT_Mu27_v, 'HLT_Mu27_v/F')
  theTree.Branch('HLT_Ele105_CaloIdVT_GsfTrkIdT_v', HLT_Ele105_CaloIdVT_GsfTrkIdT_v, 'HLT_Ele105_CaloIdVT_GsfTrkIdT_v/F')


  # declare the histograms 
  CalcMhh = np.zeros((nev))
  CalcCost = np.zeros((nev))
  CalcPtH = np.zeros((nev))
  CalcPtHH = np.zeros((nev))
  CalcWeight = np.zeros((nev))

  CalcPtHgg = np.zeros((nev))
  CalcMhhReco = np.zeros((nev))
  CalcMXReco = np.zeros((nev))

  countevent = 0
  #for kll in range(-5,5) : model.getNormalization(kll, kt,sumHBenchBin)
  for iev in range(0,nev) :
      tree.GetEntry(iev)
      mhhvar = tree.mhh
      costvar = tree.costhetast

      mhhcost= [mhhvar,costvar,0,0] # to store [mhh , cost] of that event
      # find the Nevents from the sum of events on that bin
      bmhh = sumHAnalyticalBin.GetXaxis().FindBin(mhhvar)
      bcost = sumHAnalyticalBin.GetYaxis().FindBin(abs(costvar))
      #print (tree.GenHHCost,cost,bcost)
      effSumV0 = sumHAnalyticalBin.GetBinContent(bmhh,abs(bcost))  # quantity of simulated events in that bin (without cuts)
      weight = model.getScaleFactor(mhhvar , costvar,kl, kt,c2,cg,c2g, effSumV0 , calcSumOfWeights)
      weightSig[0] = weight

      if weight > 0: 
               #print countevent
               CalcMhh[countevent] = float(mhhcost[0]) 
               CalcCost[countevent] = float(abs(mhhcost[1])) 
               CalcPtH[countevent] = float(mhhcost[2]) 
               CalcPtHH[countevent] = float(mhhcost[3]) 
               CalcWeight[countevent] = weight 
               countevent+=1
               sumWeight+=weight

      regressedJetpT_0[0] = tree.regressedJetpT_0
      regressedJetpT_1[0] = tree.regressedJetpT_1
      jet1pt[0] = tree.jet1pt
      jet2pt[0] = tree.jet2pt
      jet1pt_reg[0] = tree.jet1pt_reg
      jet2pt_reg[0] = tree.jet2pt_reg
      jet1mass_reg[0] = tree.jet1mass_reg
      jet2mass_reg[0] = tree.jet2mass_reg
      jet1mass_reg_noL2L3[0] = tree.jet1mass_reg_noL2L3
      jet2mass_reg_noL2L3[0] = tree.jet2mass_reg_noL2L3
      
#      jet1NearbyJetcsvArray = tree.jet1NearbyJetcsv
#      jet2NearbyJetcsvArray = tree.jet2NearbyJetcsv
#      jet1NearbyJetcmvaArray = tree.jet1NearbyJetcmva
#      jet2NearbyJetcmvaArray = tree.jet2NearbyJetcmva
      jet1NJcsv[0] = tree.jet1NJcsv
      jet2NJcsv[0] = tree.jet2NJcsv
      jet1NJcmva[0] = tree.jet1NJcmva
      jet2NJcmva[0] = tree.jet2NJcmva
      jet1ID[0] = tree.jet1ID
      jet2ID[0] = tree.jet2ID
      jet1eta[0] = tree.jet1eta
      jet2eta[0] = tree.jet2eta
      jet1phi[0] = tree.jet1phi
      jet2phi[0] = tree.jet2phi
      jet1mass[0] = tree.jet1mass
      jet2mass[0] = tree.jet2mass
      etadiff[0] = tree.etadiff
      dijetmass[0] = tree.dijetmass
      dijetmass_corr[0] = tree.dijetmass_corr
      dijetmass_reg[0] = tree.dijetmass_reg
      dijetmass_corr_punc[0] = tree.dijetmass_corr_punc
      jet1tau21[0] = tree.jet1tau21
      jet1tau1[0] = tree.jet1tau1
      jet1tau2[0] = tree.jet1tau2
      jet1tau3[0] = tree.jet1tau3
      jet2tau21[0] = tree.jet2tau21
      jet2tau1[0] = tree.jet2tau1
      jet2tau2[0] = tree.jet2tau2
      jet2tau3[0] = tree.jet2tau3
      jet1pmass[0] = tree.jet1pmass
      jet2pmass[0] = tree.jet2pmass
      jet1pmass_noL2L3[0] = tree.jet1pmass_noL2L3
      jet1pmass_CA15[0] = tree.jet1pmass_CA15
      jet1pmassunc[0] = tree.jet1pmassunc
      jet2pmassunc[0] = tree.jet2pmassunc
      jet1bbtag[0] = tree.jet1bbtag
      jet2bbtag[0] = tree.jet2bbtag
      jet1s1csv[0] = tree.jet1s1csv
      jet2s1csv[0] = tree.jet2s1csv
      jet1s2csv[0] = tree.jet1s2csv
      jet2s2csv[0] = tree.jet2s2csv
      
      mhh[0] = tree.mhh
      costhetast[0] = tree.costhetast
      
      jet1_puppi_pt[0] = tree.jet1_puppi_pt
      jet2_puppi_pt[0] = tree.jet2_puppi_pt
      jet1_puppi_eta[0] = tree.jet1_puppi_eta
      jet2_puppi_eta[0] = tree.jet2_puppi_eta
      jet1_puppi_phi[0] = tree.jet1_puppi_phi
      jet2_puppi_phi[0] = tree.jet2_puppi_phi
      jet1_puppi_mass[0] = tree.jet1_puppi_mass
      jet2_puppi_mass[0] = tree.jet2_puppi_mass
      jet1_puppi_tau21[0] = tree.jet1_puppi_tau21
      jet2_puppi_tau21[0] = tree.jet2_puppi_tau21
      jet1_puppi_msoftdrop[0] = tree.jet1_puppi_msoftdrop
      jet2_puppi_msoftdrop[0] = tree.jet2_puppi_msoftdrop
      jet1_puppi_msoftdrop_corrL2L3[0] = tree.jet1_puppi_msoftdrop_corrL2L3
      jet2_puppi_msoftdrop_corrL2L3[0] = tree.jet2_puppi_msoftdrop_corrL2L3
      jet1_puppi_TheaCorr[0] = tree.jet1_puppi_TheaCorr
      jet2_puppi_TheaCorr[0] = tree.jet2_puppi_TheaCorr
      jet1_puppi_msoftdrop_raw[0] = tree.jet1_puppi_msoftdrop_raw
      jet2_puppi_msoftdrop_raw[0] = tree.jet2_puppi_msoftdrop_raw
      
      jetSJfla = tree.jetSJfla
      jetSJpt =  tree.jetSJpt
      jetSJcsv = tree.jetSJcsv
      jetSJeta = tree.jetSJeta
      triggerpassbb[0] = tree.triggerpassbb
      nHiggsTags[0] = tree.nHiggsTags
      nTrueInt[0] = tree.nTrueInt
      vtype[0] = tree.vtype
      nPVs[0] = tree.nPVs
      isData[0] = tree.isData
      jet1nbHadron[0] = tree.jet1nbHadron
      jet2nbHadron[0] = tree.jet2nbHadron
      jet1flavor[0] = tree.jet1flavor
      jet2flavor[0] = tree.jet2flavor
      jet1ncHadron[0] = tree.jet1ncHadron
      jet2ncHadron[0] = tree.jet2ncHadron
      gen1Pt[0] = tree.gen1Pt
      gen1phi[0] = tree.gen1phi
      gen1Eta[0] = tree.gen1Eta
      gen1Mass[0] = tree.gen1Mass
      gen1ID[0] = tree.gen1ID
      gen2Pt[0] = tree.gen2Pt
      gen2Phi[0] = tree.gen2Phi
      gen2Eta[0] = tree.gen2Eta
      gen2Mass[0] = tree.gen2Mass
      gen2ID[0] = tree.gen2ID
      CA15jet1pt[0] = tree.CA15jet1pt
      CA15jet2pt[0] = tree.CA15jet2pt
      CA15jet1eta[0] = tree.CA15jet1eta
      CA15jet2eta[0] = tree.CA15jet2eta
      CA15jet1phi[0] = tree.CA15jet1phi
      CA15jet2phi[0] = tree.CA15jet2phi
      CA15jet1mass[0] = tree.CA15jet1mass
      CA15jet2mass[0] = tree.CA15jet2mass
      jet1l1l2l3[0] = tree.jet1l1l2l3
      jet1l2l3[0] = tree.jet1l2l3
      jet2l1l2l3[0] = tree.jet2l1l2l3
      jet2l2l3[0] = tree.jet2l2l3
      jet1l1l2l3Unc[0] = tree.jet1l1l2l3Unc
      jet1l2l3Unc[0] = tree.jet1l2l3Unc
      jet2l1l2l3Unc[0] = tree.jet2l1l2l3Unc
      jet2l2l3Unc[0] = tree.jet2l2l3Unc
      jet1JER[0] = tree.jet1JER
      jet2JER[0] = tree.jet2JER
      puWeights[0] = tree.puWeights
      puWeightsUp[0] = tree.puWeightsUp
      puWeightsDown[0] = tree.puWeightsDown
      json[0] = tree.json
      
      bbtag1SFTight[0] = tree.bbtag1SFTight
      bbtag2SFTight[0] = tree.bbtag2SFTight
      bbtag1SFTightUp[0] = tree.bbtag1SFTightUp
      bbtag2SFTightUp[0] = tree.bbtag2SFTightUp
      bbtag1SFTightDown[0] = tree.bbtag1SFTightDown
      bbtag2SFTightDown[0] = tree.bbtag2SFTightDown
      bbtag1SFLoose[0] = tree.bbtag1SFLoose
      bbtag2SFLoose[0] = tree.bbtag2SFLoose
      bbtag1SFLooseUp[0] = tree.bbtag1SFLooseUp
      bbtag2SFLooseUp[0] = tree.bbtag2SFLooseUp
      bbtag1SFLooseDown[0] = tree.bbtag1SFLooseDown
      bbtag2SFLooseDown[0] = tree.bbtag2SFLooseDown
      passesBoosted[0] = tree.passesBoosted
      passesResolved[0] = tree.passesResolved
      SFTight[0] = tree.SFTight
      SFTightup[0] = tree.SFTightup
      SFTightdown[0] = tree.SFTightdown
      SFLoose[0] = tree.SFLoose
      SFLooseup[0] = tree.SFLooseup
      SFLoosedown[0] = tree.SFLoosedown
      SF4sj[0] = tree.SF4sj
      SF4sjUp[0] = tree.SF4sjUp
      SF4sjDown[0] = tree.SF4sjDown
      SF3sj[0] = tree.SF3sj
      SF3sjUp[0] = tree.SF3sjUp
      SF3sjDown[0] = tree.SF3sjDown
      trigWeight[0] = tree.trigWeight
      trigWeightUp[0] = tree.trigWeightUp
      trigWeightDown[0] = tree.trigWeightDown
      trigWeight2Up[0] = tree.trigWeight2Up
      trigWeight2Down[0] = tree.trigWeight2Down
      
      evt[0] = tree.evt
      ht[0] = tree.ht
      htJet30[0] = tree.htJet30
      xsec[0] = tree.xsec
      sjSF[0] = tree.sjSF
      sjSFup[0] = tree.sjSFup
      sjSFdown[0] = tree.sjSFdown
      genJet1BH[0] = tree.genJet1BH
      genjet2BH[0] = tree.genjet2BH
      genjet1CH[0] = tree.genjet1CH
      genjet2CH[0] = tree.genjet2CH
      MET[0] = tree.MET
      nAK08Jets[0] = tree.nAK08Jets
      nAK04Jets[0] = tree.nAK04Jets
      DeltaPhi1[0] = tree.DeltaPhi1
      DeltaPhi2[0] = tree.DeltaPhi2
      DeltaPhi3[0] = tree.DeltaPhi3
      DeltaPhi4[0] = tree.DeltaPhi4
      nAK04btagsMWP[0] = tree.nAK04btagsMWP
      nTightEle[0] = tree.nTightEle
      nTightMu[0] = tree.nTightMu
      nLooseEle[0] = tree.nLooseEle
      nLooseMu[0] = tree.nLooseMu
      tPtsum[0] = tree.tPtsum
      
      LeadingAK8Jet_MatchedHadW[0] = tree.LeadingAK8Jet_MatchedHadW
      
      aLeptons_pT = tree.aLeptons_pT
      aLeptons_eta = tree.aLeptons_eta
      aLeptons_phi = tree.aLeptons_phi
      aLeptons_mass = tree.aLeptons_mass
      vLeptons_pT = tree.vLeptons_pT
      vLeptons_eta = tree.vLeptons_eta
      vLeptons_phi = tree.vLeptons_phi
      vLeptons_mass = tree.vLeptons_mass

      ak4jet_pt.clear()
      ak4jet_eta.clear()
      ak4jet_phi.clear()
      ak4jet_mass.clear()
      ak4jetID.clear()
      ak4jetHeppyFlavour.clear()
      ak4jetMCflavour.clear()
      ak4jetPartonFlavour.clear()
      ak4jetHadronFlavour.clear()
      ak4jetCSVLSF.clear()
      ak4jetCSVLSF_Up.clear()
      ak4jetCSVLSF_Down.clear()
      ak4jetCSVMSF.clear()
      ak4jetCSVMSF_up.clear()
      ak4jetCSVMSF_Down.clear()
      ak4jetCSVTSF.clear()
      ak4jetCSVTSF_Up.clear()
      ak4jetCSVTSF_Down.clear()
      ak4jetCMVALSF.clear()
      ak4jetCMVALSF_Up.clear()
      ak4jetCMVALSF_Down.clear()
      ak4jetCMVAMSF.clear()
      ak4jetCMVAMSF_Up.clear()
      ak4jetCMVAMSF_Down.clear()
      ak4jetCMVATSF.clear()
      ak4jetCMVATSF_Up.clear()
      ak4jetCMVATSF_Down.clear()
      ak4jetCSV.clear()
      ak4jetDeepCSVb.clear()
      ak4jetDeepCSVbb.clear()
      ak4jetCMVA.clear()
      ak4jetCorr.clear()
      ak4jetCorrJECUp.clear()
      ak4jetCorrJECDown.clear()
      ak4jetCorrJER.clear()
      ak4jetCorrJERUp.clear()
      ak4jetCorrJERDown.clear()
      ak4genJetPt.clear()
      ak4genJetPhi.clear()
      ak4genJetEta.clear()
      ak4genJetMass.clear()
      ak4genJetID.clear()

      for j in range(len(tree.ak4jet_pt)):
        ak4jet_pt.push_back(tree.ak4jet_pt[j])
        ak4jet_eta.push_back(tree.ak4jet_eta[j])
        ak4jet_phi.push_back(tree.ak4jet_phi[j])
        ak4jet_mass.push_back(tree.ak4jet_mass[j])
        ak4jetID.push_back(tree.ak4jetID[j])
        ak4jetHeppyFlavour.push_back(tree.ak4jetHeppyFlavour[j])
        ak4jetMCflavour.push_back(tree.ak4jetMCflavour[j])
        ak4jetPartonFlavour.push_back(tree.ak4jetPartonFlavour[j])
        ak4jetHadronFlavour.push_back(tree.ak4jetHadronFlavour[j])
        ak4jetCSVLSF.push_back(tree.ak4jetCSVLSF[j])
        ak4jetCSVLSF_Up.push_back(tree.ak4jetCSVLSF_Up[j])
        ak4jetCSVLSF_Down.push_back(tree.ak4jetCSVLSF_Down[j])
        ak4jetCSVMSF.push_back(tree.ak4jetCSVMSF[j])
        ak4jetCSVMSF_up.push_back(tree.ak4jetCSVMSF_up[j])
        ak4jetCSVMSF_Down.push_back(tree.ak4jetCSVMSF_Down[j])
        ak4jetCSVTSF.push_back(tree.ak4jetCSVTSF[j])
        ak4jetCSVTSF_Up.push_back(tree.ak4jetCSVTSF_Up[j])
        ak4jetCSVTSF_Down.push_back(tree.ak4jetCSVTSF_Down[j])
        ak4jetCMVALSF.push_back(tree.ak4jetCMVALSF[j])
        ak4jetCMVALSF_Up.push_back(tree.ak4jetCMVALSF_Up[j])
        ak4jetCMVALSF_Down.push_back(tree.ak4jetCMVALSF_Down[j])
        ak4jetCMVAMSF.push_back(tree.ak4jetCMVAMSF[j])
        ak4jetCMVAMSF_Up.push_back(tree.ak4jetCMVAMSF_Up[j])
        ak4jetCMVAMSF_Down.push_back(tree.ak4jetCMVAMSF_Down[j])
        ak4jetCMVATSF.push_back(tree.ak4jetCMVATSF[j])
        ak4jetCMVATSF_Up.push_back(tree.ak4jetCMVATSF_Up[j])
        ak4jetCMVATSF_Down.push_back(tree.ak4jetCMVATSF_Down[j])
        ak4jetCSV.push_back(tree.ak4jetCSV[j])
        ak4jetDeepCSVb.push_back(tree.ak4jetDeepCSVb[j])
        ak4jetDeepCSVbb.push_back(tree.ak4jetDeepCSVbb[j])
        ak4jetCMVA.push_back(tree.ak4jetCMVA[j])
        ak4jetCorr.push_back(tree.ak4jetCorr[j])
        ak4jetCorrJECUp.push_back(tree.ak4jetCorrJECUp[j])
        ak4jetCorrJECDown.push_back(tree.ak4jetCorrJECDown[j])
        ak4jetCorrJER.push_back(tree.ak4jetCorrJER[j])
        ak4jetCorrJERUp.push_back(tree.ak4jetCorrJERUp[j])
        ak4jetCorrJERDown.push_back(tree.ak4jetCorrJERDown[j])
        ak4genJetPt.push_back(tree.ak4genJetPt[j])
        ak4genJetPhi.push_back(tree.ak4genJetPhi[j])
        ak4genJetEta.push_back(tree.ak4genJetEta[j])
        ak4genJetMass.push_back(tree.ak4genJetMass[j])
        ak4genJetID.push_back(tree.ak4genJetID[j])
      HLT_PFHT900_v[0] = tree.HLT_PFHT900_v
      HLT_PFHT800_v[0] = tree.HLT_PFHT800_v
      HLT_PFJet80_v[0] = tree.HLT_PFJet80_v
      HLT_QuadJet45_TripleBTagCSV_p087_v[0] = tree.HLT_QuadJet45_TripleBTagCSV_p087_v
      HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v[0] = tree.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
      HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0] = tree.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v
      HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] = tree.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v
      HLT_AK8PFJet360_TrimMass30_v[0] = tree.HLT_AK8PFJet360_TrimMass30_v
      HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] = tree.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v
      HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] = tree.HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v
      HLT_PFJet140_v[0] = tree.HLT_PFJet140_v
      HLT_PFJet200_v[0] = tree.HLT_PFJet200_v
      HLT_PFJet260_v[0] = tree.HLT_PFJet260_v
      HLT_Mu24_eta2p1_v[0] = tree.HLT_Mu24_eta2p1_v
      HLT_Mu27_v[0] = tree.HLT_Mu27_v
      HLT_Ele105_CaloIdVT_GsfTrkIdT_v[0] = tree.HLT_Ele105_CaloIdVT_GsfTrkIdT_v

      theTree.Fill()

  print "plotted histogram reweighted from ",countevent," events, ", float(100*(nev-countevent)/nev)," % of the events was lost in empty bins in SM simulation"
  print "sum of weights",sumWeight
  f2.cd()
  f2.Write()
  f2.Close()
  file.Close()
   # model.effSM,model.MHH,model.COSTS,model.A1,model.A3,model.A7, effSumV0) 
##########################################
if __name__ == "__main__":  
   main()


#print len(MHH),A1[0][0]

#options.kll, options.ktt)


# obtaining BSM/SM scale factors

#canvas = ROOT.TCanvas("")
#scaleFactors.Draw('colz')
#canvas.SaveAs("{}.pdf".format(scaleFactors.GetName()))
