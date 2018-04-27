#!/bin/bash
for i in 750 800 900 1000 1200 1600 2000
do
	echo "mass point $i"
	mkdir Limits/sig$i
	combineCards.py outputs/datacards/HH4b2p1_dEta1p5_mX_$i\_BG_none_dEta0_13TeV.txt outputs/datacards/HH4b2p1_dEta1p5_mX_$i\_BG_none_dEta1_13TeV.txt > outputs/datacards/HH4b2p1_mX_$i\_test_13TeV.txt
	combine /uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/outputs/datacards/HH4b2p1_mX_$i\_test_13TeV.txt  -m $i -M Asymptotic > CMS_HH4b2p1_$i\_13TeV_asymptoticCLs.out
	mv higgsCombineTest.Asymptotic.mH$i\.root Limits/CMS_$i\_HH4b2p1_13TeV_asymptoticCLs.root
done
