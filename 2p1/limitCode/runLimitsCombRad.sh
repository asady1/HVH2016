#!/bin/bash
for i in 1200 1400 1600 1700 1800 1900 2000 2200 2350 2500 2750 3000 
do
	echo "mass point $i"
	mkdir Limits/sig$i
	combineCards.py outputs/datacards/HH4b2p1_Rad_mX_$i\_Rad_rej_dEta0_b_13TeV.txt outputs/datacards/HH4b2p1_Rad_mX_$i\_Rad_rej_dEta1_b_13TeV.txt > outputs/datacards/HH4b2p1_mX_$i\_2p1_Rad_13TeV.txt
	combineCards.py outputs/datacards/HH4b2p1_mX_$i\_2p1_Rad_13TeV.txt outputs/datacards/HH_mX_$i\_bump_13TeV.txt > outputs/datacards/HH4b2p1_mX_$i\_test_13TeV.txt
	combine /uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/outputs/datacards/HH4b2p1_mX_$i\_test_13TeV.txt -m $i -M Asymptotic > CMS_HH4b2p1_$i\_13TeV_asymptoticCLs.out
	mv higgsCombineTest.Asymptotic.mH$i\.root Limits/CMS_$i\_HH4b2p1_13TeV_asymptoticCLs.root
done

for i in 750 800 1000
do
	echo "mass point $i"#
	mkdir Limits/sig$i
	combineCards.py outputs/datacards/HH4b2p1_Rad_mX_$i\_Rad_rej_dEta0_b_13TeV.txt outputs/datacards/HH4b2p1_Rad_mX_$i\_Rad_rej_dEta1_b_13TeV.txt > outputs/datacards/HH4b2p1_mX_$i\_2p1_Rad_13TeV.txt
	combineCards.py outputs/datacards/HH4b2p1_mX_$i\_2p1_Rad_13TeV.txt outputs/datacards/HH_mX_$i\_Alphabet_13TeV.txt > outputs/datacards/HH4b2p1_mX_$i\_test_13TeV.txt
	combine /uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/outputs/datacards/HH4b2p1_mX_$i\_test_13TeV.txt -m $i -M Asymptotic > CMS_HH4b2p1_$i\_13TeV_asymptoticCLs.out
	mv higgsCombineTest.Asymptotic.mH$i\.root Limits/CMS_$i\_HH4b2p1_13TeV_asymptoticCLs.root
done
