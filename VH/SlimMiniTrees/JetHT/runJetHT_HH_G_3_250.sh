./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`

cp ../../ttreeAnalyzer_vh_alphabet_VbbTag.py .

python ttreeAnalyzer_vh_alphabet_VbbTag.py -f root://cmseos.fnal.gov//store/user/mkrohn/HHHHTo4b/V23/JetHT_old/JetsHT_2016G_3_250.root -o root://cmseos.fnal.gov//store/user/mkrohn/VH/

xrdcp JetsHT_2016G_3_250.root root://cmseos.fnal.gov//store/user/mkrohn/VH/
