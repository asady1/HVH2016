#!/bin/bash
for i in 1 2 3 4 5 6 7 8 9 10 11 12 100
do
	echo "mass point $i"
	mkdir Limits/sig$i
	combineCards.py outputs/datacards/HH4b_semiBoosted_mX_$i\_NRv1_unB1_boost_dEta1_13TeV.txt outputs/datacards/HH4b_semiBoosted_mX_$i\_NRv1_unB1_boost_dEta2_13TeV.txt > outputs/datacards/HH4b_semiBoosted_mX_$i\_combined_13TeV.txt
	combineCards.py HH4b_semiBoosted_mX_$i\_combined_13TeV.txt HH_mX_$i\_Alphabet_13TeV.txt > HH4b2p1_NR_mX_$i\_comb_13TeV.txt
	combine /uscms_data/d3/asady1/HHcode/CMSSW_8_0_12/src/HH2016/BackgroundEstimate/outputs/datacards/HH4b2p1_NR_mX_$i\_comb_13TeV.txt   -m $i -M Asymptotic > CMS_HH4b2p1_NR_$i\_13TeV_asymptoticCLs.out
	mv higgsCombineTest.Asymptotic.mH$i\.root Limits/CMS_$i\_HH4b2p1_NR_13TeV_asymptoticCLs.root
done
