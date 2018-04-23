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

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node10_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node10_tree_bfinally.root
xrdcp NRv1_node10_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node11_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node11_tree_bfinally.root
xrdcp NRv1_node11_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node12_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node12_tree_bfinally.root
xrdcp NRv1_node12_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node1_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node1_tree_bfinally.root
xrdcp NRv1_node1_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node2_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node2_tree_bfinally.root
xrdcp NRv1_node2_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node3_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node3_tree_bfinally.root
xrdcp NRv1_node3_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node4_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node4_tree_bfinally.root
xrdcp NRv1_node4_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node5_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node5_tree_bfinally.root
xrdcp NRv1_node5_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node6_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node6_tree_bfinally.root
xrdcp NRv1_node6_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node7_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node7_tree_bfinally.root
xrdcp NRv1_node7_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node8_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node8_tree_bfinally.root
xrdcp NRv1_node8_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node9_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node9_tree_bfinally.root
xrdcp NRv1_node9_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/


##JECUp
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node10_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node10_tree_bfinally_JECUp.root
xrdcp NRv1_node10_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node11_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node11_tree_bfinally_JECUp.root
xrdcp NRv1_node11_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node12_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node12_tree_bfinally_JECUp.root
xrdcp NRv1_node12_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node1_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node1_tree_bfinally_JECUp.root
xrdcp NRv1_node1_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node2_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node2_tree_bfinally_JECUp.root
xrdcp NRv1_node2_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node3_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node3_tree_bfinally_JECUp.root
xrdcp NRv1_node3_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node4_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node4_tree_bfinally_JECUp.root
xrdcp NRv1_node4_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node5_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node5_tree_bfinally_JECUp.root
xrdcp NRv1_node5_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node6_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node6_tree_bfinally_JECUp.root
xrdcp NRv1_node6_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node7_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node7_tree_bfinally_JECUp.root
xrdcp NRv1_node7_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node8_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node8_tree_bfinally_JECUp.root
xrdcp NRv1_node8_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node9_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node9_tree_bfinally_JECUp.root
xrdcp NRv1_node9_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

##JECDown
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node10_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node10_tree_bfinally_JECDown.root
xrdcp NRv1_node10_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node11_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node11_tree_bfinally_JECDown.root
xrdcp NRv1_node11_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node12_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node12_tree_bfinally_JECDown.root
xrdcp NRv1_node12_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node1_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node1_tree_bfinally_JECDown.root
xrdcp NRv1_node1_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node2_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node2_tree_bfinally_JECDown.root
xrdcp NRv1_node2_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node3_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node3_tree_bfinally_JECDown.root
xrdcp NRv1_node3_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node4_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node4_tree_bfinally_JECDown.root
xrdcp NRv1_node4_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node5_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node5_tree_bfinally_JECDown.root
xrdcp NRv1_node5_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node6_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node6_tree_bfinally_JECDown.root
xrdcp NRv1_node6_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node7_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node7_tree_bfinally_JECDown.root
xrdcp NRv1_node7_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node8_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node8_tree_bfinally_JECDown.root
xrdcp NRv1_node8_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node9_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NRv1_node9_tree_bfinally_JECDown.root
xrdcp NRv1_node9_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

##JERUp
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node10_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node10_tree_bfinally_JERUp.root
xrdcp NRv1_node10_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node11_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node11_tree_bfinally_JERUp.root
xrdcp NRv1_node11_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node12_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node12_tree_bfinally_JERUp.root
xrdcp NRv1_node12_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node1_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node1_tree_bfinally_JERUp.root
xrdcp NRv1_node1_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node2_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node2_tree_bfinally_JERUp.root
xrdcp NRv1_node2_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node3_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node3_tree_bfinally_JERUp.root
xrdcp NRv1_node3_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node4_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node4_tree_bfinally_JERUp.root
xrdcp NRv1_node4_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node5_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node5_tree_bfinally_JERUp.root
xrdcp NRv1_node5_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node6_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node6_tree_bfinally_JERUp.root
xrdcp NRv1_node6_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node7_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node7_tree_bfinally_JERUp.root
xrdcp NRv1_node7_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node8_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node8_tree_bfinally_JERUp.root
xrdcp NRv1_node8_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node9_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False" --useReg="False"  --outName=NRv1_node9_tree_bfinally_JERUp.root
xrdcp NRv1_node9_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

##JERDown
python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node10_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node10_tree_bfinally_JERDown.root
xrdcp NRv1_node10_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node11_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node11_tree_bfinally_JERDown.root
xrdcp NRv1_node11_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node12_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node12_tree_bfinally_JERDown.root
xrdcp NRv1_node12_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node1_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node1_tree_bfinally_JERDown.root
xrdcp NRv1_node1_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node2_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node2_tree_bfinally_JERDown.root
xrdcp NRv1_node2_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node3_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node3_tree_bfinally_JERDown.root
xrdcp NRv1_node3_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node4_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node4_tree_bfinally_JERDown.root
xrdcp NRv1_node4_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node5_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node5_tree_bfinally_JERDown.root
xrdcp NRv1_node5_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node6_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node6_tree_bfinally_JERDown.root
xrdcp NRv1_node6_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node7_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node7_tree_bfinally_JERDown.root
xrdcp NRv1_node7_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node8_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node8_tree_bfinally_JERDown.root
xrdcp NRv1_node8_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/NR/NR_node9_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True" --useReg="False"  --outName=NRv1_node9_tree_bfinally_JERDown.root
xrdcp NRv1_node9_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodeSM_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NR_nodeSM_tree_bfinally.root
xrdcp NR_nodeSM_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodebox_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False"  --outName=NR_nodebox_tree_bfinally.root
xrdcp NR_nodebox_tree_bfinally.root root://cmseos.fnal.gov//store/user/asady1/V25/


python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodeSM_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False"  --outName=NR_nodeSM_tree_bfinally_JECDown.root
xrdcp NR_nodeSM_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/


python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodebox_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="True" --JERUp="False" --JERDown="False"  --outName=NR_nodebox_tree_bfinally_JECDown.root
xrdcp NR_nodebox_tree_bfinally_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodeSM_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=NR_nodeSM_tree_final_JECUp.root
xrdcp NR_nodeSM_tree_final_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodebox_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="True" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=NR_nodebox_tree_bfinally_JECUp.root
xrdcp NR_nodebox_tree_bfinally_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/


python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodeSM_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False"  --outName=NR_nodeSM_tree_bfinally_JERUp.root
xrdcp NR_nodeSM_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodebox_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="True" --JERDown="False"  --outName=NR_nodebox_tree_bfinally_JERUp.root
xrdcp NR_nodebox_tree_bfinally_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodeSM_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True"  --outName=NR_nodeSM_tree_bfinally_JERDown.root
xrdcp NR_nodeSM_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodebox_0.root  --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="True"  --outName=NR_nodebox_tree_bfinally_JERDown.root
xrdcp NR_nodebox_tree_bfinally_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
