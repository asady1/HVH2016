import os
import glob
import math    

import ROOT 
#ROOT.gROOT.Macro("rootlogon.C")

import FWCore.ParameterSet.Config as cms

import sys
from DataFormats.FWLite import Events, Handle

from array import array

from optparse import OptionParser
parser = OptionParser()
#output file name
parser.add_option("-o", "--outName", dest="outName",
                  help="output file name")
(options, args) = parser.parse_args()
outputfilename = options.outName

#numberLimit = float(sys.argv[1])
#getting input file
f = ROOT.TFile.Open(sys.argv[1],"READ")
#making output file
f1 =  ROOT.TFile(outputfilename, 'recreate')
#print outputfilename
f1.cd()
#getting old tree
treeMine  = f.Get('mynewTree')
#making new tree
mynewTree = ROOT.TTree('mynewTree', 'mynewTree')

#getting old branches from old tree
#creating the tree objects we need
jet1pt = array('f', [-100.0])
jet2pt = array('f', [-100.0])
jet1ID = array('f', [-100.0])
jet2ID = array('f', [-100.0])
jet1eta = array('f', [-100.0])
jet2eta = array('f', [-100.0])
etadiff = array('f', [-100.0])
dijetmass = array('f', [-100.0])
dijetmass_corr = array('f', [-100.0])
dijetmass_corr_punc = array('f', [-100.0])
jet1tau21 = array('f', [-100.0])
jet2tau21 = array('f', [-100.0])
jet1pmass = array('f', [-100.0])
jet2pmass = array('f', [-100.0])
jet1pmassunc = array('f', [-100.0])
jet2pmassunc = array('f', [-100.0])
jet1bbtag = array('f', [-100.0])
jet2bbtag = array('f', [-100.0])
jet1s1csv = array('f', [-100.0])
jet2s1csv = array('f', [-100.0])
jet1s2csv = array('f', [-100.0])
jet2s2csv = array('f', [-100.0])
jetSJfla = array('f', [-100.0]*4)
jetSJpt =  array('f', [-100.0]*4)
jetSJcsv = array('f', [-100.0]*4)
jetSJeta = array('f', [-100.0]*4)
triggerpassbb = array('f', [-100.0])
triggerpasssj = array('f', [-100.0])
nHiggsTags = array('f', [-100.0])
nTrueInt = array('f', [-100])
vtype = array('f', [-100.0])
isData = array('f', [100.0])
jet1nbHadron = array('f', [-100.0])
jet2nbHadron = array('f', [-100.0])
jet1flavor = array('f', [-100.0])
jet2flavor = array('f', [-100.0])
jet1ncHadron = array('f', [-100.0])
jet2ncHadron = array('f', [-100.0])
gen1Pt = array('f', [-100.0])
ht = array('f', [-100.0])
htJet30 = array('f', [-100.0])
xsec = array('f', [-100.0])
HLT_PFHT800_v = array('f', [-100.0])
HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v = array('f', [-100.0])
HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v = array('f', [-100.0])
HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v = array('f', [-100.0])
HLT_PFJet260_v = array('f', [-100.0])
HLT_PFJet200_v = array('f', [-100.0])
HLT_PFJet140_v = array('f', [-100.0])
HLT_PFJet80_v = array('f', [-100.0])
dijetmass_puppi = array('f', [-100.0])
HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v = array('f', [-100.0])
HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v = array('f', [-100.0])
HLT_PFJet450_v = array('f', [-100.0])
HLT_AK8PFJet360_V = array('f', [-100.0])
HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
 
#creating the tree branches we need
mynewTree.Branch('jet1pt', jet1pt, 'jet1pt/F')

nevent = treeMine.GetEntries();

print outputfilename

