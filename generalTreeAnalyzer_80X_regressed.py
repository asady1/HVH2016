import os
import glob
import math
import ROOT
from ROOT import *

#ROOT.gROOT.Macro("rootlogon.C")

import FWCore.ParameterSet.Config as cms

import sys
from DataFormats.FWLite import Events, Handle

from array import *

#ROOT.gSystem.Load('libCondFormatsBTagObjects') 

#command line options 
from optparse import OptionParser
parser = OptionParser()

parser.add_option("-f", "--pathIn", dest="inputFile",
                  help="inputFile path")

parser.add_option("-o", "--outName", dest="outName",
                  help="output file name")

parser.add_option("-i", "--min", dest="min", 
		  help="input index low end")

parser.add_option("-j", "--max", dest="max", 
		  help="input index high end")

parser.add_option("-l", "--file", dest="txt", 
		  help="input txt file")

parser.add_option("-t", "--trigger", dest="trigger", 
		  help="bool for trigger cut")

parser.add_option("-k", "--jets", dest="jets", 
		  help="bool for jet cuts")

parser.add_option("-d", "--deta", dest="deta", 
		  help="bool for delta eta cut")

parser.add_option("-m", "--isMC", dest="isMC", 
		  help="bool for is MC")

parser.add_option("-q", "--is2p1", dest="is2p1",
                  help="bool to retain ak4 jet info and other 2p1 things")

parser.add_option("-y", "--saveTrig", dest="saveTrig",
                  help="bool to not save triggers for background")

parser.add_option("-x", "--xsec", dest="xsec", 
		  help="cross section")

parser.add_option("-S", "--syst", dest="syst",
                  help="Systematic")


(options, args) = parser.parse_args()

inputfile = options.txt 

ff_n = 1000

num1 = int(options.min)
num2 = int(options.max)

d1 = options.outName 
d2 = '_'
print(options.outName)
outputfilename = d1 + d2 + options.min + '.root'

print outputfilename

import copy
File_tr=ROOT.TFile.Open("trigger_objects.root", "R")
histo_efficiency=copy.copy(File_tr.Get("histo_efficiency"))
histo_efficiency_up=copy.copy(File_tr.Get("histo_efficiency_upper"))
histo_efficiency_down=copy.copy(File_tr.Get("histo_efficiency_lower"))
histo_efficiency_2up=copy.copy(File_tr.Get("histo_efficiency_upper_2sigma"))
histo_efficiency_2down=copy.copy(File_tr.Get("histo_efficiency_lower_2sigma"))
File_tr.Close()


#defining functions
def div_except(a, b):
    if b>0:
        return float(a)/b
    else:
        return 1

def btagging_efficiency_medium(pt):
   result = 0.898 + 0.0002254*pt -1.74e-6*pt*pt +2.71e-9*pt*pt*pt -1.39e-12*pt*pt*pt*pt
   return result	

def trigger_function(histo_efficiency,htJet30=700):
    result = histo_efficiency.GetBinContent(htJet30)
    return result

def ClosestJet(jets, fourvec): #returns the index of the jet (from a collection "jets") closest to the given four-vector
	DR = 9999.
	index = -1
	for j in range(0,len(jets)):
	    if jets[j].Pt() > 0 :
		dR = fourvec.DeltaR(jets[j])
		if dR < DR :
			DR = fourvec.DeltaR(jets[j])
			index = j
	return index

def MatchCollection(Col, jet): #matches a jet to a jet in a different collection
	j = -1
        dr = 0.4
	for i in range(len(Col)):
		C = ROOT.TLorentzVector()
                C.SetPtEtaPhiM( Col[i].Pt(), Col[i].Eta(), Col[i].Phi(), Col[i].M() )
		dr = abs(jet.DeltaR(C))
		if dr < 0.4 :
			#print "WOOHOO MATCH with index " + str(j) + " with dr " + str(dr)
			j = i
                        break
        if dr > 0.4:
	#	print "No Match :( for dr: " + str(dr)
#		print "index " + str(j)
		return -1
	return j

def MatchCollection2(Col, jet, index): #matches a jet to a jet in a different collection
	j = -1
        dr = 0.4
	for i in range(len(Col)):
            if i != index:
                C = ROOT.TLorentzVector()
                C.SetPtEtaPhiM( Col[i].Pt(), Col[i].Eta(), Col[i].Phi(), Col[i].M() )
		dr = abs(jet.DeltaR(C))
		if dr < 0.4 :
			#print "WOOHOO MATCH with index " + str(j) + " with dr " + str(dr)
			j = i
                        break
        if dr > 0.4:
	#	print "No Match :( for dr: " + str(dr)
#		print "index " + str(j)
		return -1
	return j

def MatchCollection3(Col, jet, index1, index2): #matches a jet to a jet in a different collection
	j = -1
        dr = 0.4
	for i in range(len(Col)):
            if i != index1 and i != index2:
                C = ROOT.TLorentzVector()
                C.SetPtEtaPhiM( Col[i].Pt(), Col[i].Eta(), Col[i].Phi(), Col[i].M() )
		dr = abs(jet.DeltaR(C))
		if dr < 0.4 :
			#print "WOOHOO MATCH with index " + str(j) + " with dr " + str(dr)
			j = i
                        break
        if dr > 0.4:
	#	print "No Match :( for dr: " + str(dr)
#		print "index " + str(j)
		return -1
	return j

def MatchCollection4(Col, jet, index1, index2, index3): #matches a jet to a jet in a different collection
	j = -1
        dr = 0.4
	for i in range(len(Col)):
            if i != index1 and i != index2 and i != index3:
                C = ROOT.TLorentzVector()
                C.SetPtEtaPhiM( Col[i].Pt(), Col[i].Eta(), Col[i].Phi(), Col[i].M() )
		dr = abs(jet.DeltaR(C))
		if dr < 0.4 :
			#print "WOOHOO MATCH with index " + str(j) + " with dr " + str(dr)
			j = i
                        break
        if dr > 0.4:
	#	print "No Match :( for dr: " + str(dr)
#		print "index " + str(j)
		return -1
	return j

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


def deltaR( particle, jet ) : #gives deltaR between two particles
    DeltaPhiHere = math.fabs( particle.phi() - jet.phi() )
    if DeltaPhiHere > math.pi :
        DeltaPhiHere = 2*math.pi - DeltaPhiHere

    deltaRHere = math.sqrt( (particle.eta() - jet.eta() )**2 + ( DeltaPhiHere )**2  )
    return deltaRHere

print sys.argv[1]

f =  ROOT.TFile(outputfilename, 'recreate')

f.cd()


myTree =  ROOT.TTree('myTree', 'myTree')

#creating the tree objects we need
jet1pt = array('f', [-100.0])
jet2pt = array('f', [-100.0])
jet1pt_reg = array('f', [-100.0])
jet2pt_reg = array('f', [-100.0])

jet1NearbyJetcsvArray = array('f', [-100.0, -100.0, -100.0, -100.0])
jet2NearbyJetcsvArray = array('f', [-100.0, -100.0, -100.0, -100.0])
jet1NearbyJetcmvaArray = array('f', [-100.0, -100.0, -100.0, -100.0])
jet2NearbyJetcmvaArray = array('f', [-100.0, -100.0, -100.0, -100.0])
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
gen1phi = array('f', [-100.0])
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
if options.is2p1 == 'True':
    bbtag1SF = array('f', [-100.0])
    bbtag2SF = array('f', [-100.0])
    bbtag1SFUp = array('f', [-100.0])
    bbtag2SFUp = array('f', [-100.0])
    bbtag1SFDown = array('f', [-100.0])
    bbtag2SFDown = array('f', [-100.0])
    passesBoosted = array('f', [-100.0])
    passesResolved = array('f', [-100.0])
else:
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
if options.isMC == 'True':
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
nLooseEle = array('f', [-100.0])
nLooseMu = array('f', [-100.0])
tPtsum = array('f', [-100.0])
if options.is2p1 == 'True':
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
if options.saveTrig == 'True':
    HLT_AK8PFJet360_V = array('f', [-100.0])
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
    HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v = array('f', [-100.0])
    HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v = array('f', [-100.0])
    HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v = array('f', [-100.0])
    HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v = array('f', [-100.0])
    HLT_QuadPFJet_VBF_v = array('f', [-100.0])
    HLT_L1_TripleJet_VBF_v = array('f', [-100.0])
    HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v  = array('f', [-100.0])
    HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v = array('f', [-100.0])
    HLT_PFJet40_v = array('f', [-100.0])
    HLT_PFJet60_v  = array('f', [-100.0])
    HLT_PFJet80_v = array('f', [-100.0])
    HLT_PFJet140_v = array('f', [-100.0])
    HLT_PFJet200_v = array('f', [-100.0])
    HLT_PFJet260_v  = array('f', [-100.0])
    HLT_PFJet320_v  = array('f', [-100.0])
    HLT_PFJet400_v  = array('f', [-100.0])
    HLT_PFJet450_v  = array('f', [-100.0])
    HLT_DiPFJetAve40_v  = array('f', [-100.0])
    HLT_DiPFJetAve60_v = array('f', [-100.0])
    HLT_DiPFJetAve80_v = array('f', [-100.0])
    HLT_DiPFJetAve140_v  = array('f', [-100.0])
    HLT_DiPFJetAve200_v = array('f', [-100.0])
    HLT_DiPFJetAve260_v = array('f', [-100.0])
    HLT_DiPFJetAve320_V = array('f', [-100.0])
    HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v = array('f', [-100.0])
    HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v = array('f', [-100.0])
    HLT_QuadJet45_TripleBTagCSV_p087_v = array('f', [-100.0])
    HLT_QuadJet45_DoubleBTagCSV_p087_v = array('f', [-100.0])
    HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v = array('f', [-100.0])
    HLT_DoubleJet90_Double30_DoubleBTagCSV_p087_v = array('f', [-100.0])
    HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v = array('f', [-100.0])
    HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v = array('f', [-100.0])
    HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v = array('f', [-100.0])
    HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
    HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
    HLT_Mu20_v = array('f', [-100.0])

#creating the tree branches we need
myTree.Branch('jet1pt', jet1pt, 'jet1pt/F')
myTree.Branch('jet2pt', jet2pt, 'jet2pt/F')
myTree.Branch('jet1pt_reg', jet1pt_reg, 'jet1pt_reg/F')
myTree.Branch('jet2pt_reg', jet2pt_reg, 'jet2pt_reg/F')
myTree.Branch('jet1NearbyJetcsv', jet1NearbyJetcsvArray, 'pt/F:eta/F:phi/F:mass/F')
myTree.Branch('jet2NearbyJetcsv', jet2NearbyJetcsvArray, 'pt/F:eta/F:phi/F:mass/F')
myTree.Branch('jet1NearbyJetcmva', jet1NearbyJetcmvaArray, 'pt/F:eta/F:phi/F:mass/F')
myTree.Branch('jet2NearbyJetcmva', jet2NearbyJetcmvaArray, 'pt/F:eta/F:phi/F:mass/F')
myTree.Branch('jet1NJcsv', jet1NJcsv, 'jet1NJcsv')
myTree.Branch('jet2NJcsv', jet2NJcsv, 'jet2NJcsv')
myTree.Branch('jet1NJcmva', jet1NJcmva, 'jet1NJcmva')
myTree.Branch('jet2NJcmva', jet2NJcmva, 'jet2NJcmva')
myTree.Branch('jet1eta', jet1eta, 'jet1eta/F')
myTree.Branch('jet2eta', jet2eta, 'jet2eta/F')
myTree.Branch('jet1phi', jet1phi, 'jet1phi/F')
myTree.Branch('jet2phi', jet2phi, 'jet2phi/F')
myTree.Branch('jet1mass', jet1mass, 'jet1mass/F')
myTree.Branch('jet2mass', jet2mass, 'jet2mass/F')
myTree.Branch('etadiff', etadiff, 'etadiff/F')
myTree.Branch('dijetmass', dijetmass, 'dijetmass/F')
myTree.Branch('dijetmass_corr', dijetmass_corr, 'dijetmass_corr/F')
myTree.Branch('dijetmass_reg', dijetmass_reg, 'dijetmass_reg/F')
myTree.Branch('dijetmass_corr_punc', dijetmass_corr_punc, 'dijetmass_corr_punc/F')
myTree.Branch('jet1tau21', jet1tau21, 'jet1tau21/F')
myTree.Branch('jet2tau21', jet2tau21, 'jet2tau21/F')
myTree.Branch('jet1pmass', jet1pmass, 'jet1pmass/F')
myTree.Branch('jet2pmass', jet2pmass, 'jet2pmass/F')
myTree.Branch('jet1pmassunc', jet1pmassunc, 'jet1pmassunc/F')
myTree.Branch('jet2pmassunc', jet2pmassunc, 'jet2pmassunc/F')
myTree.Branch('jet1bbtag', jet1bbtag, 'jet1bbtag/F')
myTree.Branch('jet2bbtag', jet2bbtag, 'jet2bbtag/F')
myTree.Branch('jet1s1csv', jet1s1csv, 'jet1s1csv/F')
myTree.Branch('jet2s1csv', jet2s1csv, 'jet2s1csv/F')
myTree.Branch('jet1s2csv', jet1s2csv, 'jet1s2csv/F')
myTree.Branch('jet2s2csv', jet2s2csv, 'jet2s2csv/F')
myTree.Branch('nAK08Jets', nAK08Jets, 'nAK08Jets/F')
myTree.Branch('nAK04Jets', nAK04Jets, 'nAK04Jets/F')
myTree.Branch('nAK04btagsMWP', nAK04btagsMWP, 'nAK04btagsMWP/F')
myTree.Branch('nHiggsTags', nHiggsTags, 'nHiggsTags/F')
myTree.Branch('triggerpassbb', triggerpassbb, 'triggerpassbb/F')
myTree.Branch('triggerpasssj', triggerpasssj, 'triggerpasssj/F')
myTree.Branch('nTrueInt',nTrueInt,'nTrueInt/F')
myTree.Branch('puWeights',puWeights,'puWeights/F')
myTree.Branch('puWeightsUp',puWeightsUp,'puWeightsUp/F')
myTree.Branch('puWeightsDown',puWeightsDown,'puWeightsDown/F')
myTree.Branch('jet1ID', jet1ID, 'jet1ID/F')
myTree.Branch('jet2ID', jet2ID, 'jet2ID/F')
myTree.Branch('vtype', vtype, 'vtype/F') 
myTree.Branch('isData', isData, 'isData/F') 
myTree.Branch('jet1nbHadron', jet1nbHadron, 'jet1nbHadron/F')
myTree.Branch('jet2nbHadron', jet2nbHadron, 'jet2nbHadron/F')
myTree.Branch('jet1flavor', jet1flavor, 'jet1flavor/F') 
myTree.Branch('jet2flavor', jet2flavor, 'jet2flavor/F') 
myTree.Branch('jet1ncHadron', jet1ncHadron, 'jet1ncHadron/F')
myTree.Branch('jet2ncHadron', jet2ncHadron, 'jet2ncHadron/F')
myTree.Branch('gen1Pt', gen1Pt, 'gen1Pt/F')
myTree.Branch('gen1phi', gen1phi, 'gen1phi/F')
myTree.Branch('gen1Eta', gen1Eta, 'gen1Eta/F')
myTree.Branch('gen1Mass', gen1Mass, 'gen1Mass/F')
myTree.Branch('gen1ID', gen1ID, 'gen1ID/F')
myTree.Branch('gen2Pt', gen2Pt, 'gen2Pt/F')
myTree.Branch('gen2Phi', gen2Phi, 'gen2Phi/F')
myTree.Branch('gen2Eta', gen2Eta, 'gen2Eta/F')
myTree.Branch('gen2Mass', gen2Mass, 'gen2Mass/F')
myTree.Branch('gen2ID', gen2ID, 'gen2ID/F')
myTree.Branch('jet1l1l2l3', jet1l1l2l3, 'jet1l1l2l3/F') 
myTree.Branch('jet1l2l3', jet1l2l3, 'jet1l2l3/F')
myTree.Branch('jet2l1l2l3', jet2l1l2l3, 'jet2l1l2l3/F') 
myTree.Branch('jet2l2l3', jet2l2l3, 'jet2l2l3/F')
myTree.Branch('jet1JER', jet1JER, 'jet1JER/F') 
myTree.Branch('jet2JER', jet2JER, 'jet2JER/F') 
myTree.Branch('json', json, 'json/F')
myTree.Branch('DeltaPhi1', DeltaPhi1, 'DeltaPhi1/F')
myTree.Branch('DeltaPhi2', DeltaPhi2, 'DeltaPhi2/F')
myTree.Branch('DeltaPhi3', DeltaPhi3, 'DeltaPhi3/F')
myTree.Branch('DeltaPhi4', DeltaPhi4, 'DeltaPhi4/F')
if options.is2p1 == 'True':
    myTree.Branch('bbtag1SF', bbtag1SF, 'bbtag1SF/F')
    myTree.Branch('bbtag2SF', bbtag2SF, 'bbtag2SF/F')
    myTree.Branch('bbtag1SFUp', bbtag1SFUp, 'bbtag1SFUp/F')
    myTree.Branch('bbtag2SFUp', bbtag2SFUp, 'bbtag2SFUp/F')
    myTree.Branch('bbtag1SFDown', bbtag1SFDown, 'bbtag1SFDown/F')
    myTree.Branch('bbtag2SFDown', bbtag2SFDown, 'bbtag2SFDown/F')
    myTree.Branch('passesBoosted', passesBoosted, 'passesBoosted/F')
    myTree.Branch('passesResolved', passesResolved, 'passesResolved/F')
