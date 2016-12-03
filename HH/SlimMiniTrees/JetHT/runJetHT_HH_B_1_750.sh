./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`

cp ../../ttreeAnalyzer_hh_alphabet.py .

python ttreeAnalyzer_hh_alphabet.py -f root://cmseos.fnal.gov//store/user/mkrohn/HHHHTo4b/V23/JetHT_old/JetsHT_2016B_1_750.root -o root://cmseos.fnal.gov//store/user/mkrohn/HH_alphabet/

xrdcp JetsHT_2016B_1_750.root root://cmseos.fnal.gov//store/user/mkrohn/HH_alphabet/
