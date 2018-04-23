#!/bin/sh

#testing

./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../addon.py .
cp ../../DeepCSV_Moriond17_B_H.csv .

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node10_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node10_tree_bfinallyb.root
xrdcp NRv1_node10_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node11_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node11_tree_bfinallyb.root
xrdcp NRv1_node11_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node12_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node12_tree_bfinallyb.root
xrdcp NRv1_node12_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node2_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node2_tree_bfinallyb.root
xrdcp NRv1_node2_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node3_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node3_tree_bfinallyb.root
xrdcp NRv1_node3_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node4_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node4_tree_bfinallyb.root
xrdcp NRv1_node4_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node5_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node5_tree_bfinallyb.root
xrdcp NRv1_node5_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node6_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node6_tree_bfinallyb.root
xrdcp NRv1_node6_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node7_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node7_tree_bfinallyb.root
xrdcp NRv1_node7_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node8_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node8_tree_bfinallyb.root
xrdcp NRv1_node8_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node9_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node9_tree_bfinallyb.root
xrdcp NRv1_node9_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodeSM_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node100_tree_bfinallyb.root
xrdcp NRv1_node100_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node1_tree_bfinally.root  --ttbar="False" --data="False" --outName=NRv1_node1_tree_bfinallyb.root
xrdcp NRv1_node1_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node10_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node10_tree_bfinallyb_JERDown.root
xrdcp NRv1_node10_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node11_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node11_tree_bfinallyb_JERDown.root
xrdcp NRv1_node11_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node12_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node12_tree_bfinallyb_JERDown.root
xrdcp NRv1_node12_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node2_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node2_tree_bfinallyb_JERDown.root
xrdcp NRv1_node2_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node3_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node3_tree_bfinallyb_JERDown.root
xrdcp NRv1_node3_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node4_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node4_tree_bfinallyb_JERDown.root
xrdcp NRv1_node4_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node5_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node5_tree_bfinallyb_JERDown.root
xrdcp NRv1_node5_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node6_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node6_tree_bfinallyb_JERDown.root
xrdcp NRv1_node6_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node7_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node7_tree_bfinallyb_JERDown.root
xrdcp NRv1_node7_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node8_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node8_tree_bfinallyb_JERDown.root
xrdcp NRv1_node8_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node9_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node9_tree_bfinallyb_JERDown.root
xrdcp NRv1_node9_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodeSM_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node100_tree_bfinallyb_JERDown.root
xrdcp NRv1_node100_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node1_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=NRv1_node1_tree_bfinallyb_JERDown.root
xrdcp NRv1_node1_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node10_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node10_tree_bfinallyb_JERUp.root
xrdcp NRv1_node10_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node11_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node11_tree_bfinallyb_JERUp.root
xrdcp NRv1_node11_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node12_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node12_tree_bfinallyb_JERUp.root
xrdcp NRv1_node12_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node2_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node2_tree_bfinallyb_JERUp.root
xrdcp NRv1_node2_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node3_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node3_tree_bfinallyb_JERUp.root
xrdcp NRv1_node3_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node4_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node4_tree_bfinallyb_JERUp.root
xrdcp NRv1_node4_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node5_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node5_tree_bfinallyb_JERUp.root
xrdcp NRv1_node5_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node6_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node6_tree_bfinallyb_JERUp.root
xrdcp NRv1_node6_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node7_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node7_tree_bfinallyb_JERUp.root
xrdcp NRv1_node7_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node8_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node8_tree_bfinallyb_JERUp.root
xrdcp NRv1_node8_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node9_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node9_tree_bfinallyb_JERUp.root
xrdcp NRv1_node9_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodeSM_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node100_tree_bfinallyb_JERUp.root
xrdcp NRv1_node100_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node1_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=NRv1_node1_tree_bfinallyb_JERUp.root
xrdcp NRv1_node1_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node10_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node10_tree_bfinallyb_JECDown.root
xrdcp NRv1_node10_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node11_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node11_tree_bfinallyb_JECDown.root
xrdcp NRv1_node11_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node12_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node12_tree_bfinallyb_JECDown.root
xrdcp NRv1_node12_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node2_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node2_tree_bfinallyb_JECDown.root
xrdcp NRv1_node2_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node3_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node3_tree_bfinallyb_JECDown.root
xrdcp NRv1_node3_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node4_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node4_tree_bfinallyb_JECDown.root
xrdcp NRv1_node4_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node5_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node5_tree_bfinallyb_JECDown.root
xrdcp NRv1_node5_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node6_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node6_tree_bfinallyb_JECDown.root
xrdcp NRv1_node6_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node7_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node7_tree_bfinallyb_JECDown.root
xrdcp NRv1_node7_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node8_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node8_tree_bfinallyb_JECDown.root
xrdcp NRv1_node8_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node9_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node9_tree_bfinallyb_JECDown.root
xrdcp NRv1_node9_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodeSM_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node100_tree_bfinallyb_JECDown.root
xrdcp NRv1_node100_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node1_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=NRv1_node1_tree_bfinallyb_JECDown.root
xrdcp NRv1_node1_tree_bfinallyb_JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node10_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node10_tree_bfinallyb_JECUp.root
xrdcp NRv1_node10_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node11_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node11_tree_bfinallyb_JECUp.root
xrdcp NRv1_node11_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node12_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node12_tree_bfinallyb_JECUp.root
xrdcp NRv1_node12_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node2_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node2_tree_bfinallyb_JECUp.root
xrdcp NRv1_node2_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node3_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node3_tree_bfinallyb_JECUp.root
xrdcp NRv1_node3_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node4_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node4_tree_bfinallyb_JECUp.root
xrdcp NRv1_node4_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node5_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node5_tree_bfinallyb_JECUp.root
xrdcp NRv1_node5_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node6_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node6_tree_bfinallyb_JECUp.root
xrdcp NRv1_node6_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node7_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node7_tree_bfinallyb_JECUp.root
xrdcp NRv1_node7_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node8_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node8_tree_bfinallyb_JECUp.root
xrdcp NRv1_node8_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node9_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node9_tree_bfinallyb_JECUp.root
xrdcp NRv1_node9_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NR_nodeSM_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node100_tree_bfinallyb_JECUp.root
xrdcp NRv1_node100_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/NRv1_node1_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=NRv1_node1_tree_bfinallyb_JECUp.root
xrdcp NRv1_node1_tree_bfinallyb_JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
 