else:
    myTree.Branch('SF', SF, 'SF/F')
    myTree.Branch('SFup', SFup, 'SFup/F')
    myTree.Branch('SFdown', SFdown, 'SFdown/F')
    myTree.Branch('SF4sj', SF4sj, 'SF4sj/F')
    myTree.Branch('SF4sjUp', SF4sjUp, 'SF4sjUp/F')
    myTree.Branch('SF4sjDown', SF4sjDown, 'SF4sjDown/F')
    myTree.Branch('SF3sj', SF3sj, 'SF3sj/F')
    myTree.Branch('SF3sjUp', SF3sjUp, 'SF3sjUp/F')
    myTree.Branch('SF3sjDown', SF3sjDown, 'SF3sjDown/F')
myTree.Branch('tPtsum', tPtsum, 'tPtsum/F')
myTree.Branch('trigWeight', trigWeight, 'trigWeight/F')
myTree.Branch('trigWeightUp', trigWeightUp, 'trigWeightUp/F')
myTree.Branch('trigWeightDown', trigWeightDown, 'trigWeightDown/F')
myTree.Branch('trigWeight2Up', trigWeight2Up, 'trigWeight2Up/F')
myTree.Branch('trigWeight2Down', trigWeight2Down, 'trigWeight2Down/F')
myTree.Branch('norm',norm,'norm/F')
myTree.Branch('evt',evt,'evt/F')
myTree.Branch('ht', ht, 'ht/F')
myTree.Branch('htJet30', htJet30, 'htJet30/F')
myTree.Branch('MET', MET, 'MET/F')
myTree.Branch('xsec', xsec, 'xsec/F')
myTree.Branch('sjSF', sjSF, 'sjSF/F')
myTree.Branch('sjSFup', sjSFup, 'sjSFup/F')
myTree.Branch('sjSFdown', sjSFdown, 'sjSFdown/F')
myTree.Branch('jetSJfla',jetSJfla,'jetSJfla[4]/F') 
myTree.Branch('jetSJpt', jetSJpt,'jetSJpt[4]/F')
myTree.Branch('jetSJcsv',jetSJcsv,'jetSJcsv[4]/F')
myTree.Branch('jetSJeta',jetSJeta,'jetSJeta[4]/F')
if options.isMC == 'True':
    myTree.Branch('genJet1BH', genJet1BH, 'genJet1BH/F')
    myTree.Branch('genjet2BH', genjet2BH, 'genjet2BH/F')
    myTree.Branch('genjet1CH', genjet1CH, 'genjet1CH/F')
    myTree.Branch('genjet2CH', genjet2CH, 'genjet2CH/F')
myTree.Branch('nLooseEle', nLooseEle, 'nLooseEle/F')
myTree.Branch('nLooseMu', nLooseMu, 'nLooseMu/F')
if options.is2p1 == 'True':
    myTree.Branch('ak4jet_pt',ak4jet_pt)
    myTree.Branch('ak4jet_eta',ak4jet_eta)
    myTree.Branch('ak4jet_phi',ak4jet_phi)
    myTree.Branch('ak4jet_mass',ak4jet_mass)
    myTree.Branch('ak4jetID',ak4jetID)
    myTree.Branch('ak4jetHeppyFlavour', ak4jetHeppyFlavour)
    myTree.Branch('ak4jetMCflavour', ak4jetMCflavour)
    myTree.Branch('ak4jetPartonFlavour', ak4jetPartonFlavour)
    myTree.Branch('ak4jetHadronFlavour', ak4jetHadronFlavour)
    myTree.Branch('ak4jetCSVLSF', ak4jetCSVLSF)
    myTree.Branch('ak4jetCSVLSF_Up', ak4jetCSVLSF_Up)
    myTree.Branch('ak4jetCSVLSF_Down', ak4jetCSVLSF_Down)
    myTree.Branch('ak4jetCSVMSF', ak4jetCSVMSF)
    myTree.Branch('ak4jetCSVMSF_up', ak4jetCSVMSF_up)
    myTree.Branch('ak4jetCSVMSF_Down', ak4jetCSVMSF_Down)
    myTree.Branch('ak4jetCSVTSF', ak4jetCSVTSF)
    myTree.Branch('ak4jetCSVTSF_Up', ak4jetCSVTSF_Up)
    myTree.Branch('ak4jetCSVTSF_Down', ak4jetCSVTSF_Down) 
    myTree.Branch('ak4jetCMVALSF', ak4jetCMVALSF)
    myTree.Branch('ak4jetCMVALSF_Up', ak4jetCMVALSF_Up)
    myTree.Branch('ak4jetCMVALSF_Down', ak4jetCMVALSF_Down) 
    myTree.Branch('ak4jetCMVAMSF', ak4jetCMVAMSF)
    myTree.Branch('ak4jetCMVAMSF_Up', ak4jetCMVAMSF_Up)
    myTree.Branch('ak4jetCMVAMSF_Down', ak4jetCMVAMSF_Down)
    myTree.Branch('ak4jetCMVATSF', ak4jetCMVATSF)
    myTree.Branch('ak4jetCMVATSF_Up', ak4jetCMVATSF_Up)
    myTree.Branch('ak4jetCMVATSF_Down', ak4jetCMVATSF_Down)
    myTree.Branch('ak4jetCSV', ak4jetCSV)
    myTree.Branch('ak4jetCMVA', ak4jetCMVA)
    myTree.Branch('ak4jetCorr', ak4jetCorr)
    myTree.Branch('ak4jetCorrJECUp', ak4jetCorrJECUp)
    myTree.Branch('ak4jetCorrJECDown', ak4jetCorrJECDown)
    myTree.Branch('ak4jetCorrJER', ak4jetCorrJER)
    myTree.Branch('ak4jetCorrJERUp', ak4jetCorrJERUp)
    myTree.Branch('ak4jetCorrJERDown', ak4jetCorrJERDown)
    myTree.Branch('ak4genJetPt', ak4genJetPt) 
    myTree.Branch('ak4genJetPhi', ak4genJetPhi)
    myTree.Branch('ak4genJetEta', ak4genJetEta)
    myTree.Branch('ak4genJetMass', ak4genJetMass)
    myTree.Branch('ak4genJetID', ak4genJetID)
