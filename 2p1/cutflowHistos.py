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


#cutflow histos
tpo1 = ROOT.TH1F("tpo1", "Reduced Mass (GeV)", 50, 0, 3000)
tpo2 = ROOT.TH1F("tpo2", "Reduced Mass (GeV)", 50, 0, 3000)
tpo3 = ROOT.TH1F("tpo3", "Reduced Mass (GeV)", 50, 0, 3000)
tpo4 = ROOT.TH1F("tpo4", "Reduced Mass (GeV)", 50, 0, 3000)
tpo5 = ROOT.TH1F("tpo5", "Reduced Mass (GeV)", 50, 0, 3000)
tpo6 = ROOT.TH1F("tpo6", "Reduced Mass (GeV)", 50, 0, 3000)
tpo7 = ROOT.TH1F("tpo7", "Reduced Mass (GeV)", 50, 0, 3000)
tpo8 = ROOT.TH1F("tpo8", "Reduced Mass (GeV)", 50, 0, 3000)
tpo9 = ROOT.TH1F("tpo9", "Reduced Mass (GeV)", 50, 0, 3000)
tpo10 = ROOT.TH1F("tpo10", "Reduced Mass (GeV)", 50, 0, 3000)
tpo11 = ROOT.TH1F("tpo11", "Reduced Mass (GeV)", 50, 0, 3000)
tpo12 = ROOT.TH1F("tpo12", "Reduced Mass (GeV)", 50, 0, 3000)

nevent = treeMine.GetEntries();
counter = 0
#run over events
for i in range(0, nevent) :
    counter = counter + 1
    treeMine.GetEntry(i)
    #passing preselection
    if treeMine.fatjetPT > 300 and treeMine.bjet1PT > 30 and treeMine.bjet2PT > 30:
        tpo1.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
        OR = treeMine.HLT2_HT800 + treeMine.HLT2_DiPFJet280 + treeMine.HLT2_AK8PFHT650 + treeMine.HLT2_AK8PFJet360 + treeMine.HLT2_PFHT650 + treeMine.HLT2_PFHT900 + treeMine.HLT2_AK8PFHT700
        #passing trigger
        if OR > 0:
            tpo2.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
            #passing AK4 btag
            if treeMine.ak4btag1 > 0.6324 and treeMine.ak4btag2 > 0.6324:
                tpo3.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
                #passing AK4 dijet mass window
                if 90 < treeMine.dijet_mass < 140:
                    tpo4.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
                    #passing tau21
                    if treeMine.fatjetptau21 < 0.55:
                        tpo5.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
                        #passing triAK4jet mass
                        if treeMine.invmAK4 > 200:
                            tpo6.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
                            #passing AK8 softdrop mass window
                            if 105 < treeMine.fatjet_mass < 135:
                                tpo7.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
                                #passing AK8 double btag
                                if treeMine.fatjet_hbb > 0.8:
                                    tpo8.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
                                    #passing reduced mass
                                    if treeMine.Red_mass > 750:
                                        tpo9.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
                                        #passing deltaEta
                                        if treeMine.deltaEta < 2.0:
                                            tpo10.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
                                            #passing full selection + no boosted 
                                            if not (treeMine.boosted > 0 and treeMine.b2 > 0.3)
                                                tpo11.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
                                            #passing full selection + no resolved
                                            if treeMine.resolved < 1:
                                                tpo12.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
    myTree.Fill()



f2.cd()
f2.Write()
f2.Close()

 
f.Close()


