#!/usr/bin/env python
import sys
import os,subprocess
import ROOT 
import math
import shutil
from array import array
import warnings
warnings.filterwarnings( action='ignore', category=RuntimeWarning, message='creating converter.*' )
ROOT.gROOT.SetBatch(True)
from optparse import OptionParser

#usage: ./write_regression_systematic.py path

#os.mkdir(path+'/sys')
argv = sys.argv
parser = OptionParser()
#parser.add_option("-P", "--path", dest="path", default="", 
#                      help="path to samples")
parser.add_option("-S", "--samples", dest="names", default="", 
                      help="samples you want to run on")
parser.add_option("-C", "--config", dest="config", default=[], action="append",
                      help="configuration defining the plots to make")
(opts, args) = parser.parse_args(argv)
if opts.config =="":
        opts.config = "config"

from myutils import BetterConfigParser, ParseInfo

print opts.config
config = BetterConfigParser()
config.read(opts.config)
anaTag = config.get("Analysis","tag")
TrainFlag = eval(config.get('Analysis','TrainFlag'))
btagLibrary = config.get('BTagReshaping','library')
samplesinfo=config.get('Directories','samplesinfo')

VHbbNameSpace=config.get('VHbbNameSpace','library')
ROOT.gSystem.Load(VHbbNameSpace)
AngLikeBkgs=eval(config.get('AngularLike','backgrounds'))
ang_yield=eval(config.get('AngularLike','yields'))

#path=opts.path
pathIN = config.get('Directories','SYSin')
pathOUT = config.get('Directories','SYSout')
tmpDir = os.environ["TMPDIR"]

print 'INput samples:\t%s'%pathIN
print 'OUTput samples:\t%s'%pathOUT


#storagesamples = config.get('Directories','storagesamples')


namelist=opts.names.split(',')

#load info
info = ParseInfo(samplesinfo,pathIN)

def deltaPhi(phi1, phi2): 
    result = phi1 - phi2
    while (result > math.pi): result -= 2*math.pi
    while (result <= -math.pi): result += 2*math.pi
    return result

def resolutionBias(eta):
    if(eta< 0.5): return 0.052
    if(eta< 1.1): return 0.057
    if(eta< 1.7): return 0.096
    if(eta< 2.3): return 0.134
    if(eta< 5): return 0.28
    return 0

def corrPt(pt,eta,mcPt):
    return (pt+resolutionBias(math.fabs(eta))*(pt-mcPt))/pt

def corrCSV(btag,  csv, flav):
    if(csv < 0.): return csv
    if(csv > 1.): return csv;
    if(flav == 0): return csv;
    if(math.fabs(flav) == 5): return  btag.ib.Eval(csv)
    if(math.fabs(flav) == 4): return  btag.ic.Eval(csv)
    if(math.fabs(flav) != 4  and math.fabs(flav) != 5): return  btag.il.Eval(csv)
    return -10000


def csvReshape(sh, pt, eta, csv, flav):
	return sh.reshape(float(eta), float(pt), float(csv), int(flav))