python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1000_tree_bfinally.root  --ttbar="False" --data="False" --outName=BG_1000_tree_bfinallyb.root
xrdcp BG_1000_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1200_tree_bfinally.root --ttbar="False" --data="False" --outName=BG_1200_tree_bfinallyb.root
xrdcp BG_1200_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1600_tree_bfinally.root --ttbar="False" --data="False" --outName=BG_1600_tree_bfinallyb.root
xrdcp BG_1600_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_2000_tree_bfinally.root --ttbar="False" --data="False" --outName=BG_2000_tree_bfinallyb.root
xrdcp BG_2000_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_500_tree_bfinally.root --ttbar="False" --data="False" --outName=BG_500_tree_bfinallyb.root
xrdcp BG_500_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_550_tree_bfinally.root --ttbar="False" --data="False" --outName=BG_550_tree_bfinallyb.root
xrdcp BG_550_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_600_tree_bfinally.root --ttbar="False" --data="False" --outName=BG_600_tree_bfinallyb.root
xrdcp BG_600_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_650_tree_bfinally.root --ttbar="False" --data="False" --outName=BG_650_tree_bfinallyb.root
xrdcp BG_650_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_750_tree_bfinally.root --ttbar="False" --data="False" --outName=BG_750_tree_bfinallyb.root
xrdcp BG_750_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_800_tree_bfinally.root --ttbar="False" --data="False" --outName=BG_800_tree_bfinallyb.root
xrdcp BG_800_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_900_tree_bfinally.root --ttbar="False" --data="False" --outName=BG_900_tree_bfinallyb.root
xrdcp BG_900_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/
 
#python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinally.root --ttbar="True" --data="False" --outName=TT_tree_bfinallyb.root
#xrdcp TT_tree_bfinallyb.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1000_tree_bfinally_JERUp.root  --ttbar="False" --data="False" --outName=BG_1000_tree_bfinallyb_JERUp.root
xrdcp BG_1000_tree_bfinallyb_JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1200_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=BG_1200_tree_bfinallyb__JERUp.root
xrdcp BG_1200_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1600_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=BG_1600_tree_bfinallyb__JERUp.root
xrdcp BG_1600_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_2000_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=BG_2000_tree_bfinallyb__JERUp.root
xrdcp BG_2000_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_500_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=BG_500_tree_bfinallyb__JERUp.root
xrdcp BG_500_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_550_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=BG_550_tree_bfinallyb__JERUp.root
xrdcp BG_550_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_600_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=BG_600_tree_bfinallyb__JERUp.root
xrdcp BG_600_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_650_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=BG_650_tree_bfinallyb__JERUp.root
xrdcp BG_650_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_750_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=BG_750_tree_bfinallyb__JERUp.root
xrdcp BG_750_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_800_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=BG_800_tree_bfinallyb__JERUp.root
xrdcp BG_800_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_900_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=BG_900_tree_bfinallyb__JERUp.root
xrdcp BG_900_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
 
