import os
import glob
import math

import ROOT
#ROOT.gROOT.Macro("rootlogon.C")

import FWCore.ParameterSet.Config as cms

import sys
from DataFormats.FWLite import Events, Handle

from array import *


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

(options, args) = parser.parse_args()

inputfile = options.txt 

ff_n = 1000

num1 = int(options.min)
num2 = int(options.max)

d1 = options.outName 
d2 = '_'
outputfilename = d1 + d2 + options.min + '.root'

print outputfilename

#defining functions
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
			j = i
                        break
        if dr > 0.4:
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
  #  print final_list
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

#creating the objects we need
jet1pt = array('f', [-100.0])
jet2pt = array('f', [-100.0])
jet1eta = array('f', [-100.0])
jet2eta = array('f', [-100.0])
etadiff = array('f', [-100.0])
dijetmass = array('f', [-100.0])
jet1tau21 = array('f', [-100.0])
jet2tau21 = array('f', [-100.0])
jet1pmass = array('f', [-100.0])
jet2pmass = array('f', [-100.0])
jet1sdmass = array('f', [-100.0])
jet2sdmass = array('f', [-100.0])
jet1bbtag = array('f', [-100.0])
jet2bbtag = array('f', [-100.0])
jet1mscsv = array('f', [-100.0])
jet2mscsv = array('f', [-100.0])
triggerpass = array('f', [-100.0])

#creating the branches we need
myTree.Branch('jet1pt', jet1pt, 'jet1pt/F')
myTree.Branch('jet2pt', jet2pt, 'jet2pt/F')
myTree.Branch('jet1eta', jet1eta, 'jet1eta/F')
myTree.Branch('jet2eta', jet2eta, 'jet2eta/F')
myTree.Branch('etadiff', etadiff, 'etadiff/F')
myTree.Branch('dijetmass', dijetmass, 'dijetmass/F')
myTree.Branch('jet1tau21', jet1tau21, 'jet1tau21/F')
myTree.Branch('jet2tau21', jet2tau21, 'jet2tau21/F')
myTree.Branch('jet1pmass', jet1pmass, 'jet1pmass/F')
myTree.Branch('jet2pmass', jet2pmass, 'jet2pmass/F')
myTree.Branch('jet1sdmass', jet1sdmass, 'jet1sdmass/F')
myTree.Branch('jet2sdmass', jet2sdmass, 'jet2sdmass/F')
myTree.Branch('jet1bbtag', jet1bbtag, 'jet1bbtag/F')
myTree.Branch('jet2bbtag', jet2bbtag, 'jet2bbtag/F')
myTree.Branch('jet1mscsv', jet1mscsv, 'jet1mscsv/F')
myTree.Branch('jet2mscsv', jet2mscsv, 'jet2mscsv/F')
myTree.Branch('triggerpass', triggerpass, 'triggerpass/F')
 
files_list = open_files( inputfile )
#nevent = treeMine.GetEntries();

ct = ROOT.TH1F("ct", "Trigger Pass", 3, -0.5, 1.5)
c0 = ROOT.TH1F("c0", "Dijet Mass No Cuts", 10000, 0, 10000)
c1 = ROOT.TH1F("c1", "Dijet Mass Jet Pt Selection", 10000, 0, 10000)
c2 = ROOT.TH1F("c2", "Dijet Mass Jet Eta Selection", 10000, 0, 10000)
c3 = ROOT.TH1F("c3", "Dijet Mass Delta Eta Selection", 10000, 0, 10000)
c4 = ROOT.TH1F("c4", "Dijet Mass Dijet Mass Selection", 100, 0, 10000)
c5 = ROOT.TH1F("c5", "Dijet Mass First tau21", 100, 0, 10000)
c6 = ROOT.TH1F("c6", "Dijet Mass Second tau21", 100, 0, 10000)
c7 = ROOT.TH1F("c7", "Dijet Mass First Higgs Pruned Mass", 100, 0, 10000)
c8 = ROOT.TH1F("c8", "Dijet Mass Second Higgs Pruned Mass", 100, 0, 10000)
c9 = ROOT.TH1F("c9", "Dijet Mass First Min Subjet CSV", 100, -2, 2)
c10 = ROOT.TH1F("c10", "Dijet Mass Second Min Subjet CSV", 100, -2, 2)
c11 = ROOT.TH1F("c11", "Dijet Mass First BB Tag", 100, -2, 2)
c12 = ROOT.TH1F("c12", "Dijet Mass Second BB Tag", 100, -2, 2)