for job in info:
    if not job.name in namelist: continue
    ROOT.gROOT.ProcessLine(
        "struct H {\
        int         HiggsFlag;\
        float         mass;\
        float         pt;\
        float         eta;\
        float         phi;\
        float         dR;\
        float         dPhi;\
        float         dEta;\
        } ;"
    )
    if anaTag == '7TeV':
        ROOT.gSystem.Load(btagLibrary)
        from ROOT import BTagShape
        btagNom = BTagShape("../data/csvdiscr.root")
        btagNom.computeFunctions()
        btagUp = BTagShape("../data/csvdiscr.root")
        btagUp.computeFunctions(+1.,0.)
        btagDown = BTagShape("../data/csvdiscr.root")
        btagDown.computeFunctions(-1.,0.)
        btagFUp = BTagShape("../data/csvdiscr.root")
        btagFUp.computeFunctions(0.,+1.)
        btagFDown = BTagShape("../data/csvdiscr.root")
        btagFDown.computeFunctions(0.,-1.)
    else:
        ROOT.gSystem.Load(btagLibrary)
        from ROOT import BTagShapeInterface
        btagNom = BTagShapeInterface("../data/csvdiscr.root",0,0)
        btagUp = BTagShapeInterface("../data/csvdiscr.root",+1,0)
        btagDown = BTagShapeInterface("../data/csvdiscr.root",-1,0)
        btagFUp = BTagShapeInterface("../data/csvdiscr.root",0,+1.)
        btagFDown = BTagShapeInterface("../data/csvdiscr.root",0,-1.)
    
    lhe_weight_map = False if not config.has_option('LHEWeights', 'weights_per_bin') else eval(config.get('LHEWeights', 'weights_per_bin'))
    
    
    print '\t - %s' %(job.name)
    input = ROOT.TFile.Open(pathIN+'/'+job.prefix+job.identifier+'.root','read')
    output = ROOT.TFile.Open(tmpDir+'/'+job.prefix+job.identifier+'.root','recreate')

    input.cd()
    if lhe_weight_map and 'DY' in job.name:
        inclusiveJob = info.get_sample('DY')
        print inclusiveJob.name
        inclusive = ROOT.TFile.Open(pathIN+inclusiveJob.get_path,'read')
        inclusive.cd()
        obj = ROOT.TObject
        for key in ROOT.gDirectory.GetListOfKeys():
            input.cd()
            obj = key.ReadObj()
            if obj.GetName() == job.tree:
                continue
            output.cd()
            obj.Write(key.GetName())
        inclusive.Close()
    else:
        obj = ROOT.TObject
        for key in ROOT.gDirectory.GetListOfKeys():
            input.cd()
            obj = key.ReadObj()
            if obj.GetName() == job.tree:
                continue
            output.cd()
            obj.Write(key.GetName())
        
    input.cd()
    tree = input.Get(job.tree)
    nEntries = tree.GetEntries()
        
    H = ROOT.H()
    HNoReg = ROOT.H()
    tree.SetBranchStatus('H',0)
    output.cd()
    newtree = tree.CloneTree(0)
        
    hJ0 = ROOT.TLorentzVector()
    hJ1 = ROOT.TLorentzVector()
    vect = ROOT.TLorentzVector()
    #hFJ0 = ROOT.TLorentzVector()
    #hFJ1 = ROOT.TLorentzVector()
        
    regWeight = config.get("Regression","regWeight")
    regDict = eval(config.get("Regression","regDict"))
    regVars = eval(config.get("Regression","regVars"))
    #regWeightFilterJets = config.get("Regression","regWeightFilterJets")
    #regDictFilterJets = eval(config.get("Regression","regDictFilterJets"))
    #regVarsFilterJets = eval(config.get("Regression","regVarsFilterJets"))
          
    #Regression branches
    applyRegression = True
    hJet_pt = array('f',[0]*2)
    hJet_e = array('f',[0]*2)
    newtree.Branch( 'H', H , 'HiggsFlag/I:mass/F:pt/F:eta/F:phi/F:dR/F:dPhi/F:dEta/F' )
    newtree.Branch( 'HNoReg', HNoReg , 'HiggsFlag/I:mass/F:pt/F:eta/F:phi/F:dR/F:dPhi/F:dEta/F' )
    #FatHReg = array('f',[0]*2)
    #newtree.Branch('FatHReg',FatHReg,'filteredmass:filteredpt/F')
    Event = array('f',[0])
    METet = array('f',[0])
    rho25 = array('f',[0])
    METphi = array('f',[0])
    fRho25 = ROOT.TTreeFormula("rho25",'rho25',tree)
    fEvent = ROOT.TTreeFormula("Event",'EVENT.event',tree)
    fFatHFlag = ROOT.TTreeFormula("FatHFlag",'FatH.FatHiggsFlag',tree)
    fFatHnFilterJets = ROOT.TTreeFormula("FatHnFilterJets",'nfathFilterJets',tree)
    fMETet = ROOT.TTreeFormula("METet",'MET.et',tree)
    fMETphi = ROOT.TTreeFormula("METphi",'MET.phi',tree)
    fHVMass = ROOT.TTreeFormula("HVMass",'HVMass',tree)
    hJet_MtArray = [array('f',[0]),array('f',[0])]
    hJet_EtArray = [array('f',[0]),array('f',[0])]
    hJet_MET_dPhi = array('f',[0]*2)
    hJet_regWeight = array('f',[0]*2)
    fathFilterJets_regWeight = array('f',[0]*2)
    hJet_MET_dPhiArray = [array('f',[0]),array('f',[0])]
    hJet_ptRawArray = [array('f',[0]),array('f',[0])]
    newtree.Branch('hJet_MET_dPhi',hJet_MET_dPhi,'hJet_MET_dPhi[2]/F')
    newtree.Branch('hJet_regWeight',hJet_regWeight,'hJet_regWeight[2]/F')
    readerJet0 = ROOT.TMVA.Reader("!Color:!Silent" )
    readerJet1 = ROOT.TMVA.Reader("!Color:!Silent" )
        
    theForms = {}
    theVars0 = {}
    theVars1 = {}
    def addVarsToReader(reader,regDict,regVars,theVars,theForms,i,hJet_MET_dPhiArray,METet,rho25,hJet_MtArray,hJet_EtArray,hJet_ptRawArray):
        for key in regVars:
            var = regDict[key]
            theVars[key] = array( 'f', [ 0 ] )
            if var == 'Jet_MET_dPhi':
                print 'Adding var: %s with %s to readerJet%.0f' %(key,var,i)
                reader.AddVariable( key, hJet_MET_dPhiArray[i] )
            elif var == 'METet':
                print 'Adding var: %s with %s to readerJet%.0f' %(key,var,i)
                reader.AddVariable( key, METet )
            elif var == 'rho25':
                print 'Adding var: %s with %s to readerJet%.0f' %(key,var,i)
                reader.AddVariable( key, rho25 )
            elif var == 'Jet_mt':
                print 'Adding var: %s with %s to readerJet%.0f' %(key,var,i)
                reader.AddVariable( key, hJet_MtArray[i] )
            elif var == 'Jet_et':
                print 'Adding var: %s with %s to readerJet%.0f' %(key,var,i)
                reader.AddVariable( key, hJet_EtArray[i] )
            elif var == 'Jet_ptRaw':
                print 'Adding var: %s with %s to readerJet%.0f' %(key,var,i)
                reader.AddVariable( key, hJet_ptRawArray[i] )
            else:
                reader.AddVariable(key,theVars[key])
                formula = regDict[key].replace("[0]","[%.0f]" %i)
                print 'Adding var: %s with %s to readerJet%.0f' %(key,formula,i)
                theForms['form_reg_%s_%.0f'%(key,i)] = ROOT.TTreeFormula("form_reg_%s_%.0f"%(key,i),'%s' %(formula),tree)
        return 
    addVarsToReader(readerJet0,regDict,regVars,theVars0,theForms,0,hJet_MET_dPhiArray,METet,rho25,hJet_MtArray,hJet_EtArray,hJet_ptRawArray)    
    addVarsToReader(readerJet1,regDict,regVars,theVars1,theForms,1,hJet_MET_dPhiArray,METet,rho25,hJet_MtArray,hJet_EtArray,hJet_ptRawArray)    
    readerJet0.BookMVA( "jet0Regression", regWeight )
    readerJet1.BookMVA( "jet1Regression", regWeight )
    
    #readerFJ0 = ROOT.TMVA.Reader("!Color:!Silent" )
    #readerFJ1 = ROOT.TMVA.Reader("!Color:!Silent" )
    #theFormsFJ = {}
    #theVars0FJ = {}
    #theVars1FJ = {}
    #addVarsToReader(readerFJ0,regDictFilterJets,regVarsFilterJets,theVars0FJ,theFormsFJ,0,hJet_MET_dPhiArray,METet,rho25,hJet_MtArray,hJet_EtArray,hJet_ptRawArray)    
    #addVarsToReader(readerFJ1,regDictFilterJets,regVarsFilterJets,theVars1FJ,theFormsFJ,1,hJet_MET_dPhiArray,METet,rho25,hJet_MtArray,hJet_EtArray,hJet_ptRawArray)    
    #readerFJ0.BookMVA( "jet0RegressionFJ", regWeightFilterJets )
    #readerFJ1.BookMVA( "jet1RegressionFJ", regWeightFilterJets )
    
        
    #Add training Flag
    EventForTraining = array('i',[0])
    newtree.Branch('EventForTraining',EventForTraining,'EventForTraining/I')
    EventForTraining[0]=0

    TFlag=ROOT.TTreeFormula("EventForTraining","EVENT.event%2",tree)

    #Angular Likelihood
    angleHB = array('f',[0])
    newtree.Branch('angleHB',angleHB,'angleHB/F')
    angleLZ = array('f',[0])
    newtree.Branch('angleLZ',angleLZ,'angleLZ/F')
    angleZZS = array('f',[0])
    newtree.Branch('angleZZS',angleZZS,'angleZZS/F')
    kinLikeRatio = array('f',[0]*len(AngLikeBkgs))
    newtree.Branch('kinLikeRatio',kinLikeRatio,'%s/F' %(':'.join(AngLikeBkgs)))
    fAngleHB = ROOT.TTreeFormula("fAngleHB",'abs(VHbb::ANGLEHB(hJet_pt[0],hJet_eta[0],hJet_phi[0],hJet_e[0],hJet_pt[1],hJet_eta[1],hJet_phi[1],hJet_e[1]))',newtree)
    fAngleLZ = ROOT.TTreeFormula("fAngleLZ",'abs(VHbb::ANGLELZ(vLepton_pt[0],vLepton_eta[0],vLepton_phi[0],vLepton_mass[0],vLepton_pt[1],vLepton_eta[1],vLepton_phi[1],vLepton_mass[1]))',newtree)
    fAngleZZS = ROOT.TTreeFormula("fAngleZZS",'abs(VHbb::ANGLELZ(H.pt,H.eta,H.phi,H.pt,V.pt,V.eta,V.phi,V.mass))',newtree)
    fVpt = ROOT.TTreeFormula("fVpt",'V.pt',tree)
    fVeta = ROOT.TTreeFormula("fVeta",'V.eta',tree)
    fVphi = ROOT.TTreeFormula("fVphi",'V.phi',tree)
    fVmass = ROOT.TTreeFormula("fVmass",'V.mass',tree)
    likeSBH = array('f',[0]*len(AngLikeBkgs))
    likeBBH = array('f',[0]*len(AngLikeBkgs))
    likeSLZ = array('f',[0]*len(AngLikeBkgs))
    likeBLZ = array('f',[0]*len(AngLikeBkgs))
    likeSZZS = array('f',[0]*len(AngLikeBkgs))
    likeBZZS = array('f',[0]*len(AngLikeBkgs))
    likeSMassZS = array('f',[0]*len(AngLikeBkgs))
    likeBMassZS = array('f',[0]*len(AngLikeBkgs))
    HVMass_Reg = array('f',[0])
    newtree.Branch('HVMass_Reg',HVMass_Reg,'HVMass_Reg/F')

    SigBH = []; BkgBH = []; SigLZ = []; BkgLZ = []; SigZZS = []; BkgZZS = []; SigMassZS = []; BkgMassZS = [];
    for angLikeBkg in AngLikeBkgs:
        f = ROOT.TFile("../data/angleFitFunctions-%s.root"%(angLikeBkg),"READ")
        SigBH.append(f.Get("sigFuncBH"))
        BkgBH.append(f.Get("bkgFuncBH"))
        SigLZ.append(f.Get("sigFuncLZ"))
        BkgLZ.append(f.Get("bkgFuncLZ"))
        SigZZS.append(f.Get("sigFuncZZS"))
        BkgZZS.append(f.Get("bkgFuncZZS"))
        SigMassZS.append(f.Get("sigFuncMassZS"))
        BkgMassZS.append(f.Get("bkgFuncMassZS"))
        f.Close()

        
    if job.type != 'DATA':
        #CSV branches
        hJet_flavour = array('f',[0]*2)
        hJet_csv = array('f',[0]*2)
        hJet_csvOld = array('f',[0]*2)
        hJet_csvUp = array('f',[0]*2)
        hJet_csvDown = array('f',[0]*2)
        hJet_csvFUp = array('f',[0]*2)
        hJet_csvFDown = array('f',[0]*2)
        newtree.Branch('hJet_csvOld',hJet_csvOld,'hJet_csvOld[2]/F')
        newtree.Branch('hJet_csvUp',hJet_csvUp,'hJet_csvUp[2]/F')
        newtree.Branch('hJet_csvDown',hJet_csvDown,'hJet_csvDown[2]/F')
        newtree.Branch('hJet_csvFUp',hJet_csvFUp,'hJet_csvFUp[2]/F')
        newtree.Branch('hJet_csvFDown',hJet_csvFDown,'hJet_csvFDown[2]/F')
        
        #JER branches
        hJet_pt_JER_up = array('f',[0]*2)
        newtree.Branch('hJet_pt_JER_up',hJet_pt_JER_up,'hJet_pt_JER_up[2]/F')
        hJet_pt_JER_down = array('f',[0]*2)
        newtree.Branch('hJet_pt_JER_down',hJet_pt_JER_down,'hJet_pt_JER_down[2]/F')
        hJet_e_JER_up = array('f',[0]*2)
        newtree.Branch('hJet_e_JER_up',hJet_e_JER_up,'hJet_e_JER_up[2]/F')
        hJet_e_JER_down = array('f',[0]*2)
        newtree.Branch('hJet_e_JER_down',hJet_e_JER_down,'hJet_e_JER_down[2]/F')
        H_JER = array('f',[0]*4)
        newtree.Branch('H_JER',H_JER,'mass_up:mass_down:pt_up:pt_down/F')
        HVMass_JER_up = array('f',[0])
        HVMass_JER_down = array('f',[0])
        newtree.Branch('HVMass_JER_up',HVMass_JER_up,'HVMass_JER_up/F')
        newtree.Branch('HVMass_JER_down',HVMass_JER_down,'HVMass_JER_down/F')
        angleHB_JER_up = array('f',[0])
        angleHB_JER_down = array('f',[0])
        angleZZS_JER_up = array('f',[0])
        angleZZS_JER_down = array('f',[0])
        newtree.Branch('angleHB_JER_up',angleHB_JER_up,'angleHB_JER_up/F')
        newtree.Branch('angleHB_JER_down',angleHB_JER_down,'angleHB_JER_down/F')
        newtree.Branch('angleZZS_JER_up',angleZZS_JER_up,'angleZZS_JER_up/F')
        newtree.Branch('angleZZS_JER_down',angleZZS_JER_down,'angleZZS_JER_down/F')
        
        #JES branches
        hJet_pt_JES_up = array('f',[0]*2)
        newtree.Branch('hJet_pt_JES_up',hJet_pt_JES_up,'hJet_pt_JES_up[2]/F')
        hJet_pt_JES_down = array('f',[0]*2)
        newtree.Branch('hJet_pt_JES_down',hJet_pt_JES_down,'hJet_pt_JES_down[2]/F')
        hJet_e_JES_up = array('f',[0]*2)
        newtree.Branch('hJet_e_JES_up',hJet_e_JES_up,'hJet_e_JES_up[2]/F')
        hJet_e_JES_down = array('f',[0]*2)
        newtree.Branch('hJet_e_JES_down',hJet_e_JES_down,'hJet_e_JES_down[2]/F')
        H_JES = array('f',[0]*4)
        newtree.Branch('H_JES',H_JES,'mass_up:mass_down:pt_up:pt_down/F')
        HVMass_JES_up = array('f',[0])
        HVMass_JES_down = array('f',[0])
        newtree.Branch('HVMass_JES_up',HVMass_JES_up,'HVMass_JES_up/F')
        newtree.Branch('HVMass_JES_down',HVMass_JES_down,'HVMass_JES_down/F')
        angleHB_JES_up = array('f',[0])
        angleHB_JES_down = array('f',[0])
        angleZZS_JES_up = array('f',[0])
        angleZZS_JES_down = array('f',[0])
        newtree.Branch('angleHB_JES_up',angleHB_JES_up,'angleHB_JES_up/F')
        newtree.Branch('angleHB_JES_down',angleHB_JES_down,'angleHB_JES_down/F')
        newtree.Branch('angleZZS_JES_up',angleZZS_JES_up,'angleZZS_JES_up/F')
        newtree.Branch('angleZZS_JES_down',angleZZS_JES_down,'angleZZS_JES_down/F')
    
        #Formulas for syst in angular
        fAngleHB_JER_up = ROOT.TTreeFormula("fAngleHB_JER_up",'abs(VHbb::ANGLEHB(hJet_pt_JER_up[0],hJet_eta[0],hJet_phi[0],hJet_e_JER_up[0],hJet_pt_JER_up[1],hJet_eta[1],hJet_phi[1],hJet_e_JER_up[1]))',newtree)
        fAngleHB_JER_down = ROOT.TTreeFormula("fAngleHB_JER_down",'abs(VHbb::ANGLEHB(hJet_pt_JER_down[0],hJet_eta[0],hJet_phi[0],hJet_e_JER_down[0],hJet_pt_JER_down[1],hJet_eta[1],hJet_phi[1],hJet_e_JER_down[1]))',newtree)
        fAngleHB_JES_up = ROOT.TTreeFormula("fAngleHB_JES_up",'abs(VHbb::ANGLEHB(hJet_pt_JES_up[0],hJet_eta[0],hJet_phi[0],hJet_e_JES_up[0],hJet_pt_JES_up[1],hJet_eta[1],hJet_phi[1],hJet_e_JES_up[1]))',newtree)
        fAngleHB_JES_down = ROOT.TTreeFormula("fAngleHB_JES_down",'abs(VHbb::ANGLEHB(hJet_pt_JES_down[0],hJet_eta[0],hJet_phi[0],hJet_e_JES_down[0],hJet_pt_JES_down[1],hJet_eta[1],hJet_phi[1],hJet_e_JES_down[1]))',newtree)
        fAngleZZS_JER_up = ROOT.TTreeFormula("fAngleZZS_JER_Up",'abs(VHbb::ANGLELZ(H_JER.pt_up,H.eta,H.phi,H_JER.pt_up,V.pt,V.eta,V.phi,V.mass))',newtree)
        fAngleZZS_JER_down = ROOT.TTreeFormula("fAngleZZS_JER_Down",'abs(VHbb::ANGLELZ(H_JER.pt_down,H.eta,H.phi,H_JER.pt_down,V.pt,V.eta,V.phi,V.mass))',newtree)
        fAngleZZS_JES_up = ROOT.TTreeFormula("fAngleZZS_JES_Up",'abs(VHbb::ANGLELZ(H_JER.pt_up,H.eta,H.phi,H_JER.pt_up,V.pt,V.eta,V.phi,V.mass))',newtree)
        fAngleZZS_JES_down = ROOT.TTreeFormula("fAngleZZS_JES_Down",'abs(VHbb::ANGLELZ(H_JER.pt_down,H.eta,H.phi,H_JER.pt_down,V.pt,V.eta,V.phi,V.mass))',newtree)
        lheWeight = array('f',[0])
        newtree.Branch('lheWeight',lheWeight,'lheWeight/F')
        theBinForms = {}
        if lhe_weight_map and 'DY' in job.name:
            for bin in lhe_weight_map:
                theBinForms[bin] = ROOT.TTreeFormula("Bin_formula_%s"%(bin),bin,tree)
        else:
            lheWeight[0] = 1.
        
        #iter=0
        
        
    for entry in range(0,nEntries):
            tree.GetEntry(entry)

            if job.type != 'DATA':
                EventForTraining[0]=int(not TFlag.EvalInstance())
            if lhe_weight_map and 'DY' in job.name:
                match_bin = None
                for bin in lhe_weight_map:
                    if theBinForms[bin].EvalInstance() > 0.:
                        match_bin = bin
                if match_bin:
                    lheWeight[0] = lhe_weight_map[match_bin]
                else:
                    lheWeight[0] = 1.

            #Has fat higgs
            #fatHiggsFlag=fFatHFlag.EvalInstance()*fFatHnFilterJets.EvalInstance()
            #get
            vect.SetPtEtaPhiM(fVpt.EvalInstance(),fVeta.EvalInstance(),fVphi.EvalInstance(),fVmass.EvalInstance())
            hJet_pt = tree.hJet_pt
            hJet_e = tree.hJet_e
            hJet_pt0 = tree.hJet_pt[0]
            hJet_pt1 = tree.hJet_pt[1]
            hJet_eta0 = tree.hJet_eta[0]
            hJet_eta1 = tree.hJet_eta[1]
            hJet_genPt0 = tree.hJet_genPt[0]
            hJet_genPt1 = tree.hJet_genPt[1]
            hJet_ptRaw0 = tree.hJet_ptRaw[0]
            hJet_ptRaw1 = tree.hJet_ptRaw[1]
            hJet_e0 = tree.hJet_e[0]
            hJet_e1 = tree.hJet_e[1]
            hJet_phi0 = tree.hJet_phi[0]
            hJet_phi1 = tree.hJet_phi[1]
            hJet_JECUnc0 = tree.hJet_JECUnc[0]
            hJet_JECUnc1 = tree.hJet_JECUnc[1]
            #Filterjets
            #if fatHiggsFlag:
            #    fathFilterJets_pt0 = tree.fathFilterJets_pt[0]
            #    fathFilterJets_pt1 = tree.fathFilterJets_pt[1]
            #    fathFilterJets_eta0 = tree.fathFilterJets_eta[0]
            #    fathFilterJets_eta1 = tree.fathFilterJets_eta[1]
            #    fathFilterJets_phi0 = tree.fathFilterJets_phi[0]
            #    fathFilterJets_phi1 = tree.fathFilterJets_phi[1]
            #    fathFilterJets_e0 = tree.fathFilterJets_e[0]
            #    fathFilterJets_e1 = tree.fathFilterJets_e[1]

            Event[0]=fEvent.EvalInstance()
            METet[0]=fMETet.EvalInstance()
            rho25[0]=fRho25.EvalInstance()
            METphi[0]=fMETphi.EvalInstance()
            for key, value in regDict.items():
                if not (value == 'Jet_MET_dPhi' or value == 'METet' or value == "rho25" or value == "Jet_et" or value == 'Jet_mt' or value == 'Jet_ptRaw'):
                    theVars0[key][0] = theForms["form_reg_%s_0" %(key)].EvalInstance()
                    theVars1[key][0] = theForms["form_reg_%s_1" %(key)].EvalInstance()
            #for key, value in regDictFilterJets.items():
            #    if not (value == 'Jet_MET_dPhi' or value == 'METet' or value == "rho25" or value == "Jet_et" or value == 'Jet_mt' or value == 'Jet_ptRaw'):
            #        theVars0FJ[key][0] = theFormsFJ["form_reg_%s_0" %(key)].EvalInstance()
            #        theVars1FJ[key][0] = theFormsFJ["form_reg_%s_1" %(key)].EvalInstance()
            hJet_MET_dPhi[0] = deltaPhi(METphi[0],hJet_phi0)
            hJet_MET_dPhi[1] = deltaPhi(METphi[0],hJet_phi1)
            hJet_MET_dPhiArray[0][0] = deltaPhi(METphi[0],hJet_phi0)
            hJet_MET_dPhiArray[1][0] = deltaPhi(METphi[0],hJet_phi1)
            if not job.type == 'DATA':
                corrRes0 = corrPt(hJet_pt0,hJet_eta0,hJet_genPt0)
                corrRes1 = corrPt(hJet_pt1,hJet_eta1,hJet_genPt1)
                hJet_ptRaw0 *= corrRes0
                hJet_ptRaw1 *= corrRes1
            hJet_ptRawArray[0][0] = hJet_ptRaw0
            hJet_ptRawArray[1][0] = hJet_ptRaw1
            hJ0.SetPtEtaPhiE(hJet_pt0,hJet_eta0,hJet_phi0,hJet_e0)
            hJ1.SetPtEtaPhiE(hJet_pt1,hJet_eta1,hJet_phi1,hJet_e1)
            hJet_et0 = hJ0.Et()
            hJet_et1 = hJ1.Et()
            hJet_mt0 = hJ0.Mt()
            hJet_mt1 = hJ1.Mt()
            
            
            if applyRegression:
                HNoReg.HiggsFlag = 1
                HNoReg.mass = (hJ0+hJ1).M()
                HNoReg.pt = (hJ0+hJ1).Pt()
                HNoReg.eta = (hJ0+hJ1).Eta()
                HNoReg.phi = (hJ0+hJ1).Phi()
                HNoReg.dR = hJ0.DeltaR(hJ1)
                HNoReg.dPhi = hJ0.DeltaPhi(hJ1)
                HNoReg.dEta = abs(hJ0.Eta()-hJ1.Eta())
                hJet_MtArray[0][0] = hJ0.Mt()
                hJet_MtArray[1][0] = hJ1.Mt()
                hJet_EtArray[0][0] = hJ0.Et()
                hJet_EtArray[1][0] = hJ1.Et()
                rPt0 = max(0.0001,readerJet0.EvaluateRegression( "jet0Regression" )[0])
                rPt1 = max(0.0001,readerJet1.EvaluateRegression( "jet1Regression" )[0])
                hJet_regWeight[0] = rPt0/hJet_pt0
                hJet_regWeight[1] = rPt1/hJet_pt1
                rE0 = hJet_e0*hJet_regWeight[0]
                rE1 = hJet_e1*hJet_regWeight[1]
                hJ0.SetPtEtaPhiE(rPt0,hJet_eta0,hJet_phi0,rE0)
                hJ1.SetPtEtaPhiE(rPt1,hJet_eta1,hJet_phi1,rE1)
                #print '###new####'
                #print 'First regression %s' %rPt0
                tree.hJet_pt[0] = rPt0
                tree.hJet_pt[1] = rPt1
                tree.hJet_e[0] = rE0
                tree.hJet_e[1] = rE1
                H.HiggsFlag = 1
                H.mass = (hJ0+hJ1).M()
                H.pt = (hJ0+hJ1).Pt()
                H.eta = (hJ0+hJ1).Eta()
                H.phi = (hJ0+hJ1).Phi()
                H.dR = hJ0.DeltaR(hJ1)
                H.dPhi = hJ0.DeltaPhi(hJ1)
                H.dEta = abs(hJ0.Eta()-hJ1.Eta())
                HVMass_Reg[0] = (hJ0+hJ1+vect).M()
                if hJet_regWeight[0] > 5. or hJet_regWeight[1] > 5.:
                    print 'Event %.0f' %(Event[0])
                    print 'MET %.2f' %(METet[0])
                    print 'rho25 %.2f' %(rho25[0])
                    for key, value in regDict.items():
                        if not (value == 'Jet_MET_dPhi' or value == 'METet' or value == "rho25" or value == "Jet_et" or value == 'Jet_mt' or value == 'Jet_ptRaw'):
                            print '%s 0: %.2f'%(key, theVars0[key][0])
                            print '%s 1: %.2f'%(key, theVars1[key][0])
                    for i in range(2):
                        print 'dPhi %.0f %.2f' %(i,hJet_MET_dPhiArray[i][0])
                    for i in range(2):
                        print 'ptRaw %.0f %.2f' %(i,hJet_ptRawArray[i][0])
                    for i in range(2):
                        print 'Mt %.0f %.2f' %(i,hJet_MtArray[i][0])
                    for i in range(2):
                        print 'Et %.0f %.2f' %(i,hJet_EtArray[i][0])
                    print 'corr 0 %.2f' %(hJet_regWeight[0])
                    print 'corr 1 %.2f' %(hJet_regWeight[1])
                    print 'rPt0 %.2f' %(rPt0)
                    print 'rPt1 %.2f' %(rPt1)
                    print 'rE0 %.2f' %(rE0)
                    print 'rE1 %.2f' %(rE1)
                    print 'Mass %.2f' %(H.mass)
                #if fatHiggsFlag:
                    #hFJ0.SetPtEtaPhiE(fathFilterJets_pt0,fathFilterJets_eta0,fathFilterJets_phi0,fathFilterJets_e0)
                    #hFJ1.SetPtEtaPhiE(fathFilterJets_pt1,fathFilterJets_eta1,fathFilterJets_phi1,fathFilterJets_e1)
                    #rFJPt0 = max(0.0001,readerFJ0.EvaluateRegression( "jet0RegressionFJ" )[0])
                    #rFJPt1 = max(0.0001,readerFJ1.EvaluateRegression( "jet1RegressionFJ" )[0])
                    #fathFilterJets_regWeight[0] = rPt0/fathFilterJets_pt0
                    #fathFilterJets_regWeight[1] = rPt1/fathFilterJets_pt1
                    #rFJE0 = fathFilterJets_e0*fathFilterJets_regWeight[0]
                    #rFJE1 = fathFilterJets_e1*fathFilterJets_regWeight[1]
                    #hFJ0.SetPtEtaPhiE(rFJPt0,fathFilterJets_eta0,fathFilterJets_phi0,rFJE0)
                    #hFJ1.SetPtEtaPhiE(rFJPt1,fathFilterJets_eta1,fathFilterJets_phi1,rFJE1)
                    #FatHReg[0] = (hFJ0+hFJ1).M()
                    #FatHReg[1] = (hFJ0+hFJ1).Pt()
                #else:
                    #FatHReg[0] = 0.
                    #FatHReg[1] = 0.

                    #print rFJPt0
                    #print rFJPt1
            
            angleHB[0]=fAngleHB.EvalInstance()
            angleLZ[0]=fAngleLZ.EvalInstance()
            angleZZS[0]=fAngleZZS.EvalInstance()

            for i, angLikeBkg in enumerate(AngLikeBkgs):
                likeSBH[i] = math.fabs(SigBH[i].Eval(angleHB[0]))
                likeBBH[i] = math.fabs(BkgBH[i].Eval(angleHB[0]))

                likeSZZS[i] = math.fabs(SigZZS[i].Eval(angleZZS[0]))
                likeBZZS[i] = math.fabs(BkgZZS[i].Eval(angleZZS[0]))         
                                   
                likeSLZ[i] = math.fabs(SigLZ[i].Eval(angleLZ[0]))         
                likeBLZ[i] = math.fabs(BkgLZ[i].Eval(angleLZ[0]))
                                                
                likeSMassZS[i] = math.fabs(SigMassZS[i].Eval(fHVMass.EvalInstance()))
                likeBMassZS[i] = math.fabs(BkgMassZS[i].Eval(fHVMass.EvalInstance()))

                scaleSig  = float( ang_yield['Sig'] / (ang_yield['Sig'] + ang_yield[angLikeBkg]))
                scaleBkg  = float( ang_yield[angLikeBkg] / (ang_yield['Sig'] + ang_yield[angLikeBkg]) )

                numerator = (likeSBH[i]*likeSZZS[i]*likeSLZ[i]*likeSMassZS[i]);
                denominator = ((scaleBkg*likeBLZ[i]*likeBZZS[i]*likeBBH[i]*likeBMassZS[i])+(scaleSig*likeSBH[i]*likeSZZS[i]*likeSLZ[i]*likeSMassZS[i]))

                if denominator > 0:
                    kinLikeRatio[i] = numerator/denominator;
                else:
                    kinLikeRatio[i] = 0;

            if job.type == 'DATA':
                newtree.Fill()
                continue

            for i in range(2):
                flavour = int(tree.hJet_flavour[i])
                pt = float(tree.hJet_pt[i])
                eta = float(tree.hJet_eta[i])
                csv = float(tree.hJet_csv[i])
                hJet_csvOld[i] = csv 
                if anaTag == '7TeV':
                    tree.hJet_csv[i] = corrCSV(btagNom,csv,flavour)
                    hJet_csvDown[i] = corrCSV(btagDown,csv,flavour)
                    hJet_csvUp[i] = corrCSV(btagUp,csv,flavour) 
                    hJet_csvFDown[i] = corrCSV(btagFDown,csv,flavour)
                    hJet_csvFUp[i] = corrCSV(btagFUp,csv,flavour)
                else:
                    #tree.hJet_csv[i] = btagNom.reshape(eta,pt,csv,flavour)
                    #hJet_csvDown[i] = btagDown.reshape(eta,pt,csv,flavour)
                    #hJet_csvUp[i] = btagUp.reshape(eta,pt,csv,flavour) 
                    #hJet_csvFDown[i] = btagFDown.reshape(eta,pt,csv,flavour)
                    #hJet_csvFUp[i] = btagFUp.reshape(eta,pt,csv,flavour)
                    tree.hJet_csv[i] = tree.hJet_csv_nominal[i]
                    hJet_csvDown[i] = tree.hJet_csv_downBC[i]
                    hJet_csvUp[i] = tree.hJet_csv_upBC[i]
                    hJet_csvFDown[i] = tree.hJet_csv_downL[i]
                    hJet_csvFUp[i] = tree.hJet_csv_upL[i]

            for updown in ['up','down']:
                #JER
                if updown == 'up':
                    inner = 0.06
                    outer = 0.1
                if updown == 'down':
                    inner = -0.06
                    outer = -0.1
                #Calculate
                if abs(hJet_eta0)<1.1: res0 = inner
                else: res0 = outer
                if abs(hJet_eta1)<1.1: res1 = inner
                else: res1 = outer
                rPt0 = hJet_pt0 + (hJet_pt0-hJet_genPt0)*res0
                rPt1 = hJet_pt1 + (hJet_pt1-hJet_genPt1)*res1
                rE0 = hJet_e0*rPt0/hJet_pt0
                rE1 = hJet_e1*rPt1/hJet_pt1
                if applyRegression:
                    hJ0.SetPtEtaPhiE(rPt0,hJet_eta0,hJet_phi0,rE0)
                    hJ1.SetPtEtaPhiE(rPt1,hJet_eta1,hJet_phi1,rE1)
                    hJet_MtArray[0][0] = hJ0.Mt()
                    hJet_MtArray[1][0] = hJ1.Mt()
                    hJet_EtArray[0][0] = hJ0.Et()
                    hJet_EtArray[1][0] = hJ1.Et()
                    for key in regVars:
                        var = regDict[key]
                        if key == 'Jet_pt' or key == 'Jet_e' or key == 'hJet_pt' or key == 'hJet_e' or key == 'Jet_ptRaw' or key =='VHbb::evalEt(hJet_pt,hJet_eta,hJet_phi,hJet_e)' or key =='VHbb::evalMt(hJet_pt,hJet_eta,hJet_phi,hJet_e)' or key == 'VHbb::evalJERBias(hJet_ptRaw,hJet_genPt,hJet_eta)':
                            if key == 'Jet_ptRaw':
                                hJet_ptRawArray[0][0] = hJet_ptRaw0*corrRes0*rPt0/hJet_pt0
                                hJet_ptRawArray[1][0] = hJet_ptRaw1*rPt1/hJet_pt1
                            elif key == 'VHbb::evalJERBias(hJet_ptRaw,hJet_genPt,hJet_eta)':
                                theVars0[key][0] = hJet_ptRaw0*corrRes0*rPt0/hJet_pt0
                                theVars1[key][0] = hJet_ptRaw1*rPt1/hJet_pt1
                            elif key == 'Jet_pt' or key == 'hJet_pt':
                                theVars0[key][0] = rPt0
                                theVars1[key][0] = rPt1
                            elif key == 'Jet_e' or key == 'hJet_e':
                                theVars0[key][0] = rE0
                                theVars1[key][0] = rE1
                            elif key == 'VHbb::evalEt(hJet_pt,hJet_eta,hJet_phi,hJet_e)':
                                theVars0[key][0] = hJ0.Et()
                                theVars1[key][0] = hJ1.Et()
                            elif key == 'VHbb::evalMt(hJet_pt,hJet_eta,hJet_phi,hJet_e)':
                                theVars0[key][0] = hJ0.Mt()
                                theVars1[key][0] = hJ1.Mt()
                    rPt0 = max(0.0001,readerJet0.EvaluateRegression( "jet0Regression" )[0])
                    rPt1 = max(0.0001,readerJet1.EvaluateRegression( "jet1Regression" )[0])
                    rE0 = hJet_e0*rPt0/hJet_pt0
                    rE1 = hJet_e1*rPt1/hJet_pt1
                hJ0.SetPtEtaPhiE(rPt0,hJet_eta0,hJet_phi0,rE0)
                hJ1.SetPtEtaPhiE(rPt1,hJet_eta1,hJet_phi1,rE1)
                #Set
                if updown == 'up':
                    hJet_pt_JER_up[0]=rPt0
                    hJet_pt_JER_up[1]=rPt1
                    hJet_e_JER_up[0]=rE0
                    hJet_e_JER_up[1]=rE1
                    H_JER[0]=(hJ0+hJ1).M()
                    H_JER[2]=(hJ0+hJ1).Pt()
                    HVMass_JER_up[0] = (hJ0+hJ1+vect).M()
                if updown == 'down':
                    hJet_pt_JER_down[0]=rPt0
                    hJet_pt_JER_down[1]=rPt1
                    hJet_e_JER_down[0]=rE0
                    hJet_e_JER_down[1]=rE1
                    H_JER[1]=(hJ0+hJ1).M()
                    H_JER[3]=(hJ0+hJ1).Pt()
                    HVMass_JER_down[0] = (hJ0+hJ1+vect).M()
                
                #JES
                if updown == 'up':
                    variation=1
                if updown == 'down':
                    variation=-1
                #calculate
                rPt0 = hJet_pt0*(1+variation*hJet_JECUnc0)
                rPt1 = hJet_pt1*(1+variation*hJet_JECUnc1)
                rE0 = hJet_e0*(1+variation*hJet_JECUnc0)
                rE1 = hJet_e1*(1+variation*hJet_JECUnc1)
                #print 'res %s: %s' %(updown,rPt0)
                if applyRegression:
                    hJ0.SetPtEtaPhiE(rPt0,hJet_eta0,hJet_phi0,rE0)
                    hJ1.SetPtEtaPhiE(rPt1,hJet_eta1,hJet_phi1,rE1)
                    hJet_MtArray[0][0] = hJ0.Mt()
                    hJet_MtArray[1][0] = hJ1.Mt()
                    hJet_EtArray[0][0] = hJ0.Et()
                    hJet_EtArray[1][0] = hJ1.Et()
                    for key in regVars:
                        var = regDict[key]
                        if key == 'Jet_pt' or key == 'Jet_e' or key == 'hJet_pt' or key == 'hJet_e' or key == 'Jet_ptRaw' or key =='VHbb::evalEt(hJet_pt,hJet_eta,hJet_phi,hJet_e)' or key =='VHbb::evalMt(hJet_pt,hJet_eta,hJet_phi,hJet_e)' or key == 'VHbb::evalJERBias(hJet_ptRaw,hJet_genPt,hJet_eta)':
                            if key == 'Jet_ptRaw':
                                hJet_ptRawArray[0][0] = hJet_ptRaw0*(1+variation*hJet_JECUnc0)
                                hJet_ptRawArray[1][0] = hJet_ptRaw1*(1+variation*hJet_JECUnc1)
                            elif key == 'VHbb::evalJERBias(hJet_ptRaw,hJet_genPt,hJet_eta)':
                                theVars0[key][0] = hJet_ptRaw0*(1+variation*hJet_JECUnc0)
                                theVars1[key][0] = hJet_ptRaw1*(1+variation*hJet_JECUnc1)
                            elif var == 'Jet_pt' or var == 'hJet_pt[0]' or var == 'hJet_pt[1]' :
                                theVars0[key][0] = rPt0
                                theVars1[key][0] = rPt1
                            elif var == 'Jet_e' or var == 'hJet_e':
                                theVars0[key][0] = rE0
                                theVars1[key][0] = rE1
                            elif var == 'hJet_e':
                                theVars0[key][0] = rE0
                                theVars1[key][0] = rE1
                            elif key == 'VHbb::evalEt(hJet_pt,hJet_eta,hJet_phi,hJet_e)':
                                theVars0[key][0] = hJ0.Et()
                                theVars1[key][0] = hJ1.Et()
                            elif key == 'VHbb::evalMt(hJet_pt,hJet_eta,hJet_phi,hJet_e)':
                                theVars0[key][0] = hJ0.Mt()
                                theVars1[key][0] = hJ1.Mt()
                    rPt0 = max(0.0001,readerJet0.EvaluateRegression( "jet0Regression" )[0])
                    rPt1 = max(0.0001,readerJet1.EvaluateRegression( "jet1Regression" )[0])
                    #print 'JES reg: %s' %rPt0
                    rE0 = hJet_e0*rPt0/hJet_pt0
                    rE1 = hJet_e1*rPt1/hJet_pt1
                hJ0.SetPtEtaPhiE(rPt0,hJet_eta0,hJet_phi0,rE0)
                hJ1.SetPtEtaPhiE(rPt1,hJet_eta1,hJet_phi1,rE1)
                #Fill
                if updown == 'up':
                    hJet_pt_JES_up[0]=rPt0
                    hJet_pt_JES_up[1]=rPt1
                    hJet_e_JES_up[0]=rE0
                    hJet_e_JES_up[1]=rE1
                    H_JES[0]=(hJ0+hJ1).M()
                    H_JES[2]=(hJ0+hJ1).Pt()
                    HVMass_JES_up[0] = (hJ0+hJ1+vect).M()
                if updown == 'down':
                    hJet_pt_JES_down[0]=rPt0
                    hJet_pt_JES_down[1]=rPt1
                    hJet_e_JES_down[0]=rE0
                    hJet_e_JES_down[1]=rE1
                    H_JES[1]=(hJ0+hJ1).M()
                    H_JES[3]=(hJ0+hJ1).Pt()
                    HVMass_JES_down[0] = (hJ0+hJ1+vect).M()
            
            angleHB_JER_up[0]=fAngleHB_JER_up.EvalInstance()
            angleHB_JER_down[0]=fAngleHB_JER_down.EvalInstance()
            angleHB_JES_up[0]=fAngleHB_JES_up.EvalInstance()
            angleHB_JES_down[0]=fAngleHB_JES_down.EvalInstance()
            angleZZS[0]=fAngleZZS.EvalInstance()
            angleZZS_JER_up[0]=fAngleZZS_JER_up.EvalInstance()
            angleZZS_JER_down[0]=fAngleZZS_JER_down.EvalInstance()
            angleZZS_JES_up[0]=fAngleZZS_JES_up.EvalInstance()
            angleZZS_JES_down[0]=fAngleZZS_JES_down.EvalInstance()
            
            newtree.Fill()
                   
    print 'Exit loop'
    newtree.AutoSave()
    print 'Save'
    output.Close()
    print 'Close'

    # In case the OUTpath is not local change the access protocol to be able to write in it.
    # Clean from possible other files with the same name in the OUTpath directory.
    # Copy from the tmp to the OUTpath.
    if OUTpath.find(':'):
        targetStorage = OUTpath.replace('root://cms-xrd-global.cern.ch//','srm://t3se01.psi.ch:8443/srm/managerv2?SFN=')+'/'+job.prefix+job.identifier+'.root'
        command = 'lcg-del -b -D srmv2 -l %s' %(targetStorage)
        print(command)
        subprocess.call([command], shell=True)
        command = 'lcg-cp -b -D srmv2 file:///%s %s' %(tmpDir+'/'+job.prefix+job.identifier+'.root',targetStorage)
        print(command)
        subprocess.call([command], shell=True)
    else:
        targetStorage = OUTpath+'/'+job.prefix+job.identifier+'.root'
        command = 'rm -f %s' %(targetStorage)
        print(command)
        subprocess.call([command], shell=True)
        command = 'cp file:///%s %s' %(tmpDir+'/'+job.prefix+job.identifier+'.root',targetStorage)
        print(command)
        subprocess.call([command], shell=True)


