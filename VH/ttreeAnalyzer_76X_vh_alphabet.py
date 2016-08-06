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
jetVpt = array('f', [-100.0])
jetHpt = array('f', [-100.0])
jetVID = array('f', [-100.0])
jetHID = array('f', [-100.0])
jetVeta = array('f', [-100.0])
jetHeta = array('f', [-100.0])
etadiff = array('f', [-100.0])
dijetmass = array('f', [-100.0])
dijetmass_corr = array('f', [-100.0])
dijetmass_corr_punc = array('f', [-100.0])
jetVtau21 = array('f', [-100.0])
jetHtau21 = array('f', [-100.0])
jetVpmass = array('f', [-100.0])
jetHpmass = array('f', [-100.0])
jetVpmassunc = array('f', [-100.0])
jetHpmassunc = array('f', [-100.0])
#pjet1pmass = array('f', [-100.0])
#pjet2pmass = array('f', [-100.0])
jetVbbtag = array('f', [-100.0])
jetHbbtag = array('f', [-100.0])
triggerpassbb = array('f', [-100.0])
triggerpasssj = array('f', [-100.0])
nHiggsTags = array('f', [-100.0]) 
nTrueInt = array('f', [-100])
#PUWeight  = array('f', [-100.0])
vtype = array('f', [-100.0])
isData = array('f', [100.0])
jetVnbHadron = array('f', [-100.0])
jetHnbHadron = array('f', [-100.0])
jetVflavor = array('f', [-100.0])
jetHflavor = array('f', [-100.0])
jetVncHadron = array('f', [-100.0])
jetHncHadron = array('f', [-100.0])
genVPt = array('f', [-100.0])
genVPhi = array('f', [-100.0])
genVEta = array('f', [-100.0])
genVMass = array('f', [-100.0])
genVID = array('f', [-100.0])
genHPt = array('f', [-100.0])
genHPhi = array('f', [-100.0])
genHEta = array('f', [-100.0])
genHMass = array('f', [-100.0])
genHID = array('f', [-100.0])
jetVl1l2l3 = array('f', [-100.0])
jetVl2l3 = array('f', [-100.0])
jetHl1l2l3 = array('f', [-100.0])
jetHl2l3 = array('f', [-100.0])
jetVJER = array('f', [-100.0])
jetHJER = array('f', [-100.0])
puWeights = array('f', [-100.0])
puWeightsUp = array('f', [-100.0])
puWeightsDown = array('f', [-100.0])
json = array('f', [-100.0])
SF = array('f', [-100.0])
SFup = array('f', [-100.0])
SFdown = array('f', [-100.0])
trigWeight = array('f', [-100.0])
trigWeightUp = array('f', [-100.0])
trigWeightDown = array('f', [-100.0])
trigWeight2Up = array('f', [-100.0])
trigWeight2Down = array('f', [-100.0])
norm = array('f', [-100.0])
evt = array('f', [-100.0])
ht = array('f', [-100.0])
xsec = array('f', [-100.0])

