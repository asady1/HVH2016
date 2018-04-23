#!/bin/sh

#testing

./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../slimTreeMaker_final.py .
cp ../../DeepCSV_Moriond17_B_H.csv .
cp ../../gravall-v25.weights.xml .

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/BulkGrav/BulkGrav_M-1000_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_1000_tree_bfinally.root
xrdcp BG_1000_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/BulkGrav/BulkGrav_M-1200_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_1200_tree_bfinally.root
xrdcp BG_1200_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/BulkGrav/BulkGrav_M-1600_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_1600_tree_bfinally.root
xrdcp BG_1600_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/BulkGrav/BulkGrav_M-2000_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_2000_tree_bfinally.root
xrdcp BG_2000_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG500_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_500_tree_bfinally.root
xrdcp BG_500_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG550_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_550_tree_bfinally.root
xrdcp BG_550_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG600_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_600_tree_bfinally.root
xrdcp BG_600_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG650_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_650_tree_bfinally.root
xrdcp BG_650_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG750_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_750_tree_bfinally.root
xrdcp BG_750_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/BulkGrav/BulkGrav_M-800_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_800_tree_bfinally.root
xrdcp BG_800_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/BulkGrav/BulkGrav_M-900_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_900_tree_bfinally.root
xrdcp BG_900_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/
 
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT.root --saveTrig="True" --ttbar="True" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=TT_tree_bfinally.root
xrdcp TT_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

