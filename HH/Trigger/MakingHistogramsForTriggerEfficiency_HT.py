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
f = ROOT.TFile(sys.argv[1])
#making output file
f1 =  ROOT.TFile(outputfilename, 'recreate')
#print outputfilename
f1.cd()
#getting old tree
treeMine  = f.Get('myTree')
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
gen1Phi = array('f', [-100.0])
gen1Eta = array('f', [-100.0])
gen1Mass = array('f', [-100.0])
gen1ID = array('f', [-100.0])
gen2Pt = array('f', [-100.0])
gen2Phi = array('f', [-100.0])
gen2Eta = array('f', [-100.0])
gen2Mass = array('f', [-100.0])
gen2ID = array('f', [-100.0])
jet1l1l2l3 = array('f', [-100.0])
jet1l2l3 = array('f', [-100.0])
jet2l1l2l3 = array('f', [-100.0])
jet2l2l3 = array('f', [-100.0])
jet1JER = array('f', [-100.0])
jet2JER = array('f', [-100.0])
puWeights = array('f', [-100.0])
puWeightsUp = array('f', [-100.0])
puWeightsDown = array('f', [-100.0])
json = array('f', [-100.0])
SF = array('f', [-100.0])
SFup = array('f', [-100.0])
SFdown = array('f', [-100.0])
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
norm = array('f', [-100.0])
evt = array('f', [-100.0])
ht = array('f', [-100.0])
htJet30 = array('f', [-100.0])
xsec = array('f', [-100.0])
sjSF = array('f', [-100.0])
sjSFup = array('f', [-100.0])
sjSFdown = array('f', [-100.0])
MET = array('f', [-100.0])
nAK08Jets = array('f', [-100.0])
nAK04Jets = array('f', [-100.0])
DeltaPhi1 = array('f', [-100.0])
DeltaPhi2 = array('f', [-100.0])
DeltaPhi3 = array('f', [-100.0])
DeltaPhi4 = array('f', [-100.0])
nAK04btagsMWP = array('f', [-100.0])
nLooseEle = array('f', [-100.0])
nLooseMu = array('f', [-100.0])
HLT_PFHT350_v = array('f', [-100.0])
HLT_PFHT400_SixJet30_v = array('f', [-100.0])
HLT_PFHT450_SixJet40_v = array('f', [-100.0])
HLT_PFMET120_Mu5_v = array('f', [-100.0])
HLT_PFHT800_v = array('f', [-100.0])
HLT_PFHT750_4JetPt50_v = array('f', [-100.0])
HLT_PFHT350_PFMET100_v = array('f', [-100.0])
HLT_PFMET170_NoiseCleaned_v = array('f', [-100.0])
HLT_PFMET120_PFMHT120_IDTight_v =  array('f', [-100.0])
HLT_PFMET110_PFMHT110_IDTight_v = array('f', [-100.0])
HLT_PFMET100_PFMHT100_IDTight_v = array('f', [-100.0])
HLT_PFMET90_PFMHT90_IDTight_v = array('f', [-100.0])
HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v = array('f', [-100.0])
HLT_PFHT450_SixJet40_BTagCSV_p056_v = array('f', [-100.0])
HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v = array('f', [-100.0])
HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v = array('f', [-100.0])
HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v = array('f', [-100.0])

