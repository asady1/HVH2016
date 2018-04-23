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
 
python  slimTreeMaker_final.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/QCD500.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False"  --JERDown="False" --useReg="False" --outName=QCD_500_tree_finally27.root
xrdcp QCD_500_tree_finally27.root root://cmseos.fnal.gov//store/user/asady1/V25/

#python  slimTreeMaker_csv.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/QCD700.root --saveTrig="True" --ttbar="False" --data="False" --outName=QCD_700_tree_dcsv.root
#xrdcp QCD_700_tree_dcsv.root root://cmseos.fnal.gov//store/user/asady1/V25/

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_700_ext.root --saveTrig="False" --ttbar="False" --data="False" --outName=QCD_700_ext_tree.root
#xrdcp QCD_700_ext_tree.root root://cmseos.fnal.gov//store/user/asady1

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_1000.root --saveTrig="False" --ttbar="False" --data="False" --outName=QCD_1000_tree.root
#xrdcp QCD_1000_tree.root root://cmseos.fnal.gov//store/user/asady1

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_1500.root --saveTrig="False" --ttbar="False" --data="False" --outName=QCD_1500_tree.root
#xrdcp QCD_1500_tree.root root://cmseos.fnal.gov//store/user/asady1

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_2000.root --saveTrig="False" --ttbar="False" --data="False" --outName=QCD_2000_tree.root
#xrdcp QCD_2000_tree.root root://cmseos.fnal.gov//store/user/asady1

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/QCD_HT500to700_V23_V2_2p1.root --saveTrig="False" --outName=QCD_500_tree.root
#xrdcp QCD_500_tree.root root://cmseos.fnal.gov//store/user/asady1

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/QCD_HT700to1000_V23_V2_2p1.root --saveTrig="False" --outName=QCD_700_tree.root
#xrdcp QCD_700_tree.root root://cmseos.fnal.gov//store/user/asady1

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BTCSV_B.root  --saveTrig="True" --ttbar="False" --data="True" --outName=BTag_B_tree.root
#xrdcp BTag_B_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BTCSV_C.root  --saveTrig="True" --ttbar="False" --data="True" --outName=BTag_C_tree.root
#xrdcp BTag_C_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BTCSV_D.root  --saveTrig="True" --ttbar="False" --data="True" --outName=BTag_D_tree.root
#xrdcp BTag_D_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BTCSV_E.root  --saveTrig="True" --ttbar="False" --data="True" --outName=BTag_E_tree.root
#xrdcp BTag_E_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BTCSV_F.root  --saveTrig="True" --ttbar="False" --data="True" --outName=BTag_F_tree.root
#xrdcp BTag_F_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BTCSV_G.root  --saveTrig="True" --ttbar="False" --data="True" --outName=BTag_G_tree.root
#xrdcp BTag_G_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BTCSV_H.root  --saveTrig="True" --ttbar="False" --data="True" --outName=BTag_H_tree.root
#xrdcp BTag_H_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_B.root  --saveTrig="True" --ttbar="False" --data="True" --outName=JetHT_B_tree.root
#xrdcp JetHT_B_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_C.root  --saveTrig="True" --ttbar="False" --data="True" --outName=JetHT_C_tree.root
#xrdcp JetHT_C_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_D.root  --saveTrig="True" --ttbar="False" --data="True" --outName=JetHT_D_tree.root
#xrdcp JetHT_D_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_E.root  --saveTrig="True" --ttbar="False" --data="True" --outName=JetHT_E_tree.root
#xrdcp JetHT_E_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_F.root  --saveTrig="True" --ttbar="False" --data="True" --outName=JetHT_F_tree.root
#xrdcp JetHT_F_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/JetHT_H.root  --saveTrig="True" --ttbar="False" --data="True" --outName=JetHT_H_tree.root
#xrdcp JetHT_H_tree.root root://cmseos.fnal.gov//store/user/asady1 

#python  slimTreeMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/JetHT_V24_VR1_2p1.root --saveTrig="True" --ttbar="False" --outName=JetHT_tree.root
#xrdcp JetHT_tree.root root://cmseos.fnal.gov//store/user/asady1


