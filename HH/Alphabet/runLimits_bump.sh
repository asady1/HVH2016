#!/bin/bash
for i in 1200 
do
	combineCards.py Name1=outputs/datacards/HH_mX_$i\_test_13TeV_pass.txt Name2=outputs/datacards/HH_mX_$i\_test_13TeV_fail.txt > outputs/datacards/HH_mX_$i\_bump_13TeV.txt
	echo "mass point $i"
	mkdir Limits/sig$i
	text2workspace.py outputs/datacards/HH_mX_$i\_bump_13TeV.txt  -o outputs/datacards/HH_mX_$i\_bump_13TeV.root
	combine outputs/datacards/HH_mX_$i\_bump_13TeV.txt --noFitAsimov -m $i -M Asymptotic &> CMS_HH4b_$i\_13TeV_asymptoticCLs.out
	mv higgsCombineTest.Asymptotic.mH$i\.root Limits/CMS_$i\_HH4b_13TeV_asymptoticCLs.root
	combine -M MaxLikelihoodFit --rMin=-100 --rMax=100 --saveNormalizations --plot --saveShapes --saveWithUncertainties  -v 4 outputs/datacards/HH_mX_$i\_bump_13TeV.txt --out outputs/datacards
done
