#!/bin/sh

#testing

./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../ttreeAnalyzer_2p1_V23.py .

#python ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_1000_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_1000_CSV.root
#xrdcp BG_1000_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_1200_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_1200_CSV.root
#xrdcp BG_1200_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_1400_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_1400_CSV.root
#xrdcp BG_1400_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_1600_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_1600_CSV.root
#xrdcp BG_1600_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_1800_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_1800_CSV.root
#xrdcp BG_1800_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_2000_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_2000_CSV.root
#xrdcp BG_2000_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_500_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_500_CSV.root
#xrdcp BG_500_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_550_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_550_CSV.root
#xrdcp BG_550_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_600_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_600_CSV.root
#xrdcp BG_600_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_650_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_650_CSV.root
#xrdcp BG_650_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_700_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_700_CSV.root
#xrdcp BG_700_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_750_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_750_CSV.root
#xrdcp BG_750_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_800_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_800_CSV.root
#xrdcp BG_800_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BG_900_V24_VR1_2p1_0.root --saveTrig="True" --ttbar="False" --outName=BG_900_CSV.root
#xrdcp BG_900_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/QCD_HT1000to1500_V23_V2_2p1.root --saveTrig="False" --outName=QCD_1000_CSV.root
#xrdcp QCD_1000_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/QCD_HT1500to2000_V23_V2_2p1.root --saveTrig="False" --outName=QCD_1500_CSV.root
#xrdcp QCD_1500_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/QCD_HT2000toInf_V23_V2_2p1.root --saveTrig="False" --outName=QCD_2000_CSV.root
#xrdcp QCD_2000_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/QCD_HT300to500_V23_V2_2p1.root --saveTrig="False" --outName=QCD_300_CSV.root
#xrdcp QCD_300_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/QCD_HT500to700_V23_V2_2p1.root --saveTrig="False" --outName=QCD_500_CSV.root
#xrdcp QCD_500_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/QCD_HT700to1000_V23_V2_2p1.root --saveTrig="False" --outName=QCD_700_CSV.root
#xrdcp QCD_700_CSV.root root://cmseos.fnal.gov//store/user/asady1

python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/BTagCSV_V24_VR1_2p1.root --saveTrig="True" --ttbar="False" --outName=BTag_CSV.root
xrdcp BTag_CSV.root root://cmseos.fnal.gov//store/user/asady1 

python  ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/JetHT_V24_VR1_2p1.root --saveTrig="True" --ttbar="False" --outName=JetHT_CSV.root
xrdcp JetHT_CSV.root root://cmseos.fnal.gov//store/user/asady1

#python ttreeAnalyzer_2p1_V23.py root://cmsxrootd.fnal.gov//store/user/asady1/TT_V24_HT.root --saveTrig="True" --ttbar="True" --outName=TT_CSV.root
#xrdcp TT_CSV.root root://cmseos.fnal.gov//store/user/asady1