d1 = ROOT.TH1F("d1", "Dijet Mass No Mass Cut No Tau21 No B Tag", 10000, 0, 10000)
d2 = ROOT.TH1F("d2", "Dijet Mass No Mass Cut Yes Tau21 No B Tag", 10000, 0, 10000)
d3 = ROOT.TH1F("d3", "Dijet Mass Yes Mass Cut No Tau21 No B Tag", 10000, 0, 10000)
d4a = ROOT.TH1F("d4a", "Dijet Mass Yes Mass Cut Yes Tau21 Subjet B Tag 20", 10000, 0, 10000)
d5a = ROOT.TH1F("d5a", "Dijet Mass Yes Mass Cut Yes Tau21 BB Tag 20", 10000, 0, 10000)
d6a = ROOT.TH1F("d6a", "Dijet Mass No Mass Cut No Tau21 Subjet B Tag 20", 10000, 0, 10000)
d7a = ROOT.TH1F("d7a", "Dijet Mass No Mass Cut No Tau21 BB Tag 20", 10000, 0, 10000)
d4b = ROOT.TH1F("d4b", "Dijet Mass Yes Mass Cut Yes Tau21 Subjet B Tag 50", 10000, 0, 10000)
d5b = ROOT.TH1F("d5b", "Dijet Mass Yes Mass Cut Yes Tau21 BB Tag 50", 10000, 0, 10000)
d6b = ROOT.TH1F("d6b", "Dijet Mass No Mass Cut No Tau21 Subjet B Tag 50", 10000, 0, 10000)
d7b = ROOT.TH1F("d7b", "Dijet Mass No Mass Cut No Tau21 BB Tag 50", 10000, 0, 10000)

j11 = ROOT.TH1F("j11", "Jet 1 Mass No Mass Cut No Tau21 No B Tag", 100, 0, 500)
j12 = ROOT.TH1F("j12", "Jet 1 Mass No Mass Cut Yes Tau21 No B Tag", 100, 0, 500)
j13 = ROOT.TH1F("j13", "Jet 1 Mass Yes Mass Cut No Tau21 No B Tag", 100, 100, 150)
j14a = ROOT.TH1F("j14a", "Jet 1 Mass Yes Mass Cut Yes Tau21 Subjet B Tag 20", 100, 100, 150)
j15a = ROOT.TH1F("j15a", "Jet 1 Mass Yes Mass Cut Yes Tau21 BB Tag 20", 100, 100, 150)
j16a = ROOT.TH1F("j16a", "Jet 1 Mass No Mass Cut No Tau21 Subjet B Tag 20", 100, 0, 500)
j17a = ROOT.TH1F("j17a", "Jet 1 Mass No Mass Cut No Tau21 BB Tag 20", 100, 0, 500)
j14b = ROOT.TH1F("j14b", "Jet 1 Mass Yes Mass Cut Yes Tau21 Subjet B Tag 50", 100, 100, 150)
j15b = ROOT.TH1F("j15b", "Jet 1 Mass Yes Mass Cut Yes Tau21 BB Tag 50", 100, 100, 150)
j16b = ROOT.TH1F("j16b", "Jet 1 Mass No Mass Cut No Tau21 Subjet B Tag 50", 100, 0, 500)
j17b = ROOT.TH1F("j17b", "Jet 1 Mass No Mass Cut No Tau21 BB Tag 50", 100, 0, 500)