#creating the tree branches we need
mynewTree.Branch('jetVpt', jetVpt, 'jetVpt/F')
mynewTree.Branch('jetHpt', jetHpt, 'jetHpt/F')
mynewTree.Branch('jetVeta', jetVeta, 'jetVeta/F')
mynewTree.Branch('jetHeta', jetHeta, 'jetHeta/F')
mynewTree.Branch('etadiff', etadiff, 'etadiff/F')
mynewTree.Branch('dijetmass', dijetmass, 'dijetmass/F')
mynewTree.Branch('dijetmass_corr', dijetmass_corr, 'dijetmass_corr/F')
mynewTree.Branch('dijetmass_corr_punc', dijetmass_corr_punc, 'dijetmass_corr_punc/F')
mynewTree.Branch('jetVtau21', jetVtau21, 'jetVtau21/F')
mynewTree.Branch('jetHtau21', jetHtau21, 'jetHtau21/F')
mynewTree.Branch('jetVpmass', jetVpmass, 'jetVpmass/F')
mynewTree.Branch('jetHpmass', jetHpmass, 'jetHpmass/F')
mynewTree.Branch('jetVpmassunc', jetVpmassunc, 'jetVpmassunc/F')
mynewTree.Branch('jetHpmassunc', jetHpmassunc, 'jetHpmassunc/F')
mynewTree.Branch('jetVbbtag', jetVbbtag, 'jetVbbtag/F')
mynewTree.Branch('jetHbbtag', jetHbbtag, 'jetHbbtag/F')
mynewTree.Branch('nHiggsTags', nHiggsTags, 'nHiggsTags/F')
mynewTree.Branch('triggerpassbb', triggerpassbb, 'triggerpassbb/F')
mynewTree.Branch('triggerpasssj', triggerpasssj, 'triggerpasssj/F')
mynewTree.Branch('nTrueInt',nTrueInt,'nTrueInt/F')
mynewTree.Branch('puWeights',puWeights,'puWeights/F')
mynewTree.Branch('puWeightsUp',puWeightsUp,'puWeightsUp/F')
mynewTree.Branch('puWeightsDown',puWeightsDown,'puWeightsDown/F')
mynewTree.Branch('jetVID', jetVID, 'jetVID/F')
mynewTree.Branch('jetHID', jetHID, 'jetHID/F')
mynewTree.Branch('vtype', vtype, 'vtype/F') 
mynewTree.Branch('isData', isData, 'isData/F') 
mynewTree.Branch('jetVnbHadron', jetVnbHadron, 'jetVnbHadron/F')
mynewTree.Branch('jetHnbHadron', jetHnbHadron, 'jetHnbHadron/F')
mynewTree.Branch('jetVflavor', jetVflavor, 'jetVflavor/F') 
mynewTree.Branch('jetHflavor', jetHflavor, 'jetHflavor/F') 
mynewTree.Branch('jetVncHadron', jetVncHadron, 'jetVncHadron/F')
mynewTree.Branch('jetHncHadron', jetHncHadron, 'jetHncHadron/F')
mynewTree.Branch('genVPt', genVPt, 'genVPt/F')
mynewTree.Branch('genVPhi', genVPhi, 'genVPhi/F')
mynewTree.Branch('genVEta', genVEta, 'genVEta/F')
mynewTree.Branch('genVMass', genVMass, 'genVMass/F')
mynewTree.Branch('genVID', genVID, 'genVID/F')
mynewTree.Branch('genHPt', genHPt, 'genHPt/F')
mynewTree.Branch('genHPhi', genHPhi, 'genHPhi/F')
mynewTree.Branch('genHEta', genHEta, 'genHEta/F')
mynewTree.Branch('genHMass', genHMass, 'genHMass/F')
mynewTree.Branch('genHID', genHID, 'genHID/F')
mynewTree.Branch('jetVl1l2l3', jetVl1l2l3, 'jetVl1l2l3/F') 
mynewTree.Branch('jetVl2l3', jetVl2l3, 'jetVl2l3/F')
mynewTree.Branch('jetHl1l2l3', jetHl1l2l3, 'jetHl1l2l3/F') 
mynewTree.Branch('jetHl2l3', jetHl2l3, 'jetHl2l3/F')
mynewTree.Branch('jetVJER', jetVJER, 'jetVJER/F') 
mynewTree.Branch('jetHJER', jetHJER, 'jetHJER/F') 
mynewTree.Branch('json', json, 'json/F')
mynewTree.Branch('SF', SF, 'SF/F')
mynewTree.Branch('SFup', SFup, 'SFup/F')
mynewTree.Branch('SFdown', SFdown, 'SFdown/F')
mynewTree.Branch('trigWeight', trigWeight, 'trigWeight/F')
mynewTree.Branch('trigWeightUp', trigWeightUp, 'trigWeightUp/F')
mynewTree.Branch('trigWeightDown', trigWeightDown, 'trigWeightDown/F')
mynewTree.Branch('trigWeight2Up', trigWeight2Up, 'trigWeight2Up/F')
mynewTree.Branch('trigWeight2Down', trigWeight2Down, 'trigWeight2Down/F')
mynewTree.Branch('norm',norm,'norm/F')
mynewTree.Branch('evt',evt,'evt/F')
mynewTree.Branch('ht', ht, 'ht/F')
mynewTree.Branch('xsec', xsec, 'xsec/F')