if options.saveTrig == 'True':
    myTree.Branch('HLT_AK8PFJet360_V', HLT_AK8PFJet360_V, 'HLT_AK8PFJet360_V/F')
    myTree.Branch('HLT_PFHT350_v', HLT_PFHT350_v, 'HLT_PFHT350_v/F')
    myTree.Branch('HLT_PFHT400_SixJet30_v', HLT_PFHT400_SixJet30_v, 'HLT_PFHT400_SixJet30_v/F')
    myTree.Branch('HLT_PFHT450_SixJet40_v', HLT_PFHT450_SixJet40_v, 'HLT_PFHT450_SixJet40_v/F')
    myTree.Branch('HLT_PFMET120_Mu5_v', HLT_PFMET120_Mu5_v, 'HLT_PFMET120_Mu5_v/F')
    myTree.Branch('HLT_PFHT800_v', HLT_PFHT800_v, 'HLT_PFHT800_v/F')
    myTree.Branch('HLT_PFHT750_4JetPt50_v', HLT_PFHT750_4JetPt50_v, 'HLT_PFHT750_4JetPt50_v/F')
    myTree.Branch('HLT_PFHT350_PFMET100_v', HLT_PFHT350_PFMET100_v, 'HLT_PFHT350_PFMET100_v/F')
    myTree.Branch('HLT_PFMET170_NoiseCleaned_v', HLT_PFMET170_NoiseCleaned_v, 'HLT_PFMET170_NoiseCleaned_v/F')
    myTree.Branch('HLT_PFMET120_PFMHT120_IDTight_v', HLT_PFMET120_PFMHT120_IDTight_v, 'HLT_PFMET120_PFMHT120_IDTight_v/F')
    myTree.Branch('HLT_PFMET110_PFMHT110_IDTight_v', HLT_PFMET110_PFMHT110_IDTight_v, 'HLT_PFMET110_PFMHT110_IDTight_v/F')
    myTree.Branch('HLT_PFMET100_PFMHT100_IDTight_v', HLT_PFMET100_PFMHT100_IDTight_v, 'HLT_PFMET100_PFMHT100_IDTight_v/F')
    myTree.Branch('HLT_PFMET90_PFMHT90_IDTight_v', HLT_PFMET90_PFMHT90_IDTight_v, 'HLT_PFMET90_PFMHT90_IDTight_v/F')
    myTree.Branch('HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v', HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v, 'HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v/F')
    myTree.Branch('HLT_PFHT450_SixJet40_BTagCSV_p056_v', HLT_PFHT450_SixJet40_BTagCSV_p056_v, 'HLT_PFHT450_SixJet40_BTagCSV_p056_v/F')
    myTree.Branch('HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v', HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v, 'HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v/F')
    myTree.Branch('HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v', HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v/F')
    myTree.Branch('HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v', HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v/F')
    myTree.Branch('HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v', HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v, 'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v/F')
    myTree.Branch('HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v', HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v, 'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v/F')
    myTree.Branch('HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v', HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v, 'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v/F')
    myTree.Branch('HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v', HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v, 'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v/F')
    myTree.Branch('HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v', HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v, 'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v/F') 
    myTree.Branch('HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v', HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v, 'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v/F')
    myTree.Branch('HLT_QuadPFJet_VBF_v', HLT_QuadPFJet_VBF_v, 'HLT_QuadPFJet_VBF_v/F')
    myTree.Branch('HLT_L1_TripleJet_VBF_v', HLT_L1_TripleJet_VBF_v, 'HLT_L1_TripleJet_VBF_v/F')
    myTree.Branch('HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v', HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v, 'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v/F') 
    myTree.Branch('HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v', HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v, 'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v/F')
    myTree.Branch('HLT_PFJet40_v', HLT_PFJet40_v, 'HLT_PFJet40_v/F')
    myTree.Branch('HLT_PFJet60_v', HLT_PFJet60_v, 'HLT_PFJet60_v/F')
    myTree.Branch('HLT_PFJet80_v', HLT_PFJet80_v, 'HLT_PFJet80_v/F')
    myTree.Branch('HLT_PFJet140_v', HLT_PFJet140_v, 'HLT_PFJet140_v/F')
    myTree.Branch('HLT_PFJet200_v', HLT_PFJet200_v, 'HLT_PFJet200_v/F')
    myTree.Branch('HLT_PFJet260_v', HLT_PFJet260_v, 'HLT_PFJet260_v/F')
    myTree.Branch('HLT_PFJet320_v', HLT_PFJet320_v, 'HLT_PFJet320_v/F')
    myTree.Branch('HLT_PFJet400_v', HLT_PFJet400_v, 'HLT_PFJet400_v/F')
    myTree.Branch('HLT_PFJet450_v', HLT_PFJet450_v, 'HLT_PFJet450_v/F')
    myTree.Branch('HLT_DiPFJetAve40_v', HLT_DiPFJetAve40_v, 'HLT_DiPFJetAve40_v/F')
    myTree.Branch('HLT_DiPFJetAve60_v', HLT_DiPFJetAve60_v, 'HLT_DiPFJetAve60_v/F')
    myTree.Branch('HLT_DiPFJetAve80_v', HLT_DiPFJetAve80_v, 'HLT_DiPFJetAve80_v/F')
    myTree.Branch('HLT_DiPFJetAve140_v', HLT_DiPFJetAve140_v, 'HLT_DiPFJetAve140_v/F')
    myTree.Branch('HLT_DiPFJetAve200_v', HLT_DiPFJetAve200_v, 'HLT_DiPFJetAve200_v/F')
    myTree.Branch('HLT_DiPFJetAve260_v', HLT_DiPFJetAve260_v, 'HLT_DiPFJetAve260_v/F')
    myTree.Branch('HLT_DiPFJetAve320_V', HLT_DiPFJetAve320_V, 'HLT_DiPFJetAve320_V/F')
    myTree.Branch('HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v', HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v, 'HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v/F')
    myTree.Branch('HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v', HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v, 'HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v/F')
    myTree.Branch('HLT_QuadJet45_TripleBTagCSV_p087_v', HLT_QuadJet45_TripleBTagCSV_p087_v, 'HLT_QuadJet45_TripleBTagCSV_p087_v/F')
    myTree.Branch('HLT_QuadJet45_DoubleBTagCSV_p087_v', HLT_QuadJet45_DoubleBTagCSV_p087_v, 'HLT_QuadJet45_DoubleBTagCSV_p087_v/F')
    myTree.Branch('HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v', HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v, 'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v/F')
    myTree.Branch('HLT_DoubleJet90_Double30_DoubleBTagCSV_p087_v', HLT_DoubleJet90_Double30_DoubleBTagCSV_p087_v, 'HLT_DoubleJet90_Double30_DoubleBTagCSV_p087_v/F')
    myTree.Branch('HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v', HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v, 'HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v/F')
    myTree.Branch('HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v', HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v, 'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v/F')
    myTree.Branch('HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v', HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v, 'HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v/F')
    myTree.Branch('HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v', HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v/F')
    myTree.Branch('HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v', HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v/F')
    myTree.Branch('HLT_Mu20_v', HLT_Mu20_v, 'HLT_Mu20_v/F')


Files_list	= open_files( inputfile )

#list of histograms that may be useful
bbj = ROOT.TH1F("bbj", "Before any cuts", 3, -0.5, 1.5)
bb0 = ROOT.TH1F("bb0", "After Json", 3, -0.5, 1.5)
bb1 = ROOT.TH1F("bb1", "After Trigger", 3, -0.5, 1.5)
bb2 = ROOT.TH1F("bb2", "After jet cuts", 3, -0.5, 1.5)
if options.is2p1 == 'False':
    bb3 = ROOT.TH1F("bb3", "After Delta Eta Cuts", 3, -0.5, 1.5)
if options.is2p1 == 'True':
    bb3 = ROOT.TH1F("bb3", "After AK4 Jet Cuts", 3, -0.5, 1.5)

if options.isMC == 'True':
    CountMC = ROOT.TH1F("Count","Count",1,0,2)
    CountFullWeightedMC = ROOT.TH1F("CountFullWeighted","Count with gen weight and pu weight",1,0,2)
    CountWeightedmc = ROOT.TH1F("CountWeighted","Count with sign(gen weight) and pu weight",1,0,2)
    CountPosWeightMC = ROOT.TH1F("CountPosWeight","Count genWeight>0",1,0,2)
    CountNegWeightMC = ROOT.TH1F("CountNegWeight","Count genWeight<0",1,0,2)
    CountWeightedLHEWeightScalemc = ROOT.TH1F("CountWeightedLHEWeightScale","Count with gen weight x LHE_weights_scale and pu weight", 6, -0.5, 5.5)
    CountWeightedLHEWeightPdfMC = ROOT.TH1F("CountWeightedLHEWeightPdf","Count with gen weight x LHE_weights_pdf and pu weight", 103, -0.5, 102.5)


this_pt=array( 'f', [ 0 ] )
this_pv=array( 'f', [ 0 ] )
this_eta=array( 'f', [ 0 ] )
this_mass=array( 'f', [ 0 ] )
this_muonF =array( 'f', [ 0 ] )
this_EmF=array( 'f', [ 0 ] )
this_HF=array( 'f', [ 0 ] )
this_multi=array( 'f', [ 0 ] )

reader = ROOT.TMVA.Reader("!Color:!Silent" )
reader.AddVariable( "FatjetAK08ungroomed_pt", this_pt)
reader.AddVariable( "nPVs", this_pv)
reader.AddVariable( "FatjetAK08ungroomed_eta", this_eta)
#reader.AddVariable( "FatjetAK08ungroomed_mass", this_mass)
reader.AddVariable( "FatjetAK08ungroomed_muonEnergyFraction", this_muonF)
reader.AddVariable( "FatjetAK08ungroomed_neutralEmEnergyFraction", this_EmF)
reader.AddVariable( "FatjetAK08ungroomed_neutralHadronEnergyFraction", this_HF)
reader.AddVariable( "FatjetAK08ungroomed_chargedMultiplicity", this_multi)
reader.BookMVA("BDTG method", "TMVARegression_BDTG.weights.xml")

#btag SF calculation
#calib = ROOT.BTagCalibration("csvv2","/uscms_data/d3/cvernier/DiH_13TeV/optimization/Alphabet-76x/CSVv2_subjet.csv")
#readerHF = ROOT.BTagCalibrationReader(calib,0, "lt","central")  # 0 is for loose op
#readerHFup = ROOT.BTagCalibrationReader(calib, 0,"lt", "up")  # 0 is for loose op
#readerHFdown = ROOT.BTagCalibrationReader(calib, 0,"lt", "down")  # 0 is for loose op
#readerLF = ROOT.BTagCalibrationReader(calib,0, "incl","central")  # 0 is for loose op
#readerLFup = ROOT.BTagCalibrationReader(calib, 0,"incl", "up")  # 0 is for loose op
#readerLFdown = ROOT.BTagCalibrationReader(calib, 0,"incl", "down")  # 0 is for loose op
'''
readerHF = ROOT.BTagCalibrationReader(0,"central")  # 0 is for loose op
readerHF.load(calib,0, "lt")
readerHFup = ROOT.BTagCalibrationReader(0,"up")  # 0 is for loose op
readerHFup.load(calib,0,"lt")
readerHFdown = ROOT.BTagCalibrationReader(0,"down")  # 0 is for loose op
readerHFdown.load(calib,0,"lt")
readerLF = ROOT.BTagCalibrationReader(0,"central")  # 0 is for loose op
readerLF.load(calib,0,"incl")
readerLFup = ROOT.BTagCalibrationReader(0,"up")  # 0 is for loose op
readerLFup.load(calib,0,"incl")
readerLFdown = ROOT.BTagCalibrationReader(0,"down")  # 0 is for loose op
readerLFdown.load(calib,0,"incl")
'''
gSystem.Load("DrawFunctions_h.so")

count = 0
#loop over files
for i in range(num1, num2):
    files = Files_list[i]
    print files
    f1 = ROOT.TFile.Open(files, "READ")
    treeMine  = f1.Get('tree')
    nevent = treeMine.GetEntries();
    nFills = 0	

    #getting the norm and other useful histos
    if options.isMC == 'True':
        histo_weight=f1.Get("CountWeighted")
        norm[0]=histo_weight.GetBinContent(1)
	CountMC.Add(f1.Get("Count"))
	CountFullWeightedMC.Add(f1.Get("CountFullWeighted"))
	CountWeightedmc.Add(f1.Get("CountWeighted"))
	CountPosWeightMC.Add(f1.Get("CountPosWeight"))
	CountNegWeightMC.Add(f1.Get("CountNegWeight"))
	CountWeightedLHEWeightScalemc.Add(f1.Get("CountWeightedLHEWeightScale"))
	CountWeightedLHEWeightPdfMC.Add(f1.Get("CountWeightedLHEWeightPdf"))
    else:
        norm[0] = 1
    #loop over events in file
    print "Start looping"
    for j in range(0,nevent):
        treeMine.GetEntry(j)
	count = count + 1
 	if count % 1000 == 0 :
	    print "processing events", count
	
	#variables we need from the heppy ntuple
	fJetPt  = treeMine.Jet_pt
        fJetEta  = treeMine.Jet_eta
        if options.is2p1 == 'True':
            fJetPhi = treeMine.Jet_phi
            fJetMass = treeMine.Jet_mass
            fJetID = treeMine.Jet_id
            if options.isMC == 'True':
                fJetHeppyFlavour = treeMine.Jet_heppyFlavour
                fJetMCflavour = treeMine.Jet_mcFlavour
                fJetPartonFlavour = treeMine.Jet_partonFlavour
                fJetHadronFlavour = treeMine.Jet_hadronFlavour
                fJetCSVLSF = treeMine.Jet_btagCSVL_SF
                fJetCSVLSF_Up = treeMine.Jet_btagCSVL_SF_up
                fJetCSVLSF_Down = treeMine.Jet_btagCSVL_SF_down
                fJetCSVMSF = treeMine.Jet_btagCSVM_SF
                fJetCSVMSF_Up = treeMine.Jet_btagCSVM_SF_up
                fJetCSVMSF_Down = treeMine.Jet_btagCSVM_SF_down
                fJetCSVTSF = treeMine.Jet_btagCSVT_SF
                fJetCSVTSF_Up = treeMine.Jet_btagCSVT_SF_up
                fJetCSVTSF_Down = treeMine.Jet_btagCSVT_SF_down
                fJetCMVALSF = treeMine.Jet_btagCMVAV2L_SF
                fJetCMVALSF_Up = treeMine.Jet_btagCMVAV2L_SF_up
                fJetCMVALSF_Down = treeMine.Jet_btagCMVAV2L_SF_down
                fJetCMVAMSF = treeMine.Jet_btagCMVAV2M_SF
                fJetCMVAMSF_Up = treeMine.Jet_btagCMVAV2M_SF_up
                fJetCMVAMSF_down = treeMine.Jet_btagCMVAV2M_SF_down
                fJetCMVATSF = treeMine.Jet_btagCMVAV2T_SF
                fJetCMVATSF_Up = treeMine.Jet_btagCMVAV2T_SF_up
                fJetCMVATSF_Down = treeMine.Jet_btagCMVAV2T_SF_down
            fJetCSV = treeMine.Jet_btagCSVV0
            fJetCMVA = treeMine.Jet_btagCMVAV2
            fJetCorr = treeMine.Jet_corr
            fJetCorrJECUp = treeMine.Jet_corr_JECUp
            fJetCorrJECDown = treeMine.Jet_corr_JECDown
            if options.isMC == 'True':
                fJetCorrJER = treeMine.Jet_corr_JER
                fJetCorrJERUp = treeMine.Jet_corr_JERUp
                fJetCorrJERDown = treeMine.Jet_corr_JERDown
        fNJets = treeMine.nJet
        nAK04Jets[0] = fNJets
        genPt = treeMine.GenJet_pt
        genEta = treeMine.GenJet_eta
        genPhi = treeMine.GenJet_phi
        genMass = treeMine.GenJet_mass
	htJet30[0] = treeMine.htJet30
        if options.isMC == 'True':
            genBH = treeMine.GenJet_numBHadrons	
            genCH = treeMine.GenJet_numCHadrons
            if len(genBH) > 0:
                genJet1BH[0] = genBH[0]
	    if len(genCH) > 0:
                genjet1CH[0] = genCH[0]
            if len(genBH) > 1:
                genjet2BH[0] = genBH[1]
            if len(genCH) > 1:
                genjet2CH[0] = genCH[1]
	MET[0] = treeMine.met_pt
	fjUngroomedN = treeMine.nFatjetAK08ungroomed
	nAK08Jets[0] = fjUngroomedN
        fjUngroomedPt = treeMine.FatjetAK08ungroomed_pt
	fjUngroomedEta = treeMine.FatjetAK08ungroomed_eta
	fjUngroomedPhi = treeMine.FatjetAK08ungroomed_phi
	fjUngroomedMass = treeMine.FatjetAK08ungroomed_mass
	fjUngroomedSDMass = treeMine.FatjetAK08ungroomed_msoftdrop
	fjUngroomedTau1 = treeMine.FatjetAK08ungroomed_tau1
	fjUngroomedTau2 = treeMine.FatjetAK08ungroomed_tau2
	fjUngroomedBbTag = treeMine.FatjetAK08ungroomed_bbtag
	fjUngroomedJetID = treeMine.FatjetAK08ungroomed_id_Tight
	fjUngroomedPrunedMass = treeMine.FatjetAK08ungroomed_mprunedcorr
        fjUngroomedPrunedMass_Unc = treeMine.FatjetAK08ungroomed_mpruned
        if options.isMC == 'True':
            fjUngroomedFlavour = treeMine.FatjetAK08ungroomed_Flavour
            fjUngroomedBHadron = treeMine.FatjetAK08ungroomed_BhadronFlavour
            fjUngroomedCHadron = treeMine.FatjetAK08ungroomed_ChadronFlavour
            fjUngroomedJER = treeMine.FatjetAK08ungroomed_GenPt
        fjL2L3 = treeMine.FatjetAK08ungroomed_JEC_L2L3
        fjL1L2L3 = treeMine.FatjetAK08ungroomed_JEC_L1L2L3
        if options.isMC == 'True':
            puweight = treeMine.puWeight 
            puweightUp = treeMine.puWeightUp
            puweightDown = treeMine.puWeightDown
	sjPrunedPt = treeMine.SubjetAK08softdrop_pt
	sjPrunedEta = treeMine.SubjetAK08softdrop_eta
	sjPrunedPhi = treeMine.SubjetAK08softdrop_phi
	sjPrunedMass = treeMine.SubjetAK08softdrop_mass
	sjPrunedBtag = treeMine.SubjetAK08softdrop_btag
        if options.isMC == 'True':
            hPt = treeMine.GenHiggsBoson_pt
            hEta = treeMine.GenHiggsBoson_eta
            hPhi = treeMine.GenHiggsBoson_phi
            hMass = treeMine.GenHiggsBoson_mass
        if options.isMC == 'True' and options.saveTrig == 'True':
            HLT_AK8PFJet360_V[0] = treeMine.HLT2_BIT_HLT_AK8PFJet360_TrimMass30_v
            HLT_PFHT350_v[0] = treeMine.HLT2_BIT_HLT_PFHT350_v
            HLT_PFHT400_SixJet30_v[0] = treeMine.HLT2_BIT_HLT_PFHT400_SixJet30_v
            HLT_PFHT450_SixJet40_v[0] = treeMine.HLT2_BIT_HLT_PFHT450_SixJet40_v
            HLT_PFMET120_Mu5_v[0] = treeMine.HLT2_BIT_HLT_PFMET120_Mu5_v
            HLT_PFHT800_v[0] = treeMine.HLT2_BIT_HLT_PFHT800_v
            HLT_PFHT750_4JetPt50_v[0] = treeMine.HLT2_BIT_HLT_PFHT750_4JetPt50_v
            HLT_PFHT350_PFMET100_v[0] = treeMine.HLT2_BIT_HLT_PFHT350_PFMET100_v
            HLT_PFMET170_NoiseCleaned_v[0] = treeMine.HLT2_BIT_HLT_PFMET170_NoiseCleaned_v
            HLT_PFMET120_PFMHT120_IDTight_v[0] = treeMine.HLT2_BIT_HLT_PFMET120_PFMHT120_IDTight_v
            HLT_PFMET110_PFMHT110_IDTight_v[0] = treeMine.HLT2_BIT_HLT_PFMET110_PFMHT110_IDTight_v
            HLT_PFMET100_PFMHT100_IDTight_v[0] = treeMine.HLT2_BIT_HLT_PFMET100_PFMHT100_IDTight_v
            HLT_PFMET90_PFMHT90_IDTight_v[0] = treeMine.HLT2_BIT_HLT_PFMET90_PFMHT90_IDTight_v
            HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v[0] = treeMine.HLT2_BIT_HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v
            HLT_PFHT450_SixJet40_BTagCSV_p056_v[0] = treeMine.HLT2_BIT_HLT_PFHT450_SixJet40_BTagCSV_p056_v
            HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v[0] = treeMine.HLT2_BIT_HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v
            HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT2_BIT_HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v
            HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT2_BIT_HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v
            HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] = treeMine.HLT2_BIT_HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v
            HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] = treeMine.HLT2_BIT_HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v
            HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v[0] = treeMine.HLT2_BIT_HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v
            HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v[0] = treeMine.HLT2_BIT_HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v
            HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v[0] = treeMine.HLT2_BIT_HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v 
            HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v[0] = treeMine.HLT2_BIT_HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v
            HLT_QuadPFJet_VBF_v[0] = treeMine.HLT2_BIT_HLT_QuadPFJet_VBF_v
            HLT_L1_TripleJet_VBF_v[0] = treeMine.HLT2_BIT_HLT_L1_TripleJet_VBF_v
            HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] = treeMine.HLT2_BIT_HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v 
            HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] = treeMine.HLT2_BIT_HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v
            HLT_PFJet40_v[0] = treeMine.HLT2_BIT_HLT_PFJet40_v
            HLT_PFJet60_v[0] = treeMine.HLT2_BIT_HLT_PFJet60_v 
            HLT_PFJet80_v[0] = treeMine.HLT2_BIT_HLT_PFJet80_v
            HLT_PFJet140_v[0] = treeMine.HLT2_BIT_HLT_PFJet140_v
            HLT_PFJet200_v[0] = treeMine.HLT2_BIT_HLT_PFJet200_v
            HLT_PFJet260_v[0] = treeMine.HLT2_BIT_HLT_PFJet260_v 
            HLT_PFJet320_v[0] = treeMine.HLT2_BIT_HLT_PFJet320_v 
            HLT_PFJet400_v[0] = treeMine.HLT2_BIT_HLT_PFJet400_v 
            HLT_PFJet450_v[0] = treeMine.HLT2_BIT_HLT_PFJet450_v 
            HLT_DiPFJetAve40_v[0] = treeMine.HLT2_BIT_HLT_DiPFJetAve40_v 
            HLT_DiPFJetAve60_v[0] = treeMine.HLT2_BIT_HLT_DiPFJetAve60_v
            HLT_DiPFJetAve80_v[0] = treeMine.HLT2_BIT_HLT_DiPFJetAve80_v
            HLT_DiPFJetAve140_v[0] = treeMine.HLT2_BIT_HLT_DiPFJetAve140_v 
            HLT_DiPFJetAve200_v[0] = treeMine.HLT2_BIT_HLT_DiPFJetAve200_v
            HLT_DiPFJetAve260_v[0] = treeMine.HLT2_BIT_HLT_DiPFJetAve260_v
            HLT_DiPFJetAve320_V[0] = treeMine.HLT2_BIT_HLT_DiPFJetAve320_v
            HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v[0] = treeMine.HLT2_BIT_HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v
            HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v[0] = treeMine.HLT2_BIT_HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v
            HLT_QuadJet45_TripleBTagCSV_p087_v[0] = treeMine.HLT2_BIT_HLT_QuadJet45_TripleBTagCSV_p087_v
            HLT_QuadJet45_DoubleBTagCSV_p087_v[0] = treeMine.HLT2_BIT_HLT_QuadJet45_DoubleBTagCSV_p087_v
            HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v[0] = treeMine.HLT2_BIT_HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
            HLT_DoubleJet90_Double30_DoubleBTagCSV_p087_v[0] = treeMine.HLT2_BIT_HLT_DoubleJet90_Double30_DoubleBTagCSV_p087_v
            HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0] = treeMine.HLT2_BIT_HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v
            HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0] = treeMine.HLT2_BIT_HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v
            HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v[0] = treeMine.HLT2_BIT_HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v
            HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT2_BIT_HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v
            HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT2_BIT_HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v
            HLT_Mu20_v[0] = treeMine.HLT2_BIT_HLT_Mu20_v

        elif options.saveTrig == 'True' and options.isMC == 'False':
            HLT_AK8PFJet360_V[0] = treeMine.HLT_BIT_HLT_AK8PFJet360_TrimMass30_v
            HLT_PFHT350_v[0] = treeMine.HLT_BIT_HLT_PFHT350_v
            HLT_PFHT400_SixJet30_v[0] = treeMine.HLT_BIT_HLT_PFHT400_SixJet30_v
            HLT_PFHT450_SixJet40_v[0] = treeMine.HLT_BIT_HLT_PFHT450_SixJet40_v
            HLT_PFMET120_Mu5_v[0] = treeMine.HLT_BIT_HLT_PFMET120_Mu5_v
            HLT_PFHT800_v[0] = treeMine.HLT_BIT_HLT_PFHT800_v
            HLT_PFHT750_4JetPt50_v[0] = treeMine.HLT_BIT_HLT_PFHT750_4JetPt50_v
            HLT_PFHT350_PFMET100_v[0] = treeMine.HLT_BIT_HLT_PFHT350_PFMET100_v
            HLT_PFMET170_NoiseCleaned_v[0] = treeMine.HLT_BIT_HLT_PFMET170_NoiseCleaned_v
            HLT_PFMET120_PFMHT120_IDTight_v[0] = treeMine.HLT_BIT_HLT_PFMET120_PFMHT120_IDTight_v
            HLT_PFMET110_PFMHT110_IDTight_v[0] = treeMine.HLT_BIT_HLT_PFMET110_PFMHT110_IDTight_v
            HLT_PFMET100_PFMHT100_IDTight_v[0] = treeMine.HLT_BIT_HLT_PFMET100_PFMHT100_IDTight_v
            HLT_PFMET90_PFMHT90_IDTight_v[0] = treeMine.HLT_BIT_HLT_PFMET90_PFMHT90_IDTight_v
            HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v[0] = treeMine.HLT_BIT_HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v
            HLT_PFHT450_SixJet40_BTagCSV_p056_v[0] = treeMine.HLT_BIT_HLT_PFHT450_SixJet40_BTagCSV_p056_v
            HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v[0] = treeMine.HLT_BIT_HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v
            HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT_BIT_HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v
            HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT_BIT_HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v
            HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] = treeMine.HLT_BIT_HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v
            HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] = treeMine.HLT_BIT_HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v
            HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v[0] = treeMine.HLT_BIT_HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v
            HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v[0] = treeMine.HLT_BIT_HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v
            HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v[0] = treeMine.HLT_BIT_HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v 
            HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v[0] = treeMine.HLT_BIT_HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v
            HLT_QuadPFJet_VBF_v[0] = treeMine.HLT_BIT_HLT_QuadPFJet_VBF_v
            HLT_L1_TripleJet_VBF_v[0] = treeMine.HLT_BIT_HLT_L1_TripleJet_VBF_v
            HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] = treeMine.HLT_BIT_HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v 
            HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] = treeMine.HLT_BIT_HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v
            HLT_PFJet40_v[0] = treeMine.HLT_BIT_HLT_PFJet40_v
            HLT_PFJet60_v[0] = treeMine.HLT_BIT_HLT_PFJet60_v 
            HLT_PFJet80_v[0] = treeMine.HLT_BIT_HLT_PFJet80_v
            HLT_PFJet140_v[0] = treeMine.HLT_BIT_HLT_PFJet140_v
            HLT_PFJet200_v[0] = treeMine.HLT_BIT_HLT_PFJet200_v
            HLT_PFJet260_v[0] = treeMine.HLT_BIT_HLT_PFJet260_v 
            HLT_PFJet320_v[0] = treeMine.HLT_BIT_HLT_PFJet320_v 
            HLT_PFJet400_v[0] = treeMine.HLT_BIT_HLT_PFJet400_v 
            HLT_PFJet450_v[0] = treeMine.HLT_BIT_HLT_PFJet450_v 
            HLT_DiPFJetAve40_v[0] = treeMine.HLT_BIT_HLT_DiPFJetAve40_v 
            HLT_DiPFJetAve60_v[0] = treeMine.HLT_BIT_HLT_DiPFJetAve60_v
            HLT_DiPFJetAve80_v[0] = treeMine.HLT_BIT_HLT_DiPFJetAve80_v
            HLT_DiPFJetAve140_v[0] = treeMine.HLT_BIT_HLT_DiPFJetAve140_v 
            HLT_DiPFJetAve200_v[0] = treeMine.HLT_BIT_HLT_DiPFJetAve200_v
            HLT_DiPFJetAve260_v[0] = treeMine.HLT_BIT_HLT_DiPFJetAve260_v
            HLT_DiPFJetAve320_V[0] = treeMine.HLT_BIT_HLT_DiPFJetAve320_v
            HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v[0] = treeMine.HLT_BIT_HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v
            HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v[0] = treeMine.HLT_BIT_HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v
            HLT_QuadJet45_TripleBTagCSV_p087_v[0] = treeMine.HLT_BIT_HLT_QuadJet45_TripleBTagCSV_p087_v
            HLT_QuadJet45_DoubleBTagCSV_p087_v[0] = treeMine.HLT_BIT_HLT_QuadJet45_DoubleBTagCSV_p087_v
            HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v[0] = treeMine.HLT_BIT_HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
            HLT_DoubleJet90_Double30_DoubleBTagCSV_p087_v[0] = treeMine.HLT_BIT_HLT_DoubleJet90_Double30_DoubleBTagCSV_p087_v
            HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v[0] = treeMine.HLT_BIT_HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20_v
            HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0] = treeMine.HLT_BIT_HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v
            HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v[0] = treeMine.HLT_BIT_HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v
            HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT_BIT_HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v
            HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT_BIT_HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v
            HLT_Mu20_v[0] = treeMine.HLT_BIT_HLT_Mu20_v
        Data = treeMine.isData
        vType = treeMine.Vtype
        EVT = treeMine.evt 
        if options.isMC == 'True':
            nTInt = treeMine.nTrueInt
        genTopPts = treeMine.GenTop_pt
        JSON = treeMine.json
        
	#saving whether an event passes desired trigger (bb = HT800 pass, sj = pass any of the five saved triggers
        matched = 0
        matchedsj = 0  
        if options.saveTrig == 'True':
            if HLT_PFHT800_v[0] > 0:
                matched += 1
        
            if HLT_PFHT800_v[0] > 0:
                matchedsj += 1
            if HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] > 0:
                matchedsj += 1
            if HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v[0] > 0:
                matchedsj += 1
            if HLT_AK8PFJet360_V[0] > 0:
                matchedsj += 1
            if HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] > 0:
                matchedsj += 1
        triggerpasssj[0] = matchedsj

        triggerpassbb[0] = matched


        #trigger weights
	hT =0
        for i in range(0,fNJets):
                if abs(fJetEta[i])<3 and fJetPt[i] >40 :
                        hT=hT+fJetPt[i]

        ht[0] = hT 
        trigWeight[0] = trigger_function(histo_efficiency, int(round(hT)))
        trigWeightUp[0] = trigger_function(histo_efficiency_up, int(round(hT)))    
        trigWeightDown[0] = trigger_function(histo_efficiency_down, int(round(hT)))    
        trigWeight2Up[0] = trigger_function(histo_efficiency_2up, int(round(hT)))   
        trigWeight2Down[0] = trigger_function(histo_efficiency_2down, int(round(hT)))                    
	 
        #json for data
        bbj.Fill(triggerpassbb[0])
        if Data and treeMine.json < 1:
            continue		
        bb0.Fill(triggerpassbb[0])

        #requiring event pass trigger
