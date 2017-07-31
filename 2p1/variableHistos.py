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


#defining variable histograms

#bjetpt1 = ROOT.TH1F("bjetpt1", "AK4 Jet 1 p_{T}", 100, 0, 1000)
#bjetpt2 = ROOT.TH1F("bjetpt2", "AK4 Jet 2 p_{T}", 100, 0, 500) 

#totalpre = ROOT.TH1F("totalpre", "Invariant Mass Total Preselection", 40, 0, 2000)
#totalpost = ROOT.TH1F("totalpost", "Invariant Mass Total Postselection", 40, 0, 2000)

#trigbtagpre = ROOT.TH1F("trigbtagpre", "Events Passing BTag Trigs Preselection", 40, 0, 2000)
#trightandpost = ROOT.TH1F("trightandpost", "Events Passing HT Trigs Postselection", 3000, 0, 3000) 
#trigbtagandpost = ROOT.TH1F("trigbtagandpost", "Events Passing BTag Trigs Postselection", 3000, 0, 3000) 

#trightpre = ROOT.TH1F("trightpre", "Events Passing HT Trigs Preselection", 40, 0, 2000)
#trightonlypost = ROOT.TH1F("trightonlypost", "Events Passing HT Trigs Only Postselection",3000, 0, 3000) 
#trigbtagonlypost = ROOT.TH1F("trigbtagonlypost", "Events Passing BTag Trigs Only Postselection", 3000, 0, 3000) 

#trigbothpre = ROOT.TH1F("trigbothpre", "Events Passing Both Trigs Preselection", 40, 0, 2000)
#trigbothpost = ROOT.TH1F("trigbothpost", "Events Passing Any Trigs Postselection", 3000, 0, 3000)

#numberORpre = ROOT.TH1F("numberORpre", "Events passing HT Trigs and BTag Trigs Preselection", 2, -0.5, 1.5)
#numberORpost = ROOT.TH1F("numberORpost", "Events passing HT Trigs and BTag Trigs Postselection", 2, -0.5, 1.5)

#trigeffbtagpre = ROOT.TH1F("trigeffbtagpre", "Efficiency BTag Trigs Preselection", 40, 0, 2000)
#trigeffbtagpost = ROOT.TH1F("trigeffbtagpost", "Efficiency BTag Trigs Postselection", 40, 0, 2000) 

#trigeffhtpre = ROOT.TH1F("trigeffhtpre", "Efficiency HT Trigs Preselection", 40, 0, 2000)
#trigeffhtpost = ROOT.TH1F("trigeffhtpost", "Efficiency HT Trigs Postselection", 40, 0, 2000) 

#trigeffbothpre = ROOT.TH1F("trigeffbothpre", "Efficiency Both Trigs Preselection", 40, 0, 2000)
#trigeffbothpost = ROOT.TH1F("trigeffbothpost", "Efficiency Both Trigs Postselection", 40, 0, 2000)
 
#nocut = ROOT.TH1F("nocut", "No ttbar cut", 3000, 0, 3000)
#tau32 = ROOT.TH1F("tau32", "Events passing CHS tau32 > 0.50 cut", 3000, 0, 3000)
#tau21 = ROOT.TH1F("tau21", "Events passing CHS tau21 < 0.55 cut", 3000, 0, 3000)
#akca0p8 = ROOT.TH1F("akca0p8", "Events passing AK8pT/CA15pT > 0.8", 3000, 0, 3000) 
#akca0p85 = ROOT.TH1F("akca0p85", "Events passing AK8pT/CA15pT > 0.85", 3000, 0, 3000)
#akca0p9 = ROOT.TH1F("akca0p9", "Events passing AK8pT/CA15pT > 0.9", 3000, 0, 3000)
 
