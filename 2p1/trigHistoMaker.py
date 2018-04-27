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
#parser.add_option("-t", "--saveTrig", dest="saveTrig",
#                  help="trigger info saved")
#parser.add_option("-b", "--ttbar", dest="ttbar",
#                  help="isttbar")
#parser.add_option("-d", "--data", dest="data",
#                  help="isdata")
(options, args) = parser.parse_args()
outputfilename = options.outName

#numberLimit = float(sys.argv[1])

f = ROOT.TFile.Open(sys.argv[1],"READ")

f2 =  ROOT.TFile(outputfilename, 'recreate')
#print outputfilename
f2.cd()

treeMine  = f.Get('mynewTree')

myTree = ROOT.TTree('myTree', 'myTree')

htes = ROOT.TH1F("htes", "HT Event Selection", 60, 0, 3000)
htes260 = ROOT.TH1F("htes260", "HT Event Selection + PFJet260", 60, 0, 3000)
htes260B = ROOT.TH1F("htes260B", "HT Event Selection + PFJet260 + Boosted OR", 60, 0, 3000)

invmes = ROOT.TH1F("invmes", "HT Event Selection", 60, 0, 3000)
invmes260 = ROOT.TH1F("invmes260", "HT Event Selection + PFJet260", 60, 0, 3000)
invmes260B = ROOT.TH1F("invmes260B", "HT Event Selection + PFJet260 + Boosted OR", 60, 0, 3000)
invmFull = ROOT.TH1F("invmFull", "Invariant Mass Full", 60, 0, 3000)

redmes = ROOT.TH1F("redmes", "HT Event Selection", 60, 0, 3000)
redmes260 = ROOT.TH1F("redmes260", "HT Event Selection + PFJet260", 60, 0, 3000)
redmes200 = ROOT.TH1F("redmes200", "HT Event Selection + PFJet200",60, 0, 3000)
redmes200B = ROOT.TH1F("redmes200B", "HT Event Selection + PFJet200 + B",60, 0, 3000)
redmes140 = ROOT.TH1F("redmes140", "HT Event Selection + PFJet140",60, 0, 3000)
redmes140B = ROOT.TH1F("redmes140B", "HT Event Selection + PFJet140 + B",60, 0, 3000)
redmes260B = ROOT.TH1F("redmes260B", "HT Event Selection + PFJet260 + Boosted OR", 60, 0, 3000)
redmes260B1 = ROOT.TH1F("redmes260B1", "HT Event Selection + PFJet260 + Boosted OR", 60, 0, 3000)
redmes260B2 = ROOT.TH1F("redmes260B2", "HT Event Selection + PFJet260 + Boosted OR", 60, 0, 3000)
redmes260B3 = ROOT.TH1F("redmes260B3", "HT Event Selection + PFJet260 + Boosted OR", 60, 0, 3000)
redmes260B4 = ROOT.TH1F("redmes260B4", "HT Event Selection + PFJet260 + Boosted OR", 60, 0, 3000)
redmes260B5 = ROOT.TH1F("redmes260B5", "HT Event Selection + PFJet260 + Boosted OR", 60, 0, 3000)
redmes260B6 = ROOT.TH1F("redmes260B6", "HT Event Selection + PFJet260 + Boosted OR", 60, 0, 3000)
redmes260B7 = ROOT.TH1F("redmes260B7", "HT Event Selection + PFJet260 + Boosted OR", 60, 0, 3000)
redmFull = ROOT.TH1F("redmFull", "Reduced Mass Full", 180, 400, 2200)

histo2D = ROOT.TH2F("histo2D", "HT vs Reduced Mass", 60, 0, 3000, 60, 0, 3000)

