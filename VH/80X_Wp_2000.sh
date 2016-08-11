#!/bin/sh

#python generalTreeAnalyzer_80X.py --pathIn=/eos/uscms/store/group/lpchbb/HeppyNtuples/V21/JetHT/VHBB_HEPPY_V21_JetHT__Run2015C_25ns-16Dec2015-v1/160318_132855/0000/ --outName=Jet_HT_C --trigger=False --jets=True --deta=True --min=0 --max=31 --file=TxtFiles/80XRunC.txt &
./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../generalTreeAnalyzer_80X.py .
cp ../../three.txt .
cp ../../trigger_objects.root .

python generalTreeAnalyzer_80X.py --pathIn=root://cmsxrootd.fnal.gov//store/user/lpchbb/HeppyNtuples/V23/WprimeToWhToWhadhbb_narrow_M-2000_13TeV-madgraph/VHBB_HEPPY_V23_WprimeToWhToWhadhbb_narrow_M-2000_13TeV-madgraph__spr16MAv2-puspr16_HLT_80r2as_v14-v1/160717_164535/0000/ --outName=Wp_2000_V23_V2 --trigger=False --jets=True --deta=True --isMC=True --xsec=1. --min=0 --max=3 --file=three.txt

xrdcp Wp_2000_V23_V2_0.root root://cmseos.fnal.gov//store/user/asady1