jetmass = ROOT.TH1F("jetmass", "Softdrop Corrected Jet Mass (GeV)", 50, 5, 505)
#tau32 = ROOT.TH1F("tau32", "Tau3/Tau2", 50, 0, 1)
#tau21 = ROOT.TH1F("tau21", "Tau2/Tau1",50, 0, 1)
#akca = ROOT.TH1F("akca", "AK8 Jet pT/CA15 Jet pT", 50, 0, 2)
#akcac = ROOT.TH1F("akcac", "AK8 Jet pT/CA15 Jet pT With Cuts", 50, 0, 2)
doubleb = ROOT.TH1F("doubleb", "Double B Tagger", 50, -1, 1)
redmass = ROOT.TH1F("redmass", "Reduced Mass (GeV)", 50, 0, 3000)
ptFJ = ROOT.TH1F("ptFJ", "p_{T} AK8 Jet (GeV)", 50, 0, 1500)
etaFJ = ROOT.TH1F("etaFJ", "#eta AK8 Jet (GeV)", 50, -2.5, 2.5)
ptJ1 = ROOT.TH1F("ptJ1", "p_{T} AK4 Jet 1 (GeV)", 50, 0, 1000)
etaJ1 = ROOT.TH1F("etaJ1", "#eta AK4 Jet 1 (GeV)",50, -2.5, 2.5)
ptJ2 = ROOT.TH1F("ptJ2", "p_{T} AK4 Jet 2 (GeV)", 50, 0, 500)
etaJ2 = ROOT.TH1F("etaJ2", "#eta AK4 Jet 2 (GeV)",50, -2.5, 2.5)
dijetmass = ROOT.TH1F("dijetmass", "Dijet Mass AK4 Jets (GeV)", 50, 5, 505)
btag1 = ROOT.TH1F("btag1", "Deep CSV AK4 Jet 1",50, 0, 1)
btag2 = ROOT.TH1F("btag2", "Deep CSV AK4 Jet 2",50, 0, 1)
ptau21 = ROOT.TH1F("ptau21", "Puppi Tau2/Tau1",50, 0, 1)
deta = ROOT.TH1F("deta", "|#Delta#eta (fatjet, AK4 jets)|", 40, 0, 4)
#dRfjAK1 = ROOT.TH1F("dRfjAK1", "#Delta R Fatjet and AK4 Jet1", 50, 0, 5)
#dRfjAK2 = ROOT.TH1F("dRfjAK2", "#Delta R Fatjet and AK4 Jet2", 50, 0, 5)
#dRfjnAK = ROOT.TH1F("dRfjnAK", "#Delta R Fatjet and Nearest AK4 Jet", 50, 0, 5)
#pTnAKfj = ROOT.TH1F("pTnAKfj", "p_{T} AK4 Jet Nearest to Fatjet (GeV)", 50, 0, 1000)
#dRAK1nAK = ROOT.TH1F("dRAK1nAK", "#Delta R AK Jet1 and Nearest Rejected AK4 Jet", 50, 0, 5)
#dRAK2nAK = ROOT.TH1F("dRAK2nAK", "#Delta R AK Jet2 and Nearest Rejected AK4 Jet", 50, 0, 5)
#pTnAKAK1 = ROOT.TH1F("pTnAKAK1", "p_{T} AK4 Jet Nearest to AK4 Jet1 (GeV)", 50, 0, 1000)
#pTnAKAK2 = ROOT.TH1F("pTnAKAK2", "p_{T} AK4 Jet Nearest to AK4 Jet2 (GeV)", 50, 0, 1000)
#numnAKAK1 = ROOT.TH1F("numnAKAK1", "Number of AK4 jets within #DeltaR 1.5 of AK4 Jet1", 11, -0.5, 10.5)
#numnAKAK2 = ROOT.TH1F("numnAKAK2", "Number of AK4 jets within #DeltaR 1.5 of AK4 Jet2", 11, -0.5, 10.5)
#dRAK1AK2 = ROOT.TH1F("dRAK1AK2", "#Delta R AK Jet1 and AK4 Jet2", 50, 0, 5)
#numAK4 = ROOT.TH1F("numAK4", "Number of AK4 jets", 13, -0.5, 12.5) 
#pTAK2AK1 = ROOT.TH1F("pTAK2AK1", "p_{T} AK Jet1/ p_{T} AK Jet2", 50, 0, 2)
#mAK1 = ROOT.TH1F("mAK1", "Mass AK Jet1 (GeV)", 50, 0, 300)
#mAK2 = ROOT.TH1F("mAK2", "Mass AK Jet2 (GeV)", 50, 0, 300) 
#flavAK1 = ROOT.TH1F("flavAK1", "Flavor AK Jet1 (GeV)", 50, 0, 300)
#flavAK2 = ROOT.TH1F("flavAK2", "Flavor AK Jet2 (GeV)", 50, 0, 300)
#dRfjCA = ROOT.TH1F("dRfjCA", "#Delta R AK8 and CA15", 50, 0, 5)
#pTnAK4AK1 = ROOT.TH1F("pTAK4AK1", "p_{T} nearest AK4 Jet to AK4Jet_1/ p_{T} AK4Jet_1", 50, 0, 2)
#pTnAK4AK2 = ROOT.TH1F("pTAK4AK2", "p_{T} nearest AK4 Jet to AK4Jet_2/ p_{T} AK4Jet_2", 50, 0, 2)
#pTnAK4AKs = ROOT.TH1F("pTAK4AKs", "p_{T} nearest AK4 Jet to AK4Jet_2/ p_{T} AK4Jet_1+2", 50, 0, 1000)
#dRsnAK4fj = ROOT.TH1F("dRsnAK4fj", "#DeltaR Fatjet and Nearest Unselected AK4 Jet", 50, 0, 5)
#invmsnAK4fj = ROOT.TH1F("invmsnAK4fj", "Invariant Mass Fatjet and Nearest Unselected AK4 Jet (GeV)", 50, 0, 1000)
#bsnAK4fj = ROOT.TH1F("bsnAK4fj", "Presence of Unselected AK4 Jet Near Fatjet", 2, -0.5, 1.5)
#dRsnAK4cl = ROOT.TH1F("dRsnAK4cl", "#Delta R AK4 Selected and Nearest AK4 Unselected Jet", 50, 0, 5)
invmsnAK4cl = ROOT.TH1F("invmsnAK4cl", "Invariant Mass AK4 Selected and Nearest AK4 Unselected Jet (GeV)", 50, 0, 1000)
#h2dcl = ROOT.TH2F("h2dcl", "#DeltaR vs Invariant Mass", 50, 0, 5, 50, 0, 1000)

