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
parser.add_option("-f", "--pathIn", dest="inputFile",
                  help="inputFile path")

parser.add_option("-o", "--outName", dest="outName",
                  help="output file name")

parser.add_option("-l", "--file", dest="txt",
                  help="input txt file")

parser.add_option("-i", "--min", dest="min",
                  help="input index low end")

parser.add_option("-j", "--max", dest="max",
                  help="input index high end")

(options, args) = parser.parse_args()
outputfilename = options.outName

#inputfile = options.txt

ff_n = 1#int(options.max)

num1 = 0#int(options.min)
num2 = 1#int(options.max)

inputFile=options.inputFile
def open_files(file_name) : #opens files to run on

    g = open(file_name)
    list_file = []
    final_list = []
    for i in range(ff_n):  # this is the length of the file
        list_file.append(g.readline().split())
    s = options.inputFile

    for i in range(len(list_file)):
        for j in range(len(list_file[i])) :
            final_list.append(s + list_file[i][j])
    print final_list
    return final_list



#Files_list      = open_files( inputfile )
f =  ROOT.TFile.Open(inputFile.replace('root://cmseos.fnal.gov//store/user/mkrohn/HHHHTo4b/V23/QCD700/',''), 'recreate')


#print outputfilename
f.cd()
#getting old tree
mynewTree = ROOT.TTree('mynewTree', 'mynewTree')

#getting old branches from old tree
#creating the tree objects we need
jet1pt = array('f', [-100.0])
jet2pt = array('f', [-100.0])

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
dijetmass_pruned_corr = array('f', [-100.0])
dijetmass_softdrop_corr = array('f', [-100.0])
dijetmass_corr_punc = array('f', [-100.0])
jet1tau21 = array('f', [-100.0])
jet2tau21 = array('f', [-100.0])
jet1pmass = array('f', [-100.0])
jet2pmass = array('f', [-100.0])
jet1bbtag = array('f', [-100.0])
jet2bbtag = array('f', [-100.0])

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
jet1_puppi_msoftdrop_TheaCorr = array('f', [-100.0])
jet2_puppi_msoftdrop_TheaCorr = array('f', [-100.0])
jet1_puppi_msoftdrop_raw_TheaCorr = array('f', [-100.0])
jet2_puppi_msoftdrop_raw_TheaCorr = array('f', [-100.0])
jet1_puppi_msoftdrop_corrL2L3 = array('f', [-100.0])
jet2_puppi_msoftdrop_corrL2L3 = array('f', [-100.0])
jet1_puppi_TheaCorr = array('f', [-100.0])
jet2_puppi_TheaCorr = array('f', [-100.0])
jet1_puppi_msoftdrop_raw = array('f', [-100.0])
jet2_puppi_msoftdrop_raw = array('f', [-100.0])
dijetmass_puppi = array('f', [-100.0])
dijetmass_puppi_uncorr = array('f', [-100.0])

nTrueInt = array('f', [-100])
vtype = array('f', [-100.0])
isData = array('f', [100.0])
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
#norm = array('f', [-100.0])
evt = array('f', [-100.0])
ht = array('f', [-100.0])
htJet30 = array('f', [-100.0])
xsec = array('f', [-100.0])
HLT_PFHT800_v = array('f', [-100.0])
HLT_PFJet80_v = array('f', [-100.0])
HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v = array('f', [-100.0])
HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v = array('f', [-100.0])
HLT_AK8PFJet360_V = array('f', [-100.0])
HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
HLT_PFJet260_v = array('f', [-100.0])