#python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinally_JERUp.root --ttbar="True" --data="False" --outName=TT_tree_bfinallyb__JERUp.root
#xrdcp TT_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1000_tree_bfinally_JECDown.root  --ttbar="False" --data="False" --outName=BG_1000_tree_bfinallyb__JECDown.root
xrdcp BG_1000_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1200_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=BG_1200_tree_bfinallyb__JECDown.root
xrdcp BG_1200_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1600_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=BG_1600_tree_bfinallyb__JECDown.root
xrdcp BG_1600_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_2000_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=BG_2000_tree_bfinallyb__JECDown.root
xrdcp BG_2000_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_500_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=BG_500_tree_bfinallyb__JECDown.root
xrdcp BG_500_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_550_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=BG_550_tree_bfinallyb__JECDown.root
xrdcp BG_550_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_600_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=BG_600_tree_bfinallyb__JECDown.root
xrdcp BG_600_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_650_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=BG_650_tree_bfinallyb__JECDown.root
xrdcp BG_650_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_750_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=BG_750_tree_bfinallyb__JECDown.root
xrdcp BG_750_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_800_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=BG_800_tree_bfinallyb__JECDown.root
xrdcp BG_800_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_900_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=BG_900_tree_bfinallyb__JECDown.root
xrdcp BG_900_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
 
#python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinally_JECDown.root --ttbar="True" --data="False" --outName=TT_tree_bfinallyb__JECDown.root
#xrdcp TT_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1000_tree_bfinally_JECUp.root  --ttbar="False" --data="False" --outName=BG_1000_tree_bfinallyb__JECUp.root
xrdcp BG_1000_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1200_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=BG_1200_tree_bfinallyb__JECUp.root
xrdcp BG_1200_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1600_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=BG_1600_tree_bfinallyb__JECUp.root
xrdcp BG_1600_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_2000_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=BG_2000_tree_bfinallyb__JECUp.root
xrdcp BG_2000_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_500_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=BG_500_tree_bfinallyb__JECUp.root
xrdcp BG_500_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_550_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=BG_550_tree_bfinallyb__JECUp.root
xrdcp BG_550_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_600_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=BG_600_tree_bfinallyb__JECUp.root
xrdcp BG_600_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_650_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=BG_650_tree_bfinallyb__JECUp.root
xrdcp BG_650_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_750_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=BG_750_tree_bfinallyb__JECUp.root
xrdcp BG_750_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_800_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=BG_800_tree_bfinallyb__JECUp.root
xrdcp BG_800_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_900_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=BG_900_tree_bfinallyb__JECUp.root
xrdcp BG_900_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/
 
#python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinally_JECUp.root --ttbar="True" --data="False" --outName=TT_tree_bfinallyb__JECUp.root
#xrdcp TT_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1000_tree_bfinally_JERDown.root  --ttbar="False" --data="False" --outName=BG_1000_tree_bfinallyb__JERDown.root
xrdcp BG_1000_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1200_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=BG_1200_tree_bfinallyb__JERDown.root
xrdcp BG_1200_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_1600_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=BG_1600_tree_bfinallyb__JERDown.root
xrdcp BG_1600_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_2000_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=BG_2000_tree_bfinallyb__JERDown.root
xrdcp BG_2000_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_500_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=BG_500_tree_bfinallyb__JERDown.root
xrdcp BG_500_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_550_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=BG_550_tree_bfinallyb__JERDown.root
xrdcp BG_550_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_600_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=BG_600_tree_bfinallyb__JERDown.root
xrdcp BG_600_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_650_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=BG_650_tree_bfinallyb__JERDown.root
xrdcp BG_650_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_750_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=BG_750_tree_bfinallyb__JERDown.root
xrdcp BG_750_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_800_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=BG_800_tree_bfinallyb__JERDown.root
xrdcp BG_800_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python  addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG_900_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=BG_900_tree_bfinallyb__JERDown.root
xrdcp BG_900_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/
 
