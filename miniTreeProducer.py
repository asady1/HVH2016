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

import copy

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

def open_files(file_name,path) : #opens files to run on
    ff_n = 1000
    g = open(file_name)
    list_file = []
    final_list = []
    for i in range(ff_n):  # this is the length of the file
        list_file.append(g.readline().split())
    s = path

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

def getPUPPIweight( puppipt, puppieta, puppisd_corrGEN, puppisd_corrRECO_cen, puppisd_corrRECO_for ):
    genCorr  = 1.
    recoCorr = 1.
    totalWeight = 1.

    corrGEN = ROOT.TF1("corrGEN","[0]+[1]*pow(x*[2],-[3])",200,3500)
    corrGEN.SetParameter(0,1.00626)
    corrGEN.SetParameter(1, -1.06161)
    corrGEN.SetParameter(2,0.0799900)
    corrGEN.SetParameter(3,1.20454)
 
    corrRECO_cen = ROOT.TF1("corrRECO_cen","[0]+[1]*x+[2]*pow(x,2)+[3]*pow(x,3)+[4]*pow(x,4)+[5]*pow(x,5)",200,3500)
    corrRECO_cen.SetParameter(0,1.09302)
    corrRECO_cen.SetParameter(1,-0.000150068)
    corrRECO_cen.SetParameter(2,3.44866e-07)
    corrRECO_cen.SetParameter(3,-2.68100e-10)
    corrRECO_cen.SetParameter(4,8.67440e-14)
    corrRECO_cen.SetParameter(5,-1.00114e-17)
 
    corrRECO_for = ROOT.TF1("corrRECO_for","[0]+[1]*x+[2]*pow(x,2)+[3]*pow(x,3)+[4]*pow(x,4)+[5]*pow(x,5)",200,3500)
    corrRECO_for.SetParameter(0,1.27212)
    corrRECO_for.SetParameter(1,-0.000571640)
    corrRECO_for.SetParameter(2,8.37289e-07)
    corrRECO_for.SetParameter(3,-5.20433e-10)
    corrRECO_for.SetParameter(4,1.45375e-13)
    corrRECO_for.SetParameter(5,-1.50389e-17)
    genCorr =  corrGEN.Eval( puppipt )
    if( abs(puppieta)  < 1.3 ):
            recoCorr = corrRECO_cen.Eval( puppipt )
    else:
            recoCorr = corrRECO_for.Eval( puppipt );
#    print(genCorr,recoCorr)
    totalWeight = genCorr*recoCorr
    return totalWeight

#    genCorr =  puppisd_corrGEN.Eval( puppipt )

#    if math.fabs(puppieta) <= 1.3:
#      recoCorr = puppisd_corrRECO_cen.Eval( puppipt )
#    else:
#      recoCorr = puppisd_corrRECO_for.Eval( puppipt )
#
#    print genCorr
#    print recoCorr
#    totalWeight = genCorr * recoCorr

#    return totalWeight

