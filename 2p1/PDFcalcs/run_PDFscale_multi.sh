#!/bin/sh     

./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../pdfScaleUncert.py .
cp ../../NR1.txt .
cp ../../NR2.txt .
cp ../../NR3.txt .
cp ../../NR4.txt .
cp ../../NR5.txt .
cp ../../NR6.txt . 
cp ../../NR7.txt .
cp ../../NR8.txt .
cp ../../NR10.txt .
cp ../../NR11.txt .
cp ../../NR12.txt .
cp ../../NRSM.txt .

python pdfScaleUncert.py --outName="NR1_totScale.txt" --mass=1 --list=NR1.txt --num=10
xrdcp NR1_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NR2_totScale.txt" --mass=2 --list=NR2.txt --num=3
xrdcp NR2_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NR3_totScale.txt" --mass=3 --list=NR3.txt --num=9
xrdcp NR3_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NR4_totScale.txt" --mass=4 --list=NR4.txt --num=10
xrdcp NR4_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NR5_totScale.txt" --mass=5 --list=NR5.txt --num=10
xrdcp NR5_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NR6_totScale.txt" --mass=6 --list=NR6.txt --num=10
xrdcp NR6_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NR7_totScale.txt" --mass=7 --list=NR7.txt --num=10
xrdcp NR7_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NR8_totScale.txt" --mass=8 --list=NR8.txt --num=2
xrdcp NR8_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NR9_totScale.txt" --mass=9 --list=NR9.txt --num=10
xrdcp NR9_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NR10_totScale.txt" --mass=10 --list=NR10.txt --num=10
xrdcp NR10_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NR11_totScale.txt" --mass=11 --list=NR11.txt --num=10
xrdcp NR11_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NR12_totScale.txt" --mass=12 --list=NR12.txt --num=10
xrdcp NR12_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfScaleUncert.py --outName="NRSM_totScale.txt" --mass=100 --list=NRSM.txt --num=10
xrdcp NRSM_totScale.txt root://cmseos.fnal.gov//store/user/asady1/V25/