#doubleb1 = ROOT.TH1F("doubleb1", "Double B Tagger", 50, -1, 1)
#doubleb2 = ROOT.TH1F("doubleb2", "Double B Tagger", 50, -1, 1)
#doubleb3 = ROOT.TH1F("doubleb3", "Double B Tagger", 50, -1, 1)
#jetmass1 = ROOT.TH1F("jetmass1", "Softdrop Corrected Jet Mass (GeV)", 50, 5, 505)
#invmass1 = ROOT.TH1F("invmass1", "Invariant Mass (GeV)", 50, 0, 3000)
#dijetmass1 = ROOT.TH1F("dijetmass1", "Dijet Mass AK4 Jets (GeV)", 50, 5, 505)

#doubleb0p6 = ROOT.TH1F("doubleb0p6", "Invariant Mass (GeV)", 50, 0, 3000)
#doubleb0p6tau = ROOT.TH1F("doubleb0p6tau", "Invariant Mass (GeV)", 50, 0, 3000)
#doubleb0p6taudR = ROOT.TH1F("doubleb0p6taudR", "Invariant Mass (GeV)", 50, 0, 3000)
#doubleb0p6dR = ROOT.TH1F("doubleb0p6dR", "Invariant Mass (GeV)", 50, 0, 3000)
#doubleb0p8 = ROOT.TH1F("doubleb0p8", "Invariant Mass (GeV)", 50, 0, 3000)
#doubleb0p8tau = ROOT.TH1F("doubleb0p8tau", "Invariant Mass (GeV)", 50, 0, 3000)
#doubleb0p8taudR = ROOT.TH1F("doubleb0p8taudR", "Invariant Mass (GeV)", 50, 0, 3000)
#doubleb0p8dR = ROOT.TH1F("doubleb0p8dR", "Invariant Mass (GeV)", 50, 0, 3000)

