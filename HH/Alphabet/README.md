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

  1) There is one script, HHSRAlphabet_fit_ReReco.py, to produce the datacards 
     and Alphabet output using QCD. The command for the LL category is:

       python HHSRAlphabet_fit_ReReco.py --Selection 
       "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135 
       & jet2bbtag > 0.3 & (!( jet1bbtag > 0.8 & jet2bbtag > 0.8))" --Cut 0.3
       --name HH_LL_QCD --log True --qcd

    The command for the TT category is:

      python HHSRAlphabet_fit_ReReco.py --Selection 
      "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135 
       & jet2bbtag > 0.8" --Cut 0.8 --name HH_TT_QCD --log True --TT --qcd

This is for LL category only (orthogonal to TT): 

 2) Create Background and Obs WS from output of 1)

   root -l -b Background.c 

 3) Create Signal WS :

   bash runSignal.sh 

 4) Run limits:

   bash runLimits_bump.sh

This is for TT category only: 

 2) Create Background and Obs WS from output of 1)

   root -l -b Background_TT.c 

 3) Create Signal WS :

   bash runSignal_TT.sh 

 4) Run limits:

   bash runLimits_bump_TT.sh


TO COMBINE THE CATEGORIES:

bash runLimits_bump_BothCategories.sh
