#!/bin/bash
for i in 1200 1400 1600 1800 2000 2500 
do
	combineCards.py SR=outputs/datacards/HH_mX_$i\_HH_TT_13TeV.txt AT=outputs/datacards/HH_mX_$i\_HH_TT_13TeV_fail.txt > outputs/datacards/HH_mX_$i\_bump_13TeV.txt
	echo "mass point $i"
	mkdir Limits_TT/sig$i
	text2workspace.py outputs/datacards/HH_mX_$i\_bump_13TeV.txt  -o outputs/datacards/HH_mX_$i\_bump_13TeV.root
	combine outputs/datacards/HH_mX_$i\_bump_13TeV.txt --noFitAsimov -m $i -M Asymptotic &> CMS_HH4b_$i\_13TeV_asymptoticCLs.out
	mv higgsCombineTest.Asymptotic.mH$i\.root Limits_TT/CMS_$i\_HH4b_13TeV_asymptoticCLs.root
#	combine -M MaxLikelihoodFit --rMin=-100 --rMax=100 --saveNormalizations --plot --saveShapes --saveWithUncertainties  -v 4 outputs/datacards/HH_mX_$i\_bump_13TeV.txt --out outputs/datacards
done