nevent = treeMine.GetEntries();

print outputfilename

for i in range(0, nevent) :
    treeMine.GetEntry(i)

    bothjets = 0
    jetV = 0
    #determining which jet is which
    if (45 < treeMine.jet1pmass < 65) and (45 < treeMine.jet2pmass < 65):
        bothjets = 1
    if bothjets == 0: #either only one jet is the V jet, or none are
        if (45 < treeMine.jet1pmass < 65): #jet 1 is V jet
            jetV = 1
        else:
            if (45 < treeMine.jet2pmass < 65):#jet 2 is V jet
                jetV = 2
    else: #both jets are in V mass window
        if treeMine.jet2tau21 > treeMine.jet1tau21: #jet 1 has the smaller tau21, so its V
            jetV = 1
        if treeMine.jet1tau21 > treeMine.jet2tau21: #jet 2 has the smaller tau21, so its V
            jetV = 2
    if jetV == 0:
        continue
    
    if jetV == 1: # jet1 is v jet, so jet 2 must be h jet
        jetVpt[0] = treeMine.jet1pt
        jetVeta[0] = treeMine.jet1eta
        jetVtau21[0] = treeMine.jet1tau21
        jetVpmass[0] = treeMine.jet1pmass
        jetVpmassunc[0] = treeMine.jet1pmassunc
        jetVbbtag[0] = treeMine.jet1bbtag
        jetVID[0] = treeMine.jet1ID
        jetVnbHadron[0] = treeMine.jet1nbHadron
        jetVflavor[0] = treeMine.jet1flavor
        jetVncHadron[0] = treeMine.jet1ncHadron
        genVPt[0] = treeMine.gen1Pt
        genVPhi[0] = treeMine.gen1Phi
        genVEta[0] = treeMine.gen1Eta
        genVMass[0] = treeMine.gen1Mass
        genVID[0] = treeMine.gen1ID
        jetVl1l2l3[0] = treeMine.jet1l1l2l3
        jetVl2l3[0] = treeMine.jet1l2l3
        jetVJER[0] = treeMine.jet1JER
        jetHpt[0] = treeMine.jet2pt
        jetHeta[0] = treeMine.jet2eta
        jetHtau21[0] = treeMine.jet2tau21
        jetHpmass[0] = treeMine.jet2pmass
        jetHpmassunc[0] = treeMine.jet2pmassunc
        jetHbbtag[0] = treeMine.jet2bbtag
        jetHID[0] = treeMine.jet2ID
        jetHnbHadron[0] = treeMine.jet2nbHadron
        jetHflavor[0] = treeMine.jet2flavor
        jetHncHadron[0] = treeMine.jet2ncHadron
        genHPt[0] = treeMine.gen2Pt
        genHPhi[0] = treeMine.gen2Phi
        genHEta[0] = treeMine.gen2Eta
        genHMass[0] = treeMine.gen2Mass
        genHID[0] = treeMine.gen2ID
        jetHl1l2l3[0] = treeMine.jet2l1l2l3
        jetHl2l3[0] = treeMine.jet2l2l3
        jetHJER[0] = treeMine.jet2JER

    if jetV == 2: # jet2 is v jet, so jet 1 must be h jet
        jetHpt[0] = treeMine.jet1pt
        jetHeta[0] = treeMine.jet1eta
        jetHtau21[0] = treeMine.jet1tau21
        jetHpmass[0] = treeMine.jet1pmass
        jetHpmassunc[0] = treeMine.jet1pmassunc
        jetHbbtag[0] = treeMine.jet1bbtag
        jetHID[0] = treeMine.jet1ID
        jetHnbHadron[0] = treeMine.jet1nbHadron
        jetHflavor[0] = treeMine.jet1flavor
        jetHncHadron[0] = treeMine.jet1ncHadron
        genHPt[0] = treeMine.gen1Pt
        genHPhi[0] = treeMine.gen1Phi
        genHEta[0] = treeMine.gen1Eta
        genHMass[0] = treeMine.gen1Mass
        genHID[0] = treeMine.gen1ID
        jetHl1l2l3[0] = treeMine.jet1l1l2l3
        jetHl2l3[0] = treeMine.jet1l2l3
        jetHJER[0] = treeMine.jet1JER
        jetVpt[0] = treeMine.jet2pt
        jetVeta[0] = treeMine.jet2eta
        jetVtau21[0] = treeMine.jet2tau21
        jetVpmass[0] = treeMine.jet2pmass
        jetVpmassunc[0] = treeMine.jet2pmassunc
        jetVbbtag[0] = treeMine.jet2bbtag
        jetVID[0] = treeMine.jet2ID
        jetVnbHadron[0] = treeMine.jet2nbHadron
        jetVflavor[0] = treeMine.jet2flavor
        jetVncHadron[0] = treeMine.jet2ncHadron
        genVPt[0] = treeMine.gen2Pt
        genVPhi[0] = treeMine.gen2Phi
        genVEta[0] = treeMine.gen2Eta
        genVMass[0] = treeMine.gen2Mass
        genVID[0] = treeMine.gen2ID
        jetVl1l2l3[0] = treeMine.jet2l1l2l3
        jetVl2l3[0] = treeMine.jet2l2l3
        jetVJER[0] = treeMine.jet2JER

    if jetHpt[0] < 400:
        sf1 = 0.929
        sf1change = 0.078
    elif jetHpt[0] >= 400 and jetHpt[0] < 500:
        sf1 = 0.999
        sf1change = 0.126
    elif jetHpt[0] >= 500 and jetHpt[0] < 600:
        sf1 = 0.933
        sf1change = 0.195
    elif jetHpt[0] >= 600:
        sf1 = 1.048
        sf1change = 0.215
        
    SF[0] = sf1
    SFup[0] = sf1*(1+sf1change)
    SFdown[0] = sf1*(1-sf1change)

    etadiff[0] = treeMine.etadiff
    dijetmass[0] = treeMine.dijetmass
    dijetmass_corr[0] = treeMine.dijetmass_corr
    dijetmass_corr_punc[0] = treeMine.dijetmass_corr_punc
    nHiggsTags[0] = treeMine.nHiggsTags
    triggerpassbb[0] = treeMine.triggerpassbb
    triggerpasssj[0] = treeMine.triggerpasssj
    nTrueInt[0] = treeMine.nTrueInt
    puWeights[0] = treeMine.puWeights
    puWeightsUp[0] = treeMine.puWeightsUp
    puWeightsDown[0] = treeMine.puWeightsDown
    vtype[0] = treeMine.vtype
    isData[0] = treeMine.isData
    json[0] = treeMine.json
    trigWeight[0] = treeMine.trigWeight
    trigWeightUp[0] = treeMine.trigWeightUp
    trigWeightDown[0] = treeMine.trigWeightDown
    trigWeight2Up[0] = treeMine.trigWeight2Up
    trigWeight2Down[0] = treeMine.trigWeight2Down
    norm[0] = treeMine.norm
    evt[0] = treeMine.evt
    ht[0] = treeMine.ht
    xsec[0] = treeMine.xsec
    mynewTree.Fill()

print "done " + outputfilename

f1.cd()
f1.Write()
f1.Close()

f.Close()


