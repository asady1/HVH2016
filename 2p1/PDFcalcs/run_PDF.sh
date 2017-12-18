#!/bin/sh     

./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../pdfUncert1.py .

#python pdfUncert.py "/eos/uscms/store/user/lpchbb/HeppyNtuples/V25/GluGluToBulkGravitonToHHTo4B_M-800_narrow_13TeV-madgraph.root" --outName="BG800PDF.txt" --mass=800
#xrdcp BG800PDF.txt root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node1_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node1_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_031958/0000/tree_1.root" --outName="NRv1_1_1PDF.root" --mass=1
xrdcp NRv1_1_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node1_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node1_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_031958/0000/tree_2.root" --outName="NRv1_1_2PDF.root" --mass=1
xrdcp NRv1_1_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node1_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node1_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_031958/0000/tree_3.root" --outName="NRv1_1_3PDF.root" --mass=1
xrdcp NRv1_1_3PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node1_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node1_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_031958/0000/tree_4.root" --outName="NRv1_1_4PDF.root" --mass=1
xrdcp NRv1_1_4PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node1_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node1_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_031958/0000/tree_5.root" --outName="NRv1_1_5PDF.root" --mass=1
xrdcp NRv1_1_5PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node1_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node1_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_031958/0000/tree_6.root" --outName="NRv1_1_6PDF.root" --mass=1
xrdcp NRv1_1_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node1_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node1_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_031958/0000/tree_7.root" --outName="NRv1_1_7PDF.root" --mass=1
xrdcp NRv1_1_7PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node1_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node1_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_031958/0000/tree_8.root" --outName="NRv1_1_8PDF.root" --mass=1
xrdcp NRv1_1_8PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node1_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node1_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_031958/0000/tree_9.root" --outName="NRv1_1_9PDF.root" --mass=1
xrdcp NRv1_1_9PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node1_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node1_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_031958/0000/tree_10.root" --outName="NRv1_1_10PDF.root" --mass=1
xrdcp NRv1_1_10PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node2_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node2_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032107/0000/tree_1.root" --outName="NRv1_2_1PDF.root" --mass=2
xrdcp NRv1_2_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node2_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node2_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032107/0000/tree_2.root" --outName="NRv1_2_2PDF.root" --mass=2
xrdcp NRv1_2_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node2_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node2_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032107/0000/tree_6.root" --outName="NRv1_2_6PDF.root" --mass=2
xrdcp NRv1_2_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node3_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node3_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032213/0000/tree_1.root" --outName="NRv1_3_1PDF.root" --mass=3
xrdcp NRv1_3_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node3_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node3_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032213/0000/tree_2.root" --outName="NRv1_3_2PDF.root" --mass=3
xrdcp NRv1_3_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node3_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node3_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032213/0000/tree_3.root" --outName="NRv1_3_3PDF.root" --mass=3
xrdcp NRv1_3_3PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node3_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node3_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032213/0000/tree_4.root" --outName="NRv1_3_4PDF.root" --mass=3
xrdcp NRv1_3_4PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node3_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node3_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032213/0000/tree_5.root" --outName="NRv1_3_5PDF.root" --mass=3
xrdcp NRv1_3_5PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node3_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node3_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032213/0000/tree_6.root" --outName="NRv1_3_6PDF.root" --mass=3
xrdcp NRv1_3_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node3_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node3_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032213/0000/tree_7.root" --outName="NRv1_3_7PDF.root" --mass=3
xrdcp NRv1_3_7PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node3_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node3_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032213/0000/tree_8.root" --outName="NRv1_3_8PDF.root" --mass=3
xrdcp NRv1_3_8PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node3_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node3_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032213/0000/tree_9.root" --outName="NRv1_3_9PDF.root" --mass=3 
xrdcp NRv1_3_9PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node4_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node4_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032321/0000/tree_1.root" --outName="NRv1_4_1PDF.root" --mass=4 
xrdcp NRv1_4_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/
 