#python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/TT_tree_bfinally_JERDown.root --ttbar="True" --data="False" --outName=TT_tree_bfinallyb__JERDown.root
#xrdcp TT_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_600_tree_finally.root --ttbar="False" --data="False" --outName=Rad_600_tree_bfinallyb_.root
xrdcp Rad_600_tree_bfinallyb_.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_650_tree_finally.root --ttbar="False" --data="False" --outName=Rad_650_tree_bfinallyb_.root
xrdcp Rad_650_tree_bfinallyb_.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_750_tree_finally.root --ttbar="False" --data="False" --outName=Rad_750_tree_bfinallyb_.root
xrdcp Rad_750_tree_bfinallyb_.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_800_tree_finally.root --ttbar="False" --data="False" --outName=Rad_800_tree_bfinallyb_.root
xrdcp Rad_800_tree_bfinallyb_.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1000_tree_finally.root --ttbar="False" --data="False" --outName=Rad_1000_tree_bfinallyb_.root
xrdcp Rad_1000_tree_bfinallyb_.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1200_tree_finally.root --ttbar="False" --data="False" --outName=Rad_1200_tree_bfinallyb_.root
xrdcp Rad_1200_tree_bfinallyb_.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1400_tree_finally.root --ttbar="False" --data="False" --outName=Rad_1400_tree_bfinallyb_.root
xrdcp Rad_1400_tree_bfinallyb_.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1600_tree_finally.root --ttbar="False" --data="False" --outName=Rad_1600_tree_bfinallyb_.root
xrdcp Rad_1600_tree_bfinallyb_.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_600_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=Rad_600_tree_bfinallyb__JERUp.root
xrdcp Rad_600_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_650_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=Rad_650_tree_bfinallyb__JERUp.root
xrdcp Rad_650_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_750_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=Rad_750_tree_bfinallyb__JERUp.root
xrdcp Rad_750_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_800_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=Rad_800_tree_bfinallyb__JERUp.root
xrdcp Rad_800_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1000_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=Rad_1000_tree_bfinallyb__JERUp.root
xrdcp Rad_1000_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1200_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=Rad_1200_tree_bfinallyb__JERUp.root
xrdcp Rad_1200_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1400_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=Rad_1400_tree_bfinallyb__JERUp.root
xrdcp Rad_1400_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1600_tree_bfinally_JERUp.root --ttbar="False" --data="False" --outName=Rad_1600_tree_bfinallyb__JERUp.root
xrdcp Rad_1600_tree_bfinallyb__JERUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_600_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=Rad_600_tree_bfinallyb__JECDown.root
xrdcp Rad_600_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_650_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=Rad_650_tree_bfinallyb__JECDown.root
xrdcp Rad_650_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_750_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=Rad_750_tree_bfinallyb__JECDown.root
xrdcp Rad_750_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_800_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=Rad_800_tree_bfinallyb__JECDown.root
xrdcp Rad_800_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1000_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=Rad_1000_tree_bfinallyb__JECDown.root
xrdcp Rad_1000_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1200_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=Rad_1200_tree_bfinallyb__JECDown.root
xrdcp Rad_1200_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1400_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=Rad_1400_tree_bfinallyb__JECDown.root
xrdcp Rad_1400_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1600_tree_bfinally_JECDown.root --ttbar="False" --data="False" --outName=Rad_1600_tree_bfinallyb__JECDown.root
xrdcp Rad_1600_tree_bfinallyb__JECDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_600_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=Rad_600_tree_bfinallyb__JECUp.root
xrdcp Rad_600_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_650_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=Rad_650_tree_bfinallyb__JECUp.root
xrdcp Rad_650_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_750_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=Rad_750_tree_bfinallyb__JECUp.root
xrdcp Rad_750_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_800_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=Rad_800_tree_bfinallyb__JECUp.root
xrdcp Rad_800_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1000_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=Rad_1000_tree_bfinallyb__JECUp.root
xrdcp Rad_1000_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1200_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=Rad_1200_tree_bfinallyb__JECUp.root
xrdcp Rad_1200_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1400_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=Rad_1400_tree_bfinallyb__JECUp.root
xrdcp Rad_1400_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1600_tree_bfinally_JECUp.root --ttbar="False" --data="False" --outName=Rad_1600_tree_bfinallyb__JECUp.root
xrdcp Rad_1600_tree_bfinallyb__JECUp.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_600_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=Rad_600_tree_bfinallyb__JERDown.root
xrdcp Rad_600_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_650_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=Rad_650_tree_bfinallyb__JERDown.root
xrdcp Rad_650_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_750_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=Rad_750_tree_bfinallyb__JERDown.root
xrdcp Rad_750_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_800_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=Rad_800_tree_bfinallyb__JERDown.root
xrdcp Rad_800_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1000_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=Rad_1000_tree_bfinallyb__JERDown.root
xrdcp Rad_1000_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1200_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=Rad_1200_tree_bfinallyb__JERDown.root
xrdcp Rad_1200_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1400_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=Rad_1400_tree_bfinallyb__JERDown.root
xrdcp Rad_1400_tree_bfinallyb__JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

python addon.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/Rad_1600_tree_bfinally_JERDown.root --ttbar="False" --data="False" --outName=Rad_1600_tree_bfinallyb__JERDown.root
xrdcp Rad_1600_tree_bfinallyb_JERDown.root root://cmseos.fnal.gov//store/user/asady1/V25/