#hhsm = ROOT.TH1F("hhsm", "Events passing HH SM Analysis", 2, -0.5, 1.5)
#hhsmt = ROOT.TH1F("hhsmt", "Events passing HH SM Analysis One Trigger", 2, -0.5, 1.5) 
#hhsmb = ROOT.TH1F("hhsmb", "Events passing HH SM Analysis BTag Triggers", 2, -0.5, 1.5)

nevent = treeMine.GetEntries();
counter = 0
#running through events
for i in range(0, nevent) :
    counter = counter + 1
    treeMine.GetEntry(i)
    
    #cuts placed on events

#    if 105 < treeMine.fatjet_mass < 135 and 105 < treeMine.dijet_mass < 135 and treeMine.ak4btag1 > 0.6324 and treeMine.ak4btag2 > 0.6324 and treeMine.fatjet_hbb > 0.8 and treeMine.fatjetptau21 < 0.55:
#    if 105 < treeMine.fatjet_mass < 135 and treeMine.dijet_mass < 70 and treeMine.ak4btag1 > 0.6324 and treeMine.ak4btag2 > 0.6324 and treeMine.fatjet_hbb > 0.8 and treeMine.LL < 1 and treeMine.LT < 1 and treeMine.TT < 1 and treeMine.resolved < 1:

#    if 105 < treeMine.dijet_mass < 135 and treeMine.ak4btag1 > 0.6324 and treeMine.ak4btag2 > 0.6324 and treeMine.LL < 1 and treeMine.LT < 1 and treeMine.TT < 1 and treeMine.resolved < 1:# and (treeMine.fatjet_mass < 105 or treeMine.fatjet_mass > 135):
    if treeMine.fatjetPT > 300 and treeMine.bjet1PT > 30 and treeMine.bjet2PT > 30 and treeMine.LL < 1 and treeMine.LT < 1 and treeMine.TT < 1 and treeMine.resolved < 1 and 105 < treeMine.fatjet_mass < 135 and 90 < treeMine.dijet_mass < 140:
#    if 105 < treeMine.fatjet_mass < 135 and 105 < treeMine.dijet_mass < 135 and treeMine.ak4btag1 > 0.6324 and treeMine.ak4btag2 > 0.6324 and treeMine.LL < 1 and treeMine.LT < 1 and treeMine.TT < 1 and treeMine.resolved < 1:
        OR = treeMine.HLT2_HT800 + treeMine.HLT2_DiPFJet280 + treeMine.HLT2_AK8PFHT650 + treeMine.HLT2_AK8PFJet360 + treeMine.HLT2_PFHT650 + treeMine.HLT2_AK8PFJet360 + treeMine.HLT2_PFHT650 + treeMine.HLT2_PFHT900 + treeMine.HLT2_AK8PFHT700
        if OR > 0:
            #filling histograms
            
#            if treeMine.hhsm > 0:
#                hhsm.Fill(1)
#                if (treeMine.HLT2_Quad_Triple + treeMine.HLT2_Double_Triple) > 0:
#                    hhsmb.Fill(1)
#                else:
#                    hhsmb.Fill(0)
#                if treeMine.HLT2_Quad_Triple > 0:
#                    hhsmt.Fill(1)
#                else:
#                    hhsmt.Fill(0)
#            else:
#                hhsm.Fill(0)
#            if 105 < treeMine.dijet_mass < 135:
#                doubleb1.Fill(treeMine.fatjet_hbb)
#                if treeMine.ak4btag1 > 0.6324 and treeMine.ak4btag2 > 0.6324:
#                    doubleb2.Fill(treeMine.fatjet_hbb)
#                    if 105 < treeMine.fatjet_mass < 
#                        doubleb3.Fill(treeMine.fatjet_hbb)
            jetmass.Fill(treeMine.fatjet_mass)