#the class - this produces the miniTrees
class miniTreeProducer:
    def __init__(self, isMC, saveTrig, syst, tree, xsec):
        #options fed to getMiniTrees.py through the command line
        self.isMC = isMC
        self.saveTrig = saveTrig
        self.theTree = tree
        self.syst = syst
        self.xsecs = xsec

        
    def runProducer(self,location,inputfile, num1, num2, histo1, histo2, histo3, histo4, histo5, histo6, histo7, histo8):
        #making the miniTrees
        #histos
        self.histo_efficiency= histo1
        self.histo_efficiency_up= histo2
        self.histo_efficiency_down= histo3
        self.histo_efficiency_2up= histo4
        self.histo_efficiency_2down= histo5
        
        self.puppisd_corrGEN = histo6
        self.puppisd_corrRECO_cen = histo7
        self.puppisd_corrRECO_for = histo8

        #branches
        self.regressedJetpT_0 = array('f', [-100.0])
        self.regressedJetpT_1 = array('f', [-100.0])
        self.jet1pt = array('f', [-100.0])
        self.jet2pt = array('f', [-100.0])
        self.jet1pt_reg = array('f', [-100.0])
        self.jet2pt_reg = array('f', [-100.0])
        self.jet1mass_reg = array('f', [-100.0])
        self.jet2mass_reg = array('f', [-100.0])
        self.jet1mass_reg_noL2L3 = array('f', [-100.0])
        self.jet2mass_reg_noL2L3 = array('f', [-100.0])

        self.jet1NearbyJetcsvArray = array('f', [-100.0, -100.0, -100.0, -100.0])
        self.jet2NearbyJetcsvArray = array('f', [-100.0, -100.0, -100.0, -100.0])
        self.jet1NearbyJetcmvaArray = array('f', [-100.0, -100.0, -100.0, -100.0])
        self.jet2NearbyJetcmvaArray = array('f', [-100.0, -100.0, -100.0, -100.0])
        self.jet1NJcsv = array('f', [-100.0])
        self.jet2NJcsv = array('f', [-100.0])
        self.jet1NJcmva = array('f', [-100.0])
        self.jet2NJcmva = array('f', [-100.0])
        self.jet1ID = array('f', [-100.0])
        self.jet2ID = array('f', [-100.0])
        self.jet1eta = array('f', [-100.0])
        self.jet2eta = array('f', [-100.0])
        self.jet1phi = array('f', [-100.0])
        self.jet2phi = array('f', [-100.0])
        self.jet1mass = array('f', [-100.0])
        self.jet2mass = array('f', [-100.0])
        self.etadiff = array('f', [-100.0])
        self.dijetmass = array('f', [-100.0])
        self.dijetmass_corr = array('f', [-100.0])
        self.dijetmass_reg = array('f', [-100.0])
        self.dijetmass_corr_punc = array('f', [-100.0])
        self.jet1tau21 = array('f', [-100.0])
        self.jet1tau1 = array('f', [-100.0])
        self.jet1tau2 = array('f', [-100.0])
        self.jet1tau3 = array('f', [-100.0])
        self.jet2tau21 = array('f', [-100.0])
        self.jet2tau1 = array('f', [-100.0])
        self.jet2tau2 = array('f', [-100.0])
        self.jet2tau3 = array('f', [-100.0])
        self.jet1pmass = array('f', [-100.0])
        self.jet2pmass = array('f', [-100.0])
        self.jet1pmass_noL2L3 = array('f', [-100.0])
        self.jet1pmass_CA15 = array('f', [-100.0])
        self.jet1pmassunc = array('f', [-100.0])
        self.jet2pmassunc = array('f', [-100.0])
        self.jet1bbtag = array('f', [-100.0])
        self.jet2bbtag = array('f', [-100.0])
        self.jet1s1csv = array('f', [-100.0])
        self.jet2s1csv = array('f', [-100.0])
        self.jet1s2csv = array('f', [-100.0])
        self.jet2s2csv = array('f', [-100.0])

        self.mhh = array('f', [-100.0])
        self.costhetast = array('f', [-100.0])

        self.jet1_puppi_pt = array('f', [-100.0])
        self.jet2_puppi_pt = array('f', [-100.0])
        self.jet1_puppi_eta = array('f', [-100.0])
        self.jet2_puppi_eta = array('f', [-100.0])
        self.jet1_puppi_phi = array('f', [-100.0])
        self.jet2_puppi_phi = array('f', [-100.0])
        self.jet1_puppi_mass = array('f', [-100.0])
        self.jet2_puppi_mass = array('f', [-100.0])
        self.jet1_puppi_tau21 = array('f', [-100.0])
        self.jet2_puppi_tau21 = array('f', [-100.0])
        self.jet1_puppi_msoftdrop = array('f', [-100.0])
        self.jet2_puppi_msoftdrop = array('f', [-100.0])
        self.jet1_puppi_msoftdrop_corrL2L3 = array('f', [-100.0])
        self.jet2_puppi_msoftdrop_corrL2L3 = array('f', [-100.0])
        self.jet1_puppi_TheaCorr = array('f', [-100.0])
        self.jet2_puppi_TheaCorr = array('f', [-100.0])
        self.jet1_puppi_msoftdrop_raw = array('f', [-100.0])
        self.jet2_puppi_msoftdrop_raw = array('f', [-100.0])

        self.jetSJfla = array('f', [-100.0]*4)
        self.jetSJpt =  array('f', [-100.0]*4)
        self.jetSJcsv = array('f', [-100.0]*4)
        self.jetSJeta = array('f', [-100.0]*4)
        self.triggerpassbb = array('f', [-100.0])
        self.nHiggsTags = array('f', [-100.0])
        self.nTrueInt = array('f', [-100])
        self.vtype = array('f', [-100.0])
	self.nPVs = array('f', [-100.0])
        self.isData = array('f', [100.0])
        self.jet1nbHadron = array('f', [-100.0])
        self.jet2nbHadron = array('f', [-100.0])
        self.jet1flavor = array('f', [-100.0])
        self.jet2flavor = array('f', [-100.0])
        self.jet1ncHadron = array('f', [-100.0])
        self.jet2ncHadron = array('f', [-100.0])
        self.gen1Pt = array('f', [-100.0])
        self.gen1phi = array('f', [-100.0])
        self.gen1Eta = array('f', [-100.0])
        self.gen1Mass = array('f', [-100.0])
        self.gen1ID = array('f', [-100.0])
        self.gen2Pt = array('f', [-100.0])
        self.gen2Phi = array('f', [-100.0])
        self.gen2Eta = array('f', [-100.0])
        self.gen2Mass = array('f', [-100.0])
        self.gen2ID = array('f', [-100.0])
        self.CA15jet1pt = array('f', [-100.0])
        self.CA15jet2pt = array('f', [-100.0])
        self.CA15jet1eta = array('f', [-100.0])
        self.CA15jet2eta = array('f', [-100.0])
        self.CA15jet1phi = array('f', [-100.0])
        self.CA15jet2phi = array('f', [-100.0])
        self.CA15jet1mass = array('f', [-100.0])
        self.CA15jet2mass = array('f', [-100.0])
        self.jet1l1l2l3 = array('f', [-100.0])
        self.jet1l2l3 = array('f', [-100.0])
        self.jet2l1l2l3 = array('f', [-100.0])
        self.jet2l2l3 = array('f', [-100.0])
        self.jet1l1l2l3Unc = array('f', [-100.0])
        self.jet1l2l3Unc = array('f', [-100.0])
        self.jet2l1l2l3Unc = array('f', [-100.0])
        self.jet2l2l3Unc = array('f', [-100.0])
        self.jet1JER = array('f', [-100.0])
        self.jet2JER = array('f', [-100.0])
        self.puWeights = array('f', [-100.0])
        self.puWeightsUp = array('f', [-100.0])
        self.puWeightsDown = array('f', [-100.0])
        self.json = array('f', [-100.0])

        self.bbtag1SFTight = array('f', [-100.0])
        self.bbtag2SFTight = array('f', [-100.0])
        self.bbtag1SFTightUp = array('f', [-100.0])
        self.bbtag2SFTightUp = array('f', [-100.0])
        self.bbtag1SFTightDown = array('f', [-100.0])
        self.bbtag2SFTightDown = array('f', [-100.0])
        self.bbtag1SFLoose = array('f', [-100.0])
        self.bbtag2SFLoose = array('f', [-100.0])
        self.bbtag1SFLooseUp = array('f', [-100.0])
        self.bbtag2SFLooseUp = array('f', [-100.0])
        self.bbtag1SFLooseDown = array('f', [-100.0])
        self.bbtag2SFLooseDown = array('f', [-100.0])
        self.passesBoosted = array('f', [-100.0])
        self.passesResolved = array('f', [-100.0])
        self.SFTight = array('f', [-100.0])
        self.SFTightup = array('f', [-100.0])
        self.SFTightdown = array('f', [-100.0])
        self.SFLoose = array('f', [-100.0])
        self.SFLooseup = array('f', [-100.0])
        self.SFLoosedown = array('f', [-100.0])
        self.SF4sj = array('f', [-100.0])
        self.SF4sjUp = array('f', [-100.0])
        self.SF4sjDown = array('f', [-100.0])
        self.SF3sj = array('f', [-100.0])
        self.SF3sjUp = array('f', [-100.0])
        self.SF3sjDown = array('f', [-100.0])
        self.trigWeight = array('f', [-100.0])
        self.trigWeightUp = array('f', [-100.0])
        self.trigWeightDown = array('f', [-100.0])
        self.trigWeight2Up = array('f', [-100.0])
        self.trigWeight2Down = array('f', [-100.0])

        self.evt = array('f', [-100.0])
        self.ht = array('f', [-100.0])
        self.htJet30 = array('f', [-100.0])
        self.xsec = array('f', [-100.0])
        self.sjSF = array('f', [-100.0])
        self.sjSFup = array('f', [-100.0])
        self.sjSFdown = array('f', [-100.0])
        if self.isMC == 'True':
            self.genJet1BH = array('f', [-100.0])
            self.genjet2BH = array('f', [-100.0])
            self.genjet1CH = array('f', [-100.0])
            self.genjet2CH = array('f', [-100.0])
        self.MET = array('f', [-100.0])
        self.nAK08Jets = array('f', [-100.0])
        self.nAK04Jets = array('f', [-100.0])
        self.DeltaPhi1 = array('f', [-100.0])
        self.DeltaPhi2 = array('f', [-100.0])
        self.DeltaPhi3 = array('f', [-100.0])
        self.DeltaPhi4 = array('f', [-100.0])
        self.nAK04btagsMWP = array('f', [-100.0])
        self.nTightEle = array('f', [-100.0])
        self.nTightMu = array('f', [-100.0])
        self.nLooseEle = array('f', [-100.0])
        self.nLooseMu = array('f', [-100.0])
        self.tPtsum = array('f', [-100.0])

	self.LeadingAK8Jet_MatchedHadW = array('f', [-100.0])

	self.aLeptons_pT = vector('double')()
	self.aLeptons_eta = vector('double')()
	self.aLeptons_phi = vector('double')()
	self.aLeptons_mass = vector('double')()
        self.vLeptons_pT = vector('double')()
        self.vLeptons_eta = vector('double')()
        self.vLeptons_phi = vector('double')()
        self.vLeptons_mass = vector('double')()

        self.ak4jet_pt = vector('double')()
        self.ak4jet_eta = vector('double')()
        self.ak4jet_phi = vector('double')()
        self.ak4jet_mass = vector('double')()
        self.ak4jetID = vector('double')()
        self.ak4jetHeppyFlavour = vector('double')()
        self.ak4jetMCflavour = vector('double')()
        self.ak4jetPartonFlavour = vector('double')()
        self.ak4jetHadronFlavour = vector('double')()
        self.ak4jetCSVLSF = vector('double')()
        self.ak4jetCSVLSF_Up = vector('double')()
        self.ak4jetCSVLSF_Down = vector('double')()
        self.ak4jetCSVMSF = vector('double')()
        self.ak4jetCSVMSF_up = vector('double')()
        self.ak4jetCSVMSF_Down = vector('double')()
        self.ak4jetCSVTSF = vector('double')()
        self.ak4jetCSVTSF_Up = vector('double')()
        self.ak4jetCSVTSF_Down = vector('double')()
        self.ak4jetCMVALSF = vector('double')()
        self.ak4jetCMVALSF_Up = vector('double')()
        self.ak4jetCMVALSF_Down = vector('double')()
        self.ak4jetCMVAMSF = vector('double')()
        self.ak4jetCMVAMSF_Up = vector('double')()
        self.ak4jetCMVAMSF_Down = vector('double')()
        self.ak4jetCMVATSF = vector('double')()
        self.ak4jetCMVATSF_Up = vector('double')()
        self.ak4jetCMVATSF_Down = vector('double')()
        self.ak4jetCSV = vector('double')()
        self.ak4jetDeepCSVb = vector('double')()
        self.ak4jetDeepCSVbb = vector('double')()
        self.ak4jetCMVA = vector('double')()
        self.ak4jetCorr = vector('double')()
        self.ak4jetCorrJECUp = vector('double')()
        self.ak4jetCorrJECDown = vector('double')()
        self.ak4jetCorrJER = vector('double')()
        self.ak4jetCorrJERUp = vector('double')()
        self.ak4jetCorrJERDown = vector('double')()
        self.ak4genJetPt = vector('double')()
        self.ak4genJetPhi = vector('double')()
        self.ak4genJetEta = vector('double')()
        self.ak4genJetMass = vector('double')()
        self.ak4genJetID = vector('double')()
        if self.saveTrig == 'True':
	    self.HLT_PFHT900_v = array('f', [-100.0])
            self.HLT_PFHT800_v = array('f', [-100.0])
            self.HLT_PFJet80_v = array('f', [-100.0])
            self.HLT_QuadJet45_TripleBTagCSV_p087_v = array('f', [-100.0])
            self.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v = array('f', [-100.0])
	    self.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v = array('f', [-100.0])
	    self.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v = array('f', [-100.0])
	    self.HLT_AK8PFJet360_TrimMass30_v = array('f', [-100.0])
	    self.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
            self.HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
            self.HLT_PFJet140_v = array('f', [-100.0])
 	    self.HLT_PFJet200_v = array('f', [-100.0])
	    self.HLT_PFJet260_v = array('f', [-100.0])
            self.HLT_Mu24_eta2p1_v = array('f', [-100.0])
            self.HLT_Mu27_v = array('f', [-100.0])
            self.HLT_Ele105_CaloIdVT_GsfTrkIdT_v = array('f', [-100.0])


        #creating the tree branches we need
        self.theTree.Branch('regressedJetpT_0', self.regressedJetpT_0, 'regressedJetpT_0/F')
        self.theTree.Branch('regressedJetpT_1', self.regressedJetpT_1, 'regressedJetpT_1/F')
        self.theTree.Branch('jet1pt', self.jet1pt, 'jet1pt/F')
        self.theTree.Branch('jet2pt', self.jet2pt, 'jet2pt/F')
        self.theTree.Branch('jet1pt_reg', self.jet1pt_reg, 'jet1pt_reg/F')
        self.theTree.Branch('jet2pt_reg', self.jet2pt_reg, 'jet2pt_reg/F')
        self.theTree.Branch('jet1mass_reg', self.jet1mass_reg, 'jet1mass_reg/F')
        self.theTree.Branch('jet2mass_reg', self.jet2mass_reg, 'jet2mass_reg/F')
        self.theTree.Branch('jet1mass_reg_noL2L3', self.jet1mass_reg_noL2L3, 'jet1mass_reg_noL2L3/F')
        self.theTree.Branch('jet2mass_reg_noL2L3', self.jet2mass_reg_noL2L3, 'jet2mass_reg_noL2L3/F')
        self.theTree.Branch('jet1NearbyJetcsv', self.jet1NearbyJetcsvArray, 'pt/F:eta/F:phi/F:mass/F')
        self.theTree.Branch('jet2NearbyJetcsv', self.jet2NearbyJetcsvArray, 'pt/F:eta/F:phi/F:mass/F')
        self.theTree.Branch('jet1NearbyJetcmva', self.jet1NearbyJetcmvaArray, 'pt/F:eta/F:phi/F:mass/F')
        self.theTree.Branch('jet2NearbyJetcmva', self.jet2NearbyJetcmvaArray, 'pt/F:eta/F:phi/F:mass/F')
        self.theTree.Branch('jet1NJcsv', self.jet1NJcsv, 'jet1NJcsv')
        self.theTree.Branch('jet2NJcsv', self.jet2NJcsv, 'jet2NJcsv')
        self.theTree.Branch('jet1NJcmva', self.jet1NJcmva, 'jet1NJcmva')
        self.theTree.Branch('jet2NJcmva', self.jet2NJcmva, 'jet2NJcmva')
        self.theTree.Branch('jet1eta', self.jet1eta, 'jet1eta/F')
        self.theTree.Branch('jet2eta', self.jet2eta, 'jet2eta/F')
        self.theTree.Branch('jet1phi', self.jet1phi, 'jet1phi/F')
        self.theTree.Branch('jet2phi', self.jet2phi, 'jet2phi/F')
        self.theTree.Branch('jet1mass', self.jet1mass, 'jet1mass/F')
        self.theTree.Branch('jet2mass', self.jet2mass, 'jet2mass/F')
        self.theTree.Branch('etadiff', self.etadiff, 'etadiff/F')
        self.theTree.Branch('dijetmass', self.dijetmass, 'dijetmass/F')
        self.theTree.Branch('dijetmass_corr', self.dijetmass_corr, 'dijetmass_corr/F')
        self.theTree.Branch('dijetmass_reg', self.dijetmass_reg, 'dijetmass_reg/F')
        self.theTree.Branch('dijetmass_corr_punc', self.dijetmass_corr_punc, 'dijetmass_corr_punc/F')
        self.theTree.Branch('jet1tau21', self.jet1tau21, 'jet1tau21/F')
        self.theTree.Branch('jet1tau1', self.jet1tau1, 'jet1tau1/F')
        self.theTree.Branch('jet1tau2', self.jet1tau2, 'jet1tau2/F')
        self.theTree.Branch('jet1tau3', self.jet1tau3, 'jet1tau3/F')
        self.theTree.Branch('jet2tau21', self.jet2tau21, 'jet2tau21/F')
        self.theTree.Branch('jet2tau1', self.jet2tau1, 'jet2tau1/F')
        self.theTree.Branch('jet2tau2', self.jet2tau2, 'jet2tau2/F')
        self.theTree.Branch('jet2tau3', self.jet2tau3, 'jet2tau3/F')
        self.theTree.Branch('jet1pmass', self.jet1pmass, 'jet1pmass/F')
        self.theTree.Branch('jet2pmass', self.jet2pmass, 'jet2pmass/F')
        self.theTree.Branch('jet1pmass_noL2L3', self.jet1pmass_noL2L3, 'jet1pmass_noL2L3/F')
        self.theTree.Branch('jet1pmass_CA15', self.jet1pmass_CA15, 'jet1pmass_CA15/F')
        self.theTree.Branch('jet1pmassunc', self.jet1pmassunc, 'jet1pmassunc/F')
        self.theTree.Branch('jet2pmassunc', self.jet2pmassunc, 'jet2pmassunc/F')
        self.theTree.Branch('jet1bbtag', self.jet1bbtag, 'jet1bbtag/F')
        self.theTree.Branch('jet2bbtag', self.jet2bbtag, 'jet2bbtag/F')
        self.theTree.Branch('jet1s1csv', self.jet1s1csv, 'jet1s1csv/F')
        self.theTree.Branch('jet2s1csv', self.jet2s1csv, 'jet2s1csv/F')
        self.theTree.Branch('jet1s2csv', self.jet1s2csv, 'jet1s2csv/F')
        self.theTree.Branch('jet2s2csv', self.jet2s2csv, 'jet2s2csv/F')

        self.theTree.Branch('jet1_puppi_pt', self.jet1_puppi_pt, 'jet1_puppi_pt/F')
        self.theTree.Branch('jet2_puppi_pt', self.jet2_puppi_pt, 'jet2_puppi_pt/F')
        self.theTree.Branch('jet1_puppi_eta', self.jet1_puppi_eta, 'jet1_puppi_eta/F')
        self.theTree.Branch('jet2_puppi_eta', self.jet2_puppi_eta, 'jet2_puppi_eta/F')
        self.theTree.Branch('jet1_puppi_phi', self.jet1_puppi_phi, 'jet1_puppi_phi/F')
        self.theTree.Branch('jet2_puppi_phi', self.jet2_puppi_phi, 'jet2_puppi_phi/F')
        self.theTree.Branch('jet1_puppi_mass', self.jet1_puppi_mass, 'jet1_puppi_mass/F')
        self.theTree.Branch('jet2_puppi_mass', self.jet2_puppi_mass, 'jet2_puppi_mass/F')
        self.theTree.Branch('jet1_puppi_tau21', self.jet1_puppi_tau21, 'jet1_puppi_tau21/F')
        self.theTree.Branch('jet2_puppi_tau21', self.jet2_puppi_tau21, 'jet2_puppi_tau21/F')
        self.theTree.Branch('jet1_puppi_msoftdrop', self.jet1_puppi_msoftdrop, 'jet1_puppi_msoftdrop/F')
        self.theTree.Branch('jet2_puppi_msoftdrop', self.jet2_puppi_msoftdrop, 'jet2_puppi_msoftdrop/F')
        self.theTree.Branch('jet1_puppi_msoftdrop_corrL2L3', self.jet1_puppi_msoftdrop_corrL2L3, 'jet1_puppi_msoftdrop_corrL2L3/F')
        self.theTree.Branch('jet2_puppi_msoftdrop_corrL2L3', self.jet2_puppi_msoftdrop_corrL2L3, 'jet2_puppi_msoftdrop_corrL2L3/F')
        self.theTree.Branch('jet1_puppi_TheaCorr', self.jet1_puppi_TheaCorr, 'jet1_puppi_TheaCorr/F')
        self.theTree.Branch('jet2_puppi_TheaCorr', self.jet2_puppi_TheaCorr, 'jet2_puppi_TheaCorr/F')
        self.theTree.Branch('jet1_puppi_msoftdrop_raw', self.jet1_puppi_msoftdrop_raw, 'jet1_puppi_msoftdrop_raw/F')
        self.theTree.Branch('jet2_puppi_msoftdrop_raw', self.jet2_puppi_msoftdrop_raw, 'jet2_puppi_msoftdrop_raw/F')

        self.theTree.Branch('mhh', self.mhh, 'mhh/F')
        self.theTree.Branch('costhetast', self.costhetast, 'costhetast/F')

        self.theTree.Branch('nAK08Jets', self.nAK08Jets, 'nAK08Jets/F')
        self.theTree.Branch('nAK04Jets', self.nAK04Jets, 'nAK04Jets/F')
        self.theTree.Branch('nAK04btagsMWP', self.nAK04btagsMWP, 'nAK04btagsMWP/F')
        self.theTree.Branch('nHiggsTags', self.nHiggsTags, 'nHiggsTags/F')
        self.theTree.Branch('triggerpassbb', self.triggerpassbb, 'triggerpassbb/F')
        self.theTree.Branch('nTrueInt',self.nTrueInt,'nTrueInt/F')
        self.theTree.Branch('puWeights',self.puWeights,'puWeights/F')
        self.theTree.Branch('puWeightsUp',self.puWeightsUp,'puWeightsUp/F')
        self.theTree.Branch('puWeightsDown',self.puWeightsDown,'puWeightsDown/F')
        self.theTree.Branch('jet1ID', self.jet1ID, 'jet1ID/F')
        self.theTree.Branch('jet2ID', self.jet2ID, 'jet2ID/F')
        self.theTree.Branch('vtype', self.vtype, 'vtype/F')
	self.theTree.Branch('nPVs', self.nPVs, 'nPVs/F')
        self.theTree.Branch('isData', self.isData, 'isData/F')
        self.theTree.Branch('jet1nbHadron', self.jet1nbHadron, 'jet1nbHadron/F')
        self.theTree.Branch('jet2nbHadron', self.jet2nbHadron, 'jet2nbHadron/F')
        self.theTree.Branch('jet1flavor', self.jet1flavor, 'jet1flavor/F')
        self.theTree.Branch('jet2flavor', self.jet2flavor, 'jet2flavor/F')
        self.theTree.Branch('jet1ncHadron', self.jet1ncHadron, 'jet1ncHadron/F')
        self.theTree.Branch('jet2ncHadron', self.jet2ncHadron, 'jet2ncHadron/F')
        self.theTree.Branch('gen1Pt', self.gen1Pt, 'gen1Pt/F')
        self.theTree.Branch('gen1phi', self.gen1phi, 'gen1phi/F')
        self.theTree.Branch('gen1Eta', self.gen1Eta, 'gen1Eta/F')
        self.theTree.Branch('gen1Mass', self.gen1Mass, 'gen1Mass/F')
        self.theTree.Branch('gen1ID', self.gen1ID, 'gen1ID/F')
        self.theTree.Branch('gen2Pt', self.gen2Pt, 'gen2Pt/F')
        self.theTree.Branch('gen2Phi', self.gen2Phi, 'gen2Phi/F')
        self.theTree.Branch('gen2Eta', self.gen2Eta, 'gen2Eta/F')
        self.theTree.Branch('gen2Mass', self.gen2Mass, 'gen2Mass/F')
        self.theTree.Branch('gen2ID', self.gen2ID, 'gen2ID/F')
        self.theTree.Branch('CA15jet1pt', self.CA15jet1pt,'CA15jet1pt/F')
        self.theTree.Branch('CA15jet1eta', self.CA15jet1eta,'CA15jet1eta/F')
        self.theTree.Branch('CA15jet1phi', self.CA15jet1phi,'CA15jet1phi/F')
        self.theTree.Branch('CA15jet1mass', self.CA15jet1mass,'CA15jet1mass/F')
        self.theTree.Branch('CA15jet2pt', self.CA15jet2pt,'CA15jet2pt/F')
        self.theTree.Branch('CA15jet2eta', self.CA15jet2eta,'CA15jet2eta/F')
        self.theTree.Branch('CA15jet2phi', self.CA15jet2phi,'CA15jet2phi/F')
        self.theTree.Branch('CA15jet2mass', self.CA15jet2mass,'CA15jet2mass/F')
        self.theTree.Branch('jet1l1l2l3', self.jet1l1l2l3, 'jet1l1l2l3/F')
        self.theTree.Branch('jet1l2l3', self.jet1l2l3, 'jet1l2l3/F')
        self.theTree.Branch('jet2l1l2l3', self.jet2l1l2l3, 'jet2l1l2l3/F')
        self.theTree.Branch('jet2l2l3', self.jet2l2l3, 'jet2l2l3/F')
        self.theTree.Branch('jet1l1l2l3Unc', self.jet1l1l2l3Unc, 'jet1l1l2l3Unc/F')
        self.theTree.Branch('jet1l2l3Unc', self.jet1l2l3Unc, 'jet1l2l3Unc/F')
        self.theTree.Branch('jet2l1l2l3Unc', self.jet2l1l2l3Unc, 'jet2l1l2l3Unc/F')
        self.theTree.Branch('jet2l2l3Unc', self.jet2l2l3Unc, 'jet2l2l3Unc/F')
        self.theTree.Branch('jet1JER', self.jet1JER, 'jet1JER/F')
        self.theTree.Branch('jet2JER', self.jet2JER, 'jet2JER/F')
        self.theTree.Branch('json', self.json, 'json/F')
        self.theTree.Branch('DeltaPhi1', self.DeltaPhi1, 'DeltaPhi1/F')
        self.theTree.Branch('DeltaPhi2', self.DeltaPhi2, 'DeltaPhi2/F')
        self.theTree.Branch('DeltaPhi3', self.DeltaPhi3, 'DeltaPhi3/F')
        self.theTree.Branch('DeltaPhi4', self.DeltaPhi4, 'DeltaPhi4/F')

        self.theTree.Branch('bbtag1SFTight', self.bbtag1SFTight, 'bbtag1SFTight/F')
        self.theTree.Branch('bbtag2SFTight', self.bbtag2SFTight, 'bbtag2SFTight/F')
        self.theTree.Branch('bbtag1SFTightUp', self.bbtag1SFTightUp, 'bbtag1SFTightUp/F')
        self.theTree.Branch('bbtag2SFTightUp', self.bbtag2SFTightUp, 'bbtag2SFTightUp/F')
        self.theTree.Branch('bbtag1SFTightDown', self.bbtag1SFTightDown, 'bbtag1SFTightDown/F')
        self.theTree.Branch('bbtag2SFTightDown', self.bbtag2SFTightDown, 'bbtag2SFTightDown/F')
        self.theTree.Branch('bbtag1SFLoose', self.bbtag1SFLoose, 'bbtag1SFLoose/F')
        self.theTree.Branch('bbtag2SFLoose', self.bbtag2SFLoose, 'bbtag2SFLoose/F')
        self.theTree.Branch('bbtag1SFLooseUp', self.bbtag1SFLooseUp, 'bbtag1SFLooseUp/F')
        self.theTree.Branch('bbtag2SFLooseUp', self.bbtag2SFLooseUp, 'bbtag2SFLooseUp/F')
        self.theTree.Branch('bbtag1SFLooseDown', self.bbtag1SFLooseDown, 'bbtag1SFLooseDown/F')
        self.theTree.Branch('bbtag2SFLooseDown', self.bbtag2SFLooseDown, 'bbtag2SFLooseDown/F')

        self.theTree.Branch('passesBoosted', self.passesBoosted, 'passesBoosted/F')
        self.theTree.Branch('passesResolved', self.passesResolved, 'passesResolved/F')

        self.theTree.Branch('SFTight', self.SFTight, 'SFTight/F')
        self.theTree.Branch('SFTightup', self.SFTightup, 'SFTightup/F')
        self.theTree.Branch('SFTightdown', self.SFTightdown, 'SFTightdown/F')
        self.theTree.Branch('SFLoose', self.SFLoose, 'SFLoose/F')
        self.theTree.Branch('SFLooseup', self.SFLooseup, 'SFLooseup/F')
        self.theTree.Branch('SFLoosedown', self.SFLoosedown, 'SFLoosedown/F')
        self.theTree.Branch('SF4sj', self.SF4sj, 'SF4sj/F')
        self.theTree.Branch('SF4sjUp', self.SF4sjUp, 'SF4sjUp/F')
        self.theTree.Branch('SF4sjDown', self.SF4sjDown, 'SF4sjDown/F')
        self.theTree.Branch('SF3sj', self.SF3sj, 'SF3sj/F')
        self.theTree.Branch('SF3sjUp', self.SF3sjUp, 'SF3sjUp/F')
        self.theTree.Branch('SF3sjDown', self.SF3sjDown, 'SF3sjDown/F')
        self.theTree.Branch('tPtsum', self.tPtsum, 'tPtsum/F')
        self.theTree.Branch('trigWeight', self.trigWeight, 'trigWeight/F')
        self.theTree.Branch('trigWeightUp', self.trigWeightUp, 'trigWeightUp/F')
        self.theTree.Branch('trigWeightDown', self.trigWeightDown, 'trigWeightDown/F')
        self.theTree.Branch('trigWeight2Up', self.trigWeight2Up, 'trigWeight2Up/F')
        self.theTree.Branch('trigWeight2Down', self.trigWeight2Down, 'trigWeight2Down/F')
        self.theTree.Branch('LeadingAK8Jet_MatchedHadW', self.LeadingAK8Jet_MatchedHadW, 'LeadingAK8Jet_MatchedHadW/F')

        self.theTree.Branch('evt',self.evt,'evt/F')
        self.theTree.Branch('ht', self.ht, 'ht/F')
        self.theTree.Branch('htJet30', self.htJet30, 'htJet30/F')
        self.theTree.Branch('MET', self.MET, 'MET/F')
        self.theTree.Branch('xsec', self.xsec, 'xsec/F')
        self.theTree.Branch('sjSF', self.sjSF, 'sjSF/F')
        self.theTree.Branch('sjSFup', self.sjSFup, 'sjSFup/F')
        self.theTree.Branch('sjSFdown', self.sjSFdown, 'sjSFdown/F')
        self.theTree.Branch('jetSJfla',self.jetSJfla,'jetSJfla[4]/F')
        self.theTree.Branch('jetSJpt', self.jetSJpt,'jetSJpt[4]/F')
        self.theTree.Branch('jetSJcsv',self.jetSJcsv,'jetSJcsv[4]/F')
        self.theTree.Branch('jetSJeta',self.jetSJeta,'jetSJeta[4]/F')
        if self.isMC == 'True':
            self.theTree.Branch('genJet1BH', self.genJet1BH, 'genJet1BH/F')
            self.theTree.Branch('genjet2BH', self.genjet2BH, 'genjet2BH/F')
            self.theTree.Branch('genjet1CH', self.genjet1CH, 'genjet1CH/F')
            self.theTree.Branch('genjet2CH', self.genjet2CH, 'genjet2CH/F')
        self.theTree.Branch('nTightEle', self.nTightEle, 'nTightEle/F')
        self.theTree.Branch('nTightMu', self.nTightMu, 'nTightMu/F')
        self.theTree.Branch('nLooseEle', self.nLooseEle, 'nLooseEle/F')
        self.theTree.Branch('nLooseMu', self.nLooseMu, 'nLooseMu/F')

        self.theTree.Branch('aLeptons_pT',self.aLeptons_pT)
        self.theTree.Branch('aLeptons_eta',self.aLeptons_eta)
        self.theTree.Branch('aLeptons_phi',self.aLeptons_phi)
        self.theTree.Branch('aLeptons_mass',self.aLeptons_mass)
        self.theTree.Branch('vLeptons_pT',self.vLeptons_pT)
        self.theTree.Branch('vLeptons_eta',self.vLeptons_eta)
        self.theTree.Branch('vLeptons_phi',self.vLeptons_phi)
        self.theTree.Branch('vLeptons_mass',self.vLeptons_mass)

        self.theTree.Branch('ak4jet_pt',self.ak4jet_pt)
        self.theTree.Branch('ak4jet_eta',self.ak4jet_eta)
        self.theTree.Branch('ak4jet_phi',self.ak4jet_phi)
        self.theTree.Branch('ak4jet_mass',self.ak4jet_mass)
        self.theTree.Branch('ak4jetID',self.ak4jetID)
        self.theTree.Branch('ak4jetHeppyFlavour', self.ak4jetHeppyFlavour)
        self.theTree.Branch('ak4jetMCflavour', self.ak4jetMCflavour)
        self.theTree.Branch('ak4jetPartonFlavour', self.ak4jetPartonFlavour)
        self.theTree.Branch('ak4jetHadronFlavour', self.ak4jetHadronFlavour)
        self.theTree.Branch('ak4jetCSVLSF', self.ak4jetCSVLSF)
        self.theTree.Branch('ak4jetCSVLSF_Up', self.ak4jetCSVLSF_Up)
        self.theTree.Branch('ak4jetCSVLSF_Down', self.ak4jetCSVLSF_Down)
        self.theTree.Branch('ak4jetCSVMSF', self.ak4jetCSVMSF)
        self.theTree.Branch('ak4jetCSVMSF_up', self.ak4jetCSVMSF_up)
        self.theTree.Branch('ak4jetCSVMSF_Down', self.ak4jetCSVMSF_Down)
        self.theTree.Branch('ak4jetCSVTSF', self.ak4jetCSVTSF)
        self.theTree.Branch('ak4jetCSVTSF_Up', self.ak4jetCSVTSF_Up)
        self.theTree.Branch('ak4jetCSVTSF_Down', self.ak4jetCSVTSF_Down)
        self.theTree.Branch('ak4jetCMVALSF', self.ak4jetCMVALSF)
        self.theTree.Branch('ak4jetCMVALSF_Up', self.ak4jetCMVALSF_Up)
        self.theTree.Branch('ak4jetCMVALSF_Down', self.ak4jetCMVALSF_Down)
        self.theTree.Branch('ak4jetCMVAMSF', self.ak4jetCMVAMSF)
        self.theTree.Branch('ak4jetCMVAMSF_Up', self.ak4jetCMVAMSF_Up)
        self.theTree.Branch('ak4jetCMVAMSF_Down', self.ak4jetCMVAMSF_Down)
        self.theTree.Branch('ak4jetCMVATSF', self.ak4jetCMVATSF)
        self.theTree.Branch('ak4jetCMVATSF_Up', self.ak4jetCMVATSF_Up)
        self.theTree.Branch('ak4jetCMVATSF_Down', self.ak4jetCMVATSF_Down)
        self.theTree.Branch('ak4jetCSV', self.ak4jetCSV)
        self.theTree.Branch('ak4jetDeepCSVb', self.ak4jetDeepCSVb)
        self.theTree.Branch('ak4jetDeepCSVbb', self.ak4jetDeepCSVbb)
        self.theTree.Branch('ak4jetCMVA', self.ak4jetCMVA)
        self.theTree.Branch('ak4jetCorr', self.ak4jetCorr)
        self.theTree.Branch('ak4jetCorrJECUp', self.ak4jetCorrJECUp)
        self.theTree.Branch('ak4jetCorrJECDown', self.ak4jetCorrJECDown)
        self.theTree.Branch('ak4jetCorrJER', self.ak4jetCorrJER)
        self.theTree.Branch('ak4jetCorrJERUp', self.ak4jetCorrJERUp)
        self.theTree.Branch('ak4jetCorrJERDown', self.ak4jetCorrJERDown)
        self.theTree.Branch('ak4genJetPt', self.ak4genJetPt)
        self.theTree.Branch('ak4genJetPhi', self.ak4genJetPhi)
        self.theTree.Branch('ak4genJetEta', self.ak4genJetEta)
        self.theTree.Branch('ak4genJetMass', self.ak4genJetMass)
        self.theTree.Branch('ak4genJetID', self.ak4genJetID)
        if self.saveTrig == 'True':
	    self.theTree.Branch('HLT_PFHT900_v', self.HLT_PFHT900_v, 'HLT_PFHT900_v/F')
            self.theTree.Branch('HLT_PFHT800_v', self.HLT_PFHT800_v, 'HLT_PFHT800_v/F')
            self.theTree.Branch('HLT_PFJet80_v', self.HLT_PFJet80_v, 'HLT_PFJet80_v/F')
            self.theTree.Branch('HLT_QuadJet45_TripleBTagCSV_p087_v', self.HLT_QuadJet45_TripleBTagCSV_p087_v, 'HLT_QuadJet45_TripleBTagCSV_p087_v/F')
            self.theTree.Branch('HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v', self.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v, 'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v/F')
	    self.theTree.Branch('HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v', self.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v/F')
	    self.theTree.Branch('HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v', self.HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v/F')
	    self.theTree.Branch('HLT_AK8PFJet360_TrimMass30_v', self.HLT_AK8PFJet360_TrimMass30_v, 'HLT_AK8PFJet360_TrimMass30_v/F')
	    self.theTree.Branch('HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v', self.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v, 'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v/F')
	    self.theTree.Branch('HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v', self.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v, 'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v/F')
	    self.theTree.Branch('HLT_PFJet140_v', self.HLT_PFJet140_v, 'HLT_PFJet140_v/F')
	    self.theTree.Branch('HLT_PFJet200_v', self.HLT_PFJet200_v, 'HLT_PFJet200_v/F')
	    self.theTree.Branch('HLT_PFJet260_v', self.HLT_PFJet260_v, 'HLT_PFJet260_v/F')
            self.theTree.Branch('HLT_Mu24_eta2p1_v', self.HLT_Mu24_eta2p1_v, 'HLT_Mu24_eta2p1_v/F')
            self.theTree.Branch('HLT_Mu27_v', self.HLT_Mu27_v, 'HLT_Mu27_v/F')
            self.theTree.Branch('HLT_Ele105_CaloIdVT_GsfTrkIdT_v', self.HLT_Ele105_CaloIdVT_GsfTrkIdT_v, 'HLT_Ele105_CaloIdVT_GsfTrkIdT_v/F')

        #getting input files
        self.Files_list	= open_files( inputfile, location )

        #list of histograms for cuts
        self.bbj = ROOT.TH1F("bbj", "Before any cuts", 3, -0.5, 1.5)
        self.bb0 = ROOT.TH1F("bb0", "After Json", 3, -0.5, 1.5)
        self.bb1 = ROOT.TH1F("bb2", "After jet cuts", 3, -0.5, 1.5)
        #histograms needed for later
        if self.isMC == 'True':
            self.CountMC = ROOT.TH1F("Count","Count",1,0,2)
            self.CountFullWeightedMC = ROOT.TH1F("CountFullWeighted","Count with gen weight and pu weight",1,0,2)
            self.CountWeightedmc = ROOT.TH1F("CountWeighted","Count with sign(gen weight) and pu weight",1,0,2)
            self.CountPosWeightMC = ROOT.TH1F("CountPosWeight","Count genWeight>0",1,0,2)
            self.CountNegWeightMC = ROOT.TH1F("CountNegWeight","Count genWeight<0",1,0,2)
            self.CountWeightedLHEWeightScalemc = ROOT.TH1F("CountWeightedLHEWeightScale","Count with gen weight x LHE_weights_scale and pu weight", 6, -0.5, 5.5)
            self.CountWeightedLHEWeightPdfMC = ROOT.TH1F("CountWeightedLHEWeightPdf","Count with gen weight x LHE_weights_pdf and pu weight", 103, -0.5, 102.5)

        #TMVA regression
        self.this_pt=array( 'f', [ 0 ] )
        self.this_pv=array( 'f', [ 0 ] )
        self.this_eta=array( 'f', [ 0 ] )
        self.this_mass=array( 'f', [ 0 ] )
        self.this_muonF =array( 'f', [ 0 ] )
        self.this_EmF=array( 'f', [ 0 ] )
        self.this_HF=array( 'f', [ 0 ] )
        self.this_multi=array( 'f', [ 0 ] )

        self.reader = ROOT.TMVA.Reader("!Color:!Silent" )
        self.reader.AddVariable( "FatjetAK08ungroomed_pt", self.this_pt)
        self.reader.AddVariable( "nPVs", self.this_pv)
        self.reader.AddVariable( "FatjetAK08ungroomed_eta", self.this_eta)
        #self.reader.AddVariable( "FatjetAK08ungroomed_mass", self.this_mass)
        self.reader.AddVariable( "FatjetAK08ungroomed_muonEnergyFraction", self.this_muonF)
        self.reader.AddVariable( "FatjetAK08ungroomed_neutralEmEnergyFraction", self.this_EmF)
        self.reader.AddVariable( "FatjetAK08ungroomed_neutralHadronEnergyFraction", self.this_HF)
        self.reader.AddVariable( "FatjetAK08ungroomed_chargedMultiplicity", self.this_multi)
        self.reader.BookMVA("BDTG method", "TMVARegression_BDTG.weights.xml")


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

        self.count = 0
        #loop over files
        for i in range(num1, num2):
            self.files = self.Files_list[i]
            print self.files
            self.f1 = ROOT.TFile.Open(self.files, "READ")
            self.treeMine  = self.f1.Get('tree')
            self.nevent = self.treeMine.GetEntries();
            self.nFills = 0
            self.nFills2 = 0

            #getting the norm and other useful histos
            if self.isMC == 'True':
                self.histo_weight=self.f1.Get("CountWeighted")
                self.CountMC.Add(self.f1.Get("Count"))
                self.CountFullWeightedMC.Add(self.f1.Get("CountFullWeighted"))
                self.CountWeightedmc.Add(self.f1.Get("CountWeighted"))
                self.CountPosWeightMC.Add(self.f1.Get("CountPosWeight"))
                self.CountNegWeightMC.Add(self.f1.Get("CountNegWeight"))
                self.CountWeightedLHEWeightScalemc.Add(self.f1.Get("CountWeightedLHEWeightScale"))
                self.CountWeightedLHEWeightPdfMC.Add(self.f1.Get("CountWeightedLHEWeightPdf"))

            #loop over events in file
            print "Start looping"
            for j in range(0,self.nevent):
#            for j in range(0,20):
                self.treeMine.GetEntry(j)
                self.count = self.count + 1
                if self.count % 1000 == 0 :
                    print "processing events", self.count
	
    
                #variables we need from the heppy ntuple
                self.Data = self.treeMine.isData
                self.vType = self.treeMine.Vtype
                self.EVT = self.treeMine.evt
                self.genTopPts = self.treeMine.GenTop_pt
                self.JSON = self.treeMine.json
                self.fJetPt  = self.treeMine.Jet_pt
                self.fJetEta  = self.treeMine.Jet_eta
                self.fJetPhi = self.treeMine.Jet_phi
                self.fJetMass = self.treeMine.Jet_mass
                self.fJetID = self.treeMine.Jet_id
                self.fJetCSV = self.treeMine.Jet_btagCSVV0
                self.fJetDeepCSVb = self.treeMine.Jet_btagDeepCSVb
                self.fJetDeepCSVbb = self.treeMine.Jet_btagDeepCSVbb
                self.fJetCMVA = self.treeMine.Jet_btagCMVAV2
                self.fJetCorr = self.treeMine.Jet_corr
                self.fJetCorrJECUp = self.treeMine.Jet_corr_JECUp
                self.fJetCorrJECDown = self.treeMine.Jet_corr_JECDown
                self.fNJets = self.treeMine.nJet
                self.nAK04Jets[0] = self.fNJets
                self.genPt = self.treeMine.GenJet_pt
                self.genEta = self.treeMine.GenJet_eta
                self.genPhi = self.treeMine.GenJet_phi
                self.genMass = self.treeMine.GenJet_mass
                self.htJet30[0] = self.treeMine.htJet30
                self.MET[0] = self.treeMine.met_pt
                self.fjUngroomedN = self.treeMine.nFatjetAK08ungroomed
                self.nAK08Jets[0] = self.fjUngroomedN
                self.fjUngroomedPt = self.treeMine.FatjetAK08ungroomed_pt
                self.fjUngroomedEta = self.treeMine.FatjetAK08ungroomed_eta
                self.fjUngroomedPhi = self.treeMine.FatjetAK08ungroomed_phi
                self.fjUngroomedMass = self.treeMine.FatjetAK08ungroomed_mass
                self.fjUngroomedSDMass = self.treeMine.FatjetAK08ungroomed_msoftdrop
                self.fjUngroomedTau1 = self.treeMine.FatjetAK08ungroomed_tau1
                self.fjUngroomedTau2 = self.treeMine.FatjetAK08ungroomed_tau2
                self.fjUngroomedTau3 = self.treeMine.FatjetAK08ungroomed_tau3
                self.fjUngroomedBbTag = self.treeMine.FatjetAK08ungroomed_bbtag
                self.fjUngroomedJetID = self.treeMine.FatjetAK08ungroomed_id_Tight
                self.fjUngroomedPrunedMass = self.treeMine.FatjetAK08ungroomed_mprunedcorr
                self.fjUngroomedPrunedMass_Unc = self.treeMine.FatjetAK08ungroomed_mpruned
                self.nFatjetCA15pruned = self.treeMine.nFatjetCA15pruned
                self.FatjetCA15pruned_pt = self.treeMine.FatjetCA15pruned_pt
                self.FatjetCA15pruned_eta = self.treeMine.FatjetCA15pruned_eta
                self.FatjetCA15pruned_phi = self.treeMine.FatjetCA15pruned_phi
                self.FatjetCA15pruned_mass = self.treeMine.FatjetCA15pruned_mass
                self.FatjetCA15ungroomed_pt = self.treeMine.FatjetCA15ungroomed_pt
                self.FatjetCA15ungroomed_eta = self.treeMine.FatjetCA15ungroomed_eta
                self.FatjetCA15ungroomed_phi = self.treeMine.FatjetCA15ungroomed_phi
                self.FatjetCA15ungroomed_mass = self.treeMine.FatjetCA15ungroomed_mass
                self.fjL2L3 = self.treeMine.FatjetAK08ungroomed_JEC_L2L3
                self.fjL1L2L3 = self.treeMine.FatjetAK08ungroomed_JEC_L1L2L3
                self.fjL2L3Unc = self.treeMine.FatjetAK08ungroomed_JEC_L2L3Unc
                self.fjL1L2L3Unc = self.treeMine.FatjetAK08ungroomed_JEC_L1L2L3Unc
                self.sjPrunedPt = self.treeMine.SubjetAK08softdrop_pt
                self.sjPrunedEta = self.treeMine.SubjetAK08softdrop_eta
                self.sjPrunedPhi = self.treeMine.SubjetAK08softdrop_phi
                self.sjPrunedMass = self.treeMine.SubjetAK08softdrop_mass
                self.sjPrunedBtag = self.treeMine.SubjetAK08softdrop_btag
                if self.isMC == 'True':
                    self.fJetHeppyFlavour = self.treeMine.Jet_heppyFlavour
                    self.fJetMCflavour = self.treeMine.Jet_mcFlavour
                    self.fJetPartonFlavour = self.treeMine.Jet_partonFlavour
                    self.fJetHadronFlavour = self.treeMine.Jet_hadronFlavour
                    self.fJetCSVLSF = self.treeMine.Jet_btagCSVL_SF
                    self.fJetCSVLSF_Up = self.treeMine.Jet_btagCSVL_SF_up
                    self.fJetCSVLSF_Down = self.treeMine.Jet_btagCSVL_SF_down
                    self.fJetCSVMSF = self.treeMine.Jet_btagCSVM_SF
                    self.fJetCSVMSF_Up = self.treeMine.Jet_btagCSVM_SF_up
                    self.fJetCSVMSF_Down = self.treeMine.Jet_btagCSVM_SF_down
                    self.fJetCSVTSF = self.treeMine.Jet_btagCSVT_SF
                    self.fJetCSVTSF_Up = self.treeMine.Jet_btagCSVT_SF_up
                    self.fJetCSVTSF_Down = self.treeMine.Jet_btagCSVT_SF_down
                    self.fJetCMVALSF = self.treeMine.Jet_btagCMVAV2L_SF
                    self.fJetCMVALSF_Up = self.treeMine.Jet_btagCMVAV2L_SF_up
                    self.fJetCMVALSF_Down = self.treeMine.Jet_btagCMVAV2L_SF_down
                    self.fJetCMVAMSF = self.treeMine.Jet_btagCMVAV2M_SF
                    self.fJetCMVAMSF_Up = self.treeMine.Jet_btagCMVAV2M_SF_up
                    self.fJetCMVAMSF_down = self.treeMine.Jet_btagCMVAV2M_SF_down
                    self.fJetCMVATSF = self.treeMine.Jet_btagCMVAV2T_SF
                    self.fJetCMVATSF_Up = self.treeMine.Jet_btagCMVAV2T_SF_up
                    self.fJetCMVATSF_Down = self.treeMine.Jet_btagCMVAV2T_SF_down
                    self.fJetCorrJER = self.treeMine.Jet_corr_JER
                    self.fJetCorrJERUp = self.treeMine.Jet_corr_JERUp
                    self.fJetCorrJERDown = self.treeMine.Jet_corr_JERDown
                    self.genBH = self.treeMine.GenJet_numBHadrons
                    self.genCH = self.treeMine.GenJet_numCHadrons
                    if len(self.genBH) > 0:
                        self.genJet1BH[0] = self.genBH[0]
                    if len(self.genCH) > 0:
                        self.genjet1CH[0] = self.genCH[0]
                    if len(self.genBH) > 1:
                        self.genjet2BH[0] = self.genBH[1]
                    if len(self.genCH) > 1:
                        self.genjet2CH[0] = self.genCH[1]
                    self.fjUngroomedFlavour = self.treeMine.FatjetAK08ungroomed_Flavour
                    self.fjUngroomedBHadron = self.treeMine.FatjetAK08ungroomed_BhadronFlavour
                    self.fjUngroomedCHadron = self.treeMine.FatjetAK08ungroomed_ChadronFlavour
                    self.fjUngroomedJER = self.treeMine.FatjetAK08ungroomed_GenPt
                    self.puweight = self.treeMine.puWeight
                    self.puweightUp = self.treeMine.puWeightUp
                    self.puweightDown = self.treeMine.puWeightDown
                    self.hPt = self.treeMine.GenHiggsBoson_pt
                    self.hEta = self.treeMine.GenHiggsBoson_eta
                    self.hPhi = self.treeMine.GenHiggsBoson_phi
                    self.hMass = self.treeMine.GenHiggsBoson_mass
                    self.nTInt = self.treeMine.nTrueInt
                if self.saveTrig == 'True':
		    self.HLT_PFHT900_v[0] = self.treeMine.HLT_BIT_HLT_PFHT900_v
                    self.HLT_PFHT800_v[0] = self.treeMine.HLT_BIT_HLT_PFHT800_v
                    self.HLT_PFJet80_v[0] = self.treeMine.HLT_BIT_HLT_PFJet80_v
                    self.HLT_QuadJet45_TripleBTagCSV_p087_v[0] = self.treeMine.HLT_BIT_HLT_QuadJet45_TripleBTagCSV_p087_v
                    self.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v[0] = self.treeMine.HLT_BIT_HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
     		    self.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0] = self.treeMine.HLT_BIT_HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v
                    self.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] = self.treeMine.HLT_BIT_HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v
                    self.HLT_AK8PFJet360_TrimMass30_v[0] = self.treeMine.HLT_BIT_HLT_AK8PFJet360_TrimMass30_v
                    self.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] = self.treeMine.HLT_BIT_HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v
		    self.HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v[0] = self.treeMine.HLT_BIT_HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v
                    self.HLT_PFJet140_v[0] = self.treeMine.HLT_BIT_HLT_PFJet140_v
                    self.HLT_PFJet200_v[0] = self.treeMine.HLT_BIT_HLT_PFJet200_v
                    self.HLT_PFJet260_v[0] = self.treeMine.HLT_BIT_HLT_PFJet260_v
                    self.HLT_Mu24_eta2p1_v[0] = self.treeMine.HLT_BIT_HLT_Mu24_eta2p1_v
                    self.HLT_Mu27_v[0] = self.treeMine.HLT_BIT_HLT_Mu27_v
                    self.HLT_Ele105_CaloIdVT_GsfTrkIdT_v[0] = self.treeMine.HLT_BIT_HLT_Ele105_CaloIdVT_GsfTrkIdT_v

     
                #saving whether an event passes desired trigger (bb = HT800 pass, sj = pass any of the five saved triggers
                self.matched = 0
                self.matchedsj = 0
                if self.saveTrig == 'True':
                    if self.HLT_PFHT800_v[0] > 0 or self.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0] > 0 or self.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] > 0 or self.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] > 0 or self.HLT_AK8PFJet360_TrimMass30_v[0] > 0:
                        self.matched += 1
            
                self.triggerpassbb[0] = self.matched


                #trigger weights
                self.hT =0
                for i in range(0,self.fNJets):
                    if abs(self.fJetEta[i])<3 and self.fJetPt[i] >40 :
                        self.hT=self.hT+self.fJetPt[i]

                self.ht[0] = self.hT
                self.trigWeight[0] = trigger_function(self.histo_efficiency, int(round(self.hT)))
                self.trigWeightUp[0] = trigger_function(self.histo_efficiency_up, int(round(self.hT)))
                self.trigWeightDown[0] = trigger_function(self.histo_efficiency_down, int(round(self.hT)))
                self.trigWeight2Up[0] = trigger_function(self.histo_efficiency_2up, int(round(self.hT)))
                self.trigWeight2Down[0] = trigger_function(self.histo_efficiency_2down, int(round(self.hT)))
	 
                #json for data
                self.bbj.Fill(self.triggerpassbb[0])
                if self.Data and self.treeMine.json < 1:
                    continue
                self.bb0.Fill(self.triggerpassbb[0])

                #Determining the number of medium working point AK4 btags
                self.nbtagMWP = 0
                self.btagCSV = self.treeMine.Jet_btagCSV
                for i in range(0,self.fNJets):
                    if self.btagCSV[i] > 0.8:
                        self.nbtagMWP += 1
                self.nAK04btagsMWP[0] = self.nbtagMWP
                #Calculating DeltaPhi between met for 4 leading pT AK4 jets
                self.Jet_phi = self.treeMine.Jet_phi
                self.met_phi = self.treeMine.met_phi
                if self.fNJets > 0:
                    if abs(self.Jet_phi[0] - self.met_phi) > 3.14159265359:
                        self.DeltaPhi1[0] = abs(2*3.14159265359 - abs(self.met_phi - self.Jet_phi[0]))
                    elif abs(self.Jet_phi[0] - self.met_phi) < 3.14159265359:
                        self.DeltaPhi1[0] = abs(self.Jet_phi[0] - self.met_phi)
                if self.fNJets > 1:
                    if abs(self.Jet_phi[1] - self.met_phi) > 3.14159265359:
                        self.DeltaPhi2[0] = abs(2*3.14159265359 - abs(self.met_phi - self.Jet_phi[1]))
                    elif abs(self.Jet_phi[1] - self.met_phi) < 3.14159265359:
                        self.DeltaPhi2[0] = abs(self.Jet_phi[1] - self.met_phi)
                if self.fNJets > 2:
                    if abs(self.Jet_phi[2] - self.met_phi) > 3.14159265359:
                        self.DeltaPhi3[0] = abs(2*3.14159265359 - abs(self.met_phi - self.Jet_phi[2]))
                    elif abs(self.Jet_phi[2] - self.met_phi) < 3.14159265359:
                        self.DeltaPhi3[0] = abs(self.Jet_phi[2] - self.met_phi)
                if self.fNJets > 3:
                    if abs(self.Jet_phi[3] - self.met_phi) > 3.14159265359:
                        self.DeltaPhi4[0] = abs(2*3.14159265359 - abs(self.met_phi - self.Jet_phi[3]))
                    elif abs(self.Jet_phi[3] - self.met_phi) < 3.14159265359:
                        self.DeltaPhi4[0] = abs(self.Jet_phi[3] - self.met_phi)


                #Determining the number of loose working point muons
                self.nLooseMuons = 0
                self.NSelLeptons = self.treeMine.nvLeptons
                self.isPFMuon = self.treeMine.vLeptons_isPFMuon
                self.isGlobalMuon = self.treeMine.vLeptons_isGlobalMuon
                self.isTrackerMuon = self.treeMine.vLeptons_isTrackerMuon

                self.NAdditLeptons = self.treeMine.naLeptons
                self.AdditisPFMuon = self.treeMine.aLeptons_isPFMuon
                self.AdditisGlobalMuon = self.treeMine.aLeptons_isGlobalMuon
                self.AdditisTrackerMuon = self.treeMine.aLeptons_isTrackerMuon