python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node4_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node4_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032321/0000/tree_2.root" --outName="NRv1_4_2PDF.root" --mass=4 
xrdcp NRv1_4_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node4_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node4_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032321/0000/tree_3.root" --outName="NRv1_4_3PDF.root" --mass=4 
xrdcp NRv1_4_3PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node4_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node4_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032321/0000/tree_4.root" --outName="NRv1_4_4PDF.root" --mass=4 
xrdcp NRv1_4_4PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node4_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node4_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032321/0000/tree_5.root" --outName="NRv1_4_5PDF.root" --mass=4 
xrdcp NRv1_4_5PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node4_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node4_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032321/0000/tree_6.root" --outName="NRv1_4_6PDF.root" --mass=4 
xrdcp NRv1_4_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node4_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node4_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032321/0000/tree_7.root" --outName="NRv1_4_7PDF.root" --mass=4 
xrdcp NRv1_4_7PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node4_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node4_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032321/0000/tree_8.root" --outName="NRv1_4_8PDF.root" --mass=4 
xrdcp NRv1_4_8PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node4_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node4_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032321/0000/tree_9.root" --outName="NRv1_4_9PDF.root" --mass=4 
xrdcp NRv1_4_9PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node4_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node4_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032321/0000/tree_10.root" --outName="NRv1_4_10PDF.root" --mass=4 
xrdcp NRv1_4_10PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node5_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node5_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032427/0000/tree_1.root" --outName="NRv1_5_1PDF.root" --mass=5
xrdcp NRv1_5_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node5_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node5_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032427/0000/tree_2.root" --outName="NRv1_5_2PDF.root" --mass=5
xrdcp NRv1_5_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node5_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node5_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032427/0000/tree_3.root" --outName="NRv1_5_3PDF.root" --mass=5
xrdcp NRv1_5_3PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node5_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node5_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032427/0000/tree_4.root" --outName="NRv1_5_4PDF.root" --mass=5
xrdcp NRv1_5_4PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node5_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node5_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032427/0000/tree_5.root" --outName="NRv1_5_5PDF.root" --mass=5
xrdcp NRv1_5_5PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node5_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node5_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032427/0000/tree_6.root" --outName="NRv1_5_6PDF.root" --mass=5
xrdcp NRv1_5_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node5_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node5_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032427/0000/tree_7.root" --outName="NRv1_5_7PDF.root" --mass=5
xrdcp NRv1_5_7PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node5_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node5_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032427/0000/tree_8.root" --outName="NRv1_5_8PDF.root" --mass=5
xrdcp NRv1_5_8PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node5_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node5_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032427/0000/tree_9.root" --outName="NRv1_5_9PDF.root" --mass=5
xrdcp NRv1_5_9PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node5_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node5_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032427/0000/tree_10.root" --outName="NRv1_5_10PDF.root" --mass=5
xrdcp NRv1_5_10PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node6_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node6_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032533/0000/tree_1.root" --outName="NRv1_6_1PDF.root" --mass=6
xrdcp NRv1_6_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node6_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node6_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032533/0000/tree_2.root" --outName="NRv1_6_2PDF.root" --mass=6
xrdcp NRv1_6_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node6_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node6_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032533/0000/tree_3.root" --outName="NRv1_6_3PDF.root" --mass=6
xrdcp NRv1_6_3PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node6_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node6_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032533/0000/tree_4.root" --outName="NRv1_6_4PDF.root" --mass=6
xrdcp NRv1_6_4PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node6_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node6_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032533/0000/tree_5.root" --outName="NRv1_6_5PDF.root" --mass=6
xrdcp NRv1_6_5PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node6_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node6_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032533/0000/tree_6.root" --outName="NRv1_6_6PDF.root" --mass=6
xrdcp NRv1_6_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node6_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node6_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032533/0000/tree_7.root" --outName="NRv1_6_7PDF.root" --mass=6
xrdcp NRv1_6_7PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node6_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node6_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032533/0000/tree_8.root" --outName="NRv1_6_8PDF.root" --mass=6
xrdcp NRv1_6_8PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node6_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node6_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032533/0000/tree_9.root" --outName="NRv1_6_9PDF.root" --mass=6
xrdcp NRv1_6_9PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node6_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node6_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032533/0000/tree_10.root" --outName="NRv1_6_10PDF.root" --mass=6
xrdcp NRv1_6_10PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node7_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node7_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032642/0000/tree_1.root" --outName="NRv1_7_1PDF.root" --mass=7
xrdcp NRv1_7_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node7_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node7_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032642/0000/tree_2.root" --outName="NRv1_7_2PDF.root" --mass=7
xrdcp NRv1_7_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node7_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node7_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032642/0000/tree_3.root" --outName="NRv1_7_3PDF.root" --mass=7
xrdcp NRv1_7_3PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node7_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node7_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032642/0000/tree_4.root" --outName="NRv1_7_4PDF.root" --mass=7
xrdcp NRv1_7_4PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node7_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node7_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032642/0000/tree_5.root" --outName="NRv1_7_5PDF.root" --mass=7
xrdcp NRv1_7_5PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node7_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node7_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032642/0000/tree_6.root" --outName="NRv1_7_6PDF.root" --mass=7
xrdcp NRv1_7_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node7_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node7_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032642/0000/tree_7.root" --outName="NRv1_7_7PDF.root" --mass=7
xrdcp NRv1_7_7PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node7_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node7_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032642/0000/tree_8.root" --outName="NRv1_7_8PDF.root" --mass=7
xrdcp NRv1_7_8PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node7_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node7_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032642/0000/tree_9.root" --outName="NRv1_7_9PDF.root" --mass=7
xrdcp NRv1_7_9PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node7_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node7_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032642/0000/tree_10.root" --outName="NRv1_7_10PDF.root" --mass=7
xrdcp NRv1_7_10PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node8_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node8_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032750/0000/tree_1.root" --outName="NRv1_8_1PDF.root" --mass=8 
xrdcp NRv1_8_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node8_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node8_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032750/0000/tree_2.root" --outName="NRv1_8_2PDF.root" --mass=8 
xrdcp NRv1_8_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node9_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node9_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032857/0000/tree_1.root" --outName="NRv1_9_1PDF.root" --mass=9
xrdcp NRv1_9_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node9_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node9_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032857/0000/tree_2.root" --outName="NRv1_9_2PDF.root" --mass=9
xrdcp NRv1_9_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node9_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node9_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032857/0000/tree_3.root" --outName="NRv1_9_3PDF.root" --mass=9
xrdcp NRv1_9_3PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node9_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node9_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032857/0000/tree_4.root" --outName="NRv1_9_4PDF.root" --mass=9
xrdcp NRv1_9_4PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node9_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node9_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032857/0000/tree_5.root" --outName="NRv1_9_5PDF.root" --mass=9
xrdcp NRv1_9_5PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node9_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node9_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032857/0000/tree_6.root" --outName="NRv1_9_6PDF.root" --mass=9
xrdcp NRv1_9_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node9_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node9_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032857/0000/tree_7.root" --outName="NRv1_9_7PDF.root" --mass=9
xrdcp NRv1_9_7PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node9_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node9_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032857/0000/tree_8.root" --outName="NRv1_9_8PDF.root" --mass=9
xrdcp NRv1_9_8PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node9_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node9_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032857/0000/tree_9.root" --outName="NRv1_9_9PDF.root" --mass=9
xrdcp NRv1_9_9PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node9_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node9_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_032857/0000/tree_10.root" --outName="NRv1_9_10PDF.root" --mass=9
xrdcp NRv1_9_10PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node10_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node10_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033031/0000/tree_1.root" --outName="NRv1_10_1PDF.root" --mass=10
xrdcp NRv1_10_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node10_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node10_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033031/0000/tree_2.root" --outName="NRv1_10_2PDF.root" --mass=10
xrdcp NRv1_10_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node10_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node10_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033031/0000/tree_3.root" --outName="NRv1_10_3PDF.root" --mass=10
xrdcp NRv1_10_3PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node10_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node10_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033031/0000/tree_4.root" --outName="NRv1_10_4PDF.root" --mass=10
xrdcp NRv1_10_4PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node10_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node10_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033031/0000/tree_5.root" --outName="NRv1_10_5PDF.root" --mass=10
xrdcp NRv1_10_5PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node10_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node10_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033031/0000/tree_6.root" --outName="NRv1_10_6PDF.root" --mass=10
xrdcp NRv1_10_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node10_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node10_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033031/0000/tree_7.root" --outName="NRv1_10_7PDF.root" --mass=10
xrdcp NRv1_10_7PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node10_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node10_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033031/0000/tree_8.root" --outName="NRv1_10_8PDF.root" --mass=10
xrdcp NRv1_10_8PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node10_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node10_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033031/0000/tree_9.root" --outName="NRv1_10_9PDF.root" --mass=10
xrdcp NRv1_10_9PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node10_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node10_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033031/0000/tree_10.root" --outName="NRv1_10_10PDF.root" --mass=10
xrdcp NRv1_10_10PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node11_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node11_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033138/0000/tree_1.root"  --outName="NRv1_11_1PDF.root" --mass=11
xrdcp NRv1_11_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node11_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node11_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033138/0000/tree_2.root"  --outName="NRv1_11_2PDF.root" --mass=11
xrdcp NRv1_11_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node11_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node11_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033138/0000/tree_3.root"  --outName="NRv1_11_3PDF.root" --mass=11
xrdcp NRv1_11_3PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node11_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node11_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033138/0000/tree_4.root"  --outName="NRv1_11_4PDF.root" --mass=11
xrdcp NRv1_11_4PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node11_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node11_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033138/0000/tree_5.root"  --outName="NRv1_11_5PDF.root" --mass=11
xrdcp NRv1_11_5PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node11_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node11_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033138/0000/tree_6.root"  --outName="NRv1_11_6PDF.root" --mass=11
xrdcp NRv1_11_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node11_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node11_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033138/0000/tree_7.root"  --outName="NRv1_11_7PDF.root" --mass=11
xrdcp NRv1_11_7PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node11_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node11_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033138/0000/tree_8.root"  --outName="NRv1_11_8PDF.root" --mass=11
xrdcp NRv1_11_8PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node11_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node11_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033138/0000/tree_9.root"  --outName="NRv1_11_9PDF.root" --mass=11
xrdcp NRv1_11_9PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node11_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node11_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033138/0000/tree_10.root"  --outName="NRv1_11_10PDF.root" --mass=11
xrdcp NRv1_11_10PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node12_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node12_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033245/0000/tree_1.root" --outName="NRv1_12_1PDF.root" --mass=12
xrdcp NRv1_12_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node12_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node12_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033245/0000/tree_2.root" --outName="NRv1_12_2PDF.root" --mass=12
xrdcp NRv1_12_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node12_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node12_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033245/0000/tree_3.root" --outName="NRv1_12_3PDF.root" --mass=12
xrdcp NRv1_12_3PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node12_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node12_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033245/0000/tree_4.root" --outName="NRv1_12_4PDF.root" --mass=12
xrdcp NRv1_12_4PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node12_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node12_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033245/0000/tree_5.root" --outName="NRv1_12_5PDF.root" --mass=12
xrdcp NRv1_12_5PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node12_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node12_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033245/0000/tree_6.root" --outName="NRv1_12_6PDF.root" --mass=12
xrdcp NRv1_12_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node12_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node12_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033245/0000/tree_7.root" --outName="NRv1_12_7PDF.root" --mass=12
xrdcp NRv1_12_7PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node12_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node12_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033245/0000/tree_8.root" --outName="NRv1_12_8PDF.root" --mass=12
xrdcp NRv1_12_8PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node12_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node12_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033245/0000/tree_9.root" --outName="NRv1_12_9PDF.root" --mass=12
xrdcp NRv1_12_9PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GF_HHTo4B_node12_13TeV-madgraph-pythia8/VHBB_HEPPY_V25c_GF_HHTo4B_node12_13TeV-madgraph-Py8__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v3/171026_033245/0000/tree_10.root" --outName="NRv1_12_10PDF.root" --mass=12
xrdcp NRv1_12_10PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GluGluToHHTo4B_node_SM_13TeV-madgraph/VHBB_HEPPY_V25c_GluGluToHHTo4B_node_SM_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170523_043254/0000/tree_1.root" --outName="NRv1_100_1PDF.root" --mass=100
xrdcp NRv1_100_1PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GluGluToHHTo4B_node_SM_13TeV-madgraph/VHBB_HEPPY_V25c_GluGluToHHTo4B_node_SM_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170523_043254/0000/tree_2.root" --outName="NRv1_100_2PDF.root" --mass=100
xrdcp NRv1_100_2PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GluGluToHHTo4B_node_SM_13TeV-madgraph/VHBB_HEPPY_V25c_GluGluToHHTo4B_node_SM_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170523_043254/0000/tree_3.root" --outName="NRv1_100_3PDF.root" --mass=100
xrdcp NRv1_100_3PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GluGluToHHTo4B_node_SM_13TeV-madgraph/VHBB_HEPPY_V25c_GluGluToHHTo4B_node_SM_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170523_043254/0000/tree_4.root" --outName="NRv1_100_4PDF.root" --mass=100
xrdcp NRv1_100_4PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GluGluToHHTo4B_node_SM_13TeV-madgraph/VHBB_HEPPY_V25c_GluGluToHHTo4B_node_SM_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170523_043254/0000/tree_5.root" --outName="NRv1_100_5PDF.root" --mass=100
xrdcp NRv1_100_5PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GluGluToHHTo4B_node_SM_13TeV-madgraph/VHBB_HEPPY_V25c_GluGluToHHTo4B_node_SM_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170523_043254/0000/tree_6.root" --outName="NRv1_100_6PDF.root" --mass=100
xrdcp NRv1_100_6PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GluGluToHHTo4B_node_SM_13TeV-madgraph/VHBB_HEPPY_V25c_GluGluToHHTo4B_node_SM_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170523_043254/0000/tree_7.root" --outName="NRv1_100_7PDF.root" --mass=100
xrdcp NRv1_100_7PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GluGluToHHTo4B_node_SM_13TeV-madgraph/VHBB_HEPPY_V25c_GluGluToHHTo4B_node_SM_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170523_043254/0000/tree_8.root" --outName="NRv1_100_8PDF.root" --mass=100
xrdcp NRv1_100_8PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GluGluToHHTo4B_node_SM_13TeV-madgraph/VHBB_HEPPY_V25c_GluGluToHHTo4B_node_SM_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170523_043254/0000/tree_9.root" --outName="NRv1_100_9PDF.root" --mass=100
xrdcp NRv1_100_9PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/

python pdfUncert1.py "root://cmsxrootd.fnal.gov//store/user/cvernier/VHBBHeppyV25/GluGluToHHTo4B_node_SM_13TeV-madgraph/VHBB_HEPPY_V25c_GluGluToHHTo4B_node_SM_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170523_043254/0000/tree_10.root" --outName="NRv1_100_10PDF.root" --mass=100 
xrdcp NRv1_100_10PDF.root root://cmseos.fnal.gov//store/user/asady1/V25/