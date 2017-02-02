#!/bin/bash
#for i in 1200 
for i in 1200 1400 1600 1800 2000 2500 3000 
do
	combineCards.py SR1=outputs/datacards/HH_mX_$i\_HH_LL_QCD_13TeV.txt SR2=outputs/datacards/HH_mX_$i\_HH_TT_QCD_13TeV.txt AT1=outputs/datacards/HH_mX_$i\_HH_LL_QCD_13TeV_fail.txt AT2=outputs/datacards/HH_mX_$i\_HH_TT_QCD_13TeV_fail.txt > outputs/datacards/HH_mX_$i\_bump_13TeV.txt
	echo "mass point $i"
	mkdir Limits_QCD_Combined_Summer16/sig$i
	text2workspace.py outputs/datacards/HH_mX_$i\_bump_13TeV.txt  -o outputs/datacards/HH_mX_$i\_bump_13TeV.root
#        combine -M MaxLikelihoodFit --rMin=-50 --rMax=50 --saveNormalizations --plot --saveShapes --saveWithUncertainties  -v 4 outputs/datacards/HH_mX_$i\_bump_13TeV.txt
	combine outputs/datacards/HH_mX_$i\_bump_13TeV.txt --noFitAsimov -m $i -M Asymptotic &> CMS_HH4b_$i\_13TeV_asymptoticCLs.out
	mv higgsCombineTest.Asymptotic.mH$i\.root Limits_QCD_Combined_Summer16/CMS_$i\_HH4b_13TeV_asymptoticCLs.root
#	combine -M MaxLikelihoodFit --rMin=-100 --rMax=100 --saveNormalizations --plot --saveShapes --saveWithUncertainties  -v 4 outputs/datacards/HH_mX_$i\_bump_13TeV.txt --out outputs/datacards
done