#                for i in range(0,self.NAdditLeptons):
#                    if self.AdditisPFMuon[i] == 1:
#                        if self.AdditisGlobalMuon[i] == 1 or self.AdditisTrackerMuon[i] == 1:
#                                self.nLooseMuons += 1
#
#                self.nLooseMu[0] = self.nLooseMuons

	        self.aLeptons_pT.clear()
       		self.aLeptons_eta.clear()
        	self.aLeptons_phi.clear()
	        self.aLeptons_mass.clear()
	        self.vLeptons_pT.clear()
	        self.vLeptons_eta.clear()
	        self.vLeptons_phi.clear()
	        self.vLeptons_mass.clear()

		#Determining the number of Tight Muons for WTaggerSF
		self.nTightMuons = 0

		self.vLeptons_dxy = self.treeMine.vLeptons_dxy
		self.vLeptons_dz = self.treeMine.vLeptons_dz
		self.vLeptons_nStations = self.treeMine.vLeptons_nStations
		self.vLeptons_nChamberHits = self.treeMine.vLeptons_nChamberHits
		self.vLeptons_pixelHits = self.treeMine.vLeptons_pixelHits
		self.vLeptons_trackerLayers = self.treeMine.vLeptons_trackerLayers
		self.vLeptons_pt_single = self.treeMine.vLeptons_pt
		self.vLeptons_eta_single = self.treeMine.vLeptons_eta
                self.vLeptons_phi_single = self.treeMine.vLeptons_phi
                self.vLeptons_mass_single = self.treeMine.vLeptons_mass
		self.vLeptons_pfRelIso04 = self.treeMine.vLeptons_pfRelIso04
		for i in range(0,self.NSelLeptons):
		    if self.isGlobalMuon[i] == 1 and self.vLeptons_nChamberHits[i] > 0 and self.vLeptons_nStations[i] > 1 and abs(self.vLeptons_dxy[i]) < 0.2 and abs(self.vLeptons_dz[i]) < 0.5 and self.vLeptons_pixelHits[i] > 0 and self.vLeptons_trackerLayers[i] > 5 and self.vLeptons_pt_single[i] > 53 and abs(self.vLeptons_eta_single[i]) < 2.1 and self.vLeptons_pfRelIso04[i] < 0.25:
			self.nTightMuons += 1;
			self.vLeptons_pT.push_back(self.vLeptons_pt_single[i])
                        self.vLeptons_eta.push_back(self.vLeptons_eta_single[i])
                        self.vLeptons_phi.push_back(self.vLeptons_phi_single[i])
                        self.vLeptons_mass.push_back(self.vLeptons_mass_single[i])

                self.aLeptons_dxy = self.treeMine.aLeptons_dxy
                self.aLeptons_dz = self.treeMine.aLeptons_dz
                self.aLeptons_nStations = self.treeMine.aLeptons_nStations
                self.aLeptons_nChamberHits = self.treeMine.aLeptons_nChamberHits
                self.aLeptons_pixelHits = self.treeMine.aLeptons_pixelHits
                self.aLeptons_trackerLayers = self.treeMine.aLeptons_trackerLayers
                self.aLeptons_pt_single = self.treeMine.aLeptons_pt
                self.aLeptons_eta_single = self.treeMine.aLeptons_eta
                self.aLeptons_phi_single = self.treeMine.aLeptons_phi
                self.aLeptons_mass_single = self.treeMine.aLeptons_mass
                self.aLeptons_pfRelIso04 = self.treeMine.aLeptons_pfRelIso04
                for i in range(0,self.NAdditLeptons):
                    if self.AdditisGlobalMuon[i] == 1 and self.aLeptons_nChamberHits[i] > 0 and self.aLeptons_nStations[i] > 1 and abs(self.aLeptons_dxy[i]) < 0.2 and abs(self.aLeptons_dz[i]) < 0.5 and self.aLeptons_pixelHits[i] > 0 and self.aLeptons_trackerLayers[i] > 5 and self.aLeptons_pt_single[i] > 53 and abs(self.aLeptons_eta_single[i]) < 2.1 and self.aLeptons_pfRelIso04[i] < 0.25:
                        self.nTightMuons += 1;
                        self.aLeptons_pT.push_back(self.aLeptons_pt_single[i])
                        self.aLeptons_eta.push_back(self.aLeptons_eta_single[i])
                        self.aLeptons_phi.push_back(self.aLeptons_phi_single[i])
                        self.aLeptons_mass.push_back(self.aLeptons_mass_single[i])

		self.nTightMu[0] = self.nTightMuons
		#Determing the number of Loose Muons for WTaggerSF
                self.nLooseMuons = 0

