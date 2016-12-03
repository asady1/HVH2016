:!/bin/sh

#python generalTreeAnalyzer_76X.py --pathIn=/eos/uscms/store/group/lpchbb/HeppyNtuples/V21/JetHT/VHBB_HEPPY_V21_JetHT__Run2015C_25ns-16Dec2015-v1/160318_132855/0000/ --outName=Jet_HT_C --trigger=False --jets=True --deta=True --min=0 --max=31 --file=TxtFiles/76XRunC.txt &
./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../generalTreeAnalyzer_76X_noTriggerBits_450.py .
cp ../../BulkGrav_M-450.txt .
cp ../../trigger_objects.root .

python generalTreeAnalyzer_76X_noTriggerBits_450.py --pathIn=root://cmsxrootd.fnal.gov//store/user/lpchbb/HeppyNtuples/V23/GluGluToBulkGravitonToHHTo4B_M-450_narrow_13TeV-madgraph/VHBB_HEPPY_V23_GluGluToBulkGravitonToHHTo4B_M-450_narrow_13TeV-madgraph__spr16MAv2-puspr16_HLT_80r2as_v14-v1/160716_235817/0000/ --outName=BulkGrav_M-450 --trigger=False --jets=True --deta=True --isMC=True --xsec=1 --min=0 --max=4 --file=BulkGrav_M-450.txt

xrdcp BulkGrav_M-450_0.root root://cmseos.fnal.gov//store/user/mkrohn/HHTo4b/V23/SignalSamples/