j21 = ROOT.TH1F("j21", "Jet 2 Mass No Mass Cut No Tau21 No B Tag", 100, 0, 500)
j22 = ROOT.TH1F("j22", "Jet 2 Mass No Mass Cut Yes Tau21 No B Tag", 100, 0, 500)
j23 = ROOT.TH1F("j23", "Jet 2 Mass Yes Mass Cut No Tau21 No B Tag", 100, 100, 150)
j24a = ROOT.TH1F("j24a", "Jet 2 Mass Yes Mass Cut Yes Tau21 Subjet B Tag 20", 100, 100, 150)
j25a = ROOT.TH1F("j25a", "Jet 2 Mass Yes Mass Cut Yes Tau21 BB Tag 20", 100, 100, 150)
j26a = ROOT.TH1F("j26a", "Jet 2 Mass No Mass Cut No Tau21 Subjet B Tag 20", 100, 0, 500)
j27a = ROOT.TH1F("j27a", "Jet 2 Mass No Mass Cut No Tau21 BB Tag 20", 100, 0, 500)
j24b = ROOT.TH1F("j24b", "Jet 2 Mass Yes Mass Cut Yes Tau21 Subjet B Tag 50", 100, 100, 150)
j25b = ROOT.TH1F("j25b", "Jet 2 Mass Yes Mass Cut Yes Tau21 BB Tag 50", 100, 100, 150)
j26b = ROOT.TH1F("j26b", "Jet 2 Mass No Mass Cut No Tau21 Subjet B Tag 50", 100, 0, 500)
j27b = ROOT.TH1F("j27b", "Jet 2 Mass No Mass Cut No Tau21 BB Tag 50", 100, 0, 500)

njet = ROOT.TH1F("njet", "Number of jet with pt > 30 |eta| < 2.4, passing the trigger selection", 15., 0, 15)
jet_H1_idx  = ROOT.TH1F("jet_H1_idx","idx selected H1 ",   15., 0, 15)
jet_H2_idx = ROOT.TH1F("jet_H2_idx","idx selected H2 ",   15., 0, 15)

count = 0
for i in range(num1, num2):
    files = files_list[i]
    print files
    f1 = ROOT.TFile(files, "READ")
    treeMine  = f1.Get('tree')
    nevent = treeMine.GetEntries();


    print "Start looping"
    for j in range(0,nevent):
        treeMine.GetEntry(j)
	count = count + 1
 	if count % 1000 == 0 :
	    print "processing events", count

	fjUngroomedPt = treeMine.FatjetAK08ungroomed_pt
	fjUngroomedEta = treeMine.FatjetAK08ungroomed_eta
	fjUngroomedPhi = treeMine.FatjetAK08ungroomed_phi
	fjUngroomedMass = treeMine.FatjetAK08ungroomed_mass
	fjUngroomedSDMass = treeMine.FatjetAK08ungroomed_msoftdrop
	fjUngroomedTau1 = treeMine.FatjetAK08ungroomed_tau1
	fjUngroomedTau2 = treeMine.FatjetAK08ungroomed_tau2
	fjUngroomedBbTag = treeMine.FatjetAK08ungroomed_bbtag
	fjPrunedPt = treeMine.FatjetAK08pruned_pt
	fjPrunedEta = treeMine.FatjetAK08pruned_eta
	fjPrunedPhi = treeMine.FatjetAK08pruned_phi
	fjPrunedMass = treeMine.FatjetAK08pruned_mass
	sjPrunedPt = treeMine.SubjetAK08pruned_pt
	sjPrunedEta = treeMine.SubjetAK08pruned_eta
	sjPrunedPhi = treeMine.SubjetAK08pruned_phi
	sjPrunedMass = treeMine.SubjetAK08pruned_mass
	sjPrunedBtag = treeMine.SubjetAK08pruned_btag
	hltMatch = treeMine.HLT_BIT_HLT_PFHT900_v

	#saving whether an event passes desired trigger
        matched = 0    