#                self.vLeptons_dxy = self.treeMine.vLeptons_dxy
#                self.vLeptons_dz = self.treeMine.vLeptons_dz
#                self.vLeptons_nStations = self.treeMine.vLeptons_nStations
#                self.vLeptons_nChamberHits = self.treeMine.vLeptons_nChamberHits
#                self.vLeptons_pixelHits = self.treeMine.vLeptons_pixelHits
#                self.vLeptons_trackerLayers = self.treeMine.vLeptons_trackerLayers
#                self.vLeptons_pt = self.treeMine.vLeptons_pt
#                self.vLeptons_eta = self.treeMine.vLeptons_eta
#                self.vLeptons_pfRelIso04 = self.treeMine.vLeptons_pfRelIso04
                for i in range(0,self.NSelLeptons):
                    if self.isGlobalMuon[i] == 1 and self.vLeptons_nChamberHits[i] > 0 and self.vLeptons_nStations[i] > 1 and abs(self.vLeptons_dxy[i]) < 0.2 and abs(self.vLeptons_dz[i]) < 0.5 and self.vLeptons_pixelHits[i] > 0 and self.vLeptons_trackerLayers[i] > 5 and self.vLeptons_pt_single[i] > 20 and abs(self.vLeptons_eta_single[i]) < 2.1 and self.vLeptons_pfRelIso04[i] < 0.25:
                        self.nLooseMuons += 1;

