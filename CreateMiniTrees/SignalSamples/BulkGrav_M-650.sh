#:!/bin/sh

#python generalTreeAnalyzer_76X.py --pathIn=/eos/uscms/store/group/lpchbb/HeppyNtuples/V21/JetHT/VHBB_HEPPY_V21_JetHT__Run2015C_25ns-16Dec2015-v1/160318_132855/0000/ --outName=Jet_HT_C --trigger=False --jets=True --deta=True --min=0 --max=31 --file=TxtFiles/76XRunC.txt &
./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../generalTreeAnalyzer_80X.py .
cp ../../BulkGrav_M-650.txt .
cp ../../trigger_objects.root .

python generalTreeAnalyzer_80X.py --pathIn=root://cmsxrootd.fnal.gov//store/user/lpchbb/HeppyNtuples/V23/GluGluToBulkGravitonToHHTo4B_M-650_narrow_13TeV-madgraph/VHBB_HEPPY_V23_GluGluToBulkGravitonToHHTo4B_M-650_narrow_13TeV-madgraph__spr16MAv2-puspr16_HLT_80r2as_v14-v1/160717_000039/0000/ --outName=BulkGrav_M-650 --trigger=False --jets=True --deta=True --isMC=True --xsec=1 --is2p1=False --saveTrig=True --min=0 --max=3 --file=BulkGrav_M-650.txt

xrdcp BulkGrav_M-650_0.root root://cmseos.fnal.gov//store/user/mkrohn/HHHHTo4b/V23/
ZJets/