#            tau32.Fill(treeMine.fatjettau32)
#            tau21.Fill(treeMine.fatjettau21)
#            akca.Fill(treeMine.fatjetAKCAratio)
            doubleb.Fill(treeMine.fatjet_hbb)
            redmass.Fill(treeMine.Inv_mass + 250 - treeMine.fatjet_mass - treeMine.dijet_mass)
            ptFJ.Fill(treeMine.fatjetPT)
            etaFJ.Fill(treeMine.fatjetETA)
            ptJ1.Fill(treeMine.bjet1PT)
            etaJ1.Fill(treeMine.bjet1ETA)
            ptJ2.Fill(treeMine.bjet2PT)
            etaJ2.Fill(treeMine.bjet2ETA)
            dijetmass.Fill(treeMine.dijet_mass)
            btag1.Fill(treeMine.ak4btag1)
            btag2.Fill(treeMine.ak4btag2)
            ptau21.Fill(treeMine.fatjetptau21)
            
            fatjet = TLorentzVector()
            bjet1 = TLorentzVector()
            bjet2 = TLorentzVector()
#            nAK4FJ = TLorentzVector()
            nAK4AK1 = TLorentzVector()
            nAK4AK2 = TLorentzVector()
#            CA = TLorentzVector()
#            if treeMine.sak4nfatjetPT > 30:
#                snAK4FJ = TLorentzVector()
            
            fatjet.SetPtEtaPhiM(treeMine.fatjetPT, treeMine.fatjetETA, treeMine.fatjetPHI, treeMine.fatjetM)
            bjet1.SetPtEtaPhiM(treeMine.bjet1PT, treeMine.bjet1ETA, treeMine.bjet1PHI, treeMine.bjet1M)
            bjet2.SetPtEtaPhiM(treeMine.bjet2PT, treeMine.bjet2ETA, treeMine.bjet2PHI, treeMine.bjet2M)
#            nAK4FJ.SetPtEtaPhiM(treeMine.ak4nfatjetPT, treeMine.ak4nfatjetETA, treeMine.ak4nfatjetPHI, treeMine.ak4nfatjetM)
#            if treeMine.sak4nfatjetPT > 30:
#                snAK4FJ.SetPtEtaPhiM(treeMine.sak4nfatjetPT, treeMine.sak4nfatjetETA, treeMine.sak4nfatjetPHI, treeMine.sak4nfatjetM)
            nAK4AK1.SetPtEtaPhiM(treeMine.ak4nbjet1PT, treeMine.ak4nbjet1ETA, treeMine.ak4nbjet1PHI, treeMine.ak4nbjet1M)
            nAK4AK2.SetPtEtaPhiM(treeMine.ak4nbjet2PT, treeMine.ak4nbjet2ETA, treeMine.ak4nbjet2PHI, treeMine.ak4nbjet2M)
            deta.Fill(abs(fatjet.Eta() - (bjet1 + bjet2).Eta()))
#            CA.SetPtEtaPhiM(treeMine.fatjetCAPT, treeMine.fatjetCAETA, treeMine.fatjetCAPHI, treeMine.fatjetCAM)

