#!/bin/sh

#python generalTreeAnalyzer_76X.py --pathIn=/eos/uscms/store/group/lpchbb/HeppyNtuples/V21/JetHT/VHBB_HEPPY_V21_JetHT__Run2015C_25ns-16Dec2015-v1/160318_132855/0000/ --outName=Jet_HT_C    --min=0 --max=31 --file=TxtFiles/76XRunC.txt &
./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../getMiniTrees_pT200.py .
cp ../../TT_1.txt .
cp ../../trigger_objects.root .
cp ../../TMVARegression_BDTG.weights.xml .
cp ../../puppiCorr.root .
cp ../../miniTreeFunctions.py .
cp ../../miniTreeProducer_pT200.py .

python getMiniTrees_pT200.py --pathIn=root://cmseos.fnal.gov//store/user/lpchbb/HeppyNtuples/V24b/TT_TuneCUETP8M1_13TeV-powheg-pythia8/VHBB_HEPPY_V24a_TT_TuneCUETP8M1_13TeV-powheg-Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext3-v1/161115_010427/0001/ --outName=TT_1 --isMC=True --xsec=831.76 --saveTrig=True --min=0 --max=100 --file=TT_1.txt

xrdcp TT_1_0.root root://cmseos.fnal.gov//store/user/mkrohn/HHHHTo4b/V23/TT/