#	print hltMatch
	if hltMatch > 0:
            matched += 1
        triggerpass[0] = matched
        ct.Fill(triggerpass[0])
	if triggerpass[0] < 1:
            continue
        jets = []
	jet_tau = []
	jet_bbtag = []
        for j in range(len(fjUngroomedPt)):
            jettemp = ROOT.TLorentzVector()
            jettemp.SetPtEtaPhiM(fjUngroomedPt[j], fjUngroomedEta[j], fjUngroomedPhi[j], fjUngroomedMass[j])
	    if jettemp.Pt() > 30. and abs(jettemp.Eta()) < 2.5: 	
                    jets.append(jettemp)
		    jet_tau.append(fjUngroomedTau2[j]/fjUngroomedTau1[j])
		    jet_bbtag.append(fjUngroomedBbTag[j])	

	#look at the jet multiplicity here:
	njet.Fill(len(jets))


	if len(jets) < 2: # two jets with pt > 30 and central 
		continue

	#dEta selection : selecting the two jets which minimizes the dEta requirement. (to find a better one?)
	idxH1 =-1
	idxH2=-1
	for i in range(0,len(jets)):
		minDEta= 1.3
		for j in range(0,len(jets)):
			if abs(jets[i].Eta() - jets[j].Eta()) < minnDEta:
				minDEta = abs(jets[i].Eta() - jets[j].Eta())
				idxH1 = i
				idxH2 = j
			
	if idxH1 < 0 or idxH2 <0 : continue
	
	jet_H1_idx.Fill(idxH1)
	jet_H2_idx.Fill(idxH2)
	
	dijetm = (jets[idxH1] + jets[idxH2]).M()
        #dijet selection
	c0.Fill(dijetm)




        ujets = []
        for j in range(len(fjPrunedPt)):
            jettemp = ROOT.TLorentzVector()
            jettemp.SetPtEtaPhiM(fjPrunedPt[j], fjPrunedEta[j], fjPrunedPhi[j], fjPrunedMass[j])
            ujets.append(jettemp)

	j1 = MatchCollection(ujets, jets[idxH1])
	j2 = MatchCollection(ujets, jets[idxH2])
	#selecting HH events
	#softdrop mass
	

	#tau21 cut
	jet1t21 = 100.
	jet2t21 = 100.
	passjet1taucut = 0
	passjet2taucut = 0

	if j2 < 0:
		continue
	if j2 > len(jets):
		continue
	if j2 == len(jets):
		continue


	#mass cut - here we use pruned mass - ONLY here 
        jet1pmass[0] = fjPrunedMass[j1]
        jet2pmass[0] = fjPrunedMass[j2]

        passjet1mass = 0
        passjet2mass = 0

        if 105 < jet1pmass[0] < 135:
                passjet1mass +=1
                c5.Fill(dijetm)
        if 105 < jet2pmass[0] < 135:
                passjet2mass +=1
        if passjet1mass > 0 and passjet2mass > 0:
                c6.Fill(dijetm)



	#jet1sdmass[0] = fjUngroomedSDMass[idxH1]
	#jet2sdmass[0] = fjUngroomedSDMass[idxH2]

	#if fjUngroomedTau1[j1] > 0:
	jet1t21 = jet_tau[idxH1]# fjUngroomedTau2[j1]/fjUngroomedTau1[j1]
	#if fjUngroomedTau1[j2] > 0:
        jet2t21 = jet_tau[idxH2]# fjUngroomedTau2[j2]/fjUngroomedTau1[j2]
	if jet1t21 < 0.75:
		passjet1taucut +=1
	if passjet1mass> 0 and passjet2mass > 0 and passjet1taucut > 0:
		c7.Fill(dijetm) 
	if jet2t21 < 0.75:
		passjet2taucut +=1
	if passjet1mass> 0 and passjet2mass > 0 and passjet1taucut > 0 and passjet2taucut > 0:
		c8.Fill(dijetm)

	#filling min subjet csv
	subjets = []
	jet1sj = []
	jet1sjcsv = []
	jet2sj = []
	jet2sjcsv = []
        for j in range(len(sjPrunedPt)):
            jettemp = ROOT.TLorentzVector()
            jettemp.SetPtEtaPhiM(sjPrunedPt[j], sjPrunedEta[j], sjPrunedPhi[j], sjPrunedMass[j])
            subjets.append(jettemp)

	for j in range(len(subjets)):
            dR1 = subjets[j].DeltaR(jets[idxH1])
	    dR2 = subjets[j].DeltaR(jets[idxH2])
	    if dR1 < 0.4 and dR2 < 0.4:
		    samesj[0] += 1
	    elif dR1 < 0.4:
	#	    print "subjet for jet 1 found at index " + str(j)
		    jet1sj.append(subjets[j])
		    jet1sjcsv.append(sjPrunedBtag[j])
	    elif dR2 < 0.4:
	#	    print "subjet for jet 2 found at index " + str(j)
		    jet2sj.append(subjets[j])
		    jet2sjcsv.append(sjPrunedBtag[j])
	n1sj = len(jet1sj)
	n2sj = len(jet2sj)

	#Finding the subjet with the smallest csv in each jet min(subjet csv)
	jet1mscsv[0] = 1000.
	jet2mscsv[0] = 1000.
	for j in range(len(jet1sjcsv)):
     #       print "jet1sjcsv: " + str(jet1sjcsv[j])
	    if jet1sjcsv[j] < jet1mscsv[0]:
		    jet1mscsv[0] = jet1sjcsv[j]
	for j in range(len(jet2sjcsv)):
	    if jet2sjcsv[j] < jet2mscsv[0]:
		    jet2mscsv[0] = jet2sjcsv[j]