h0 = ROOT.TH1F("h0", "HLT PFJet260", 3000, 0, 3000.)
h0_a = ROOT.TH1F("h0_a", "HLT PFJet200", 300, 0, 3000.)
h0_b = ROOT.TH1F("h0_b", "HLT PFJet140", 300, 0, 3000.)
h0_c = ROOT.TH1F("h0_c", "HLT PFJet80", 300, 0, 3000.)

h1 = ROOT.TH1F("h1", "HLT PFHT800 and HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v", 300, 0, 3000)
h2 = ROOT.TH1F("h2", "HLT PFHT800 and HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v", 300, 0, 3000)
h3 = ROOT.TH1F("h3", "HLT PFHT800 and HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v", 300, 0, 3000)
h4 = ROOT.TH1F("h4", "HLT PFHT800 and HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v", 300, 0, 3000)
h5 = ROOT.TH1F("h5", "HLT PFHT800 and HLT_PFJet450_v", 300, 0, 3000)
h6 = ROOT.TH1F("h6", "HLT PFHT800 and HLT_AK8PFJet360_V", 300, 0, 3000)
h7 = ROOT.TH1F("h7", "HLT PFHT800 and HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v", 300, 0, 3000)
h8 = ROOT.TH1F("h8", "HLT PFHT800 and HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v", 300, 0, 3000)

h9 = ROOT.TH1F("h9", "HLT PFJet260 and (PFHT800 or Widejet900 or AK8PFJet360 or AK8PFHT650 or Dijet250)", 300, 0, 3000)
h10 = ROOT.TH1F("h10", "HLT PFJet260 and (PFHT800 or Widejet950 or AK8PFJet360 or AK8PFHT650 or Dijet250)", 300, 0, 3000)
h11 = ROOT.TH1F("h11", "HLT PFJet260 and (PFHT800 or Widejet900 or PFJet450 or AK8PFHT650 or Dijet250)", 300, 0, 3000)
h12 = ROOT.TH1F("h12", "HLT PFJet260 and (PFHT800 or Widejet950 or PFJet450 or AK8PFHT650 or Dijet250)", 300, 0, 3000)
h13 = ROOT.TH1F("h13", "HLT PFJet260 and (PFHT800 or Widejet900 or AK8PFJet360 or AK8PFHT700 or Dijet250)", 300, 0, 3000)
h14 = ROOT.TH1F("h14", "HLT PFJet260 and (PFHT800 or Widejet950 or AK8PFJet360 or AK8PFHT700 or Dijet250)", 300, 0, 3000)
h15 = ROOT.TH1F("h15", "HLT PFJet260 and (PFHT800 or Widejet900 or PFJet450 or AK8PFHT700 or Dijet250)", 300, 0, 3000)
h16 = ROOT.TH1F("h16", "HLT PFJet260 and (PFHT800 or Widejet950 or PFJet450 or AK8PFHT700 or Dijet250)", 300, 0, 3000)

h17 = ROOT.TH1F("h17", "HLT PFJet260 and (PFHT800 or Widejet900 or AK8PFJet360 or AK8PFHT650 or Dijet280)", 3000, 0, 3000)
h18 = ROOT.TH1F("h18", "HLT PFJet260 and (PFHT800 or Widejet950 or AK8PFJet360 or AK8PFHT650 or Dijet280)", 300, 0, 3000)
h19 = ROOT.TH1F("h19", "HLT PFJet260 and (PFHT800 or Widejet900 or PFJet450 or AK8PFHT650 or Dijet280)", 300, 0, 3000)
h20 = ROOT.TH1F("h20", "HLT PFJet260 and (PFHT800 or Widejet950 or PFJet450 or AK8PFHT650 or Dijet280)", 300, 0, 3000)
h21 = ROOT.TH1F("h21", "HLT PFJet260 and (PFHT800 or Widejet900 or AK8PFJet360 or AK8PFHT700 or Dijet280)", 300, 0, 3000)
h22 = ROOT.TH1F("h22", "HLT PFJet260 and (PFHT800 or Widejet950 or AK8PFJet360 or AK8PFHT700 or Dijet280)", 300, 0, 3000)
h23 = ROOT.TH1F("h23", "HLT PFJet260 and (PFHT800 or Widejet900 or PFJet450 or AK8PFHT700 or Dijet280)", 300, 0, 3000)
h24 = ROOT.TH1F("h24", "HLT PFJet260 and (PFHT800 or Widejet950 or PFJet450 or AK8PFHT700 or Dijet280)", 300, 0, 3000)

