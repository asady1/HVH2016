#!/bin/sh     

./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../pdfUncert.py .
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

python pdfUncert.py --outName="NR1_tot.txt" --mass=1 --list=NR1.txt --num=10
xrdcp NR1_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NR2_tot.txt" --mass=2 --list=NR2.txt --num=3
xrdcp NR2_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NR3_tot.txt" --mass=3 --list=NR3.txt --num=9
xrdcp NR3_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NR4_tot.txt" --mass=4 --list=NR4.txt --num=10
xrdcp NR4_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NR5_tot.txt" --mass=5 --list=NR5.txt --num=10
xrdcp NR5_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NR6_tot.txt" --mass=6 --list=NR6.txt --num=10
xrdcp NR6_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NR7_tot.txt" --mass=7 --list=NR7.txt --num=10
xrdcp NR7_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NR8_tot.txt" --mass=8 --list=NR8.txt --num=2
xrdcp NR8_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NR9_tot.txt" --mass=9 --list=NR9.txt --num=10
xrdcp NR9_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NR10_tot.txt" --mass=10 --list=NR10.txt --num=10
xrdcp NR10_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NR11_tot.txt" --mass=11 --list=NR11.txt --num=10
xrdcp NR11_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NR12_tot.txt" --mass=12 --list=NR12.txt --num=10
xrdcp NR12_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert.py --outName="NRSM_tot.txt" --mass=100 --list=NRSM.txt --num=10
xrdcp NRSM_tot.txt root://cmseos.fnal.gov//store/user/asady1/V25/
