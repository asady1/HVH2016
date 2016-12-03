#:!/bin/sh

#python generalTreeAnalyzer_76X.py --pathIn=/eos/uscms/store/group/lpchbb/HeppyNtuples/V21/JetHT/VHBB_HEPPY_V21_JetHT__Run2015C_25ns-16Dec2015-v1/160318_132855/0000/ --outName=Jet_HT_C --trigger=False --jets=True --deta=True --min=0 --max=31 --file=TxtFiles/76XRunC.txt &
./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../getMiniTrees.py .
cp ../../BulkGrav_M-800.txt .
cp ../../trigger_objects.root .
cp ../../TMVARegression_BDTG.weights.xml .
cp ../../puppiCorr.root .
cp ../../miniTreeFunctions.py .
cp ../../miniTreeProducer.py .

python getMiniTrees.py --pathIn=root://cmseos.fnal.gov//store/user/lpchbb/HeppyNtuples/V24b/GluGluToBulkGravitonToHHTo4B_M-800_narrow_13TeV-madgraph/VHBB_HEPPY_V24a_GluGluToBulkGravitonToHHTo4B_M-800_narrow_13TeV-madgraph__spr16MAv2-puspr16_HLT_80r2as_v14-v1/161014_192551/0000/ --outName=BulkGrav_M-800 --isMC=True --xsec=1.0 --saveTrig=True --min=0 --max=4 --file=BulkGrav_M-800.txt

xrdcp BulkGrav_M-800_0.root root://cmseos.fnal.gov//store/user/mkrohn/HHHHTo4b/V23/BulkGrav_old/