h25 = ROOT.TH1F("h25", "HT PFJet260 and PFHT800", 300, 0, 3000)
h25_a = ROOT.TH1F("h25_a", "HT PFJet260 and PFHT800", 300, 0, 3000)
h25_b = ROOT.TH1F("h25_b", "HT PFJet260 and PFHT800", 300, 0, 3000)
h25_c = ROOT.TH1F("h25_c", "HT PFJet260 and PFHT800", 300, 0, 3000)

h26 = ROOT.TH1F("h26", "HT PFHT800", 300, 0, 3000)

h27 = ROOT.TH1F("h27", "HT PFJet260 and (PFHT800 or Dijet250 or Widejet)", 300, 0, 3000)
h28 = ROOT.TH1F("h28", "HT PFJet260 and (PFHT800 or Dijet280 or Widejet)", 300, 0, 3000)


#Weight = 0.1

count = 0
print "Number of Events:", nevent

for i in range(0, nevent) :
    treeMine.GetEntry(i)
    count = count + 1
    if count % 100000 == 0 :
	print "processing events", count

    if treeMine.jet2pt == -100:
        continue



    ht[0] = treeMine.ht
    etadiff[0] = treeMine.etadiff
    HLT_PFHT800_v[0] = treeMine.HLT_PFHT800_v
    HLT_PFJet80_v[0] = treeMine.HLT_PFJet80_v
    HLT_PFJet140_v[0] = treeMine.HLT_PFJet140_v
    HLT_PFJet200_v[0] = treeMine.HLT_PFJet200_v
    HLT_PFJet260_v[0] = treeMine.HLT_PFJet260_v
#    HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0] = treeMine.HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v
    HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0] = treeMine.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v
    HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] = treeMine.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v
#    HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] = treeMine.HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v
#    HLT_PFJet450_v[0] = treeMine.HLT_PFJet450_v
    HLT_AK8PFJet360_V[0] = treeMine.HLT_AK8PFJet360_V
#    HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v
    HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v

    jet1_puppi_TL = ROOT.TLorentzVector()
    jet1_puppi_TL.SetPtEtaPhiM(treeMine.jet1_puppi_pt, treeMine.jet1_puppi_eta, treeMine.jet1_puppi_phi, treeMine.jet1_puppi_msoftdrop*treeMine.jet1_puppi_TheaCorr)

    jet2_puppi_TL = ROOT.TLorentzVector()
    jet2_puppi_TL.SetPtEtaPhiM(treeMine.jet2_puppi_pt, treeMine.jet2_puppi_eta, treeMine.jet2_puppi_phi, treeMine.jet2_puppi_msoftdrop*treeMine.jet2_puppi_TheaCorr)

    dijetmass_puppi[0] = (jet1_puppi_TL + jet2_puppi_TL).M()
    dijetmass_corr[0] = treeMine.dijetmass_corr


    if abs(treeMine.jet1eta) > 2.4:
	continue

    if abs(treeMine.jet2eta) > 2.4:
        continue


    if abs(treeMine.jet1eta-treeMine.jet2eta) > 1.3:
	continue

    if treeMine.jet1_puppi_msoftdrop*treeMine.jet1_puppi_TheaCorr < 50:
	continue

    if treeMine.jet2_puppi_msoftdrop*treeMine.jet2_puppi_TheaCorr < 50:
        continue

    if treeMine.jet1pt < 200:
	continue

    if treeMine.jet2pt < 200:
        continue


    if HLT_PFJet260_v[0] == 1:
	h0.Fill(dijetmass_corr[0])

    if HLT_PFJet200_v[0] == 1:
	h0_a.Fill(dijetmass_corr[0])

    if HLT_PFJet140_v[0] == 1:
	h0_b.Fill(dijetmass_corr[0])

    if HLT_PFJet80_v[0] == 1:
	h0_c.Fill(dijetmass_corr[0])


