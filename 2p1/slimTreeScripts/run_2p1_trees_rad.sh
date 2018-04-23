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

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1000_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=Rad_1000_tree_bfinally.root
xrdcp Rad_1000_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1000_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=Rad_1000_tree_bfinally_JECUp.root
xrdcp Rad_1000_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1000_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False"  --outName=Rad_1000_tree_bfinally_JECDown.root
xrdcp Rad_1000_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1000_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False"  --outName=Rad_1000_tree_bfinally_JERUp.root
xrdcp Rad_1000_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1000_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True"  --outName=Rad_1000_tree_bfinally_JERDown.root
xrdcp Rad_1000_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1200_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=Rad_1200_tree_bfinally.root
xrdcp Rad_1200_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1200_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=Rad_1200_tree_bfinally_JECUp.root
xrdcp Rad_1200_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1200_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False"  --outName=Rad_1200_tree_bfinally_JECDown.root
xrdcp Rad_1200_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1200_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False"  --outName=Rad_1200_tree_bfinally_JERUp.root
xrdcp Rad_1200_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1200_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True"  --outName=Rad_1200_tree_bfinally_JERDown.root
xrdcp Rad_1200_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1400_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=Rad_1400_tree_bfinally.root
xrdcp Rad_1400_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1400_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=Rad_1400_tree_bfinally_JECUp.root
xrdcp Rad_1400_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1400_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False"  --outName=Rad_1400_tree_bfinally_JECDown.root
xrdcp Rad_1400_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1400_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False"  --outName=Rad_1400_tree_bfinally_JERUp.root
xrdcp Rad_1400_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1400_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True"  --outName=Rad_1400_tree_bfinally_JERDown.root
xrdcp Rad_1400_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1600_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=Rad_1600_tree_bfinally.root
xrdcp Rad_1600_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1600_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=Rad_1600_tree_bfinally_JECUp.root
xrdcp Rad_1600_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1600_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False"  --outName=Rad_1600_tree_bfinally_JECDown.root
xrdcp Rad_1600_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1600_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False"  --outName=Rad_1600_tree_bfinally_JERUp.root
xrdcp Rad_1600_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad1600_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True"  --outName=Rad_1600_tree_bfinally_JERDown.root
xrdcp Rad_1600_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad600_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=Rad_600_tree_bfinally.root
xrdcp Rad_600_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad600_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=Rad_600_tree_bfinally_JECUp.root
xrdcp Rad_600_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad600_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False"  --outName=Rad_600_tree_bfinally_JECDown.root
xrdcp Rad_600_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad600_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False"  --outName=Rad_600_tree_bfinally_JERUp.root
xrdcp Rad_600_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad600_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True"  --outName=Rad_600_tree_bfinally_JERDown.root
xrdcp Rad_600_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad650_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=Rad_650_tree_bfinally.root
xrdcp Rad_650_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad650_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=Rad_650_tree_bfinally_JECUp.root
xrdcp Rad_650_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad650_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False"  --outName=Rad_650_tree_bfinally_JECDown.root
xrdcp Rad_650_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad650_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False"  --outName=Rad_650_tree_bfinally_JERUp.root
xrdcp Rad_650_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad650_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True"  --outName=Rad_650_tree_bfinally_JERDown.root
xrdcp Rad_650_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad750_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=Rad_750_tree_bfinally.root
xrdcp Rad_750_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad750_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=Rad_750_tree_bfinally_JECUp.root
xrdcp Rad_750_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad750_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False"  --outName=Rad_750_tree_bfinally_JECDown.root
xrdcp Rad_750_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad750_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False"  --outName=Rad_750_tree_bfinally_JERUp.root
xrdcp Rad_750_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad750_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True"  --outName=Rad_750_tree_bfinally_JERDown.root
xrdcp Rad_750_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad800_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=Rad_800_tree_bfinally.root
xrdcp Rad_800_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad800_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=Rad_800_tree_bfinally_JECUp.root
xrdcp Rad_800_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad800_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False"  --outName=Rad_800_tree_bfinally_JECDown.root
xrdcp Rad_800_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad800_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False"  --outName=Rad_800_tree_bfinally_JERUp.root
xrdcp Rad_800_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad800_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True"  --outName=Rad_800_tree_bfinally_JERDown.root
xrdcp Rad_800_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
