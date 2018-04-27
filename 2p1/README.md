making miniTrees: miniTreeProducer.py, ex for running: python getMiniTrees.py --pathIn=root://cmseos.fnal.gov//store/user/lpchbb/HeppyNtuples/V25/GluGluToBulkGravitonToHHTo4B_M-500_narrow_13TeV-madgraph/VHBB_HEPPY_V25_GluGluToBulkGravitonToHHTo4B_M-500_narrow_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170220_145926/0000/ --outName=BG500 --isMC=True --saveTrig=True --min=0 --max=1 --xsec=1 --file=BG500.txt
-----------------------------------  
making slimTrees: slimTreeMaker_final.py, ex for running: python  slimTreeMaker_finalBG.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG500_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_500_tree_final.root 
NB: needs to be run 5 times, once for nominal, once for JERUp/Down and JECUp/Down each
-----------------------------------
slimTreesScripts directory has all .py and .sh files needed to run full slimTree production, as well as the add on .py script that runs on slimTrees to produce altered slimTrees (faster but only possible if information is being changed in trees, but not added), and also condor scripts (NB - condor ID must be changed to your condor ID) - extra files needed to run can be found here: https://drive.google.com/drive/folders/1aifwYPkXgqJwzNclGZFa578nRDrh2O74?usp=sharing
-----------------------------------
finalAlphabet directory has scripts needed to make datacards (final.py is for bulk graviton, finalRad.py is for radion, NRSM.py is for non-resonant) - run as follows:

1) category 1: python -i 2p1Alphabet_NRSM.py --Selection="dijet_mass < 140 && dijet_mass > 90 && ak4btag1 > 0.6324 && ak4btag2 > 0.6324 && fatjetptau21 < 0.55 && invmAK4 > 200 && bjet2PT > 30 && fatjetPT > 300 && deltaEta < 1.0 && Red_mass > 750"

2) category 2: python -i 2p1Alphabet_NRSM.py --Selection="dijet_mass < 140 && dijet_mass > 90 && ak4btag1 > 0.6324 && ak4btag2 > 0.6324 && fatjetptau21 < 0.55 && invmAK4 > 200 && bjet2PT > 30 && fatjetPT > 300 && deltaEta < 2.0 && deltaEta >= 1.0 && Red_mass > 750"

3) add in Selection for rejecting boosted events: "!(boosted > 0 && b2 > 0.3)", add in Selection for rejecting resolved resonant events: "resolved < 1", add in Selection for rejecting resolved non-resonant events: "nAK4 < 1", add in command line for legend header (only on NRSM): --leghead="#Delta#eta 0-1"
-----------------------------------
limit calculations are in limitCode (.sh files for running combine, .py files for making brazilian flag plots)
-----------------------------------
datacards in directory, "retain" means 2p1 by itself, "boost" means rejecting boosted events, "boostres" means rejecting boosted and resolved events, NB the Radion retain files have a misnomer of "BG" in the title but this is just a typo 
-----------------------------------
calculating trigger efficiency: trigHistoMaker.py, triggerEfficiency.py, and triggerSF.C
1) trigHistoMaker.py makes histograms for QCD and data for calculating trigger efficiency from slimTrees, ex for running: python trigHistoMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_300_tree_final.root --outName=QCD_300_trig.root
2) triggerEfficiency.py takes all QCD files and hadded data file run in step 1 and makes efficiency plots and calculates SFs, ex for running: python triggerEfficiency.py
3) triggerSF.C makes trigger SF plots, ex for running: root -l triggerSF.C
-----------------------------------
drawing dataMC and shape plots: variableHistos.py and variablePlots.py
1) variableHistos.py makes variable histos with cuts on them from slimTrees, ex for running: python variableHistos.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_300_tree_final.root --outName=QCD_300_shape.root
2) variablePlots.py takes these histograms and makes them into plots for a given set of QCD, ttbar, background and/or data histograms, ex for running: python variablePlots.py
-----------------------------------
making cutflow: cutflowHistos.py and cutflowTable.py
1) cutflowHistos.py makes cutflow histos cut by cut, ex for running: python cutflowHistos.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_300_tree_final.root --outName=QCD_300_cut.root
2) cutflowTable.py takes the output of cutflowHistos.py and makes a cutflow table in Latex format, ex for running: python cutflowTable.py