#creating the tree branches we need
mynewTree.Branch('jet1pt', jet1pt, 'jet1pt/F')
mynewTree.Branch('jet2pt', jet2pt, 'jet2pt/F')
mynewTree.Branch('jet1eta', jet1eta, 'jet1eta/F')
mynewTree.Branch('jet2eta', jet2eta, 'jet2eta/F')
mynewTree.Branch('jet1phi', jet1phi, 'jet1phi/F')
mynewTree.Branch('jet2phi', jet2phi, 'jet2phi/F')
mynewTree.Branch('jet1mass', jet1mass, 'jet1mass/F')
mynewTree.Branch('jet2mass', jet2mass, 'jet2mass/F')
mynewTree.Branch('etadiff', etadiff, 'etadiff/F')
mynewTree.Branch('dijetmass', dijetmass, 'dijetmass/F')
mynewTree.Branch('dijetmass_pruned_corr', dijetmass_pruned_corr, 'dijetmass_pruned_corr/F')
mynewTree.Branch('dijetmass_softdrop_corr', dijetmass_softdrop_corr, 'dijetmass_softdrop_corr/F')
mynewTree.Branch('dijetmass_corr_punc', dijetmass_corr_punc, 'dijetmass_corr_punc/F')
mynewTree.Branch('jet1tau21', jet1tau21, 'jet1tau21/F')
mynewTree.Branch('jet2tau21', jet2tau21, 'jet2tau21/F')
mynewTree.Branch('jet1pmass', jet1pmass, 'jet1pmass/F')
mynewTree.Branch('jet2pmass', jet2pmass, 'jet2pmass/F')
mynewTree.Branch('jet1bbtag', jet1bbtag, 'jet1bbtag/F')
mynewTree.Branch('jet2bbtag', jet2bbtag, 'jet2bbtag/F')

mynewTree.Branch('jet1_puppi_pt', jet1_puppi_pt, 'jet1_puppi_pt/F')
mynewTree.Branch('jet2_puppi_pt', jet2_puppi_pt, 'jet2_puppi_pt/F')
mynewTree.Branch('jet1_puppi_eta', jet1_puppi_eta, 'jet1_puppi_eta/F')
mynewTree.Branch('jet2_puppi_eta', jet2_puppi_eta, 'jet2_puppi_eta/F')
mynewTree.Branch('jet1_puppi_phi', jet1_puppi_phi, 'jet1_puppi_phi/F')
mynewTree.Branch('jet2_puppi_phi', jet2_puppi_phi, 'jet2_puppi_phi/F')
mynewTree.Branch('jet1_puppi_mass', jet1_puppi_mass, 'jet1_puppi_mass/F')
mynewTree.Branch('jet2_puppi_mass', jet2_puppi_mass, 'jet2_puppi_mass/F')
mynewTree.Branch('jet1_puppi_tau21', jet1_puppi_tau21, 'jet1_puppi_tau21/F')
mynewTree.Branch('jet2_puppi_tau21', jet2_puppi_tau21, 'jet2_puppi_tau21/F')
mynewTree.Branch('jet1_puppi_msoftdrop', jet1_puppi_msoftdrop, 'jet1_puppi_msoftdrop/F')
mynewTree.Branch('jet2_puppi_msoftdrop', jet2_puppi_msoftdrop, 'jet2_puppi_msoftdrop/F')
mynewTree.Branch('jet1_puppi_msoftdrop_TheaCorr', jet1_puppi_msoftdrop_TheaCorr, 'jet1_puppi_msoftdrop_TheaCorr/F')
mynewTree.Branch('jet2_puppi_msoftdrop_TheaCorr', jet2_puppi_msoftdrop_TheaCorr, 'jet2_puppi_msoftdrop_TheaCorr/F')
mynewTree.Branch('jet1_puppi_msoftdrop_raw_TheaCorr', jet1_puppi_msoftdrop_raw_TheaCorr, 'jet1_puppi_msoftdrop_raw_TheaCorr/F')
mynewTree.Branch('jet2_puppi_msoftdrop_raw_TheaCorr', jet2_puppi_msoftdrop_raw_TheaCorr, 'jet2_puppi_msoftdrop_raw_TheaCorr/F')
mynewTree.Branch('jet1_puppi_msoftdrop_corrL2L3', jet1_puppi_msoftdrop_corrL2L3, 'jet1_puppi_msoftdrop_corrL2L3/F')
mynewTree.Branch('jet2_puppi_msoftdrop_corrL2L3', jet2_puppi_msoftdrop_corrL2L3, 'jet2_puppi_msoftdrop_corrL2L3/F')
mynewTree.Branch('jet1_puppi_TheaCorr', jet1_puppi_TheaCorr, 'jet1_puppi_TheaCorr/F')
mynewTree.Branch('jet2_puppi_TheaCorr', jet2_puppi_TheaCorr, 'jet2_puppi_TheaCorr/F')
mynewTree.Branch('jet1_puppi_msoftdrop_raw', jet1_puppi_msoftdrop_raw, 'jet1_puppi_msoftdrop_raw/F')
mynewTree.Branch('jet2_puppi_msoftdrop_raw', jet2_puppi_msoftdrop_raw, 'jet2_puppi_msoftdrop_raw/F')
mynewTree.Branch('dijetmass_puppi_uncorr', dijetmass_puppi_uncorr, 'dijetmass_puppi_uncorr/F')