#creating the tree branches we need
mynewTree.Branch('jet1pt', jet1pt, 'jet1pt/F')
mynewTree.Branch('jet2pt', jet2pt, 'jet2pt/F')
mynewTree.Branch('jet1eta', jet1eta, 'jet1eta/F')
mynewTree.Branch('jet2eta', jet2eta, 'jet2eta/F')
mynewTree.Branch('etadiff', etadiff, 'etadiff/F')
mynewTree.Branch('dijetmass', dijetmass, 'dijetmass/F')
mynewTree.Branch('dijetmass_corr', dijetmass_corr, 'dijetmass_corr/F')
mynewTree.Branch('dijetmass_corr_punc', dijetmass_corr_punc, 'dijetmass_corr_punc/F')
mynewTree.Branch('jet1tau21', jet1tau21, 'jet1tau21/F')
mynewTree.Branch('jet2tau21', jet2tau21, 'jet2tau21/F')
mynewTree.Branch('jet1pmass', jet1pmass, 'jet1pmass/F')
mynewTree.Branch('jet2pmass', jet2pmass, 'jet2pmass/F')
mynewTree.Branch('jet1pmassunc', jet1pmassunc, 'jet1pmassunc/F')
mynewTree.Branch('jet2pmassunc', jet2pmassunc, 'jet2pmassunc/F')
mynewTree.Branch('jet1bbtag', jet1bbtag, 'jet1bbtag/F')
mynewTree.Branch('jet2bbtag', jet2bbtag, 'jet2bbtag/F')
mynewTree.Branch('jet1s1csv', jet1s1csv, 'jet1s1csv/F')
mynewTree.Branch('jet2s1csv', jet2s1csv, 'jet2s1csv/F')
mynewTree.Branch('jet1s2csv', jet1s2csv, 'jet1s2csv/F')
mynewTree.Branch('jet2s2csv', jet2s2csv, 'jet2s2csv/F')
mynewTree.Branch('nAK08Jets', nAK08Jets, 'nAK08Jets/F')
mynewTree.Branch('nAK04Jets', nAK04Jets, 'nAK04Jets/F')
mynewTree.Branch('nAK04btagsMWP', nAK04btagsMWP, 'nAK04btagsMWP/F')
mynewTree.Branch('nHiggsTags', nHiggsTags, 'nHiggsTags/F')
mynewTree.Branch('triggerpassbb', triggerpassbb, 'triggerpassbb/F')
mynewTree.Branch('triggerpasssj', triggerpasssj, 'triggerpasssj/F')
mynewTree.Branch('nTrueInt',nTrueInt,'nTrueInt/F')
mynewTree.Branch('puWeights',puWeights,'puWeights/F')
mynewTree.Branch('puWeightsUp',puWeightsUp,'puWeightsUp/F')
mynewTree.Branch('puWeightsDown',puWeightsDown,'puWeightsDown/F')
mynewTree.Branch('jet1ID', jet1ID, 'jet1ID/F')
mynewTree.Branch('jet2ID', jet2ID, 'jet2ID/F')
mynewTree.Branch('vtype', vtype, 'vtype/F')
mynewTree.Branch('isData', isData, 'isData/F')
mynewTree.Branch('jet1nbHadron', jet1nbHadron, 'jet1nbHadron/F')
mynewTree.Branch('jet2nbHadron', jet2nbHadron, 'jet2nbHadron/F')
mynewTree.Branch('jet1flavor', jet1flavor, 'jet1flavor/F')
mynewTree.Branch('jet2flavor', jet2flavor, 'jet2flavor/F')
mynewTree.Branch('jet1ncHadron', jet1ncHadron, 'jet1ncHadron/F')
mynewTree.Branch('jet2ncHadron', jet2ncHadron, 'jet2ncHadron/F')
mynewTree.Branch('gen1Pt', gen1Pt, 'gen1Pt/F')
mynewTree.Branch('gen1Phi', gen1Phi, 'gen1Phi/F')
mynewTree.Branch('gen1Eta', gen1Eta, 'gen1Eta/F')
mynewTree.Branch('gen1Mass', gen1Mass, 'gen1Mass/F')
mynewTree.Branch('gen1ID', gen1ID, 'gen1ID/F')
mynewTree.Branch('gen2Pt', gen2Pt, 'gen2Pt/F')
mynewTree.Branch('gen2Phi', gen2Phi, 'gen2Phi/F')
mynewTree.Branch('gen2Eta', gen2Eta, 'gen2Eta/F')
mynewTree.Branch('gen2Mass', gen2Mass, 'gen2Mass/F')
mynewTree.Branch('gen2ID', gen2ID, 'gen2ID/F')
mynewTree.Branch('jet1l1l2l3', jet1l1l2l3, 'jet1l1l2l3/F')
mynewTree.Branch('jet1l2l3', jet1l2l3, 'jet1l2l3/F')
mynewTree.Branch('jet2l1l2l3', jet2l1l2l3, 'jet2l1l2l3/F')
mynewTree.Branch('jet2l2l3', jet2l2l3, 'jet2l2l3/F')
mynewTree.Branch('jet1JER', jet1JER, 'jet1JER/F')
mynewTree.Branch('jet2JER', jet2JER, 'jet2JER/F')
mynewTree.Branch('json', json, 'json/F')
mynewTree.Branch('DeltaPhi1', DeltaPhi1, 'DeltaPhi1/F')
mynewTree.Branch('DeltaPhi2', DeltaPhi2, 'DeltaPhi2/F')
mynewTree.Branch('DeltaPhi3', DeltaPhi3, 'DeltaPhi3/F')
mynewTree.Branch('DeltaPhi4', DeltaPhi4, 'DeltaPhi4/F')
mynewTree.Branch('SF', SF, 'SF/F')
mynewTree.Branch('SFup', SFup, 'SFup/F')
mynewTree.Branch('SFdown', SFdown, 'SFdown/F')
mynewTree.Branch('SF4sj', SF4sj, 'SF4sj/F')
mynewTree.Branch('SF4sjUp', SF4sjUp, 'SF4sjUp/F')
mynewTree.Branch('SF4sjDown', SF4sjDown, 'SF4sjDown/F')
mynewTree.Branch('SF3sj', SF3sj, 'SF3sj/F')
mynewTree.Branch('SF3sjUp', SF3sjUp, 'SF3sjUp/F')
mynewTree.Branch('SF3sjDown', SF3sjDown, 'SF3sjDown/F')
mynewTree.Branch('trigWeight', trigWeight, 'trigWeight/F')
mynewTree.Branch('trigWeightUp', trigWeightUp, 'trigWeightUp/F')
mynewTree.Branch('trigWeightDown', trigWeightDown, 'trigWeightDown/F')
mynewTree.Branch('trigWeight2Up', trigWeight2Up, 'trigWeight2Up/F')
mynewTree.Branch('trigWeight2Down', trigWeight2Down, 'trigWeight2Down/F')
mynewTree.Branch('norm',norm,'norm/F')
mynewTree.Branch('evt',evt,'evt/F')
mynewTree.Branch('ht', ht, 'ht/F')
mynewTree.Branch('htJet30', htJet30, 'htJet30/F')
mynewTree.Branch('MET', MET, 'MET/F')
mynewTree.Branch('xsec', xsec, 'xsec/F')
mynewTree.Branch('sjSF', sjSF, 'sjSF/F')
mynewTree.Branch('sjSFup', sjSFup, 'sjSFup/F')
mynewTree.Branch('sjSFdown', sjSFdown, 'sjSFdown/F')
mynewTree.Branch('jetSJfla',jetSJfla,'jetSJfla[4]/F')
mynewTree.Branch('jetSJpt', jetSJpt,'jetSJpt[4]/F')
mynewTree.Branch('jetSJcsv',jetSJcsv,'jetSJcsv[4]/F')
mynewTree.Branch('jetSJeta',jetSJeta,'jetSJeta[4]/F')
mynewTree.Branch('nLooseEle', nLooseEle, 'nLooseEle/F')
mynewTree.Branch('nLooseMu', nLooseMu, 'nLooseMu/F')
mynewTree.Branch('HLT_PFHT350_v', HLT_PFHT350_v, 'HLT_PFHT350_v/F')
mynewTree.Branch('HLT_PFHT400_SixJet30_v', HLT_PFHT400_SixJet30_v, 'HLT_PFHT400_SixJet30_v/F')
mynewTree.Branch('HLT_PFHT450_SixJet40_v', HLT_PFHT450_SixJet40_v, 'HLT_PFHT450_SixJet40_v/F')
mynewTree.Branch('HLT_PFMET120_Mu5_v', HLT_PFMET120_Mu5_v, 'HLT_PFMET120_Mu5_v/F')
mynewTree.Branch('HLT_PFHT800_v', HLT_PFHT800_v, 'HLT_PFHT800_v/F')
mynewTree.Branch('HLT_PFHT750_4JetPt50_v', HLT_PFHT750_4JetPt50_v, 'HLT_PFHT750_4JetPt50_v/F')
mynewTree.Branch('HLT_PFHT350_PFMET100_v', HLT_PFHT350_PFMET100_v, 'HLT_PFHT350_PFMET100_v/F')
mynewTree.Branch('HLT_PFMET170_NoiseCleaned_v', HLT_PFMET170_NoiseCleaned_v, 'HLT_PFMET170_NoiseCleaned_v/F')
mynewTree.Branch('HLT_PFMET120_PFMHT120_IDTight_v', HLT_PFMET120_PFMHT120_IDTight_v, 'HLT_PFMET120_PFMHT120_IDTight_v/F')
mynewTree.Branch('HLT_PFMET110_PFMHT110_IDTight_v', HLT_PFMET110_PFMHT110_IDTight_v, 'HLT_PFMET110_PFMHT110_IDTight_v/F')
mynewTree.Branch('HLT_PFMET100_PFMHT100_IDTight_v', HLT_PFMET100_PFMHT100_IDTight_v, 'HLT_PFMET100_PFMHT100_IDTight_v/F')
mynewTree.Branch('HLT_PFMET90_PFMHT90_IDTight_v', HLT_PFMET90_PFMHT90_IDTight_v, 'HLT_PFMET90_PFMHT90_IDTight_v/F')
mynewTree.Branch('HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v', HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v, 'HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v/F')
mynewTree.Branch('HLT_PFHT450_SixJet40_BTagCSV_p056_v', HLT_PFHT450_SixJet40_BTagCSV_p056_v, 'HLT_PFHT450_SixJet40_BTagCSV_p056_v/F')
mynewTree.Branch('HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v', HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v, 'HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v/F')
mynewTree.Branch('HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v', HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v/F')
mynewTree.Branch('HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v', HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v/F')
mynewTree.Branch('HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v', HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v, 'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v/F')
mynewTree.Branch('HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v', HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v, 'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v/F')

nevent = treeMine.GetEntries();

print outputfilename

h0 = ROOT.TH1F("h0", "HT PFHT350", 150, 0, 1500)
h1 = ROOT.TH1F("h1", "HT PFHT350 and PFHT800", 150, 0, 1500)

Weight = 0.1

count = 0
print "Number of Events:", nevent

for i in range(0, nevent) :
    treeMine.GetEntry(i)
    count = count + 1
    if count % 100000 == 0 :
	print "processing events", count




    triggerpassbb[0] = treeMine.triggerpassbb
    vtype[0] = treeMine.vtype
    jet1pt[0] = treeMine.jet1pt
    jet2pt[0] = treeMine.jet2pt
    jet2eta[0] = treeMine.jet2eta
    jet1eta[0] = treeMine.jet1eta
    dijetmass_corr[0] = treeMine.dijetmass_corr
    jet1pmass[0] = treeMine.jet1pmass
    jet2pmass[0] = treeMine.jet2pmass
    ht[0] = treeMine.ht
    etadiff[0] = treeMine.etadiff
    HLT_PFHT800_v[0] = treeMine.HLT_PFHT800_v
    HLT_PFHT350_v[0] = treeMine.HLT_PFHT350_v

    if HLT_PFHT350_v[0]:
	continue
    h0.Fill(ht[0],Weight)

    if HLT_PFHT800_v[0] == 0:
	continue
    h1.Fill(ht[0],Weight)


print "done " + outputfilename

f1.cd()
f1.Write()
f1.Close()

f.Close()
