Procedure
  
  To run the alphabet method for HH you need to run two different alphabet
  scripts, HHSRAlphabet_puppi_LL.py and HHSRAlphabet_puppi_TT.py, for the
  two different bbtag categories. The commands to run these script are:
  
  python HHSRAlphabet_puppi_LL.py --Selection 
  "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135
  & jet2bbtag > 0.3 & (!( jet1bbtag > 0.8 & jet2bbtag > 0.8))" --Cut 0.3 
  --name HH_LL --log True
  
  python HHSRAlphabet_puppi_TT.py --Selection
  "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135
  & jet2bbtag > 0.8" --Cut 0.8 --name HH_TT --log True


*AABH procedure* :

This is for LL category only (orthogonal to TT): 

 1) Get Alphabet output and datacards using QCD : 

   python HHSRAlphabet_puppi_LL_fit.py --Selection
  "jet2_puppi_msoftdrop_raw_TheaCorr > 105 & jet2_puppi_msoftdrop_raw_TheaCorr < 135
  & jet2bbtag > 0.3 & (!( jet1bbtag > 0.8 & jet2bbtag > 0.8))" --Cut 0.3
  --name HH_LL --log True --qcd 

 2) Create Background and Obs WS from output of 1)

   root -l -b Background.c 

 3) Create Signal WS :

   bash runSignal.sh 

 4) Run limits:

   bash runLimits_bump.sh

This is for TT category only: 

 1) Get Alphabet output and datacards using QCD : 

   python HHSRAlphabet_puppi_TT_fit.py --Selection
  "jet2_puppi_msoftdrop_raw_TheaCorr > 105 & jet2_puppi_msoftdrop_raw_TheaCorr < 135
  & jet2bbtag > 0.8" --Cut 0.8
  --name HH_TT --log True --qcd 

 2) Create Background and Obs WS from output of 1)

   root -l -b Background_TT.c 

 3) Create Signal WS :

   bash runSignal_TT.sh 

 4) Run limits:

   bash runLimits_bump_TT.sh


TO COMBINE THE CATEGORIES:

bash runLimits_bump_BothCategories.sh