#	

	#filling bbtag
	jet1bbtag[0] = jet_bbtag[idxH1] #fjUngroomedBbTag[j1]
	jet2bbtag[0] = jet_bbtag[idxH2] # fjUngroomedBbTag[j2]

	if passjet1mass> 0 and passjet2mass > 0 and passjet1taucut > 0 and passjet2taucut > 0:
		c11.Fill(jet1bbtag[0])
		c12.Fill(jet2bbtag[0])
		c9.Fill(jet1mscsv[0])
		c10.Fill(jet2mscsv[0])

	passjet1sjb2 = 0
	passjet1sjb5 = 0
	passjet2sjb2 = 0
	passjet2sjb5 = 0
	passjet1bb2 = 0
	passjet1bb5 = 0
	passjet2bb2 = 0
	passjet2bb5 = 0

	if jet1mscsv[0] > 0.6:
		passjet1sjb2 +=1
	if jet1mscsv[0] > 0.24:
		passjet1sjb5 +=1
	if jet2mscsv[0] > 0.64:
		passjet2sjb2 +=1
	if jet2mscsv[0] > 0.28:
		passjet2sjb5 +=1
	if jet1bbtag[0] > -0.44:
		passjet1bb2 +=1
	if jet1bbtag[0] > -0.84:
		passjet1bb5 +=1
	if jet2bbtag[0] > -0.4:
		passjet2bb2 +=1
	if jet2bbtag[0] > -0.84:
		passjet2bb5 +=1

	#filling histograms
	#no mass no tau no btag
	d1.Fill(dijetm)
	j11.Fill(jet1pmass[0])
	j21.Fill(jet2pmass[0])
	#no mass yes tau no btag
	if passjet1taucut > 0 and passjet2taucut > 0:
		d2.Fill(dijetm)
		j12.Fill(jet1pmass[0])
		j22.Fill(jet2pmass[0])
	#yes mass no tau no btag
	if passjet1mass > 0 and passjet2mass > 0:
		d3.Fill(dijetm)
		j13.Fill(jet1pmass[0])
		j23.Fill(jet2pmass[0])
        #yes mass yes tau subjet btag 20% and 50%
	if passjet1mass > 0 and passjet2mass > 0 and passjet1taucut > 0 and passjet2taucut > 0 and passjet1sjb2 > 0 and passjet2sjb2 > 0:
		d4a.Fill(dijetm)
		j14a.Fill(jet1pmass[0])
		j24a.Fill(jet2pmass[0])
	if passjet1mass > 0 and passjet2mass > 0 and passjet1taucut > 0 and passjet2taucut > 0 and passjet1sjb5 > 0 and passjet2sjb5 > 0:	
		d4b.Fill(dijetm)
		j14b.Fill(jet1pmass[0])
		j24b.Fill(jet2pmass[0])
	#yes mass yes tau bbtag
	if passjet1mass > 0 and passjet2mass > 0 and passjet1taucut > 0 and passjet2taucut > 0 and passjet1bb2 > 0 and passjet2bb2 > 0:
		d5a.Fill(dijetm)
		j15a.Fill(jet1pmass[0])
		j25a.Fill(jet2pmass[0])
	if passjet1mass > 0 and passjet2mass > 0 and passjet1taucut > 0 and passjet2taucut > 0 and passjet1bb5 > 0 and passjet2bb5 > 0:	
	 	d5b.Fill(dijetm)
		j15b.Fill(jet1pmass[0])
		j25b.Fill(jet2pmass[0])
	#no mass no tau subjet btag
	if passjet1sjb2 > 0 and passjet2sjb2 > 0:
		d6a.Fill(dijetm)
		j16a.Fill(jet1pmass[0])
		j26a.Fill(jet2pmass[0])
	if passjet1sjb5 > 0 and passjet2sjb5 > 0:
		d6b.Fill(dijetm)
		j16b.Fill(jet1pmass[0])
		j26b.Fill(jet2pmass[0])
        #no mass no tau bbtag
    	if passjet1bb2 > 0 and passjet2bb2 > 0:
		d7a.Fill(dijetm)
		j17a.Fill(jet1pmass[0])
		j27a.Fill(jet2pmass[0])
	if passjet1bb5 > 0 and passjet2bb5 > 0:
		d7b.Fill(dijetm)
		j17b.Fill(jet1pmass[0])
		j27b.Fill(jet2pmass[0])
        
        
        #writing variables to the tree    
	jet1pt[0] = jets[idxH1].Pt()
	jet2pt[0] = jets[idxH2].Pt()
	jet1eta[0] = jets[idxH1].Eta()
	jet2eta[0] = jets[idxH2].Eta()
	etadiff[0] = abs(jets[idxH1].Eta() - jets[idxH2].Eta())
	dijetmass[0] = (jets[idxH0] + jets[idxH2]).M()
	jet1tau21[0] = jet1t21
	jet2tau21[0] = jet2t21

	#filling the tree
        myTree.Fill()

	#filling error values for each object
	jet1pt[0] = -100.0
	jet2pt[0] = -100.0
	jet1eta[0] = -100.0
	jet2eta[0] = -100.0
	etadiff[0] = -100.0
	dijetmass[0] = -100.0
	jet1pmass[0] = -100.0
	jet2pmass[0] = -100.0
	jet1tau21[0] = -100.0
	jet2tau21[0] = -100.0
	jet1mscsv[0] = -100.0
	jet2mscsv[0] = -100.0
	jet1bbtag[0] = -100.0
	jet2bbtag[0] = -100.0
	triggerpass[0] = -100.0
	
    
    f1.Close()

print "OK"

f.cd()
f.Write()
f.Close()




