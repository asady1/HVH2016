#!/bin/bash
for i in 1200 1600 2000 2200 2500 2750 3000
do
	echo "mass point $i"
	mkdir Limits/sig$i
	combineCards.py outputs/datacards/HH4b2p1_BG_mX_$i\_BG_PA_boostres_dEta0_13TeV.txt outputs/datacards/HH4b2p1_BG_mX_$i\_BG_PA_boostres_dEta1_13TeV.txt > outputs/datacards/HH4b2p1_mX_$i\_2p1_BG_13TeV.txt
	combineCards.py outputs/datacards/HH4b2p1_mX_$i\_2p1_BG_13TeV.txt outputs/datacards/HH_mX_$i\_bump_13TeV.txt > outputs/datacards/HH4b2p1_mX_$i\_test_13TeV.txt
	combine /uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/outputs/datacards/HH4b2p1_mX_$i\_test_13TeV.txt  -m $i -M Asymptotic > CMS_HH4b2p1_$i\_13TeV_asymptoticCLs.out
	mv higgsCombineTest.Asymptotic.mH$i\.root Limits/CMS_$i\_HH4b2p1_13TeV_asymptoticCLs.root
done

for i in 750 800 900 1000
do
	echo "mass point $i"
	mkdir Limits/sig$i
	combineCards.py outputs/datacards/HH4b2p1_BG_mX_$i\_BG_PA_boostres_dEta0_13TeV.txt outputs/datacards/HH4b2p1_BG_mX_$i\_BG_PA_boostres_dEta1_13TeV.txt > outputs/datacards/HH4b2p1_mX_$i\_2p1_BG_13TeV.txt
	combineCards.py outputs/datacards/HH4b2p1_mX_$i\_2p1_BG_13TeV.txt outputs/datacards/HH_mX_$i\_Alphabet_13TeV.txt > outputs/datacards/HH4b2p1_mX_$i\_test_13TeV.txt
	combine /uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/outputs/datacards/HH4b2p1_mX_$i\_test_13TeV.txt  -m $i -M Asymptotic > CMS_HH4b2p1_$i\_13TeV_asymptoticCLs.out
	mv higgsCombineTest.Asymptotic.mH$i\.root Limits/CMS_$i\_HH4b2p1_13TeV_asymptoticCLs.root
done

#  LocalWords:  BackgroundEstimate
