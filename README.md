This repository contains the code necessary for the boosted HH4b, semi-resloved HH4b, and HVbbjj analyses. 

generalTreeAnalyzer_80X.py is designed to run over heppy ntuples to produce miniTrees for analysis:

python generalTreeAnalyzer_80X.py --pathIn=root://cmsxrootd.fnal.gov//store/user/lpchbb/HeppyNtuples/V23/BulkGravTohhTohbbhbb_narrow_M-1800_13TeV-madgraph/VHBB_HEPPY_V23_BulkGravTohhTohbbhbb_narrow_M-1800_13TeV-madgraph__spr16MAv2-puspr16_HLT_80r2as_v14-v1/160716_234632/0000/  --outName=BG_1800_80X_2p1 --jets='True' --isMC='True' --is2p1='True' --xsec=1.0 --min=0 --max=1 --file=TxtFiles/one.txt --syst=None

Command line options include pathIn (directory of root files to be processed), outName (outname of miniTree file), min (number of first file to run over), max (number of last file to run over), file (.txt file containing list of all the names of files to run over), trigger (bool for whether to make trigger cut, currently commented out), jets (bool for whether to make jet cuts), deta (bool for whether to make delta eta cut), isMC (bool for whether it's MC), is2p1 (bool for whether it's the 2p1 analysis or not), xsec (cross section), and syst (whether its a systematic or not).

trigger_efficiency.py is designed to create a trigger efficiency plot given a file specified in the code and two histograms, one before the trigger cut and one after:

python trigger_efficiency.py

cutflowtable.py is designed to create a .tex file that provides both a number of events and a comparative cutflow given files that have histograms that have the number of events corresponding to each cut:

python cutflowtable.py

shape_plots.py is designed to create .pdf file for each histogram from several different MC and data files, so that shapes of different kinematic variables can be compared for different samples:

shape_plots.py

VH/ttreeAnalyzer_vh_alphabet.py runs over the miniTrees to produce ttrees that will be ready to be passed to Alphabet, namely identifying a V and H jet and applying the V mass cut:

python ttreeAnalyzer_vh_alphabet.py WP_600_miniTree_vh_0.root --outName=tree_WP_600_VH_alph.root

2p1/ttreeAnalyzer_2p1.py runs over the miniTrees produced with the is2p1 bool set to true to make ttrees that can be passed to the 2p1 Alphabet. This code needs to be run twice, once for SR events and once for CR events, and currently needs to be edited as this is hard-coded (to be updated to a command line option when we run the 80X miniTrees):

python ttreeAnalyzer_2p1.py BG_1800_miniTree_2p1_0.root --outName=tree_BG_1800_2p1.root