mynewTree.Branch('nTrueInt',nTrueInt,'nTrueInt/F')
mynewTree.Branch('puWeights',puWeights,'puWeights/F')
mynewTree.Branch('puWeightsUp',puWeightsUp,'puWeightsUp/F')
mynewTree.Branch('puWeightsDown',puWeightsDown,'puWeightsDown/F')
mynewTree.Branch('jet1ID', jet1ID, 'jet1ID/F')
mynewTree.Branch('jet2ID', jet2ID, 'jet2ID/F')
mynewTree.Branch('vtype', vtype, 'vtype/F')
mynewTree.Branch('isData', isData, 'isData/F')
mynewTree.Branch('json', json, 'json/F')
mynewTree.Branch('bbtag1SFTight', bbtag1SFTight, 'bbtag1SFTight/F')
mynewTree.Branch('bbtag2SFTight', bbtag2SFTight, 'bbtag2SFTight/F')
mynewTree.Branch('bbtag1SFTightUp', bbtag1SFTightUp, 'bbtag1SFTightUp/F')
mynewTree.Branch('bbtag2SFTightUp', bbtag2SFTightUp, 'bbtag2SFTightUp/F')
mynewTree.Branch('bbtag1SFTightDown', bbtag1SFTightDown, 'bbtag1SFTightDown/F')
mynewTree.Branch('bbtag2SFTightDown', bbtag2SFTightDown, 'bbtag2SFTightDown/F')
mynewTree.Branch('bbtag1SFLoose', bbtag1SFLoose, 'bbtag1SFLoose/F')
mynewTree.Branch('bbtag2SFLoose', bbtag2SFLoose, 'bbtag2SFLoose/F')
mynewTree.Branch('bbtag1SFLooseUp', bbtag1SFLooseUp, 'bbtag1SFLooseUp/F')
mynewTree.Branch('bbtag2SFLooseUp', bbtag2SFLooseUp, 'bbtag2SFLooseUp/F')
mynewTree.Branch('bbtag1SFLooseDown', bbtag1SFLooseDown, 'bbtag1SFLooseDown/F')
mynewTree.Branch('bbtag2SFLooseDown', bbtag2SFLooseDown, 'bbtag2SFLooseDown/F')
mynewTree.Branch('SFTight', SFTight, 'SFTight/F')
mynewTree.Branch('SFTightup', SFTightup, 'SFTightup/F')
mynewTree.Branch('SFTightdown', SFTightdown, 'SFTightdown/F')
mynewTree.Branch('SFLoose', SFLoose, 'SFLoose/F')
mynewTree.Branch('SFLooseup', SFLooseup, 'SFLooseup/F')
mynewTree.Branch('SFLoosedown', SFLoosedown, 'SFLoosedown/F')

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
#myTree.Branch('norm',norm,'norm/F')
mynewTree.Branch('evt',evt,'evt/F')
mynewTree.Branch('ht', ht, 'ht/F')
mynewTree.Branch('htJet30', htJet30, 'htJet30/F')
mynewTree.Branch('xsec', xsec, 'xsec/F')

