#!/bin/bash
for i in 750 800 900 1000 3000 3500 4500
#for i in 750 800 1000 1200 1400 1600 1800 2000 2500 3000 4000 4500
do

	combineCards.py SR1=outputs/datacards/HH_mX_$i\_HH_LL_Data_Radion_13TeV.txt SR2=outputs/datacards/HH_mX_$i\_HH_TT_Data_Radion_13TeV.txt > outputs/datacards/HH_mX_$i\_Alphabet_13TeV.txt

	echo "mass point $i"
	mkdir Limits_Combined_Alpha_Radion_Moriond_Data/sigH$i
	combine outputs/datacards/HH_mX_$i\_Alphabet_13TeV.txt -m $i -M Asymptotic &> CMS_HH_$i\_13TeV_asymptoticCLs.out
#	combine outputs/datacards/HH_mX_$i\_Alphabet_13TeV.txt -m $i -M Asymptotic --rMax 20 --rMin 0.01 &> CMS_HH_$i\_13TeV_asymptoticCLs.out
	mv higgsCombineTest.Asymptotic.mH120.root Limits_Combined_Alpha_Radion_Moriond_Data/CMS_$i\_HH_13TeV_asymptoticCLs.root

done
