making miniTrees: miniTreeProducer.py, ex for running: python getMiniTrees.py --pathIn=root://cmseos.fnal.gov//store/user/lpchbb/HeppyNtuples/V25/GluGluToBulkGravitonToHHTo4B_M-500_narrow_13TeV-madgraph/VHBB_HEPPY_V25_GluGluToBulkGravitonToHHTo4B_M-500_narrow_13TeV-madgraph__RunIISummer16MAv2-PUMoriond17_80r2as_2016_TrancheIV_v6-v1/170220_145926/0000/ --outName=BG500 --isMC=True --saveTrig=True --min=0 --max=1 --xsec=1 --file=BG500.txt
  
making slimTrees: slimTreeMaker_final.py, ex for running: python  slimTreeMaker_finalBG.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/BG500_0.root --saveTrig="True" --ttbar="False" --data="False" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False"  --outName=BG_500_tree_final.root 
NB: needs to be run 5 times, once for nominal, once for JERUp/Down and JECUp/Down each

slimTreesScripts directory has all .py and .sh files needed to run full slimTree production, as well as the add on .py script that runs on slimTrees to produce altered slimTrees (faster but only possible if information is being changed in trees, but not added), and also condor scripts (NB - condor ID must be changed to your condor ID)

calculating trigger efficiency: trigHistoMaker.py, triggerEfficiency.py, and triggerSF.C
1) trigHistoMaker.py makes histograms for QCD and data for calculating trigger efficiency from slimTrees, ex for running: python trigHistoMaker.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_300_tree_final.root --outName=QCD_300_trig.root
2) triggerEfficiency.py takes all QCD files and hadded data file run in step 1 and makes efficiency plots and calculates SFs, ex for running: python triggerEfficiency.py
3) triggerSF.C makes trigger SF plots, ex for running: root -l triggerSF.C

drawing dataMC and shape plots: variableHistos.py and variablePlots.py
1) variableHistos.py makes variable histos with cuts on them from slimTrees, ex for running: python variableHistos.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_300_tree_final.root --outName=QCD_300_shape.root
2) variablePlots.py takes these histograms and makes them into plots for a given set of QCD, ttbar, background and/or data histograms, ex for running: python variablePlots.py

making cutflow: cutflowHistos.py and cutflowTable.py
1) cutflowHistos.py makes cutflow histos cut by cut, ex for running: python cutflowHistos.py root://cmsxrootd.fnal.gov//store/user/asady1/V25/QCD_300_tree_final.root --outName=QCD_300_cut.root
2) cutflowTable.py takes the output of cutflowHistos.py and makes a cutflow table in Latex format, ex for running: python cutflowTable.py

background estimate + limits: three sets of code for three different signal categories (bulk graviton, radion, non resonant) - 2p1Alphabet_X.py, runLimits_X.sh, brazilianFlag13TeV_X.py
1) 2p1Alphabet_X.py: to produce background estimate and data cards, run for different deltaEta regions, run for different selections (no rejection, rejecting boosted events, rejecting boosted and resolved events), run for signal region vs control region, ex for running: python 2p1Alphabet_X.py --Selection="dijet_mass < 70 && ak4btag1 > 0.6324 && ak4btag2 > 0.6324 && LL < 1 && TT < 1 && LT < 1 && resolved < 1 && fatjetptau21 < 0.55 && invmAK4 > 200 && bjet2PT > 30 && fatjetPT > 300 && deltaEta >= 1.0 && deltaEta < 2.0 && Red_mass > 700" --BG_both_ 
2) runLimits_X.sh runs combine, combining different deltaEta regions and calculating limits, ex for running: sh runLimits_X.sh
3) brazilianFlag13TeV_X.py makes limit plot and prints out limits, ex for running: python brazilianFlag13TeV_X.py

reweighing non resonant samples to make new miniTrees from current hadded miniTree of nodes 2-13 + box + SM, with per event weight: nonResonant_test_v0.py, used in conjunction with the following package: https://github.com/cms-hh/HHStatAnalysis, run inside the following directory HHStatAnalysis/AnalyticalModels/test/, ex for running:  python nonResonant_test_v0.py --kl 1 --kt 1 (SM) other parameter values for the 12 BSM samples are:

klJHEP=[1.0,  7.5,  1.0,  1.0,  -3.5, 1.0, 2.4, 5.0, 15.0, 1.0, 10.0, 2.4, 15.0]

ktJHEP=[1.0,  1.0,  1.0,  1.0,  1.5,  1.0, 1.0, 1.0, 1.0,  1.0, 1.5,  1.0, 1.0]

c2JHEP=[0.0,  -1.0, 0.5, -1.5, -3.0,  0.0, 0.0, 0.0, 0.0,  1.0, -1.0, 0.0, 1.0]

cgJHEP=[0.0,  0.0, -0.8,  0.0, 0.0,   0.8, 0.2, 0.2, -1.0, -0.6, 0.0, 1.0, 0.0]

c2gJHEP=[0.0, 0.0, 0.6, -0.8, 0.0, -1.0, -0.2,-0.2,  1.0,  0.6, 0.0, -1.0, 0.0]