nevent = treeMine.GetEntries();
counter = 0
for i in range(0, nevent) :
    counter = counter + 1
    treeMine.GetEntry(i)

    bjet1 = TLorentzVector()
    bjet2 = TLorentzVector()
    nAK4AK1 = TLorentzVector()
    nAK4AK2 = TLorentzVector()
    fatjet = TLorentzVector()
    bjet1.SetPtEtaPhiM(treeMine.bjet1PT, treeMine.bjet1ETA, treeMine.bjet1PHI, treeMine.bjet1M)
    bjet2.SetPtEtaPhiM(treeMine.bjet2PT, treeMine.bjet2ETA, treeMine.bjet2PHI, treeMine.bjet2M)
    nAK4AK1.SetPtEtaPhiM(treeMine.ak4nbjet1PT, treeMine.ak4nbjet1ETA, treeMine.ak4nbjet1PHI, treeMine.ak4nbjet1M)
    nAK4AK2.SetPtEtaPhiM(treeMine.ak4nbjet2PT, treeMine.ak4nbjet2ETA, treeMine.ak4nbjet2PHI, treeMine.ak4nbjet2M)
    fatjet.SetPtEtaPhiM(treeMine.fatjetPT, treeMine.fatjetETA, treeMine.fatjetPHI, treeMine.fatjetM)
    deltaEta = abs(fatjet.Eta() - (bjet1 + bjet2).Eta())
    reducedMass = treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.)
    #pass preselection
    if 105 < treeMine.fatjet_mass < 135 and 90 < treeMine.dijet_mass < 140 and treeMine.fatjetPT > 300 and treeMine.bjet1PT > 30 and treeMine.bjet2PT > 30 and reducedMass > 750 and 1.0 <= deltaEta < 2.0 and treeMine.ak4btag1 > 0.6324 and treeMine.ak4btag2 > 0.6324:
#    if 105 < treeMine.fatjet_mass < 135 and 90 < treeMine.dijet_mass < 140 and treeMine.fatjetPT > 300 and treeMine.bjet1PT > 30 and treeMine.bjet2PT > 30 and reducedMass > 750 and deltaEta < 1.0 and treeMine.ak4btag1 > 0.6324 and treeMine.ak4btag2 > 0.6324:
        htes.Fill(treeMine.HT)
        invmes.Fill(treeMine.Inv_mass)
        redmes.Fill(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.))
        #pass PFJet260
        if treeMine.HLT2_PFJet260 > 0:
            htes260.Fill(treeMine.HT)
            invmes260.Fill(treeMine.Inv_mass)
            redmes260.Fill(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.))
            #pass OR
            OR = treeMine.HLT2_HT800 + treeMine.HLT2_DiPFJet280 + treeMine.HLT2_AK8PFHT650 + treeMine.HLT2_AK8PFJet360 + treeMine.HLT2_PFHT650 + treeMine.HLT2_PFHT900 + treeMine.HLT2_AK8PFHT700
            if OR > 0:
                htes260B.Fill(treeMine.HT)
                invmes260B.Fill(treeMine.Inv_mass)
                redmes260B.Fill(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.))
                histo2D.Fill(treeMine.HT,(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.)))
           # if treeMine.HLT2_HT800 > 0:
           #     redmes260B1.Fill(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.))
           # if treeMine.HLT2_DiPFJet280 > 0:
           #     redmes260B2.Fill(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.))
            if treeMine.HLT2_AK8PFHT650 > 0:
                redmes260B3.Fill(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.))
            if treeMine.HLT2_AK8PFJet360 > 0:
                redmes260B4.Fill(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.))
            if treeMine.HLT2_PFHT650 > 0:
                redmes260B5.Fill(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.))
            if treeMine.HLT2_PFHT900 > 0:
                redmes260B6.Fill(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.))
            if treeMine.HLT2_AK8PFHT700 > 0:
                redmes260B7.Fill(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.))
            if treeMine.ak4btag1 > 0.6324 and treeMine.ak4btag2 > 0.6324 and treeMine.fatjet_hbb > 0.8 and treeMine.fatjetptau21 < 0.55 and OR > 0:
                    if bjet1.DeltaR(nAK4AK1) < bjet2.DeltaR(nAK4AK2):
                        invmAK4 = (bjet1 + bjet2 + nAK4AK1).M()
                    else:
                        invmAK4 = (bjet1 + bjet2 + nAK4AK2).M()
                    if invmAK4 > 200:
                        invmFull.Fill(treeMine.Inv_mass)
                        redmFull.Fill(treeMine.Inv_mass - (treeMine.fatjet_mass - 125.) - (treeMine.dijet_mass - 125.))
    myTree.Fill()

f2.cd()
f2.Write()
f2.Close()

f.Close()