#        if options.trigger and triggerpass[0] < 1:
#            continue

        bb1.Fill(triggerpassbb[0])

	#Determining the number of medium working point AK4 btags
	nbtagMWP = 0
	btagCSV = treeMine.Jet_btagCSV
        for i in range(0,fNJets):
		if btagCSV[i] > 0.8:
			nbtagMWP += 1 	
	nAK04btagsMWP[0] = nbtagMWP
	#Calculating DeltaPhi between met for 4 leading pT AK4 jets
	Jet_phi = treeMine.Jet_phi
	met_phi = treeMine.met_phi	
        if fNJets > 0:
		if abs(Jet_phi[0] - met_phi) > 3.14159265359:
			DeltaPhi1[0] = abs(2*3.14159265359 - abs(met_phi - Jet_phi[0]))
		elif abs(Jet_phi[0] - met_phi) < 3.14159265359:
			DeltaPhi1[0] = abs(Jet_phi[0] - met_phi)
        if fNJets > 1:
                if abs(Jet_phi[1] - met_phi) > 3.14159265359:
                        DeltaPhi2[0] = abs(2*3.14159265359 - abs(met_phi - Jet_phi[1]))
                elif abs(Jet_phi[1] - met_phi) < 3.14159265359:
                        DeltaPhi2[0] = abs(Jet_phi[1] - met_phi)
        if fNJets > 2:
                if abs(Jet_phi[2] - met_phi) > 3.14159265359:
                        DeltaPhi3[0] = abs(2*3.14159265359 - abs(met_phi - Jet_phi[2]))
                elif abs(Jet_phi[2] - met_phi) < 3.14159265359:
                        DeltaPhi3[0] = abs(Jet_phi[2] - met_phi)
        if fNJets > 3:
                if abs(Jet_phi[3] - met_phi) > 3.14159265359:
                        DeltaPhi4[0] = abs(2*3.14159265359 - abs(met_phi - Jet_phi[3]))
                elif abs(Jet_phi[3] - met_phi) < 3.14159265359:
                        DeltaPhi4[0] = abs(Jet_phi[3] - met_phi)


	#Determining the number of loose working point muons
	nLooseMuons = 0
	NSelLeptons = treeMine.nselLeptons
	isPFMuon = treeMine.selLeptons_isPFMuon
	isGlobalMuon = treeMine.selLeptons_isGlobalMuon
	isTrackerMuon = treeMine.selLeptons_isTrackerMuon
	#for i in range(0,NSelLeptons):
	#	if isPFMuon[i] == 1:
	#		if isGlobalMuon[i] == 1 or isTrackerMuon[i] == 1:
	#			nLooseMuons += 1

	NAdditLeptons = treeMine.naLeptons
        AdditisPFMuon = treeMine.aLeptons_isPFMuon
        AdditisGlobalMuon = treeMine.aLeptons_isGlobalMuon
        AdditisTrackerMuon = treeMine.aLeptons_isTrackerMuon
        for i in range(0,NAdditLeptons):
                if AdditisPFMuon[i] == 1:
                        if AdditisGlobalMuon[i] == 1 or AdditisTrackerMuon[i] == 1:
                                nLooseMuons += 1

	nLooseMu[0] = nLooseMuons

	#Determining the number of loose working point electrons
	nLooseElectrons = 0
	SetaSc = treeMine.selLeptons_etaSc
	SrelIso03 = treeMine.selLeptons_relIso03
	SeleSieie = treeMine.selLeptons_eleSieie
	SeleDEta = treeMine.selLeptons_eleDEta
	SeleDPhi = treeMine.selLeptons_eleDPhi
	SeleHoE = treeMine.selLeptons_eleHoE
	SeleExpMissingInnerHits = treeMine.selLeptons_eleExpMissingInnerHits
	SeleooEmooP = treeMine.selLeptons_eleooEmooP
	#for i in range(0,NSelLeptons):
	#	if abs(SetaSc[i]) <= 1.479:
	#		if SrelIso03[i] < 0.0994 and SeleSieie[i] < 0.011 and abs(SeleDEta[i]) < 0.00477 and abs(SeleDPhi[i]) < 0.222 and SeleHoE[i] < 0.298 and SeleooEmooP[i] < 0.241 and SeleExpMissingInnerHits[i] <= 1:
#				nLooseElectrons += 1
	#	elif abs(SetaSc[i]) > 1.479:
	#		if SrelIso03[i] < 0.107 and SeleSieie[i] < 0.0314 and abs(SeleDEta[i]) < 0.00868 and abs(SeleDPhi[i]) < 0.213 and SeleHoE[i] < 0.101 and SeleooEmooP[i] < 0.14 and SeleExpMissingInnerHits[i] <= 1:
#				nLooseElectrons += 1

        AetaSc = treeMine.aLeptons_etaSc
        ArelIso03 = treeMine.aLeptons_relIso03
        AeleSieie = treeMine.aLeptons_eleSieie
        AeleDEta = treeMine.aLeptons_eleDEta
        AeleDPhi = treeMine.aLeptons_eleDPhi
        AeleHoE = treeMine.aLeptons_eleHoE
        AeleExpMissingInnerHits = treeMine.aLeptons_eleExpMissingInnerHits
        AeleooEmooP = treeMine.aLeptons_eleooEmooP
        for i in range(0,NAdditLeptons):
                if abs(AetaSc[i]) <= 1.479:
	                if ArelIso03[i] < 0.0994 and AeleSieie[i] < 0.011 and abs(AeleDEta[i]) < 0.00477 and abs(AeleDPhi[i]) < 0.222 and AeleHoE[i] < 0.298 and AeleooEmooP[i] < 0.241 and AeleExpMissingInnerHits[i] <= 1:
                        	nLooseElectrons += 1
                elif abs(AetaSc[i]) > 1.479:
                        if ArelIso03[i] < 0.107 and AeleSieie[i] < 0.0314 and abs(AeleDEta[i]) < 0.00868 and abs(AeleDPhi[i]) < 0.213 and AeleHoE[i] < 0.101 and AeleooEmooP[i] < 0.14 and AeleExpMissingInnerHits[i] <= 1:
                        	nLooseElectrons += 1

	nLooseEle[0] = nLooseElectrons

	#filling an array with jet 4-vectors for jets pt > 30 and |eta| < 2.5, an array of tau21s, and an array of bbtag values, pmass, id, nbhadrons, nchadrons, flavor, l1l2l3 corr, l2l3 corr, JER
        jets = []
	jet_tau = []
	jet_bbtag = []
        jet_pmass = []
        jet_pmassunc = []
        jet_id = []
        jet_nb = []
        jet_nc = []
        jet_flav = []
        jet_123 = []
        jet_23 = []
        jet_JER = []
        jet_mass = []
        jet_eta = []
        jet_muonF= []
        jet_EmF=[]
        jet_HF=[]
        jet_multi=[]

        for j in range(len(fjUngroomedPt)):
            jettemp = ROOT.TLorentzVector()
            jettemp.SetPtEtaPhiM(fjUngroomedPt[j], fjUngroomedEta[j], fjUngroomedPhi[j], fjUngroomedMass[j])
	    if (options.syst=="FJEC_Up"):
                            correction_factor=1+(treeMine.FatjetAK08ungroomed_JEC_UP[j]-treeMine.FatjetAK08ungroomed_JEC_L1L2L3[j])
                            jettemp*=correction_factor
	    if (options.syst=="FJEC_Down"):
                            correction_factor=1-(treeMine.FatjetAK08ungroomed_JEC_UP[j]-treeMine.FatjetAK08ungroomed_JEC_L1L2L3[j])
                            jettemp*=correction_factor
	    if (options.syst=="FJER_Up"):
                            correction_factor=div_except(treeMine.FatjetAK08ungroomed_JER_UP_PT[j],treeMine.FatjetAK08ungroomed_pt[j])
                            jettemp*=correction_factor
	    if (options.syst=="FJER_Down"):
                            pJERDown=2*treeMine.FatjetAK08ungroomed_pt[j]-treeMine.FatjetAK08ungroomed_JER_UP_PT[j]
			    correction_factor=div_except((pJERDown),treeMine.FatjetAK08ungroomed_pt[j])
			    jettemp*=correction_factor
	
	
	    if jettemp.Pt() > 200. and abs(jettemp.Eta()) < 2.4: 	
                    jets.append(jettemp)
		    if fjUngroomedTau1[j] > 0:
			    jet_tau.append(fjUngroomedTau2[j]/fjUngroomedTau1[j])
		    else:
			    jet_tau.append(100)
		    mpruned_syst=fjUngroomedPrunedMass[j]
		    if (options.syst=="MJEC_Down"):
                            sigma=treeMine.FatjetAK08ungroomed_JEC_L2L3_UP[j]-treeMine.FatjetAK08ungroomed_JEC_L2L3[j]
                            mpruned_syst=treeMine.FatjetAK08ungroomed_mpruned[j]*(treeMine.FatjetAK08ungroomed_JEC_L2L3[j]-sigma)
                    if (options.syst=="MJEC_Up"): 
			mpruned_syst=treeMine.FatjetAK08ungroomed_mpruned[j]*treeMine.FatjetAK08ungroomed_JEC_L2L3_UP[j]

		    jet_bbtag.append(fjUngroomedBbTag[j])	
                    jet_pmass.append(mpruned_syst)
                    jet_pmassunc.append(fjUngroomedPrunedMass_Unc[j])
                    jet_id.append(fjUngroomedJetID[j])
                    jet_mass.append(fjUngroomedMass[j])
                    jet_eta.append(treeMine.FatjetAK08ungroomed_eta[j])
                    jet_muonF.append(treeMine.FatjetAK08ungroomed_muonEnergyFraction[j])
                    jet_EmF.append(treeMine.FatjetAK08ungroomed_neutralEmEnergyFraction[j])
                    jet_HF.append(treeMine.FatjetAK08ungroomed_neutralHadronEnergyFraction[j])
                    jet_multi.append(treeMine.FatjetAK08ungroomed_chargedMultiplicity[j])

                    if options.isMC == 'True':
                        jet_nb.append(fjUngroomedBHadron[j])
                        jet_nc.append(fjUngroomedCHadron[j])
                        jet_flav.append(fjUngroomedFlavour[j])
                        jet_JER.append(fjUngroomedJER[j])
                    jet_123.append(fjL1L2L3[j])
                    jet_23.append(fjL2L3[j])
                        
                        
                            
                        
        
	if options.jets == 'True'  and len(jets) < 1: # one jet with pt > 200 and |eta| < 2.4
		continue
        if options.is2p1 == 'False' and options.jets == 'True' and len(jets) < 2: #2 if not 2p1
            continue
        
 
        bb2.Fill(triggerpassbb[0])

	#dEta selection : selecting the two jets which minimizes the dEta requirement. (to find a better one?)
	idxH1 = -1
	idxH2=-1
        if options.is2p1 == 'False' and len(jets) > 1 and (abs(jets[0].Eta() - jets[1].Eta()) < 1.3):
		minDEta = abs(jets[0].Eta() - jets[1].Eta())
		idxH1 = 0
		idxH2 = 1
        if options.is2p1 == 'True' and len(jets) > 1:
            idxH1 = 0
            idxH2 = 1

        if len(jets) == 1:
            idxH1 = 0

	if options.deta and options.is2p1 == 'False' and (idxH1 < 0 or idxH2 <0) : continue
  
        nFills += 1

	#higgs tagging - matching higgs gen jet to the 1 and 2 pt jet
	if options.isMC == 'True':
            hjets = []
            for j in range(len(hPt)):
		jettemp = ROOT.TLorentzVector()
		jettemp.SetPtEtaPhiM(hPt[j], hEta[j], hPhi[j], hMass[j])
		hjets.append(jettemp)

                h1 = MatchCollection(hjets, jets[idxH1])

                if len(jets) > 1: 
                    h2 = MatchCollection(hjets, jets[idxH2])

                nHiggsTags[0] = 0
                if h1 > -1:
                    nHiggsTags[0] += 1
                if len(jets) > 1:
                    if h2 > -1:
                        nHiggsTags[0] += 1
        
        maxcsv1 = -100
        maxcmva1 = -100
	maxcsv2 = -100
	maxcmva2 = -100
        jet1FoundNearby = 0
        jet2FoundNearby = 0
        for j in range(len(treeMine.Jet_pt)):
            jettemp = ROOT.TLorentzVector()
            jettemp.SetPtEtaPhiM(treeMine.Jet_pt[j], treeMine.Jet_eta[j], treeMine.Jet_phi[j], treeMine.Jet_mass[j])
            cmva = treeMine.Jet_btagCMVAV2[j]
            csv = treeMine.Jet_btagCSVV0[j]
            if jets[idxH1].DeltaR(jettemp) > math.pi/2:
                jet1FoundNearby = 1
                if csv > maxcsv1:
                    jet1NearbyJetcsvpt = treeMine.Jet_pt[j]
                    jet1NearbyJetcsveta = treeMine.Jet_eta[j]
                    jet1NearbyJetcsvphi = treeMine.Jet_phi[j]
                    jet1NearbyJetcsvmass = treeMine.Jet_mass[j]
                    jet1NJCSV = csv
                    maxcsv1 = csv
                if cmva > maxcmva1:
                    jet1NearbyJetcmvapt = treeMine.Jet_pt[j]
                    jet1NearbyJetcmvaeta = treeMine.Jet_eta[j]
                    jet1NearbyJetcmvaphi = treeMine.Jet_phi[j]
                    jet1NearbyJetcmvamass = treeMine.Jet_mass[j]
                    jet1NJCMVA = cmva
                    maxcmva1 = cmva
            if len(jets) > 1:
               if jets[idxH2].DeltaR(jettemp) > math.pi/2:
                   jet2FoundNearby = 1
                   if csv > maxcsv2:
                       jet2NearbyJetcsvpt = treeMine.Jet_pt[j]
                       jet2NearbyJetcsveta = treeMine.Jet_eta[j]
                       jet2NearbyJetcsvphi = treeMine.Jet_phi[j]
                       jet2NearbyJetcsvmass = treeMine.Jet_mass[j]
                       jet2NJCSV = csv
                       maxcsv2 = csv
                   if cmva > maxcmva2:
                       jet2NearbyJetcmvapt = treeMine.Jet_pt[j]
                       jet2NearbyJetcmvaeta = treeMine.Jet_eta[j]
                       jet2NearbyJetcmvaphi = treeMine.Jet_phi[j]
                       jet2NearbyJetcmvamass = treeMine.Jet_mass[j]
                       jet2NJCMVA = cmva
                       maxcmva2 = cmva
                
        if jet1FoundNearby == 1:
            jet1NearbyJetcsvArray[0] = jet1NearbyJetcsvpt
            jet1NearbyJetcsvArray[1] = jet1NearbyJetcsveta
            jet1NearbyJetcsvArray[2] = jet1NearbyJetcsvphi
            jet1NearbyJetcsvArray[3] = jet1NearbyJetcsvmass
            jet1NJcsv[0] = jet1NJCSV
            jet1NearbyJetcmvaArray[0] = jet1NearbyJetcmvapt
            jet1NearbyJetcmvaArray[1] = jet1NearbyJetcmvaeta
            jet1NearbyJetcmvaArray[2] = jet1NearbyJetcmvaphi
            jet1NearbyJetcmvaArray[3] = jet1NearbyJetcmvamass
            jet1NJcmva[0] = jet1NJCMVA
        if jet2FoundNearby == 1:
            jet2NearbyJetcsvArray[0] = jet2NearbyJetcsvpt
            jet2NearbyJetcsvArray[1] = jet2NearbyJetcsveta
            jet2NearbyJetcsvArray[2] = jet2NearbyJetcsvphi
            jet2NearbyJetcsvArray[3] = jet2NearbyJetcsvmass
            jet2NJcsv[0] = jet2NJCSV
            jet2NearbyJetcmvaArray[0] = jet2NearbyJetcmvapt
            jet2NearbyJetcmvaArray[1] = jet2NearbyJetcmvaeta
            jet2NearbyJetcmvaArray[2] = jet2NearbyJetcmvaphi
            jet2NearbyJetcmvaArray[3] = jet2NearbyJetcmvamass
            jet2NJcmva[0] = jet2NJCMVA


	#evaluating regressed pt 
	this_pt=jets[idxH1].Pt()
	this_pv= treeMine.nPVs
	this_eta=jet_eta[idxH1]
	this_mass=jet_mass[idxH1]
	this_muonF=jet_muonF[idxH1]
	this_EmF =jet_EmF[idxH1]
	this_HF=jet_HF[idxH1]
	this_multi=jet_multi[idxH1]
	regressedJetpT_0=(reader.EvaluateRegression("BDTG method"))[0]
	this_pt=jets[idxH2].Pt()
        this_eta=jet_eta[idxH2]
        this_mass=jet_mass[idxH2]
        this_muonF=jet_muonF[idxH2]
        this_EmF =jet_EmF[idxH2]
        this_HF=jet_HF[idxH2]
        this_multi=jet_multi[idxH2]
	regressedJetpT_1=(reader.EvaluateRegression("BDTG method"))[0]

            




        #filling jet variables
        jet1pmass[0] = jet_pmass[idxH1]
        jet1pmassunc[0] = jet_pmassunc[idxH1]
        if len(jets) > 1: 
            jet2pmass[0] = jet_pmass[idxH2]
            jet2pmassunc[0] = jet_pmassunc[idxH2]
	jet1ID[0] = jet_id[idxH1]
        if len(jets) > 1: 
            jet2ID[0] = jet_id[idxH2]
	jet1tau21[0] = jet_tau[idxH1]# fjUngroomedTau2[j1]/fjUngroomedTau1[j1]
        if len(jets) > 1: 
            jet2tau21[0] = jet_tau[idxH2]# fjUngroomedTau2[j2]/fjUngroomedTau1[j2]
        if options.isMC == 'True':
            jet1nbHadron[0] = jet_nb[idxH1]
            if len(jets) > 1: 
                jet2nbHadron[0] = jet_nb[idxH2]
            jet1ncHadron[0] = jet_nc[idxH1]
            if len(jets) > 1: 
                jet2ncHadron[0] = jet_nc[idxH2]
            jet1flavor[0] = jet_flav[idxH1]
            if len(jets) > 1: 
                jet2flavor[0] = jet_flav[idxH2]
            jet1JER[0] = jet_JER[idxH1]
            if len(jets) > 1: 
                jet2JER[0] = jet_JER[idxH2]
        jet1l1l2l3[0] = jet_123[idxH1]
        if len(jets) > 1: 
            jet2l1l2l3[0] = jet_123[idxH2]
        jet1l2l3[0] = jet_23[idxH1]
        if len(jets) > 1: 
            jet2l2l3[0] = jet_23[idxH2]

        #finding gen jets to match higgs jets
        if options.isMC == 'True':
            ujets = []
            ujetsCH = []
            ujetsBH = []
            for j in range(len(genPt)):
                jettemp = ROOT.TLorentzVector()
                jettemp.SetPtEtaPhiM(genPt[j], genEta[j], genPhi[j], genMass[j])
                ujets.append(jettemp)
                ujetsCH.append(genCH[j])
                ujetsBH.append(genBH[j])

            j1 = MatchCollection(ujets, jets[idxH1])
            if len(jets) > 1: 
                j2 = MatchCollection2(ujets, jets[idxH2],j1)
           
            #filling gen jet info
            gen1Pt[0] = ujets[j1].Pt()
            gen1phi[0] = ujets[j1].Phi()
            gen1Eta[0] = ujets[j1].Eta()
            gen1Mass[0] = ujets[j1].M()
            gen1ID[0] = j1
            if len(jets) > 1:
                gen2Pt[0] = ujets[j2].Pt()
                gen2Phi[0] = ujets[j2].Phi()
                gen2Eta[0] = ujets[j2].Eta()
                gen2Mass[0] = ujets[j2].M()
                gen2ID[0] = j2

        tPtSums = 0
        if options.isMC == 'True':
            for pt in treeMine.GenTop_pt:
                tPtSums = tPtSums + pt
        tPtsum[0] = tPtSums

	#filling bbtag
	jet1bbtag[0] = jet_bbtag[idxH1] #fjUngroomedBbTag[j1]
	if len(jets) > 1: 
            jet2bbtag[0] = jet_bbtag[idxH2] # fjUngroomedBbTag[j2]

	#filling min subjet csv
	subjets = []
	jet1sj = []
	jet1sjcsv = []
	jet2sj = []
	jet2sjcsv = []
	samesj = 0
        for j in range(len(sjPrunedPt)):
            jettemp = ROOT.TLorentzVector()
            jettemp.SetPtEtaPhiM(sjPrunedPt[j], sjPrunedEta[j], sjPrunedPhi[j], sjPrunedMass[j])
            subjets.append(jettemp)

	n1sj = -100
	n2sj = -100
        if len(jets) == 1:
            for j in range(len(subjets)):
                dR1 = subjets[j].DeltaR(jets[idxH1])
                if dR1 < 0.4:
                    jet1sj.append(subjets[j])
                    jet1sjcsv.append(sjPrunedBtag[j])
                n1sj = len(jet1sj)

        if len(jets) > 1:
            for j in range(len(subjets)): 
                dR1 = subjets[j].DeltaR(jets[idxH1])     
                dR2 = subjets[j].DeltaR(jets[idxH2])
                if dR1 < 0.4 and dR2 < 0.4:
		    samesj += 1
                elif dR1 < 0.4:
		    jet1sj.append(subjets[j])
		    jet1sjcsv.append(sjPrunedBtag[j])
                elif dR2 < 0.4:
		    jet2sj.append(subjets[j])
		    jet2sjcsv.append(sjPrunedBtag[j])
                n1sj = len(jet1sj)
                n2sj = len(jet2sj) 

	#Finding the subjet csvs
	jet1s1csv[0] = -1.
	jet2s1csv[0] = -1.
        jet1s2csv[0] = -1.
	jet2s2csv[0] = -1.
	
	for i in range(0,4):
	  jetSJfla[i] =-1
	  jetSJpt[i]  =-1
	  jetSJcsv[i] =-1
	  jetSJeta[i] =-1

        
        if len(jet1sjcsv) > 1:
            jet1s1csv[0] = jet1sjcsv[0]
            jet1s2csv[0] = jet1sjcsv[1]
        elif len(jet1sjcsv) == 1:
            jet1s1csv[0] = jet1sjcsv[0]

        if len(jet2sjcsv) > 1:
            jet2s1csv[0] = jet2sjcsv[0]
            jet2s2csv[0] = jet2sjcsv[1]
        elif len(jet2sjcsv) == 1:
            jet2s1csv[0] = jet2sjcsv[0]
        sfsj3 =-1
        sfsj4 =-1
	sfsj1 =-1
        sfsj2 =-1	
	sfsj3up =-1
        sfsj4up =-1
        sfsj1up =-1
        sfsj2up =-1
	sfsj3down =-1
        sfsj4down =-1
        sfsj1down =-1
        sfsj2down =-1
        #finding gen jets for subjets
        '''
        if options.isMC == 'True' and options.is2p1 == 'False':
            if len(jet1sjcsv) > 1:
                sj1gen = MatchCollection(ujets, jet1sj[0])
                sj2gen = MatchCollection2(ujets, jet1sj[1],sj1gen)
		isL = False
		isL2 = False
                if sj1gen>0 and ujetsBH[sj1gen]>0 :
                    sj1flav = BTagEntry.FLAV_B
		    jetSJfla[0] = 1
		    jetSJpt[0] = jet1sj[0].Pt()
        	    jetSJcsv[0] = jet1sjcsv[0]
                    jetSJeta[0] = jet1sj[0].Eta()
                elif ujetsCH[sj1gen]>0 and sj1gen>0:
                    sj1flav = BTagEntry.FLAV_C
                else:
		    isL= True 
		    sj1flav = BTagEntry.FLAV_UDSG	
                if  ujetsBH[sj2gen]>0 and sj2gen>0:
                    sj2flav = BTagEntry.FLAV_B
		    jetSJpt[1] = jet1sj[1].Pt()
           	    jetSJeta[1] = jet1sj[1].Eta()
                    jetSJcsv[1] = jet1sjcsv[1]
		    jetSJfla[1] = 1
                elif ujetsCH[sj2gen]>0 and sj2gen>0:
                    sj2flav = BTagEntry.FLAV_C
                else:
		    sj2flav = BTagEntry.FLAV_UDSG
		    isL2 = True
	   #compute SF
	        if not isL:	
	         if(jet1sj[0].Pt()<670. and abs(jet1sj[0].Eta())<2.4 ) :

                  sfsj1 = readerHF.eval(sj1flav, jet1sj[0].Eta(), jet1sj[0].Pt())  # jet flavor, eta, pt
		  sfsj1up = readerHFup.eval(sj1flav, jet1sj[0].Eta(), jet1sj[0].Pt()) 
		  sfsj1down = readerHFdown.eval(sj1flav, jet1sj[0].Eta(), jet1sj[0].Pt())
		 elif abs(jet1sj[0].Eta())>2.4:
		  sfsj1 = readerHF.eval(sj1flav, 2.399, jet1sj[0].Pt()) 
		  sfsj1up = readerHFup.eval(sj1flav, 2.399, jet1sj[0].Pt())	
		  sfsj1down = readerHFdown.eval(sj1flav, 2.399, jet1sj[0].Pt())
		 elif jet1sj[0].Pt()>670.:
		  sfsj1 = readerHF.eval(sj1flav, jet1sj[0].Eta(), 669.)   
		  sfsj1up = readerHFup.eval(sj1flav, jet1sj[0].Eta(), 669.)
		  sfsj1down = readerHFdown.eval(sj1flav, jet1sj[0].Eta(), 669.)
		else:
		 if(jet1sj[0].Pt()<670. and abs(jet1sj[0].Eta())<2.4 ) :
                  sfsj1 = readerLF.eval(sj1flav, jet1sj[0].Eta(), jet1sj[0].Pt())  # jet flavor, eta, pt
                  sfsj1up = readerLFup.eval(sj1flav, jet1sj[0].Eta(), jet1sj[0].Pt())
                  sfsj1down = readerLFdown.eval(sj1flav, jet1sj[0].Eta(), jet1sj[0].Pt())
                 elif abs(jet1sj[0].Eta())>2.4:
                  sfsj1 = readerLF.eval(sj1flav, 2.399, jet1sj[0].Pt())
                  sfsj1up = readerLFup.eval(sj1flav, 2.399, jet1sj[0].Pt())
                  sfsj1down = readerLFdown.eval(sj1flav, 2.399, jet1sj[0].Pt())
                 elif jet1sj[0].Pt()>670.:
                  sfsj1 = readerLF.eval(sj1flav, jet1sj[0].Eta(), 669.)
                  sfsj1up = readerLFup.eval(sj1flav, jet1sj[0].Eta(), 669.)
                  sfsj1down = readerLFdown.eval(sj1flav, jet1sj[0].Eta(), 669.)
		if not isL2:
		 if(jet1sj[1].Pt()<670. and abs(jet1sj[1].Eta())<2.4 ) :
                  sfsj2 = readerHF.eval(sj2flav, jet1sj[1].Eta(), jet1sj[1].Pt())  # jet flavor, eta, pt
                  sfsj2up = readerHFup.eval(sj2flav, jet1sj[1].Eta(), jet1sj[1].Pt())
                  sfsj2down = readerHFdown.eval(sj2flav, jet1sj[1].Eta(), jet1sj[1].Pt())
                 elif abs(jet1sj[1].Eta())>2.4:
                  sfsj2 = readerHF.eval(sj2flav, 2.399, jet1sj[1].Pt())
                  sfsj2up = readerHFup.eval(sj2flav, 2.399, jet1sj[1].Pt())
                  sfsj2down = readerHFdown.eval(sj2flav, 2.399, jet1sj[1].Pt())
                 elif jet1sj[1].Pt()>670.:
                  sfsj2 = readerHF.eval(sj2flav, jet1sj[1].Eta(), 669.)
                  sfsj2up = readerHFup.eval(sj2flav, jet1sj[1].Eta(), 669.)
                  sfsj2down = readerHFdown.eval(sj2flav, jet1sj[1].Eta(), 669.)
	        else:	
		 if(jet1sj[1].Pt()<670. and abs(jet1sj[1].Eta())<2.4 ) :
                  sfsj2 = readerLF.eval(sj2flav, jet1sj[1].Eta(), jet1sj[1].Pt())  # jet flavor, eta, pt
                  sfsj2up = readerLFup.eval(sj2flav, jet1sj[1].Eta(), jet1sj[1].Pt())
                  sfsj2down = readerLFdown.eval(sj2flav, jet1sj[1].Eta(), jet1sj[1].Pt())
                 elif abs(jet1sj[1].Eta())>2.4:
                  sfsj2 = readerLF.eval(sj2flav, 2.399, jet1sj[1].Pt())
                  sfsj2up = readerLFup.eval(sj2flav, 2.399, jet1sj[1].Pt())
                  sfsj2down = readerLFdown.eval(sj2flav, 2.399, jet1sj[1].Pt())
                 elif jet1sj[1].Pt()>670.:
                  sfsj2 = readerLF.eval(sj2flav, jet1sj[1].Eta(), 669.)
                  sfsj2up = readerLFup.eval(sj2flav, jet1sj[1].Eta(), 669.)
                  sfsj2down = readerLFdown.eval(sj2flav, jet1sj[1].Eta(), 669.)
	    
	    if len(jet2sjcsv) > 1:
                sj3gen = MatchCollection(ujets, jet2sj[0])
                sj4gen = MatchCollection2(ujets, jet2sj[1],sj3gen)
		isL = False
                isL2 = False
                if  ujetsBH[sj3gen]>0 and sj3gen>0.:
                    sj3flav = BTagEntry.FLAV_B
		    jetSJpt[2] = jet2sj[0].Pt()
                    jetSJeta[2] = jet2sj[0].Eta()
                    jetSJcsv[2] = jet2sjcsv[0]
		    jetSJfla[2] = 1
                elif ujetsCH[sj3gen]>0 and sj3gen>0.:
                    sj3flav = BTagEntry.FLAV_C
                else:
                    sj3flav = BTagEntry.FLAV_UDSG
	 	    isL = True
                if  ujetsBH[sj4gen]>0 and sj4gen>0.:
                    sj4flav = BTagEntry.FLAV_B
		    jetSJpt[3] = jet2sj[1].Pt()
                    jetSJeta[3] = jet2sj[1].Eta()
                    jetSJcsv[3] = jet2sjcsv[1]
                    jetSJfla[3] = 1
                elif ujetsCH[sj4gen]>0 and sj4gen>0.:
                    sj4flav = BTagEntry.FLAV_C
                else:
                    sj4flav = BTagEntry.FLAV_UDSG
		    isL2 = True
           #compute SF
		if not isL:
                 if(jet2sj[0].Pt()<670. and abs(jet2sj[0].Eta())<2.4 ) :
                  sfsj3 = readerHF.eval(sj3flav, jet2sj[0].Eta(), jet2sj[0].Pt())  # jet flavor, eta, pt
                  sfsj3up = readerHFup.eval(sj3flav, jet2sj[0].Eta(), jet2sj[0].Pt())
                  sfsj3down = readerHFdown.eval(sj3flav, jet2sj[0].Eta(), jet2sj[0].Pt())
                 elif abs(jet2sj[0].Eta())>2.4:
                  sfsj3 = readerHF.eval(sj3flav, 2.399, jet2sj[0].Pt())
                  sfsj3up = readerHFup.eval(sj3flav, 2.399, jet2sj[0].Pt())
                  sfsj3down = readerHFdown.eval(sj3flav, 2.399, jet2sj[0].Pt())
                 elif jet2sj[0].Pt()>670.:
                  sfsj3 = readerHF.eval(sj3flav, jet2sj[0].Eta(), 669.)
                  sfsj3up = readerHFup.eval(sj3flav, jet2sj[0].Eta(), 669.)
                  sfsj3down = readerHFdown.eval(sj3flav, jet2sj[0].Eta(), 669.)
		else:
		 if(jet2sj[0].Pt()<670. and abs(jet2sj[0].Eta())<2.4 ) :
                  sfsj3 = readerLF.eval(sj3flav, jet2sj[0].Eta(), jet2sj[0].Pt())  # jet flavor, eta, pt
                  sfsj3up = readerLFup.eval(sj3flav, jet2sj[0].Eta(), jet2sj[0].Pt())
                  sfsj3down = readerLFdown.eval(sj3flav, jet2sj[0].Eta(), jet2sj[0].Pt())
                 elif abs(jet2sj[0].Eta())>2.4:
                  sfsj3 = readerLF.eval(sj3flav, 2.399, jet2sj[0].Pt())
                  sfsj3up = readerLFup.eval(sj3flav, 2.399, jet2sj[0].Pt())
                  sfsj3down = readerLFdown.eval(sj3flav, 2.399, jet2sj[0].Pt())
                 elif jet2sj[0].Pt()>670.:
                  sfsj3 = readerLF.eval(sj3flav, jet2sj[0].Eta(), 669.)
                  sfsj3up = readerLFup.eval(sj3flav, jet2sj[0].Eta(), 669.)
                  sfsj3down = readerLFdown.eval(sj3flav, jet2sj[0].Eta(), 669.)
		if not isL2:
                 if(jet2sj[1].Pt()<670. and abs(jet2sj[1].Eta())<2.4 ) :
                  sfsj4 = readerHF.eval(sj4flav, jet2sj[1].Eta(), jet2sj[1].Pt())  # jet flavor, eta, pt
                  sfsj4up = readerHFup.eval(sj4flav, jet2sj[1].Eta(), jet2sj[1].Pt())
                  sfsj4down = readerHFdown.eval(sj4flav, jet2sj[1].Eta(), jet2sj[1].Pt())
                 elif abs(jet2sj[1].Eta())>2.4:
                  sfsj4 = readerHF.eval(sj4flav, 2.399, jet2sj[1].Pt())
                  sfsj4up = readerHFup.eval(sj4flav, 2.399, jet2sj[1].Pt())
                  sfsj4down = readerHFdown.eval(sj4flav, 2.399, jet2sj[1].Pt())
                 elif jet2sj[1].Pt()>670.:
                  sfsj4 = readerHF.eval(sj4flav, jet2sj[1].Eta(), 669.)
                  sfsj4up = readerHFup.eval(sj4flav, jet2sj[1].Eta(), 669.)
                  sfsj4down = readerHFdown.eval(sj4flav, jet2sj[1].Eta(), 669.)
		else:
		 if(jet2sj[1].Pt()<670. and abs(jet2sj[1].Eta())<2.4 ) :
                  sfsj4 = readerLF.eval(sj4flav, jet2sj[1].Eta(), jet2sj[1].Pt())  # jet flavor, eta, pt
                  sfsj4up = readerLFup.eval(sj4flav, jet2sj[1].Eta(), jet2sj[1].Pt())
                  sfsj4down = readerLFdown.eval(sj4flav, jet2sj[1].Eta(), jet2sj[1].Pt())
                 elif abs(jet2sj[1].Eta())>2.4:
                  sfsj4 = readerLF.eval(sj4flav, 2.399, jet2sj[1].Pt())
                  sfsj4up = readerLFup.eval(sj4flav, 2.399, jet2sj[1].Pt())
                  sfsj4down = readerLFdown.eval(sj4flav, 2.399, jet2sj[1].Pt())
                 elif jet2sj[1].Pt()>670.:
                  sfsj4 = readerLF.eval(sj4flav, jet2sj[1].Eta(), 669.)
                  sfsj4up = readerLFup.eval(sj4flav, jet2sj[1].Eta(), 669.)
                  sfsj4down = readerLFdown.eval(sj4flav, jet2sj[1].Eta(), 669.)
            
                #sfsj2 = reader.eval(sj2flav, jet1sj[1].Eta(), jet1sj[1].Pt())
#                print "SF " + str(sfsj1) + " for flavor " + str(sj1flav) + " for eta " + str(jet1sj[0].Eta()) + " for pt " + str(jet1sj[0].Pt())
'''

        #for min subjet csv