#    if HLT_PFHT800_v[0] == 1 and HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0] == 1:
#        h1.Fill(dijetmass_corr[0])

    if HLT_PFHT800_v[0] == 1 and HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0] == 1:
        h2.Fill(dijetmass_corr[0])
    
    if HLT_PFHT800_v[0] == 1 and HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] == 1:
        h3.Fill(dijetmass_corr[0])

#    if HLT_PFHT800_v[0] == 1 and HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] == 1:
#        h4.Fill(dijetmass_corr[0])

#    if HLT_PFHT800_v[0] == 1 and HLT_PFJet450_v[0] == 1:
#        h5.Fill(dijetmass_corr[0])

    if HLT_PFHT800_v[0] == 1 and HLT_AK8PFJet360_V[0] == 1:
        h6.Fill(dijetmass_corr[0])

#    if HLT_PFHT800_v[0] == 1 and HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] == 1:
#        h7.Fill(dijetmass_corr[0])

    if HLT_PFHT800_v[0] == 1 and HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] == 1:
        h8.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] or HLT_AK8PFJet360_V[0] or HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h9.Fill(dijetmass_corr[0])
    
#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] or HLT_AK8PFJet360_V[0] or HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h10.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] or HLT_PFJet450_v[0] or HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h11.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] or HLT_PFJet450_v[0] or HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h12.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] or HLT_AK8PFJet360_V[0] or HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h13.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] or HLT_AK8PFJet360_V[0] or HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h14.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] or HLT_PFJet450_v[0] or HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h15.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] or HLT_PFJet450_v[0] or HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h16.Fill(dijetmass_corr[0])

    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] or HLT_AK8PFJet360_V[0] or HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
        h17.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] or HLT_AK8PFJet360_V[0] or HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h18.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] or HLT_PFJet450_v[0] or HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h19.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] or HLT_PFJet450_v[0] or HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h20.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] or HLT_AK8PFJet360_V[0] or HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h21.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] or HLT_AK8PFJet360_V[0] or HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h22.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] or HLT_PFJet450_v[0] or HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h23.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] or HLT_PFJet450_v[0] or HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] or HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0]) and HLT_PFJet260_v[0] == 1:
#        h24.Fill(dijetmass_corr[0])


    if HLT_PFHT800_v[0] == 1 and HLT_PFJet260_v[0] == 1:
	h25.Fill(dijetmass_corr[0])

    if HLT_PFHT800_v[0] == 1 and HLT_PFJet200_v[0] == 1:
        h25_a.Fill(dijetmass_corr[0])

    if HLT_PFHT800_v[0] == 1 and HLT_PFJet140_v[0] == 1:
        h25_b.Fill(dijetmass_corr[0])

    if HLT_PFHT800_v[0] == 1 and HLT_PFJet80_v[0] == 1:
        h25_c.Fill(dijetmass_corr[0])


    if HLT_PFHT800_v[0] == 1:
	h26.Fill(dijetmass_corr[0])

#    if (HLT_PFHT800_v[0] == 1 or HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0] == 1 or HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] == 1) and HLT_PFJet260_v[0] == 1:
#        h27.Fill(dijetmass_corr[0])

    if (HLT_PFHT800_v[0] == 1 or HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0]==1 or HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] == 1) and HLT_PFJet260_v[0]==1:
        h28.Fill(dijetmass_corr[0])




print "done " + outputfilename

f1.cd()
f1.Write()
f1.Close()

f.Close()
