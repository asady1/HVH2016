#!/bin/sh

#python generalTreeAnalyzer_76X.py --pathIn=/eos/uscms/store/group/lpchbb/HeppyNtuples/V21/JetHT/VHBB_HEPPY_V21_JetHT__Run2015C_25ns-16Dec2015-v1/160318_132855/0000/ --outName=Jet_HT_C    --min=0 --max=31 --file=TxtFiles/76XRunC.txt &
./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../getMiniTrees.py .
cp ../../QCD_HT_700to1000_noExt.txt .
cp ../../trigger_objects.root .
cp ../../TMVARegression_BDTG.weights.xml .
cp ../../puppiCorr.root .
cp ../../miniTreeFunctions.py .
cp ../../miniTreeProducer.py .

python getMiniTrees.py --pathIn=root://cmseos.fnal.gov//store/user/lpchbb/HeppyNtuples/V24b/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VHBB_HEPPY_V24a_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v1/161115_134658/0000/ --outName=QCD_HT700to1000_noExt    --isMC=True --xsec=6831  --saveTrig=True --min=190 --max=200 --file=QCD_HT_700to1000_noExt.txt

xrdcp QCD_HT700to1000_noExt_190.root root://cmseos.fnal.gov//store/user/mkrohn/HHHHTo4b/V23/QCD700/