mynewTree.Branch('HLT_PFHT800_v', HLT_PFHT800_v, 'HLT_PFHT800_v/F')
mynewTree.Branch('HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v', HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v/F')
mynewTree.Branch('HLT_AK8PFJet360_V', HLT_AK8PFJet360_V, 'HLT_AK8PFJet360_V/F')
mynewTree.Branch('HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v', HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v, 'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v/F')
mynewTree.Branch('HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v', HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v, 'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v/F')
mynewTree.Branch('HLT_PFJet260_v', HLT_PFJet260_v, 'HLT_PFJet260_v/F')

CountWeightedmc = ROOT.TH1F("CountWeighted","Count with sign(gen weight) and pu weight",1,0,2)


print outputfilename

DataFile="JetHT_TriggerComparisons.root"
fin2 = ROOT.TFile.Open(DataFile, "READ")
h1_Data = fin2.Get("h17")
h2_Data = fin2.Get("h0")
DataEf = ROOT.TH1F("DataEf", "", 3000, 0., 3000.)

DataEf.Sumw2()
DataEf.Divide(h1_Data,h2_Data,1,1,"B")


count = 0
for i in range(num1, num2):
#    files = Files_list[i]
    print inputFile
    f1 = ROOT.TFile.Open(inputFile, "READ")
    treeMine  = f1.Get('myTree')
    nevent = treeMine.GetEntries();
    nFills = 0

    CountWeightedmc.Add(f1.Get("CountWeighted"))


    for i in range(0, nevent) :
        treeMine.GetEntry(i)
	count = count + 1
        if count % 1000 == 0 :
            print "processing events", count

	if treeMine.jet2pt == -100:
	    continue

#	if treeMine.HLT_PFHT800_v == 0:
#	    continue

        jet1pt[0] = treeMine.jet1pt
        jet2pt[0] = treeMine.jet2pt
        jet1ID[0] = treeMine.jet1ID
        jet2ID[0] = treeMine.jet2ID
        jet1eta[0] = treeMine.jet1eta
        jet2eta[0] = treeMine.jet2eta
        jet1phi[0] = treeMine.jet1phi
        jet2phi[0] = treeMine.jet2phi
        jet1mass[0] = treeMine.jet1mass
        jet2mass[0] = treeMine.jet2mass
        etadiff[0] = abs(treeMine.jet1eta - treeMine.jet2eta)
        dijetmass[0] = treeMine.dijetmass	
        dijetmass_pruned_corr[0] = treeMine.dijetmass_corr
        dijetmass_corr_punc[0] = treeMine.dijetmass_corr_punc
        jet1tau21[0] = treeMine.jet1tau21
        jet2tau21[0] = treeMine.jet2tau21
        jet1pmass[0] = treeMine.jet1pmass
        jet2pmass[0] = treeMine.jet2pmass
        jet1bbtag[0] = treeMine.jet1bbtag
        jet2bbtag[0] = treeMine.jet2bbtag
        jet1_puppi_pt[0] = treeMine.jet1_puppi_pt
        jet2_puppi_pt[0] = treeMine.jet2_puppi_pt
        jet1_puppi_eta[0] = treeMine.jet1_puppi_eta
        jet2_puppi_eta[0] = treeMine.jet2_puppi_eta
        jet1_puppi_phi[0] = treeMine.jet1_puppi_phi
        jet2_puppi_phi[0] = treeMine.jet2_puppi_phi
        jet1_puppi_mass[0] = treeMine.jet1_puppi_mass
        jet2_puppi_mass[0] = treeMine.jet2_puppi_mass
        jet1_puppi_tau21[0] = treeMine.jet1_puppi_tau21
        jet2_puppi_tau21[0] = treeMine.jet2_puppi_tau21
        jet1_puppi_msoftdrop[0] = treeMine.jet1_puppi_msoftdrop
        jet2_puppi_msoftdrop[0] = treeMine.jet2_puppi_msoftdrop
        jet1_puppi_msoftdrop_corrL2L3[0] = treeMine.jet1_puppi_msoftdrop_corrL2L3
        jet2_puppi_msoftdrop_corrL2L3[0] = treeMine.jet2_puppi_msoftdrop_corrL2L3
        jet1_puppi_TheaCorr[0] = treeMine.jet1_puppi_TheaCorr
        jet2_puppi_TheaCorr[0] = treeMine.jet2_puppi_TheaCorr
	jet1_puppi_msoftdrop_raw[0] = treeMine.jet1_puppi_msoftdrop_raw
        jet2_puppi_msoftdrop_raw[0] = treeMine.jet2_puppi_msoftdrop_raw

        jet1_puppi_msoftdrop_TheaCorr[0] = jet1_puppi_msoftdrop[0]*jet1_puppi_TheaCorr[0]
        jet2_puppi_msoftdrop_TheaCorr[0] = jet2_puppi_msoftdrop[0]*jet2_puppi_TheaCorr[0]
        jet1_puppi_msoftdrop_raw_TheaCorr[0] = jet1_puppi_msoftdrop_raw[0]*jet1_puppi_TheaCorr[0]
        jet2_puppi_msoftdrop_raw_TheaCorr[0] = jet2_puppi_msoftdrop_raw[0]*jet2_puppi_TheaCorr[0]

        
        nTrueInt[0] = treeMine.nTrueInt
        puWeights[0] = treeMine.puWeights
        puWeightsUp[0] = treeMine.puWeightsUp
        puWeightsDown[0] = treeMine.puWeightsDown
        vtype[0] = treeMine.vtype
        isData[0] = treeMine.isData
        json[0] = treeMine.json

	bbtag1SFTight[0] = treeMine.bbtag1SFTight
	bbtag2SFTight[0] = treeMine.bbtag2SFTight
	bbtag1SFTightUp[0] = treeMine.bbtag1SFTightUp
	bbtag2SFTightUp[0] = treeMine.bbtag2SFTightUp
	bbtag1SFTightDown[0] = treeMine.bbtag1SFTightDown
	bbtag2SFTightDown[0] = treeMine.bbtag2SFTightDown
	bbtag1SFLoose[0] = treeMine.bbtag1SFLoose
	bbtag2SFLoose[0] = treeMine.bbtag2SFLoose
	bbtag1SFLooseUp[0] = treeMine.bbtag1SFLooseUp
	bbtag2SFLooseUp[0] = treeMine.bbtag2SFLooseUp
	bbtag1SFLooseDown[0] = treeMine.bbtag1SFLooseDown
	bbtag2SFLooseDown[0] = treeMine.bbtag2SFLooseDown
	SFTight[0] = treeMine.SFTight
	SFTightup[0] = treeMine.SFTightup
	SFTightdown[0] = treeMine.SFTightdown
	SFLoose[0] = treeMine.SFLoose
	SFLooseup[0] = treeMine.SFLooseup
	SFLoosedown[0] = treeMine.SFLoosedown

        SF4sj[0] = treeMine.SF4sj
        SF4sjUp[0] = treeMine.SF4sjUp
        SF4sjDown[0] = treeMine.SF4sjDown
        SF3sj[0] = treeMine.SF3sj
        SF3sjUp[0] = treeMine.SF3sjUp
        SF3sjDown[0] = treeMine.SF3sjDown

        trigWeight2Up[0] = treeMine.trigWeight2Up
        trigWeight2Down[0] = treeMine.trigWeight2Down
        evt[0] = treeMine.evt
        ht[0] = treeMine.ht
        xsec[0] = treeMine.xsec
        HLT_PFHT800_v[0] = treeMine.HLT_PFHT800_v
        HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0] = treeMine.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v
        HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] = treeMine.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v
        HLT_AK8PFJet360_V[0] = treeMine.HLT_AK8PFJet360_TrimMass30_v
        HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v
        HLT_PFJet260_v[0] = treeMine.HLT_PFJet260_v

        jet1_puppi_raw_TL = ROOT.TLorentzVector()
        jet1_puppi_raw_TL.SetPtEtaPhiM(treeMine.jet1_puppi_pt, treeMine.jet1_puppi_eta, treeMine.jet1_puppi_phi, treeMine.jet1_puppi_msoftdrop_raw*treeMine.jet1_puppi_TheaCorr)

        jet2_puppi_raw_TL = ROOT.TLorentzVector()
        jet2_puppi_raw_TL.SetPtEtaPhiM(treeMine.jet2_puppi_pt, treeMine.jet2_puppi_eta, treeMine.jet2_puppi_phi, treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr)

        jet1_puppi_TL = ROOT.TLorentzVector()
        jet1_puppi_TL.SetPtEtaPhiM(jet1_puppi_pt[0], jet1_puppi_eta[0], jet1_puppi_phi[0], treeMine.jet1_puppi_msoftdrop*treeMine.jet1_puppi_TheaCorr)

        jet2_puppi_TL = ROOT.TLorentzVector()
        jet2_puppi_TL.SetPtEtaPhiM(jet2_puppi_pt[0], jet2_puppi_eta[0], jet2_puppi_phi[0], treeMine.jet2_puppi_msoftdrop*treeMine.jet2_puppi_TheaCorr)

        dijetmass_puppi[0] = (jet1_puppi_TL + jet2_puppi_TL).M() - (jet1_puppi_msoftdrop[0]*jet1_puppi_TheaCorr[0]-125)-(jet2_puppi_msoftdrop[0]*jet2_puppi_TheaCorr[0]-125)

	dijetmass_puppi_uncorr[0] = (jet1_puppi_raw_TL + jet2_puppi_raw_TL).M()

        jet1_ungroomed_TL = ROOT.TLorentzVector()
        jet1_ungroomed_TL.SetPtEtaPhiM(treeMine.jet1pt, treeMine.jet1eta, treeMine.jet1phi, treeMine.jet1mass)

        jet2_ungroomed_TL = ROOT.TLorentzVector()
        jet2_ungroomed_TL.SetPtEtaPhiM(treeMine.jet2pt, treeMine.jet2eta, treeMine.jet2phi, treeMine.jet2mass)


	dijetmass_softdrop_corr[0] = (jet1_ungroomed_TL + jet2_ungroomed_TL).M() - (jet1_puppi_msoftdrop_raw[0]*jet1_puppi_TheaCorr[0]-125)-(jet2_puppi_msoftdrop_raw[0]*jet2_puppi_TheaCorr[0]-125)

	if math.isnan(dijetmass_softdrop_corr[0]):
           trigWeight[0] = 1
           trigWeightUp[0] = 1
           trigWeightDown[0] = 1
        else:
           trigWeight[0] = DataEf.GetBinContent(int(round(dijetmass_softdrop_corr[0])))
           trigWeightUp[0] = trigWeight[0] + DataEf.GetBinError(int(round(dijetmass_softdrop_corr[0])))
           trigWeightDown[0] = trigWeight[0] - DataEf.GetBinError(int(round(dijetmass_softdrop_corr[0])))


        mynewTree.Fill()

    f1.Close()


print "nFills"
print nFills
print "OK"
print "done " + outputfilename

f.cd()
f.Write()
f.Close()