#            if (CA.Pt() > 250) and (CA.DeltaR(bjet1) > 0.8) and (CA.DeltaR(bjet2) > 0.8):
#                akcac.Fill(treeMine.fatjetAKCAratio)
#            dRfjAK1.Fill(fatjet.DeltaR(bjet1))
#            dRfjAK2.Fill(fatjet.DeltaR(bjet2))
#            dRfjnAK.Fill(fatjet.DeltaR(nAK4FJ))
#            pTnAKfj.Fill(nAK4FJ.Pt())
#            dRAK1nAK.Fill(bjet1.DeltaR(nAK4AK1))
#            dRAK2nAK.Fill(bjet2.DeltaR(nAK4AK2))
#            pTnAKAK1.Fill(nAK4AK1.Pt())
#            pTnAKAK2.Fill(nAK4AK2.Pt())
#            numnAKAK1.Fill(treeMine.nAK4near1)
#            numnAKAK2.Fill(treeMine.nAK4near2)
#            dRAK1AK2.Fill(bjet1.DeltaR(bjet2))
#            numAK4.Fill(treeMine.nAK4)
#            pTAK2AK1.Fill(treeMine.bjet2PT/treeMine.bjet1PT)
#            mAK1.Fill(treeMine.bjet1M)
#            mAK2.Fill(treeMine.bjet2M)
#            flavAK1.Fill(treeMine.ak4jetflav1)
#            flavAK2.Fill(treeMine.ak4jetflav2)
#            dRfjCA.Fill(fatjet.DeltaR(CA))
#            pTnAK4AK1.Fill(nAK4AK1.Pt()/bjet1.Pt())
#            pTnAK4AK2.Fill(nAK4AK1.Pt()/bjet2.Pt())
#            pTnAK4AKs.Fill(nAK4AK1.Pt()/(bjet1+bjet2).Pt())
            if bjet1.DeltaR(nAK4AK1) < bjet2.DeltaR(nAK4AK2):
#                dRsnAK4cl.Fill(bjet1.DeltaR(nAK4AK1))
                invmsnAK4cl.Fill((bjet1 + bjet2 + nAK4AK1).M())
#                pTnAK4AKs.Fill(nAK4AK1.Pt())
#                if (bjet1 + bjet2 + nAK4AK1).M() > 200:
#                    invmass1.Fill(treeMine.Inv_mass) 
            else:
#                dRsnAK4cl.Fill(bjet2.DeltaR(nAK4AK2))
                invmsnAK4cl.Fill((bjet1 + bjet2 + nAK4AK2).M())
#                pTnAK4AKs.Fill(nAK4AK2.Pt())
#                h2dcl.Fill(bjet2.DeltaR(nAK4AK2), (bjet1 + bjet2 + nAK4AK2).M())
#                if (bjet1 + bjet2 + nAK4AK2).M() > 200:
#                    invmass1.Fill(treeMine.Inv_mass)
#            if treeMine.sak4nfatjetPT > 30:# and (bjet1 + bjet2 + nAK4AK2).M() > 200:
#                h2dcl.Fill(snAK4FJ.DeltaR(fatjet), (bjet1 + bjet2 + nAK4AK2).M())
#                dRsnAK4fj.Fill(snAK4FJ.DeltaR(fatjet)) 
#                invmsnAK4fj.Fill((snAK4FJ+fatjet).M())
#                bsnAK4fj.Fill(1)
#            else:
#                bsnAK4fj.Fill(0)
#            if (bjet1.DeltaR(nAK4AK1)) > 1.0:
#                jetmass1.Fill(treeMine.fatjet_mass)
##                invmass1.Fill(treeMine.Inv_mass)
#                dijetmass1.Fill(treeMine.dijet_mass)

#            if treeMine.fatjet_hbb > 0.6:
#                doubleb0p6.Fill(treeMine.Inv_mass)
#                if treeMine.fatjetptau21 < 0.55:
#                    doubleb0p6tau.Fill(treeMine.Inv_mass)
#                if (bjet1.DeltaR(nAK4AK1)) > 1.0:
#                    doubleb0p6dR.Fill(treeMine.Inv_mass)
#                    if treeMine.fatjetptau21 < 0.55:
#                        doubleb0p6taudR.Fill(treeMine.Inv_mass)
#
#            if treeMine.fatjet_hbb > 0.8:
#                doubleb0p8.Fill(treeMine.Inv_mass)
#                if treeMine.fatjetptau21 < 0.55:
#                    doubleb0p8tau.Fill(treeMine.Inv_mass)
#                if (bjet1.DeltaR(nAK4AK1)) > 1.0:
#                    doubleb0p8dR.Fill(treeMine.Inv_mass)
#                    if treeMine.fatjetptau21 < 0.55:
#                        doubleb0p8taudR.Fill(treeMine.Inv_mass)

    myTree.Fill()

f2.cd()
f2.Write()
f2.Close()

f.Close()