#	for j in range(len(jet1sjcsv)):
#     	    if jet1sjcsv[j] < jet1mscsv[0]:
#		    jet1mscsv[0] = jet1sjcsv[j]
#	for j in range(len(jet2sjcsv)):
#	    if jet2sjcsv[j] < jet2mscsv[0]:
#		    jet2mscsv[0] = jet2sjcsv[j]
	
	#filling bbtag
#	jet1bbtag[0] = jet_bbtag[idxH1]
#        if len(jets) > 1:
#            jet2bbtag[0] = jet_bbtag[idxH2]
	
        #writing variables to the tree    
	jet1pt[0] = jets[idxH1].Pt()
	jet1eta[0] = jets[idxH1].Eta()
        jet1phi[0] = jets[idxH1].Phi()
        jet1mass[0] = jets[idxH1].M()
	jet1_reg =ROOT.TLorentzVector()
	jet1_reg.SetPtEtaPhiM(jet1pt[0],jet1eta[0],jet1phi[0],jet1mass[0])
	jet1_reg=jet1_reg*(regressedJetpT_0)
	jet1pt_reg[0] = jet1_reg.Pt()
	jet1_ureg =ROOT.TLorentzVector()
	jet1_ureg.SetPtEtaPhiM(jet1pt[0],jet1eta[0],jet1phi[0],jet1_reg.M())

        if len(jets) > 1:
            jet2pt[0] = jets[idxH2].Pt()
            jet2eta[0] = jets[idxH2].Eta()
            jet2phi[0] = jets[idxH2].Phi()
            jet2mass[0] = jets[idxH2].M()
	    jet2_reg =ROOT.TLorentzVector()
	    jet2_reg.SetPtEtaPhiM(jet2pt[0],jet2eta[0],jet2phi[0],jet2mass[0])
            jet2_reg=jet2_reg*(regressedJetpT_1)
	    jet2_ureg =ROOT.TLorentzVector()
	    jet2_ureg.SetPtEtaPhiM(jet2pt[0],jet2eta[0],jet2phi[0],jet2_reg.M())
            etadiff[0] = abs(jets[idxH1].Eta() - jets[idxH2].Eta())
            dijetmass[0] = (jets[idxH1] + jets[idxH2]).M()
            dijetmass_corr[0] = (jets[idxH1] + jets[idxH2]).M() - (jet1mass[0]-125)-(jet2mass[0]-125)
            dijetmass_corr_punc[0] = (jets[idxH1] + jets[idxH2]).M() - (jet1pmassunc[0]-125)-(jet2pmassunc[0]-125)
            dijetmass_reg[0]=(jet1_ureg+jet2_ureg).M()- (jet1_ureg.M()-125)-(jet2_ureg.M()-125)
        if options.isMC == 'True':
            puWeights[0]= puweight
            puWeightsUp[0] = puweightUp
            puWeightsDown[0] = puweightDown
            nTrueInt[0] = nTInt 
            xsec[0] = float(options.xsec)
        json[0] = JSON
        evt[0] = EVT
        vtype[0] = vType
        if Data:
            isData[0] = 1
        else:
            isData[0] = 0

        #handling hbb tagger SFs
        sf1 = -1
        sf2 = -1
        sf1change = 1000000
        sf2change = 1000000

        if jet1pt[0] < 400:
            sf1 = 0.929
            sf1change = 0.078
        elif jet1pt[0] >= 400 and jet1pt[0] < 500:
            sf1 = 0.999
            sf1change = 0.126
        elif jet1pt[0] >= 500 and jet1pt[0] < 600:
            sf1 = 0.933
            sf1change = 0.195
        elif jet1pt[0] >= 600:
            sf1 = 1.048
            sf1change = 0.215
        
        if len(jets) > 1:
            if jet2pt[0] < 400:
                sf2 = 0.929
                sf2change = 0.078
            elif jet2pt[0] >= 400 and jet2pt[0] < 500:
                sf2 = 0.999
                sf2change = 0.126
            elif jet2pt[0] >= 500 and jet2pt[0] < 600:
                sf2 = 0.933
                sf2change = 0.195
            elif jet2pt[0] >= 600:
                sf2 = 1.048
                sf2change = 0.215
        
        if options.is2p1 == 'True':
            bbtag1SF[0] = sf1
            bbtag1SFUp[0] = sf1*(1+sf1change)
            bbtag1SFDown[0] = sf1*(1-sf1change)
        else:
            SF[0] = sf1*sf2
            SFup[0] = sf1*(1+sf1change)*sf2*(1+sf2change)
            SFdown[0] = sf1*(1-sf1change)*sf2*(1-sf2change)

        if options.is2p1 == 'False':
            SF4sj[0] = -1
            SF4sjUp[0] = -1
            SF4sjDown[0] = -1	
            if n1sj >1 and n2sj>1:
                SF4sj[0] = sfsj1*sfsj2*sfsj3*sfsj4
                SF4sjUp[0] = sfsj1up*sfsj2up*sfsj3up*sfsj4up 	
                SF4sjDown[0] = sfsj1down*sfsj2down*sfsj3down*sfsj4down  
                
            SF3sj[0] =-1.
            SF3sjUp[0] =-1.
            SF3sjDown[0] =-1.
	#3b-tag category
	#SF=[((1-SF1e1))/(1-e1)]*SF2*SF3*SF4
	#e1 estimated in HH signal sample to be 
            '''	
            if (jet1s1csv[0] >0.460 and jet2s1csv[0] >0.460  and jet1s2csv[0] >0.460 and jet2s2csv[0] < 0.460 ) or (jet1s1csv[0] >0.460 and jet2s1csv[0] >0.460  and jet1s2csv[0] <0.460 and jet2s2csv[0] > 0.460 ) or (jet1s1csv[0] >0.460 and jet2s1csv[0] <0.460  and jet1s2csv[0] >0.460 and jet2s2csv[0] > 0.460 ) or (jet1s1csv[0] <0.460 and jet2s1csv[0] > 0.460  and jet1s2csv[0] >0.460 and jet2s2csv[0] > 0.460 ):
               if n1sj >1 and n2sj>1:
                 if(jet1s1csv[0] >0.460) :
                    SF3sj[0] *= sfsj1
                    SF3sjUp[0] *= sfsj1up
                    SF3sjDown[0] *= sfsj1down
                 else : 
	            SF3sj[0] *= (1-sfsj1*btagging_efficiency_medium(jet1sj[0].Pt()))/(1-btagging_efficiency_medium(jet1sj[0].Pt()))
                    SF3sjUp[0] *= (1-sfsj1up*btagging_efficiency_medium(jet1sj[0].Pt()))/(1-btagging_efficiency_medium(jet1sj[0].Pt()))
                    SF3sjDown[0] *= (1-sfsj1down*btagging_efficiency_medium(jet1sj[0].Pt()))/(1-btagging_efficiency_medium(jet1sj[0].Pt()))
                 if(jet1s2csv[0] >0.460) :
                    SF3sj[0] *= sfsj2
                    SF3sjUp[0] *= sfsj2up
                    SF3sjDown[0] *= sfsj2down
                 else :
                    SF3sj[0] *= (1-sfsj2*btagging_efficiency_medium(jet1sj[1].Pt()))/(1-btagging_efficiency_medium(jet1sj[1].Pt()))
                    SF3sjUp[0] *= (1-sfsj2up*btagging_efficiency_medium(jet1sj[1].Pt()))/(1-btagging_efficiency_medium(jet1sj[1].Pt()))
                    SF3sjDown[0] *= (1-sfsj2down*btagging_efficiency_medium(jet1sj[1].Pt()))/(1-btagging_efficiency_medium(jet1sj[1].Pt()))

                 if(jet2s1csv[0] >0.460) :
                    SF3sj[0] *= sfsj3
                    SF3sjUp[0] *= sfsj3up
                    SF3sjDown[0] *= sfsj3down
                 else:
                    SF3sj[0] *= (1-sfsj3*btagging_efficiency_medium(jet2sj[0].Pt()))/(1-btagging_efficiency_medium(jet2sj[0].Pt()))
                    SF3sjUp[0] *= (1-sfsj3up*btagging_efficiency_medium(jet2sj[0].Pt()))/(1-btagging_efficiency_medium(jet2sj[0].Pt()))
                    SF3sjDown[0] *= (1-sfsj3down*btagging_efficiency_medium(jet2sj[0].Pt()))/(1-btagging_efficiency_medium(jet2sj[0].Pt()))
                 if(jet2s2csv[0] >0.460) :
                    SF3sj[0] *= sfsj4
                    SF3sjUp[0] *= sfsj4up
                    SF3sjDown[0] *= sfsj4down
                 else:
                    SF3sj[0] *= (1-sfsj4*btagging_efficiency_medium(jet2sj[1].Pt()))/(1-btagging_efficiency_medium(jet2sj[1].Pt()))
                    SF3sjUp[0] *= (1-sfsj4up*btagging_efficiency_medium(jet2sj[1].Pt()))/(1-btagging_efficiency_medium(jet2sj[1].Pt()))
                    SF3sjDown[0] *= (1-sfsj4down*btagging_efficiency_medium(jet2sj[1].Pt()))/(1-btagging_efficiency_medium(jet2sj[1].Pt()))
	
	    if SF3sj[0] <0. : SF3sj[0] = -SF3sj[0]
	    if SF3sjUp[0] <0. : SF3sjUp[0] = -SF3sjUp[0]
	    if SF3sjDown[0] <0. : SF3sjDown[0] = -SF3sjDown[0]	
  	    '''
        if options.is2p1 == 'True':
            if len(jets) > 1:
                if jets[1].Pt() < 400:
                    sf2 = 0.929
                    sf2change = 0.078
                elif jets[1].Pt() >= 400 and jets[1].Pt() < 500:
                    sf2 = 0.999
                    sf2change = 0.126
                elif jets[1].Pt() >= 500 and jets[1].Pt() < 600:
                    sf2 = 0.933
                    sf2change = 0.195
                elif jets[1].Pt() >= 600:
                    sf2 = 1.048
                    sf2change = 0.215

                bbtag2SF[0] = sf2
                bbtag2SFUp[0] = sf2*(1+sf2change)
                bbtag2SFDown[0] = sf2*(1-sf2change)


            if len(jets) > 1 and jets[0].Pt() > 300 and jets[1].Pt() > 300 and abs(jets[0].Eta() - jets[1].Eta()) < 1.3 and ((jets[idxH1] + jets[idxH2]).M() - (jet1pmass[0]-125)-(jet2pmass[0]-125)) > 800 and jet1tau21[0] < 0.6 and jet2tau21[0] < 0.6 and jet1pmass[0] > 105 and jet1pmass[0] < 135 and jet2pmass[0] > 105 and jet2pmass[0] < 135 and jet1bbtag[0] > 0.6 and jet2bbtag[0] > 0.6:
                passesBoosted[0] = 1
            else:
                passesBoosted[0] = 0

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
                
        #ak4 jets
            akjets = [] 
            for j in range(len(fJetPt)):
                if (options.syst=="JEC_Up"): jet_pT = treeMine.Jet_pt[j]*treeMine.Jet_corr_JECUp[j]/treeMine.Jet_corr[j]
                elif (options.syst=="JEC_Down"): jet_pT = treeMine.Jet_pt[j]*treeMine.Jet_corr_JECDown[j]/treeMine.Jet_corr[j]
                elif (options.syst=="JER_Up"): jet_pT = treeMine.Jet_pt[j]*treeMine.Jet_corr_JERUp[j]*treeMine.Jet_corr_JER[j]
                elif (options.syst=="JER_Down"): jet_pT = treeMine.Jet_pt[j]*treeMine.Jet_corr_JERDown[j]*treeMine.Jet_corr_JER[j]
                else: jet_pT = treeMine.Jet_pt[j]
                jettemp = ROOT.TLorentzVector()
                jettemp.SetPtEtaPhiM(jet_pT, fJetEta[j], fJetPhi[j], fJetMass[j])
                if abs(jettemp.Eta()) < 2.4 and jet_pT > 30:     
                    akjets.append(jettemp)
                    ak4jet_pt.push_back(jet_pT)
                    ak4jet_eta.push_back(fJetEta[j])
                    ak4jet_phi.push_back(fJetPhi[j])
                    ak4jet_mass.push_back(fJetMass[j])
                    ak4jetID.push_back(fJetID[j])
                    if options.isMC == 'True':
                        ak4jetHeppyFlavour.push_back(fJetHeppyFlavour[j])
                        ak4jetMCflavour.push_back(fJetMCflavour[j])
                        ak4jetPartonFlavour.push_back(fJetPartonFlavour[j]) 
                        ak4jetHadronFlavour.push_back(fJetHadronFlavour[j])
                        ak4jetCSVLSF.push_back(fJetCSVLSF[j])
                        ak4jetCSVLSF_Up.push_back(fJetCSVLSF_Up[j])
                        ak4jetCSVLSF_Down.push_back(fJetCSVLSF_Down[j])
                        ak4jetCSVMSF.push_back(fJetCSVMSF[j])
                        ak4jetCSVMSF_up.push_back(fJetCSVMSF_Up[j])
                        ak4jetCSVMSF_Down.push_back(fJetCSVMSF_Down[j])
                        ak4jetCSVTSF.push_back(fJetCSVTSF[j])
                        ak4jetCSVTSF_Up.push_back(fJetCSVTSF_Up[j])
                        ak4jetCSVTSF_Down.push_back(fJetCSVTSF_Down[j])
                        ak4jetCMVALSF.push_back(fJetCMVALSF[j])
                        ak4jetCMVALSF_Up.push_back(fJetCMVALSF_Up[j])
                        ak4jetCMVALSF_Down.push_back(fJetCMVALSF_Down[j])
                        ak4jetCMVAMSF.push_back(fJetCMVAMSF[j])
                        ak4jetCMVAMSF_Up.push_back(fJetCMVAMSF_Up[j])
                        ak4jetCMVAMSF_Down.push_back(fJetCMVAMSF_down[j])
                        ak4jetCMVATSF.push_back(fJetCMVATSF[j])
                        ak4jetCMVATSF_Up.push_back(fJetCMVATSF_Up[j])
                        ak4jetCMVATSF_Down.push_back(fJetCMVATSF_Down[j])
                        ak4jetCorr.push_back(fJetCorr[j])
                        ak4jetCorrJECUp.push_back(fJetCorrJECUp[j])
                        ak4jetCorrJECDown.push_back(fJetCorrJECDown[j])
                        ak4jetCorrJER.push_back(fJetCorrJER[j])
                        ak4jetCorrJERUp.push_back(fJetCorrJERUp[j])
                        ak4jetCorrJERDown.push_back(fJetCorrJERDown[j])
                    ak4jetCSV.push_back(fJetCSV[j])
                    ak4jetCMVA.push_back(fJetCMVA[j])

                    if options.isMC == 'True':
                        akj = MatchCollection(ujets, jettemp)
                        ak4genJetPt.push_back(ujets[akj].Pt())
                        ak4genJetEta.push_back(ujets[akj].Eta())
                        ak4genJetPhi.push_back(ujets[akj].Phi())
                        ak4genJetMass.push_back(ujets[akj].M())
                        ak4genJetID.push_back(akj)
        
            if options.jets == 'True' and len(ak4jet_pt) < 2:        
                continue

        #resolved
            ak4res = []
            chi2_old=200
            foundRes = False
            passesResolved[0] = 0
            for j in range(len(akjets)):
                if ak4jetCMVA[j] > 0.185:
                    ak4res.append(akjets[j])
            if len(ak4res) > 3:
                jet1=TLorentzVector()
                jet2=TLorentzVector()
                jet3=TLorentzVector()    
                jet4=TLorentzVector()
                for l in range(len(ak4res)):
                    jet1.SetPtEtaPhiM(ak4res[l].Pt(), ak4res[l].Eta(), ak4res[l].Phi(), ak4res[l].M())
                    for m in range(len(ak4res)):
                        if m!=l:
                            jet2.SetPtEtaPhiM(ak4res[m].Pt(), ak4res[m].Eta(), ak4res[m].Phi(),ak4res[m].M())
                            for n in range(len(ak4res)):
                                if (n!=l and n!=m):
                                    jet3.SetPtEtaPhiM(ak4res[n].Pt(), ak4res[n].Eta(), ak4res[n].Phi(),ak4res[n].M())
                                    for k in range(len(ak4res)):
                                        if (k!=l and k!=m and k!=n):
                                            jet4.SetPtEtaPhiM(ak4res[k].Pt(), ak4res[k].Eta(), ak4res[k].Phi(),ak4res[k].M())

                                            dijet1=jet1+jet2
                                            dijet2=jet3+jet4
                                        
                                            deltar1=jet1.DeltaR(jet2)
                                            deltar2=jet3.DeltaR(jet4)
                                        
                                            mH1=dijet1.M()
                                            mH2=dijet2.M()
                                            
                                            chi2=((mH1-115)/23)**2+((mH2-115)/23)**2
                                        
                                            if (chi2<chi2_old and deltar1<1.5 and deltar2<1.5):
                                                chi2_old=chi2
                                                foundRes=True

            if foundRes:
                chi=chi2_old**0.5
                if chi<=1:
                    passesResolved[0] = 1

        bb3.Fill(triggerpassbb[0])
	#filling the tree
        myTree.Fill()
	
	#filling error values for each object
        if options.isMC == 'True':
       #     genjet1BH[0] = -100.0
            genjet2BH[0] = -100.0
            genjet1CH[0] = -100.0
            genjet2CH[0] = -100.0
	htJet30[0] = -100.0
	jet1pt[0] = -100.0
	jet2pt[0] = -100.0
        jet1pt_reg[0] = -100.0
        jet2pt_reg[0] = -100.0
	jet1eta[0] = -100.0
	jet2eta[0] = -100.0
	etadiff[0] = -100.0
	dijetmass[0] = -100.0
	dijetmass_corr[0]=-100.0
        dijetmass_reg[0]=-100.0
	jet1pmass[0] = -100.0
	jet2pmass[0] = -100.0
	jet1tau21[0] = -100.0
	jet2tau21[0] = -100.0
#	jet1mscsv[0] = -100.0
#	jet2mscsv[0] = -100.0
	jet1bbtag[0] = -100.0
	jet2bbtag[0] = -100.0
	triggerpassbb[0] = -100.0
	DeltaPhi1[0] = -100.0
        DeltaPhi2[0] = -100.0
        DeltaPhi3[0] = -100.0
        DeltaPhi4[0] = -100.0
#	PUWeight[0]= -100.0
	
    
    f1.Close()

print "nFills"
print nFills
print "OK"

f.cd()
f.Write()
f.Close()



