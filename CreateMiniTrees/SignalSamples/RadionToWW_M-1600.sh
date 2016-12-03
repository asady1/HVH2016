#:!/bin/sh

#python generalTreeAnalyzer_76X.py --pathIn=/eos/uscms/store/group/lpchbb/HeppyNtuples/V21/JetHT/VHBB_HEPPY_V21_JetHT__Run2015C_25ns-16Dec2015-v1/160318_132855/0000/ --outName=Jet_HT_C --trigger=False --jets=True --deta=True --min=0 --max=31 --file=TxtFiles/76XRunC.txt &
./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../getMiniTrees.py .
cp ../../RadionToWW_M-1600.txt .
cp ../../trigger_objects.root .
cp ../../TMVARegression_BDTG.weights.xml .
cp ../../puppiCorr.root .

python getMiniTrees.py --pathIn=root://cmseos.fnal.gov//store/user/lpchbb/HeppyNtuples/V24b/user/cvernier/VHBBHeppyV24a/RadionToWW_narrow_M-1600_13TeV-madgraph/VHBB_HEPPY_V24a_RadionToWW_narrow_M-1600_13TeV-madgraph__spr16MAv2-puspr16_HLT_80r2as_v14-v1/161108_170756/0000/ --outName=RadionToWW_M-1600 --isMC=True --saveTrig=True --xsec=1.0 --min=0 --max=2 --file=RadionToWW_M-1600.txt --syst=None

xrdcp RadionToWW_M-1600_0.root root://cmseos.fnal.gov//store/user/mkrohn/HHHHTo4b/V23/Wprime/
