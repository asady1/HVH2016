#!/bin/bash
for i in 1200 1400 1600 1800 2000 2500 3000
do
	echo "mass point $i"
	mkdir Limits/sig$i
	text2workspace.py outputs/bump/datacards/HH_mX_$i\_13TeV.txt  -o outputs/bump/datacards/HH_mX_$i\_13TeV.root
	combine outputs/bump/datacards/HH_mX_$i\_13TeV.txt --noFitAsimov -m $i -M Asymptotic &> CMS_HH4b_$i\_13TeV_asymptoticCLs.out
	mv higgsCombineTest.Asymptotic.mH$i\.root Limits/CMS_$i\_HH4b_13TeV_asymptoticCLs.root
done