#                self.aLeptons_dxy = self.treeMine.aLeptons_dxy
#                self.aLeptons_dz = self.treeMine.aLeptons_dz
#                self.aLeptons_nStations = self.treeMine.aLeptons_nStations
#                self.aLeptons_nChamberHits = self.treeMine.aLeptons_nChamberHits
#                self.aLeptons_pixelHits = self.treeMine.aLeptons_pixelHits
#                self.aLeptons_trackerLayers = self.treeMine.aLeptons_trackerLayers
#                self.aLeptons_pt = self.treeMine.aLeptons_pt
#                self.aLeptons_eta = self.treeMine.aLeptons_eta
#                self.aLeptons_pfRelIso04 = self.treeMine.aLeptons_pfRelIso04
                for i in range(0,self.NAdditLeptons):
                    if self.AdditisGlobalMuon[i] == 1 and self.aLeptons_nChamberHits[i] > 0 and self.aLeptons_nStations[i] > 1 and abs(self.aLeptons_dxy[i]) < 0.2 and abs(self.aLeptons_dz[i]) < 0.5 and self.aLeptons_pixelHits[i] > 0 and self.aLeptons_trackerLayers[i] > 5 and self.aLeptons_pt_single[i] > 20 and abs(self.aLeptons_eta_single[i]) < 2.1 and self.aLeptons_pfRelIso04[i] < 0.25:
                        self.nLooseMuons += 1;

		self.nLooseMu[0] = self.nLooseMuons

		#Determining the number of tight electrons for WTaggerSF
                self.nTightElectrons = 0

                self.vetaSc = self.treeMine.vLeptons_etaSc
                self.vrelIso03 = self.treeMine.vLeptons_relIso03
                self.veleSieie = self.treeMine.vLeptons_eleSieie
                self.veleDEta = self.treeMine.vLeptons_eleDEta
                self.veleDPhi = self.treeMine.vLeptons_eleDPhi
                self.veleHoE = self.treeMine.vLeptons_eleHoE
                self.veleExpMissingInnerHits = self.treeMine.vLeptons_eleExpMissingInnerHits
                self.vLeptons_lostHits = self.treeMine.vLeptons_lostHits
                self.vLeptons_dr03TkSumPt = self.treeMine.vLeptons_dr03TkSumPt

                self.aetaSc = self.treeMine.aLeptons_etaSc
                self.arelIso03 = self.treeMine.aLeptons_relIso03
                self.aeleSieie = self.treeMine.aLeptons_eleSieie
                self.aeleDEta = self.treeMine.aLeptons_eleDEta
                self.aeleDPhi = self.treeMine.aLeptons_eleDPhi
                self.aeleHoE = self.treeMine.aLeptons_eleHoE
                self.aeleExpMissingInnerHits = self.treeMine.aLeptons_eleExpMissingInnerHits
		self.aLeptons_lostHits = self.treeMine.aLeptons_lostHits
		self.aLeptons_dr03TkSumPt = self.treeMine.aLeptons_dr03TkSumPt

                for i in range(0,self.NSelLeptons):
                    if abs(self.vetaSc[i]) < 1.4442:
                        if self.vLeptons_pt_single[i] > 120 and abs(self.veleDEta[i]) < 0.004 and abs(self.veleDPhi[i]) < 0.06 and self.vLeptons_dr03TkSumPt[i] < 5 and self.vLeptons_lostHits[i] < 2 and abs(self.vLeptons_dxy[i]) < 0.02:
                                self.nTightElectrons += 1
	                        self.vLeptons_pT.push_back(self.vLeptons_pt_single[i])
        	                self.vLeptons_eta.push_back(self.vLeptons_eta_single[i])
                	        self.vLeptons_phi.push_back(self.vLeptons_phi_single[i])
                        	self.vLeptons_mass.push_back(self.vLeptons_mass_single[i])

		for i in range(0,self.NAdditLeptons):
		    if abs(self.aetaSc[i]) < 1.4442:
			if self.aLeptons_pt_single[i] > 120 and abs(self.aeleDEta[i]) < 0.004 and abs(self.aeleDPhi[i]) < 0.06 and self.aLeptons_dr03TkSumPt[i] < 5 and self.aLeptons_lostHits[i] < 2 and abs(self.aLeptons_dxy[i]) < 0.02:
				self.nTightElectrons += 1
	                        self.aLeptons_pT.push_back(self.aLeptons_pt_single[i])
        	                self.aLeptons_eta.push_back(self.aLeptons_eta_single[i])
                	        self.aLeptons_phi.push_back(self.aLeptons_phi_single[i])
                        	self.aLeptons_mass.push_back(self.aLeptons_mass_single[i])

                for i in range(0,self.NSelLeptons):
                    if 1.566 < abs(self.vetaSc[i]) < 2.5:
                        if self.vLeptons_pt_single[i] > 120 and abs(self.veleDEta[i]) < 0.006 and abs(self.veleDPhi[i]) < 0.06 and self.veleSieie[i] < 0.03 and self.vLeptons_dr03TkSumPt[i] < 5 and self.vLeptons_lostHits[i] < 2 and abs(self.vLeptons_dxy[i]) < 0.05:
                                self.nTightElectrons += 1
	                        self.vLeptons_pT.push_back(self.vLeptons_pt_single[i])
        	                self.vLeptons_eta.push_back(self.vLeptons_eta_single[i])
                	        self.vLeptons_phi.push_back(self.vLeptons_phi_single[i])
                        	self.vLeptons_mass.push_back(self.vLeptons_mass_single[i])

                for i in range(0,self.NAdditLeptons):
                    if 1.566 < abs(self.aetaSc[i]) < 2.5:
                        if self.aLeptons_pt_single[i] > 120 and abs(self.aeleDEta[i]) < 0.006 and abs(self.aeleDPhi[i]) < 0.06 and self.aeleSieie[i] < 0.03 and self.aLeptons_dr03TkSumPt[i] < 5 and self.aLeptons_lostHits[i] < 2 and abs(self.aLeptons_dxy[i]) < 0.05:
                                self.nTightElectrons += 1
	                        self.aLeptons_pT.push_back(self.aLeptons_pt_single[i])
        	                self.aLeptons_eta.push_back(self.aLeptons_eta_single[i])
                	        self.aLeptons_phi.push_back(self.aLeptons_phi_single[i])
                        	self.aLeptons_mass.push_back(self.aLeptons_mass_single[i])

		self.nTightEle[0] = self.nTightElectrons
		#Determining the number of loose working point electrons for WTaggerSF
		self.nLooseElectrons = 0

                for i in range(0,self.NSelLeptons):
                    if abs(self.vetaSc[i]) < 1.4442:
                        if self.vLeptons_pt_single[i] > 35 and abs(self.veleDEta[i]) < 0.004 and abs(self.veleDPhi[i]) < 0.06 and self.vLeptons_dr03TkSumPt[i] < 5 and self.vLeptons_lostHits[i] < 2 and abs(self.vLeptons_dxy[i]) < 0.02:
                                self.nLooseElectrons += 1

                for i in range(0,self.NAdditLeptons):
                    if abs(self.aetaSc[i]) < 1.4442:
                        if self.aLeptons_pt_single[i] > 35 and abs(self.aeleDEta[i]) < 0.004 and abs(self.aeleDPhi[i]) < 0.06 and self.aLeptons_dr03TkSumPt[i] < 5 and self.aLeptons_lostHits[i] < 2 and abs(self.aLeptons_dxy[i]) < 0.02:
                                self.nLooseElectrons += 1

                for i in range(0,self.NSelLeptons):
                    if 1.566 < abs(self.vetaSc[i]) < 2.5:
                        if self.vLeptons_pt_single[i] > 35 and abs(self.veleDEta[i]) < 0.006 and abs(self.veleDPhi[i]) < 0.06 and self.veleSieie[i] < 0.03 and self.vLeptons_dr03TkSumPt[i] < 5 and self.vLeptons_lostHits[i] < 2 and abs(self.vLeptons_dxy[i]) < 0.05:
                                self.nLooseElectrons += 1

                for i in range(0,self.NAdditLeptons):
                    if 1.566 < abs(self.aetaSc[i]) < 2.5:
                        if self.aLeptons_pt_single[i] > 35 and abs(self.aeleDEta[i]) < 0.006 and abs(self.aeleDPhi[i]) < 0.06 and self.aeleSieie[i] < 0.03 and self.aLeptons_dr03TkSumPt[i] < 5 and self.aLeptons_lostHits[i] < 2 and abs(self.aLeptons_dxy[i]) < 0.05:
                                self.nLooseElectrons += 1

		self.nLooseEle[0] = self.nLooseElectrons


                #Determining the number of loose working point electrons
#                self.nLooseElectrons = 0
#                self.SetaSc = self.treeMine.selLeptons_etaSc
#                self.SrelIso03 = self.treeMine.selLeptons_relIso03
#                self.SeleSieie = self.treeMine.selLeptons_eleSieie
#                self.SeleDEta = self.treeMine.selLeptons_eleDEta
#                self.SeleDPhi = self.treeMine.selLeptons_eleDPhi
#                self.SeleHoE = self.treeMine.selLeptons_eleHoE
#                self.SeleExpMissingInnerHits = self.treeMine.selLeptons_eleExpMissingInnerHits
#                self.SeleooEmooP = self.treeMine.selLeptons_eleooEmooP
#                self.AetaSc = self.treeMine.aLeptons_etaSc
#                self.ArelIso03 = self.treeMine.aLeptons_relIso03
#                self.AeleSieie = self.treeMine.aLeptons_eleSieie
#                self.AeleDEta = self.treeMine.aLeptons_eleDEta
#                self.AeleDPhi = self.treeMine.aLeptons_eleDPhi
#                self.AeleHoE = self.treeMine.aLeptons_eleHoE
#                self.AeleExpMissingInnerHits = self.treeMine.aLeptons_eleExpMissingInnerHits
#                self.AeleooEmooP = self.treeMine.aLeptons_eleooEmooP
#                for i in range(0,self.NAdditLeptons):
#                    if abs(self.AetaSc[i]) <= 1.479:
#                        if self.ArelIso03[i] < 0.0994 and self.AeleSieie[i] < 0.011 and abs(self.AeleDEta[i]) < 0.00477 and abs(self.AeleDPhi[i]) < 0.222 and self.AeleHoE[i] < 0.298 and self.AeleooEmooP[i] < 0.241 and self.AeleExpMissingInnerHits[i] <= 1:
#                        	self.nLooseElectrons += 1
#                    elif abs(self.AetaSc[i]) > 1.479:
#                        if self.ArelIso03[i] < 0.107 and self.AeleSieie[i] < 0.0314 and abs(self.AeleDEta[i]) < 0.00868 and abs(self.AeleDPhi[i]) < 0.213 and self.AeleHoE[i] < 0.101 and self.AeleooEmooP[i] < 0.14 and self.AeleExpMissingInnerHits[i] <= 1:
#                        	self.nLooseElectrons += 1
#
#                self.nLooseEle[0] = self.nLooseElectrons

                #filling an array with jet 4-vectors for jets pt > 30 and |eta| < 2.5, an array of tau21s, and an array of bbtag values, pmass, id, nbhadrons, nchadrons, flavor, l1l2l3 corr, l2l3 corr, JER
                self.jets = []
                self.jets_noL2L3 = []
                self.jet_tau = []
                self.jet_tau1 = []
                self.jet_tau2 = []
                self.jet_tau3 = []
                self.jet_bbtag = []
                self.jet_pmass = []
                self.jet_pmass_noL2L3 = []
                self.jet_pmassunc = []
                self.jet_id = []
                self.jet_nb = []
                self.jet_nc = []
                self.jet_flav = []
                self.jet_123 = []
                self.jet_23 = []
                self.jet_123Unc = []
                self.jet_23Unc = []
                self.jet_JER = []
                self.jet_mass = []
                self.jet_eta = []
                self.jet_muonF= []
                self.jet_EmF=[]
                self.jet_HF=[]
                self.jet_multi=[]
                self.jet_puppi_pt=[]
                self.jet_puppi_eta=[]
                self.jet_puppi_phi=[]
                self.jet_puppi_mass=[]
                self.jet_puppi_tau21=[]
                self.jet_puppi_msoftdrop=[]
                self.jet_puppi_msoftdrop_corrL2L3=[]
                self.jet_puppi_msoftdrop_raw=[]


                for j in range(len(self.fjUngroomedPt)):
                    #print"pt " + str(self.fjUngroomedPt[j])
                    self.jettemp = ROOT.TLorentzVector()
                    self.jettemp.SetPtEtaPhiM(self.fjUngroomedPt[j], self.fjUngroomedEta[j], self.fjUngroomedPhi[j], self.fjUngroomedMass[j])
                    self.jettemp_noL2L3 = ROOT.TLorentzVector()
                    self.jettemp_noL2L3.SetPtEtaPhiM(self.fjUngroomedPt[j], self.fjUngroomedEta[j], self.fjUngroomedPhi[j], self.fjUngroomedMass[j])
                    if (self.syst=="FJEC_Up"):
                            self.correction_factor=1+(self.treeMine.FatjetAK08ungroomed_JEC_UP[j]-self.treeMine.FatjetAK08ungroomed_JEC_L1L2L3[j])
                            self.jettemp*=self.correction_factor
                    if (self.syst=="FJEC_Down"):
                            self.correction_factor=1-(self.treeMine.FatjetAK08ungroomed_JEC_UP[j]-self.treeMine.FatjetAK08ungroomed_JEC_L1L2L3[j])
                            self.jettemp*=self.correction_factor
                    if (self.syst=="FJER_Up"):
                            self.correction_factor=div_except(self.treeMine.FatjetAK08ungroomed_JER_UP_PT[j],self.treeMine.FatjetAK08ungroomed_pt[j])
                            self.jettemp*=self.correction_factor
                    if (self.syst=="FJER_Down"):
                            self.pJERDown=2*self.treeMine.FatjetAK08ungroomed_pt[j]-self.treeMine.FatjetAK08ungroomed_JER_UP_PT[j]
                            self.correction_factor=div_except((self.pJERDown),self.treeMine.FatjetAK08ungroomed_pt[j])
                            self.jettemp*=self.correction_factor
	
	
                    if self.jettemp.Pt() > 225. and abs(self.jettemp.Eta()) < 2.4:
                        self.jets.append(self.jettemp)
                        self.jets_noL2L3.append(self.jettemp_noL2L3)
                        if self.fjUngroomedTau1[j] > 0:
                            self.jet_tau.append(self.fjUngroomedTau2[j]/self.fjUngroomedTau1[j])
                        else:
                            self.jet_tau.append(100)
                        self.jet_tau1.append(self.fjUngroomedTau1[j])
                        self.jet_tau2.append(self.fjUngroomedTau2[j])
                        self.jet_tau3.append(self.fjUngroomedTau3[j])
                        self.mpruned_syst=self.fjUngroomedPrunedMass[j]
                        if (self.syst=="MJEC_Down"):
                            self.sigma=self.treeMine.FatjetAK08ungroomed_JEC_L2L3_UP[j]-self.treeMine.FatjetAK08ungroomed_JEC_L2L3[j]
                            self.mpruned_syst=self.treeMine.FatjetAK08ungroomed_mpruned[j]*(self.treeMine.FatjetAK08ungroomed_JEC_L2L3[j]-self.sigma)
                        if (self.syst=="MJEC"):
                            self.mpruned_syst=self.treeMine.FatjetAK08ungroomed_mpruned[j]*self.treeMine.FatjetAK08ungroomed_JEC_L2L3[j]

                        self.jet_bbtag.append(self.fjUngroomedBbTag[j])
                        self.jet_pmass.append(self.mpruned_syst)
                        self.jet_pmassunc.append(self.fjUngroomedPrunedMass_Unc[j])
                        self.jet_pmass_noL2L3.append(self.fjUngroomedPrunedMass[j])
                        self.jet_id.append(self.fjUngroomedJetID[j])
                        self.jet_mass.append(self.fjUngroomedMass[j])
                        self.jet_eta.append(self.treeMine.FatjetAK08ungroomed_eta[j])
                        self.jet_muonF.append(self.treeMine.FatjetAK08ungroomed_muonEnergyFraction[j])
                        self.jet_EmF.append(self.treeMine.FatjetAK08ungroomed_neutralEmEnergyFraction[j])
                        self.jet_HF.append(self.treeMine.FatjetAK08ungroomed_neutralHadronEnergyFraction[j])
                        self.jet_multi.append(self.treeMine.FatjetAK08ungroomed_chargedMultiplicity[j])
                        self.jet_puppi_pt.append(self.treeMine.FatjetAK08ungroomed_puppi_pt[j])
                        self.jet_puppi_eta.append(self.treeMine.FatjetAK08ungroomed_puppi_eta[j])
                        self.jet_puppi_phi.append(self.treeMine.FatjetAK08ungroomed_puppi_phi[j])
                        self.jet_puppi_mass.append(self.treeMine.FatjetAK08ungroomed_puppi_mass[j])
                        if self.treeMine.FatjetAK08ungroomed_puppi_tau1[j]>0:
                            self.jet_puppi_tau21.append(self.treeMine.FatjetAK08ungroomed_puppi_tau2[j]/self.treeMine.FatjetAK08ungroomed_puppi_tau1[j])
                        else:
                            self.jet_puppi_tau21.append(100)
                        self.jet_puppi_msoftdrop.append(self.treeMine.FatjetAK08ungroomed_puppi_msoftdrop[j])
                        self.jet_puppi_msoftdrop_corrL2L3.append(self.treeMine.FatjetAK08ungroomed_puppi_msoftdrop_corrL2L3[j])
                        self.jet_puppi_msoftdrop_raw.append(self.treeMine.FatjetAK08ungroomed_puppi_msoftdrop_raw[j])


                        if self.isMC == 'True':
                            self.jet_nb.append(self.fjUngroomedBHadron[j])
                            self.jet_nc.append(self.fjUngroomedCHadron[j])
                            self.jet_flav.append(self.fjUngroomedFlavour[j])
                            self.jet_JER.append(self.fjUngroomedJER[j])
                        self.jet_123.append(self.fjL1L2L3[j])
                        self.jet_23.append(self.fjL2L3[j])
                        self.jet_123Unc.append(self.fjL1L2L3Unc[j])
                        self.jet_23Unc.append(self.fjL2L3Unc[j])

                        
                        
                            
                        
        
                if len(self.jets) < 1: # one jet with pt > 250 and |eta| < 2.4
                    continue
 
                self.bb1.Fill(self.triggerpassbb[0])

                #dEta selection : selecting the two jets which minimizes the dEta requirement. (to find a better one?)
                self.idxH1 = -1
                self.idxH2=-1
#                if len(self.jets) > 1 and (abs(self.jets[0].Eta() - self.jets[1].Eta()) < 1.3):
#                    self.minDEta = abs(self.jets[0].Eta() - self.jets[1].Eta())
#                    self.idxH1 = 0
#                    self.idxH2 = 1
#                elif len(self.jets) > 2 and (abs(self.jets[0].Eta() - self.jets[2].Eta()) < 1.3):
#                    self.minDEta = abs(self.jets[0].Eta() - self.jets[2].Eta())
#                    self.idxH1 = 0
#                    self.idxH2 = 2
#                elif len(self.jets) > 2 and (abs(self.jets[1].Eta() - self.jets[2].Eta()) < 1.3):
#                    self.minDEta = abs(self.jets[1].Eta() - self.jets[2].Eta())
#                    self.idxH1 = 1
#                    self.idxH2 = 2
#                elif len(self.jets) > 3 and (abs(self.jets[0].Eta() - self.jets[3].Eta()) < 1.3):
#                    self.minDEta = abs(self.jets[0].Eta() - self.jets[3].Eta())
#                    self.idxH1 = 0
#                    self.idxH2 = 3
#                elif len(self.jets) > 3 and (abs(self.jets[1].Eta() - self.jets[3].Eta()) < 1.3):
#                    self.minDEta = abs(self.jets[1].Eta() - self.jets[3].Eta())
#                    self.idxH1 = 1
#                    self.idxH2 = 3
#                elif len(self.jets) > 3 and (abs(self.jets[2].Eta() - self.jets[3].Eta()) < 1.3):
#                    self.minDEta = abs(self.jets[2].Eta() - self.jets[3].Eta())
#                    self.idxH1 = 2
#                    self.idxH2 = 3
                if len(self.jets) > 1:
                    self.idxH1 = 0
                    self.idxH2 = 1

                if len(self.jets) == 1:
                    self.idxH1 = 0
  
                self.nFills += 1

                #higgs tagging - matching higgs gen jet to the 1 and 2 pt jet
                if self.isMC == 'True':
                    self.hjets = []
                    for j in range(len(self.hPt)):
                        self.jettemp = ROOT.TLorentzVector()
                        self.jettemp.SetPtEtaPhiM(self.hPt[j], self.hEta[j], self.hPhi[j], self.hMass[j])
                        self.hjets.append(self.jettemp)

                        self.h1 = MatchCollection(self.hjets, self.jets[self.idxH1])

                        if len(self.jets) > 1:
                            self.h2 = MatchCollection(self.hjets, self.jets[self.idxH2])

                        self.nHiggsTags[0] = 0
                        if self.h1 > -1:
                            self.nHiggsTags[0] += 1
                        if len(self.jets) > 1:
                            if self.h2 > -1:
                                self.nHiggsTags[0] += 1
         
                    if len(self.hPt) > 1:
                        self.genh1 = ROOT.TLorentzVector()
                        self.genh2 = ROOT.TLorentzVector()
                        self.genh1.SetPtEtaPhiM(self.hPt[0], self.hEta[0], self.hPhi[0], self.hMass[0])
                        self.genh2.SetPtEtaPhiM(self.hPt[1], self.hEta[1], self.hPhi[1], self.hMass[1])
                        self.genmhh = (self.genh1 + self.genh2).M()
                    
                        self.mhh[0] = self.genmhh
                        self.P1boost = self.genh1
                        self.P12 = self.genh1 + self.genh2
                        self.P1boost.Boost(-self.P12.BoostVector()) 
                        self.thetast = self.P1boost.Theta()
                        self.costhetastvar = self.P1boost.CosTheta()
                        self.costhetast[0] = abs(self.costhetastvar)
                        

                self.maxcsv1 = -100
                self.maxcmva1 = -100
                self.maxcsv2 = -100
                self.maxcmva2 = -100
                self.jet1FoundNearby = 0
                self.jet2FoundNearby = 0
                for j in range(len(self.treeMine.Jet_pt)):
                    self.jettemp = ROOT.TLorentzVector()
                    self.jettemp.SetPtEtaPhiM(self.treeMine.Jet_pt[j], self.treeMine.Jet_eta[j], self.treeMine.Jet_phi[j], self.treeMine.Jet_mass[j])
                    self.cmva = self.treeMine.Jet_btagCMVAV2[j]
                    self.csv = self.treeMine.Jet_btagCSVV0[j]
                    if self.jets[self.idxH1].DeltaR(self.jettemp) > math.pi/2:
                        self.jet1FoundNearby = 1
                        if self.csv > self.maxcsv1:
                            self.jet1NearbyJetcsvpt = self.treeMine.Jet_pt[j]
                            self.jet1NearbyJetcsveta = self.treeMine.Jet_eta[j]
                            self.jet1NearbyJetcsvphi = self.treeMine.Jet_phi[j]
                            self.jet1NearbyJetcsvmass = self.treeMine.Jet_mass[j]
                            self.jet1NJCSV = self.csv
                            self.maxcsv1 = self.csv
                        if self.cmva > self.maxcmva1:
                            self.jet1NearbyJetcmvapt = self.treeMine.Jet_pt[j]
                            self.jet1NearbyJetcmvaeta = self.treeMine.Jet_eta[j]
                            self.jet1NearbyJetcmvaphi = self.treeMine.Jet_phi[j]
                            self.jet1NearbyJetcmvamass = self.treeMine.Jet_mass[j]
                            self.jet1NJCMVA = self.cmva
                            self.maxcmva1 = self.cmva
                    if len(self.jets) > 1:
                        if self.jets[self.idxH2].DeltaR(self.jettemp) > math.pi/2:
                            self.jet2FoundNearby = 1
                            if self.csv > self.maxcsv2:
                                self.jet2NearbyJetcsvpt = self.treeMine.Jet_pt[j]
                                self.jet2NearbyJetcsveta = self.treeMine.Jet_eta[j]
                                self.jet2NearbyJetcsvphi = self.treeMine.Jet_phi[j]
                                self.jet2NearbyJetcsvmass = self.treeMine.Jet_mass[j]
                                self.jet2NJCSV = self.csv
                                self.maxcsv2 = self.csv
                            if self.cmva > self.maxcmva2:
                                self.jet2NearbyJetcmvapt = self.treeMine.Jet_pt[j]
                                self.jet2NearbyJetcmvaeta = self.treeMine.Jet_eta[j]
                                self.jet2NearbyJetcmvaphi = self.treeMine.Jet_phi[j]
                                self.jet2NearbyJetcmvamass = self.treeMine.Jet_mass[j]
                                self.jet2NJCMVA = self.cmva
                                self.maxcmva2 = self.cmva
                
                if self.jet1FoundNearby == 1:
                    self.jet1NearbyJetcsvArray[0] = self.jet1NearbyJetcsvpt
                    self.jet1NearbyJetcsvArray[1] = self.jet1NearbyJetcsveta
                    self.jet1NearbyJetcsvArray[2] = self.jet1NearbyJetcsvphi
                    self.jet1NearbyJetcsvArray[3] = self.jet1NearbyJetcsvmass
                    self.jet1NJcsv[0] = self.jet1NJCSV
                    self.jet1NearbyJetcmvaArray[0] = self.jet1NearbyJetcmvapt
                    self.jet1NearbyJetcmvaArray[1] = self.jet1NearbyJetcmvaeta
                    self.jet1NearbyJetcmvaArray[2] = self.jet1NearbyJetcmvaphi
                    self.jet1NearbyJetcmvaArray[3] = self.jet1NearbyJetcmvamass
                    self.jet1NJcmva[0] = self.jet1NJCMVA
                if self.jet2FoundNearby == 1:
                    self.jet2NearbyJetcsvArray[0] = self.jet2NearbyJetcsvpt
                    self.jet2NearbyJetcsvArray[1] = self.jet2NearbyJetcsveta
                    self.jet2NearbyJetcsvArray[2] = self.jet2NearbyJetcsvphi
                    self.jet2NearbyJetcsvArray[3] = self.jet2NearbyJetcsvmass
                    self.jet2NJcsv[0] = self.jet2NJCSV
                    self.jet2NearbyJetcmvaArray[0] = self.jet2NearbyJetcmvapt
                    self.jet2NearbyJetcmvaArray[1] = self.jet2NearbyJetcmvaeta
                    self.jet2NearbyJetcmvaArray[2] = self.jet2NearbyJetcmvaphi
                    self.jet2NearbyJetcmvaArray[3] = self.jet2NearbyJetcmvamass
                    self.jet2NJcmva[0] = self.jet2NJCMVA


                #evaluating regressed pt
                self.this_pt[0]=self.jets[self.idxH1].Pt()
                self.this_pv[0]= self.treeMine.nPVs
                self.this_eta[0]=self.jet_eta[self.idxH1]
                self.this_mass[0]=self.jet_mass[self.idxH1]
                self.this_muonF[0]=self.jet_muonF[self.idxH1]
                self.this_EmF[0] =self.jet_EmF[self.idxH1]
                self.this_HF[0]=self.jet_HF[self.idxH1]
                self.this_multi[0]=self.jet_multi[self.idxH1]
                self.regressedJetpT_0[0]=(self.reader.EvaluateRegression("BDTG method"))[0]
                if len(self.jets) > 1:
                    self.this_pt[0]=self.jets[self.idxH2].Pt()
                    self.this_eta[0]=self.jet_eta[self.idxH2]
                    self.this_mass[0]=self.jet_mass[self.idxH2]
                    self.this_muonF[0]=self.jet_muonF[self.idxH2]
                    self.this_EmF[0] =self.jet_EmF[self.idxH2]
                    self.this_HF[0]=self.jet_HF[self.idxH2]
                    self.this_multi[0]=self.jet_multi[self.idxH2]
                    self.regressedJetpT_1[0]=(self.reader.EvaluateRegression("BDTG method"))[0]
	

                #filling jet variables
                self.jet1pmass[0] = self.jet_pmass[self.idxH1]
                self.jet1pmassunc[0] = self.jet_pmassunc[self.idxH1]
                self.jet1pmass_noL2L3[0] = self.jet_pmass_noL2L3[self.idxH1]
                if len(self.jets) > 1:
                    self.jet2pmass[0] = self.jet_pmass[self.idxH2]
                    self.jet2pmassunc[0] = self.jet_pmassunc[self.idxH2]
                self.jet1ID[0] = self.jet_id[self.idxH1]
                if len(self.jets) > 1:
                    self.jet2ID[0] = self.jet_id[self.idxH2]
                self.jet1tau21[0] = self.jet_tau[self.idxH1]# fjUngroomedTau2[j1]/fjUngroomedTau1[j1]
                self.jet1tau1[0] = self.jet_tau1[self.idxH1]
                self.jet1tau2[0] = self.jet_tau2[self.idxH1]
                self.jet1tau3[0] = self.jet_tau3[self.idxH1]
                if len(self.jets) > 1:
                    self.jet2tau21[0] = self.jet_tau[self.idxH2]# fjUngroomedTau2[j2]/fjUngroomedTau1[j2]
                    self.jet2tau1[0] = self.jet_tau1[self.idxH2]
                    self.jet2tau2[0] = self.jet_tau2[self.idxH2]
                    self.jet2tau3[0] = self.jet_tau3[self.idxH2]
                if self.isMC == 'True':
                    self.jet1nbHadron[0] = self.jet_nb[self.idxH1]
                    if len(self.jets) > 1:
                        self.jet2nbHadron[0] = self.jet_nb[self.idxH2]
                    self.jet1ncHadron[0] = self.jet_nc[self.idxH1]
                    if len(self.jets) > 1:
                        self.jet2ncHadron[0] = self.jet_nc[self.idxH2]
                    self.jet1flavor[0] = self.jet_flav[self.idxH1]
                    if len(self.jets) > 1:
                        self.jet2flavor[0] = self.jet_flav[self.idxH2]
                    self.jet1JER[0] = self.jet_JER[self.idxH1]
                    if len(self.jets) > 1:
                        self.jet2JER[0] = self.jet_JER[self.idxH2]
                self.jet1l1l2l3[0] = self.jet_123[self.idxH1]
                if len(self.jets) > 1:
                    self.jet2l1l2l3[0] = self.jet_123[self.idxH2]
                self.jet1l2l3[0] = self.jet_23[self.idxH1]
                if len(self.jets) > 1:
                    self.jet2l2l3[0] = self.jet_23[self.idxH2]
                self.jet1l1l2l3Unc[0] = self.jet_123Unc[self.idxH1]
                if len(self.jets) > 1:
                    self.jet2l1l2l3Unc[0] = self.jet_123Unc[self.idxH2]
                self.jet1l2l3Unc[0] = self.jet_23Unc[self.idxH1]
                if len(self.jets) > 1:
                    self.jet2l2l3Unc[0] = self.jet_23Unc[self.idxH2]

                self.CA15jets = []
                for j in range(len(self.FatjetCA15ungroomed_pt)):
                    self.jettemp = ROOT.TLorentzVector()
                    self.jettemp.SetPtEtaPhiM(self.FatjetCA15ungroomed_pt[j], self.FatjetCA15ungroomed_eta[j], self.FatjetCA15ungroomed_phi[j], self.FatjetCA15ungroomed_mass[j])
                    self.CA15jets.append(self.jettemp)
                self.cajet1 = MatchCollection(self.CA15jets, self.jets[self.idxH1])
                if len(self.jets) > 1:
                    self.cajet2 = MatchCollection2(self.CA15jets, self.jets[self.idxH2],self.cajet1)
                if self.cajet1 > -1:
                    self.CA15jet1pt[0] = self.CA15jets[self.cajet1].Pt()
                    self.CA15jet1eta[0] = self.CA15jets[self.cajet1].Eta()
                    self.CA15jet1phi[0] = self.CA15jets[self.cajet1].Phi()
                    self.CA15jet1mass[0] = self.CA15jets[self.cajet1].M()
                if len(self.jets) > 1:
                    if self.cajet2 > -1:
                        self.CA15jet2pt[0] = self.CA15jets[self.cajet2].Pt()
                        self.CA15jet2eta[0] = self.CA15jets[self.cajet2].Eta()
                        self.CA15jet2phi[0] = self.CA15jets[self.cajet2].Phi()
                        self.CA15jet2mass[0] = self.CA15jets[self.cajet2].M()
                #finding gen jets to match higgs jets
                if self.isMC == 'True':
                    self.ujets = []
                    self.ujetsCH = []
                    self.ujetsBH = []
                    for j in range(len(self.genPt)):
                        self.jettemp = ROOT.TLorentzVector()
                        self.jettemp.SetPtEtaPhiM(self.genPt[j], self.genEta[j], self.genPhi[j], self.genMass[j])
                        self.ujets.append(self.jettemp)
                        self.ujetsCH.append(self.genCH[j])
                        self.ujetsBH.append(self.genBH[j])

                    self.j1 = MatchCollection(self.ujets, self.jets[self.idxH1])
                    if len(self.jets) > 1:
                        self.j2 = MatchCollection2(self.ujets, self.jets[self.idxH2],self.j1)
           
                    #filling gen jet info
		    if len(self.ujets) > 0:
                        self.gen1Pt[0] = self.ujets[self.j1].Pt()
                        self.gen1phi[0] = self.ujets[self.j1].Phi()
                        self.gen1Eta[0] = self.ujets[self.j1].Eta()
                        self.gen1Mass[0] = self.ujets[self.j1].M()
                        self.gen1ID[0] = self.j1
                    if len(self.jets) > 1:
                        self.gen2Pt[0] = self.ujets[self.j2].Pt()
                        self.gen2Phi[0] = self.ujets[self.j2].Phi()
                        self.gen2Eta[0] = self.ujets[self.j2].Eta()
                        self.gen2Mass[0] = self.ujets[self.j2].M()
                        self.gen2ID[0] = self.j2

                self.tPtSums = 0
                if self.isMC == 'True':
                    for pt in self.treeMine.GenTop_pt:
                        self.tPtSums = self.tPtSums + pt
                self.tPtsum[0] = self.tPtSums

                #filling bbtag
                self.jet1bbtag[0] = self.jet_bbtag[self.idxH1] #fjUngroomedBbTag[j1]
                if len(self.jets) > 1:
                    self.jet2bbtag[0] = self.jet_bbtag[self.idxH2] # fjUngroomedBbTag[j2]

                #filling min subjet csv
                self.subjets = []
                self.jet1sj = []
                self.jet1sjcsv = []
                self.jet2sj = []
                self.jet2sjcsv = []
                self.samesj = 0
                for j in range(len(self.sjPrunedPt)):
                    self.jettemp = ROOT.TLorentzVector()
                    self.jettemp.SetPtEtaPhiM(self.sjPrunedPt[j], self.sjPrunedEta[j], self.sjPrunedPhi[j], self.sjPrunedMass[j])
                    self.subjets.append(self.jettemp)

                self.n1sj = -100
                self.n2sj = -100
                if len(self.jets) == 1:
                    for j in range(len(self.subjets)):
                        self.dR1 = self.subjets[j].DeltaR(self.jets[self.idxH1])
                        if self.dR1 < 0.4:
                            self.jet1sj.append(self.subjets[j])
                            self.jet1sjcsv.append(self.sjPrunedBtag[j])
                        self.n1sj = len(self.jet1sj)

                if len(self.jets) > 1:
                    for j in range(len(self.subjets)):
                        self.dR1 = self.subjets[j].DeltaR(self.jets[self.idxH1])
                        self.dR2 = self.subjets[j].DeltaR(self.jets[self.idxH2])
                        if self.dR1 < 0.4 and self.dR2 < 0.4:
                            self.samesj += 1
                        elif self.dR1 < 0.4:
                            self.jet1sj.append(self.subjets[j])
                            self.jet1sjcsv.append(self.sjPrunedBtag[j])
                        elif self.dR2 < 0.4:
                            self.jet2sj.append(self.subjets[j])
                            self.jet2sjcsv.append(self.sjPrunedBtag[j])
                        self.n1sj = len(self.jet1sj)
                        self.n2sj = len(self.jet2sj)

                #Finding the subjet csvs
                self.jet1s1csv[0] = -1.
                self.jet2s1csv[0] = -1.
                self.jet1s2csv[0] = -1.
                self.jet2s2csv[0] = -1.
	
                for i in range(0,4):
                    self.jetSJfla[i] =-1
                    self.jetSJpt[i]  =-1
                    self.jetSJcsv[i] =-1
                    self.jetSJeta[i] =-1

        
                if len(self.jet1sjcsv) > 1:
                    self.jet1s1csv[0] = self.jet1sjcsv[0]
                    self.jet1s2csv[0] = self.jet1sjcsv[1]
                elif len(self.jet1sjcsv) == 1:
                    self.jet1s1csv[0] = self.jet1sjcsv[0]

                if len(self.jet2sjcsv) > 1:
                    self.jet2s1csv[0] = self.jet2sjcsv[0]
                    self.jet2s2csv[0] = self.jet2sjcsv[1]
                elif len(self.jet2sjcsv) == 1:
                    self.jet2s1csv[0] = self.jet2sjcsv[0]
                self.sfsj3 =-1
                self.sfsj4 =-1
                self.sfsj1 =-1
                self.sfsj2 =-1
                self.sfsj3up =-1
                self.sfsj4up =-1
                self.sfsj1up =-1
                self.sfsj2up =-1
                self.sfsj3down =-1
                self.sfsj4down =-1
                self.sfsj1down =-1
                self.sfsj2down =-1

               # print "id " + str(self.idxH1)
               # print "pt id " + str(self.jets[self.idxH1].Pt())
                #writing variables to the tree

		#Matching the leading AK8 jet to a Hadronic W
		if self.isMC == 'True':
		   self.Matched = 0
		   self.FirstQuark = 0
		   self.GenWZQuark_pt = self.treeMine.GenWZQuark_pt
                   self.GenWZQuark_phi = self.treeMine.GenWZQuark_phi
                   self.GenWZQuark_eta = self.treeMine.GenWZQuark_eta
                   self.GenWZQuark_mass = self.treeMine.GenWZQuark_mass
		   for genQ in range(1,len(self.GenWZQuark_pt)+1):
                      self.GenQuark = ROOT.TLorentzVector()
		      self.GenQuark.SetPtEtaPhiM(self.GenWZQuark_pt[genQ-1],self.GenWZQuark_phi[genQ-1],self.GenWZQuark_eta[genQ-1],self.GenWZQuark_mass[genQ-1])
		      self.HadW_dR = abs(self.jets[self.idxH1].DeltaR(self.GenQuark))
		      if self.HadW_dR < 0.8:
			if (genQ%2) == 1:
			   self.FirstQuark = 1
			if (genQ%2) == 0 and self.FirstQuark == 1:
			   self.Matched = 1
			if (genQ%2) == 0:
                           self.FirstQuark = 0
		      else:
                           self.FirstQuark = 0
		   if self.Matched == 1:
		      self.LeadingAK8Jet_MatchedHadW[0] = 1.
		   else:
		      self.LeadingAK8Jet_MatchedHadW[0] = 0.


                self.jet1pt[0] = self.jets[self.idxH1].Pt()
                self.jet1eta[0] = self.jets[self.idxH1].Eta()
                self.jet1phi[0] = self.jets[self.idxH1].Phi()
                self.jet1mass[0] = self.jets[self.idxH1].M()

                self.jet1_puppi_pt[0] = self.jet_puppi_pt[self.idxH1]
                self.jet1_puppi_eta[0] = self.jet_puppi_eta[self.idxH1]
                self.jet1_puppi_phi[0] = self.jet_puppi_phi[self.idxH1]
                self.jet1_puppi_mass[0] = self.jet_puppi_mass[self.idxH1]
                self.jet1_puppi_tau21[0] = self.jet_puppi_tau21[self.idxH1]
                self.jet1_puppi_msoftdrop[0] = self.jet_puppi_msoftdrop[self.idxH1]
                self.jet1_puppi_msoftdrop_corrL2L3[0] = self.jet_puppi_msoftdrop_corrL2L3[self.idxH1]
                self.jet1_puppi_msoftdrop_raw[0] = self.jet_puppi_msoftdrop_raw[self.idxH1]

                self.jet1_puppi_TheaCorr[0] = getPUPPIweight(self.jet_puppi_pt[self.idxH1], self.jet_puppi_eta[self.idxH1], self.puppisd_corrGEN, self.puppisd_corrRECO_cen, self.puppisd_corrRECO_for)

                self.jet1_reg_beforeL2L3 = ROOT.TLorentzVector()
                self.jet1_reg_beforeL2L3.SetPtEtaPhiM(self.jet1pt[0],self.jet1eta[0],self.jet1phi[0], self.jet1pmassunc[0])
                self.jet1_reg_beforeL2L3 = self.jet1_reg_beforeL2L3*(self.regressedJetpT_0[0])
                self.jet1mass_reg_noL2L3[0] = self.jet1_reg_beforeL2L3.M()
                self.jet1_reg =ROOT.TLorentzVector()
                self.jet1_reg.SetPtEtaPhiM(self.jet1pt[0],self.jet1eta[0],self.jet1phi[0],self.jet1pmass[0])
                self.jet1_reg=self.jet1_reg*(self.regressedJetpT_0[0])
                self.jet1pt_reg[0] = self.jet1_reg.Pt()
                self.jet1mass_reg[0] = self.jet1_reg.M()
                self.jet1_ureg =ROOT.TLorentzVector()
                self.jet1_ureg.SetPtEtaPhiM(self.jet1pt[0],self.jet1eta[0],self.jet1phi[0],self.jet1_reg.M())

                self.jet1_pruned =  ROOT.TLorentzVector()
                self.jet1_pruned.SetPtEtaPhiM(self.jet1pt[0],self.jet1eta[0],self.jet1phi[0],self.jet1pmass[0])

                if len(self.jets) > 1:
                    self.jet2pt[0] = self.jets[self.idxH2].Pt()
                    self.jet2eta[0] = self.jets[self.idxH2].Eta()
                    self.jet2phi[0] = self.jets[self.idxH2].Phi()
                    self.jet2mass[0] = self.jets[self.idxH2].M()
                    self.jet2_puppi_pt[0] = self.jet_puppi_pt[self.idxH2]
                    self.jet2_puppi_eta[0] = self.jet_puppi_eta[self.idxH2]
                    self.jet2_puppi_phi[0] = self.jet_puppi_phi[self.idxH2]
                    self.jet2_puppi_mass[0] = self.jet_puppi_mass[self.idxH2]
                    self.jet2_puppi_tau21[0] = self.jet_puppi_tau21[self.idxH2]
                    self.jet2_puppi_msoftdrop[0] = self.jet_puppi_msoftdrop[self.idxH2]
                    self.jet2_puppi_msoftdrop_corrL2L3[0] = self.jet_puppi_msoftdrop_corrL2L3[self.idxH2]
                    self.jet2_puppi_TheaCorr[0] = getPUPPIweight(self.jet_puppi_pt[self.idxH2], self.jet_puppi_eta[self.idxH2],self.puppisd_corrGEN, self.puppisd_corrRECO_cen, self.puppisd_corrRECO_for)
                    self.jet2_puppi_msoftdrop_raw[0] = self.jet_puppi_msoftdrop_raw[self.idxH2]

                    self.jet2_reg_beforeL2L3 = ROOT.TLorentzVector()
                    self.jet2_reg_beforeL2L3.SetPtEtaPhiM(self.jet2pt[0],self.jet2eta[0],self.jet2phi[0], self.jet2pmassunc[0])
                    self.jet2_reg_beforeL2L3 = self.jet2_reg_beforeL2L3*(self.regressedJetpT_1[0])
                    self.jet2mass_reg_noL2L3[0] = self.jet2_reg_beforeL2L3.M()
                    self.jet2_reg =ROOT.TLorentzVector()
                    self.jet2_reg.SetPtEtaPhiM(self.jet2pt[0],self.jet2eta[0],self.jet2phi[0],self.jet2pmass[0])
                    self.jet2_reg=self.jet2_reg*(self.regressedJetpT_1[0])
                    self.jet2pt_reg[0] = self.jet2_reg.Pt()
                    self.jet2mass_reg[0] = self.jet2_reg.M()
                    self.jet2_ureg =ROOT.TLorentzVector()
                    self.jet2_ureg.SetPtEtaPhiM(self.jet2pt[0],self.jet2eta[0],self.jet2phi[0],self.jet2_reg.M())
                    self.etadiff[0] = abs(self.jets[self.idxH1].Eta() - self.jets[self.idxH2].Eta())

                    self.jet2_pruned =  ROOT.TLorentzVector()
                    self.jet2_pruned.SetPtEtaPhiM(self.jet2pt[0],self.jet2eta[0],self.jet2phi[0],self.jet2pmass[0])

                    self.dijetmass[0] = (self.jets[self.idxH1] + self.jets[self.idxH2]).M()
                    self.dijetmass_corr[0] = (self.jets[self.idxH1] + self.jets[self.idxH2]).M() - (self.jet1pmass[0]-125)-(self.jet2pmass[0]-125)
                    self.dijetmass_corr_punc[0] = (self.jets[self.idxH1] + self.jets[self.idxH2]).M() - (self.jet1pmassunc[0]-125)-(self.jet2pmassunc[0]-125)
                    self.dijetmass_reg[0]=(self.jet1_ureg+self.jet2_ureg).M() - (self.jet1mass[0]-125)-(self.jet2mass[0]-125)#(jet1_ureg.M()-125)-(jet2_ureg.M()-125)


                if self.isMC == 'True':
                    self.puWeights[0]= self.puweight
                    self.puWeightsUp[0] = self.puweightUp
                    self.puWeightsDown[0] = self.puweightDown
                    self.nTrueInt[0] = self.nTInt
                    self.xsec[0] = float(self.xsecs)
                self.json[0] = self.JSON
                self.evt[0] = self.EVT
                self.vtype[0] = self.vType
	        self.nPVs[0] = self.treeMine.nPVs	
                if self.Data:
                    self.isData[0] = 1
                else:
                    self.isData[0] = 0

                #handling hbb tagger SFs
                self.sf1Tight = -1
                self.sf2Tight = -1
                self.sf1Tightchangeup = 1000000
                self.sf2Tightchangeup = 1000000
                self.sf1Tightchangedown = 1000000
                self.sf2Tightchangedown = 1000000
                self.sf1Loose = -1
                self.sf2Loose = -1
                self.sf1Loosechangeup = 1000000
                self.sf2Loosechangeup = 1000000
                self.sf1Loosechangedown = 1000000
                self.sf2Loosechangedown = 1000000

                if self.jet1pt[0] >= 250 and self.jet1pt[0] < 350:
                    self.sf1Tight = 0.92
                    self.sf1Tightchangeup = 0.03
                    self.sf1Tightchangedown = 0.03
                    self.sf1Loose = 0.96
                    self.sf1Loosechangeup = 0.03
                    self.sf1Loosechangedown = 0.02
                elif self.jet1pt[0] >= 350 and self.jet1pt[0] < 430:
                    self.sf1Tight = 1.01
                    self.sf1Tightchangeup = 0.03
                    self.sf1Tightchangedown = 0.04
                    self.sf1Loose = 1.00
                    self.sf1Loosechangeup = 0.04
                    self.sf1Loosechangedown = 0.03
                elif self.jet1pt[0] >= 430:
                    self.sf1Tight = 0.92
                    self.sf1Tightchangeup = 0.03
                    self.sf1Tightchangedown = 0.05
                    self.sf1Loose = 1.01
                    self.sf1Loosechangeup = 0.02
                    self.sf1Loosechangedown = 0.04

        
                if len(self.jets) > 1:
                    if self.jet2pt[0] >= 250 and self.jet2pt[0] < 350:
                        self.sf2Tight = 0.92
                        self.sf2Tightchangeup = 0.03
                        self.sf2Tightchangedown = 0.03
                        self.sf2Loose = 0.96
                        self.sf2Loosechangeup = 0.03
                        self.sf2Loosechangedown = 0.02
                    elif self.jet2pt[0] >= 350 and self.jet2pt[0] < 430:
                        self.sf2Tight = 1.01
                        self.sf2Tightchangeup = 0.03
                        self.sf2Tightchangedown = 0.04
                        self.sf2Loose = 1.00
                        self.sf2Loosechangeup = 0.04
                        self.sf2Loosechangedown = 0.03
                    elif self.jet2pt[0] >= 430:
                        self.sf2Tight = 0.92
                        self.sf2Tightchangeup = 0.03
                        self.sf2Tightchangedown = 0.05
                        self.sf2Loose = 1.01
                        self.sf2Loosechangeup = 0.02
                        self.sf2Loosechangedown = 0.04


                self.bbtag1SFTight[0] = self.sf1Tight
                self.bbtag1SFTightUp[0] = self.sf1Tight*(1+self.sf1Tightchangeup)
                self.bbtag1SFTightDown[0] = self.sf1Tight*(1-self.sf1Tightchangedown)
                self.bbtag1SFLoose[0] = self.sf1Loose
                self.bbtag1SFLooseUp[0] = self.sf1Loose*(1+self.sf1Loosechangeup)
                self.bbtag1SFLooseDown[0] = self.sf1Loose*(1-self.sf1Loosechangedown)
                self.SFTight[0] = self.sf1Tight*self.sf2Tight
                self.SFTightup[0] = self.sf1Tight*(1+self.sf1Tightchangeup)*self.sf2Tight*(1+self.sf2Tightchangeup)
                self.SFTightdown[0] = self.sf1Tight*(1-self.sf1Tightchangedown)*self.sf2Tight*(1-self.sf2Tightchangedown)
                self.SFLoose[0] = self.sf1Loose*self.sf2Loose
                self.SFLooseup[0] = self.sf1Loose*(1+self.sf1Loosechangeup)*self.sf2Loose*(1+self.sf2Loosechangeup)
                self.SFLoosedown[0] = self.sf1Loose*(1-self.sf1Loosechangedown)*self.sf2Loose*(1-self.sf2Loosechangedown)
                self.SF4sj[0] = -1
                self.SF4sjUp[0] = -1
                self.SF4sjDown[0] = -1
                if self.n1sj >1 and self.n2sj>1:
                    self.SF4sj[0] = self.sfsj1*self.sfsj2*self.sfsj3*self.sfsj4
                    self.SF4sjUp[0] = self.sfsj1up*self.sfsj2up*self.sfsj3up*self.sfsj4up
                    self.SF4sjDown[0] = self.sfsj1down*self.sfsj2down*self.sfsj3down*self.sfsj4down
                
                self.SF3sj[0] =-1.
                self.SF3sjUp[0] =-1.
                self.SF3sjDown[0] =-1.
	

                self.bbtag2SFTight[0] = self.sf2Tight
                self.bbtag2SFTightUp[0] = self.sf2Tight*(1+self.sf2Tightchangeup)
                self.bbtag2SFTightDown[0] = self.sf2Tight*(1-self.sf2Tightchangedown)
                self.bbtag2SFLoose[0] = self.sf2Loose
                self.bbtag2SFLooseUp[0] = self.sf2Loose*(1+self.sf2Loosechangeup)
                self.bbtag2SFLooseDown[0] = self.sf2Loose*(1-self.sf2Loosechangedown)


                if len(self.jets) > 1 and self.jets[0].Pt() > 300 and self.jets[1].Pt() > 300 and abs(self.jets[0].Eta() - self.jets[1].Eta()) < 1.3 and ((self.jets[self.idxH1] + self.jets[self.idxH2]).M() - (self.jet1pmass[0]-125)-(self.jet2pmass[0]-125)) > 800 and self.jet1tau21[0] < 0.6 and self.jet2tau21[0] < 0.6 and self.jet1pmass[0] > 105 and self.jet1pmass[0] < 135 and self.jet2pmass[0] > 105 and self.jet2pmass[0] < 135 and self.jet1bbtag[0] > 0.6 and self.jet2bbtag[0] > 0.6:
                    self.passesBoosted[0] = 1
                else:
                    self.passesBoosted[0] = 0

                self.ak4jet_pt.clear()
                self.ak4jet_eta.clear()
                self.ak4jet_phi.clear()
                self.ak4jet_mass.clear()
                self.ak4jetID.clear()
                self.ak4jetHeppyFlavour.clear()
                self.ak4jetMCflavour.clear()
                self.ak4jetPartonFlavour.clear()
                self.ak4jetHadronFlavour.clear()
                self.ak4jetCSVLSF.clear()
                self.ak4jetCSVLSF_Up.clear()
                self.ak4jetCSVLSF_Down.clear()
                self.ak4jetCSVMSF.clear()
                self.ak4jetCSVMSF_up.clear()
                self.ak4jetCSVMSF_Down.clear()
                self.ak4jetCSVTSF.clear()
                self.ak4jetCSVTSF_Up.clear()
                self.ak4jetCSVTSF_Down.clear()
                self.ak4jetCMVALSF.clear()
                self.ak4jetCMVALSF_Up.clear()
                self.ak4jetCMVALSF_Down.clear()
                self.ak4jetCMVAMSF.clear()
                self.ak4jetCMVAMSF_Up.clear()
                self.ak4jetCMVAMSF_Down.clear()
                self.ak4jetCMVATSF.clear()
                self.ak4jetCMVATSF_Up.clear()
                self.ak4jetCMVATSF_Down.clear()
                self.ak4jetCSV.clear()
                self.ak4jetDeepCSVb.clear()
                self.ak4jetDeepCSVbb.clear()
                self.ak4jetCMVA.clear()
                self.ak4jetCorr.clear()
                self.ak4jetCorrJECUp.clear()
                self.ak4jetCorrJECDown.clear()
                self.ak4jetCorrJER.clear()
                self.ak4jetCorrJERUp.clear()
                self.ak4jetCorrJERDown.clear()
                self.ak4genJetPt.clear()
                self.ak4genJetPhi.clear()
                self.ak4genJetEta.clear()
                self.ak4genJetMass.clear()
                self.ak4genJetID.clear()
  
                self.akjets = []
                for j in range(len(self.fJetPt)):
                    if (self.syst=="JEC_Up"): self.jet_pT = self.treeMine.Jet_pt[j]*self.treeMine.Jet_corr_JECUp[j]/self.treeMine.Jet_corr[j]
                    elif (self.syst=="JEC_Down"): self.jet_pT = self.treeMine.Jet_pt[j]*self.treeMine.Jet_corr_JECDown[j]/self.treeMine.  Jet_corr[j]
                    elif (self.syst=="JER_Up"): self.jet_pT = self.treeMine.Jet_pt[j]*self.treeMine.Jet_corr_JERUp[j]*self.treeMine.Jet_corr_JER[j]
                    elif (self.syst=="JER_Down"): self.jet_pT = self.treeMine.Jet_pt[j]*self.treeMine.Jet_corr_JERDown[j]*self.treeMine.Jet_corr_JER[j]
                    else: self.jet_pT = self.treeMine.Jet_pt[j]
                    self.jettemp = ROOT.TLorentzVector()
                    self.jettemp.SetPtEtaPhiM(self.jet_pT, self.fJetEta[j], self.fJetPhi[j], self.fJetMass[j])
                    if abs(self.jettemp.Eta()) < 2.4 and self.jet_pT > 25:
                        self.akjets.append(self.jettemp)
                        self.ak4jet_pt.push_back(self.jet_pT)
                        self.ak4jet_eta.push_back(self.fJetEta[j])
                        self.ak4jet_phi.push_back(self.fJetPhi[j])
                        self.ak4jet_mass.push_back(self.fJetMass[j])
                        self.ak4jetID.push_back(self.fJetID[j])
                        if self.isMC == 'True':
                            self.ak4jetHeppyFlavour.push_back(self.fJetHeppyFlavour[j])
                            self.ak4jetMCflavour.push_back(self.fJetMCflavour[j])
                            self.ak4jetPartonFlavour.push_back(self.fJetPartonFlavour[j])
                            self.ak4jetHadronFlavour.push_back(self.fJetHadronFlavour[j])
                            self.ak4jetCSVLSF.push_back(self.fJetCSVLSF[j])
                            self.ak4jetCSVLSF_Up.push_back(self.fJetCSVLSF_Up[j])
                            self.ak4jetCSVLSF_Down.push_back(self.fJetCSVLSF_Down[j])
                            self.ak4jetCSVMSF.push_back(self.fJetCSVMSF[j])
                            self.ak4jetCSVMSF_up.push_back(self.fJetCSVMSF_Up[j])
                            self.ak4jetCSVMSF_Down.push_back(self.fJetCSVMSF_Down[j])
                            self.ak4jetCSVTSF.push_back(self.fJetCSVTSF[j])
                            self.ak4jetCSVTSF_Up.push_back(self.fJetCSVTSF_Up[j])
                            self.ak4jetCSVTSF_Down.push_back(self.fJetCSVTSF_Down[j])
                            self.ak4jetCMVALSF.push_back(self.fJetCMVALSF[j])
                            self.ak4jetCMVALSF_Up.push_back(self.fJetCMVALSF_Up[j])
                            self.ak4jetCMVALSF_Down.push_back(self.fJetCMVALSF_Down[j])
                            self.ak4jetCMVAMSF.push_back(self.fJetCMVAMSF[j])
                            self.ak4jetCMVAMSF_Up.push_back(self.fJetCMVAMSF_Up[j])
                            self.ak4jetCMVAMSF_Down.push_back(self.fJetCMVAMSF_down[j])
                            self.ak4jetCMVATSF.push_back(self.fJetCMVATSF[j])
                            self.ak4jetCMVATSF_Up.push_back(self.fJetCMVATSF_Up[j])
                            self.ak4jetCMVATSF_Down.push_back(self.fJetCMVATSF_Down[j])
                            self.ak4jetCorr.push_back(self.fJetCorr[j])
                            self.ak4jetCorrJECUp.push_back(self.fJetCorrJECUp[j])
                            self.ak4jetCorrJECDown.push_back(self.fJetCorrJECDown[j])
                            self.ak4jetCorrJER.push_back(self.fJetCorrJER[j])
                            self.ak4jetCorrJERUp.push_back(self.fJetCorrJERUp[j])
                            self.ak4jetCorrJERDown.push_back(self.fJetCorrJERDown[j])
                        self.ak4jetCSV.push_back(self.fJetCSV[j])
                        self.ak4jetDeepCSVb.push_back(self.fJetDeepCSVb[j])
                        self.ak4jetDeepCSVbb.push_back(self.fJetDeepCSVbb[j])
                        self.ak4jetCMVA.push_back(self.fJetCMVA[j])

                        if self.isMC == 'True':
                            if len(self.ujets) > 0:
                               self.akj = MatchCollection(self.ujets, self.jettemp)
                               self.ak4genJetPt.push_back(self.ujets[self.akj].Pt())
                               self.ak4genJetEta.push_back(self.ujets[self.akj].Eta())
                               self.ak4genJetPhi.push_back(self.ujets[self.akj].Phi())
                               self.ak4genJetMass.push_back(self.ujets[self.akj].M())
                               self.ak4genJetID.push_back(self.akj)
        

                #resolved
                self.ak4res = []
                self.chi2_old=200
                self.foundRes = False
                self.passesResolved[0] = 0
                for j in range(len(self.akjets)):
                    if self.ak4jetCMVA[j] > 0.4432:
                        self.ak4res.append(self.akjets[j])
                if len(self.ak4res) > 3:
                    self.jet1=TLorentzVector()
                    self.jet2=TLorentzVector()
                    self.jet3=TLorentzVector()
                    self.jet4=TLorentzVector()
                    for l in range(len(self.ak4res)):
                        self.jet1.SetPtEtaPhiM(self.ak4res[l].Pt(), self.ak4res[l].Eta(), self.ak4res[l].Phi(), self.ak4res[l].M())
                        for m in range(len(self.ak4res)):
                            if m!=l:
                                self.jet2.SetPtEtaPhiM(self.ak4res[m].Pt(), self.ak4res[m].Eta(), self.ak4res[m].Phi(),self.ak4res[m].M())
                                for n in range(len(self.ak4res)):
                                    if (n!=l and n!=m):
                                        self.jet3.SetPtEtaPhiM(self.ak4res[n].Pt(), self.ak4res[n].Eta(), self.ak4res[n].Phi(),self.ak4res[n].M())
                                        for k in range(len(self.ak4res)):
                                            if (k!=l and k!=m and k!=n):
                                                self.jet4.SetPtEtaPhiM(self.ak4res[k].Pt(), self.ak4res[k].Eta(), self.ak4res[k].Phi(),self.ak4res[k].M())

                                                self.dijet1=self.jet1+self.jet2
                                                self.dijet2=self.jet3+self.jet4
                                            
                                                self.deltar1=self.jet1.DeltaR(self.jet2)
                                                self.deltar2=self.jet3.DeltaR(self.jet4)
                                        
                                                self.mH1=self.dijet1.M()
                                                self.mH2=self.dijet2.M()
                                            
                                                self.chi2=((self.mH1-120)/20)**2+((self.mH2-120)/20)**2
                                        
                                                if (self.chi2<self.chi2_old and self.deltar1<1.5 and self.deltar2<1.5):
                                                    self.chi2_old=self.chi2
                                                    self.foundRes=True

                if self.foundRes:
                    self.chi=self.chi2_old**0.5
                    if self.chi<=1:
                        self.passesResolved[0] = 1

                #filling the tree
                self.theTree.Fill()
                self.nFills2 += 1
                #filling error values for each object
                if self.isMC == 'True':
                    #     self.genjet1BH[0] = -100.0
                    self.genjet2BH[0] = -100.0
                    self.genjet1CH[0] = -100.0
                    self.genjet2CH[0] = -100.0
                self.htJet30[0] = -100.0
                self.jet1pt[0] = -100.0
                self.jet2pt[0] = -100.0
                self.jet1pt_reg[0] = -100.0
                self.jet2pt_reg[0] = -100.0
                self.jet1eta[0] = -100.0
                self.jet2eta[0] = -100.0
                self.etadiff[0] = -100.0
                self.dijetmass[0] = -100.0
                self.dijetmass_corr[0]=-100.0
                self.dijetmass_reg[0]=-100.0
                self.jet1pmass[0] = -100.0
                self.jet2pmass[0] = -100.0
                self.jet1tau21[0] = -100.0
                self.jet2tau21[0] = -100.0
                #	self.jet1mscsv[0] = -100.0
                #	self.jet2mscsv[0] = -100.0
                self.jet1bbtag[0] = -100.0
                self.jet2bbtag[0] = -100.0
                self.triggerpassbb[0] = -100.0
                self.DeltaPhi1[0] = -100.0
                self.DeltaPhi2[0] = -100.0
                self.DeltaPhi3[0] = -100.0
                self.DeltaPhi4[0] = -100.0
                #	PUWeight[0]= -100.0
	        self.jet1_puppi_pt[0] = -100.0
        	self.jet2_puppi_pt[0] = -100.0
	        self.jet1_puppi_eta[0] = -100.0
	        self.jet2_puppi_eta[0] = -100.0
	        self.jet1_puppi_phi[0] = -100.0
	        self.jet2_puppi_phi[0] = -100.0
	        self.jet1_puppi_mass[0] = -100.0
	        self.jet2_puppi_mass[0] = -100.0
	        self.jet1_puppi_tau21[0] = -100.0
	        self.jet2_puppi_tau21[0] = -100.0
	        self.jet1_puppi_msoftdrop[0] = -100.0
	        self.jet2_puppi_msoftdrop[0] = -100.0
	        self.jet1_puppi_msoftdrop_corrL2L3[0] = -100.0
	        self.jet2_puppi_msoftdrop_corrL2L3[0] = -100.0
	        self.jet1_puppi_TheaCorr[0] = -100.0
	        self.jet2_puppi_TheaCorr[0] = -100.0
	        self.jet1_puppi_msoftdrop_raw[0] = -100.0
	        self.jet2_puppi_msoftdrop_raw[0] = -100.0


	
            self.f1.Close()




