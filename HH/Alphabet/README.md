Procedure
  
  To run the alphabet method for the BulkGrav(Radion) samples you need to run two different alphabet
  scripts, HHSRAlphabet_puppi_LL_QCD_ChingWei.py(HHSRAlphabet_puppi_LL_QCD_ChingWei_Radion.py) and
  HHSRAlphabet_puppi_TT_QCD_ChingWei.py(HHSRAlphabet_puppi_TT_QCD_ChingWei_Radion.py), for the
  two different bbtag categories. The commands to run these script are:
  
    python HHSRAlphabet_puppi_LL_QCD_ChingWei.py --Selection 
    "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135
    & jet2bbtag > 0.3 & (!( jet1bbtag > 0.8 & jet2bbtag > 0.8))" --Cut 0.3 
    --name HH_LL --log True
  
    (python HHSRAlphabet_puppi_LL_QCD_ChingWei_Radion.py --Selection 
    "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135
    & jet2bbtag > 0.3 & (!( jet1bbtag > 0.8 & jet2bbtag > 0.8))" --Cut 0.3 
    --name HH_LL_Radion --log True)
  
    python HHSRAlphabet_puppi_TT_QCD_ChingWei.py --Selection
    "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135
    & jet2bbtag > 0.8" --Cut 0.8 --name HH_TT --log True
  
    (python HHSRAlphabet_puppi_TT_QCD_ChingWei_Radion.py --Selection
    "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135
    & jet2bbtag > 0.8" --Cut 0.8 --name HH_TT_Radion --log True)

Then to combine the datacards:
    ./runLimitsHH_BothCategories.sh
    (./runLimitsHH_BothCategories_Radion.sh)


*AABH procedure* :

1)There is one script, HHSRAlphabet_fit_ReReco.py(HHSRAlphabet_fit_ReReco_Radion.py), 
  to produce the datacards and Alphabet output. The command for the LL category is:

      python HHSRAlphabet_fit_ReReco.py --Selection 
      "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135 
      & jet2bbtag > 0.3 & (!( jet1bbtag > 0.8 & jet2bbtag > 0.8))" --Cut 0.3
      --name HH_LL_Data --log True
       
      (python HHSRAlphabet_fit_ReReco_Radion.py --Selection 
      "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135 
      & jet2bbtag > 0.3 & (!( jet1bbtag > 0.8 & jet2bbtag > 0.8))" --Cut 0.8
      --name HH_LL_Data_Radion --log True)
       

The command for the TT category is:

      python HHSRAlphabet_fit_ReReco.py --Selection 
      "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135 
      & jet2bbtag > 0.8" --Cut 0.8 --name HH_TT_Data --log True --TT
       
      (python HHSRAlphabet_fit_ReReco_Radion.py --Selection 
      "jet2_puppi_msoftdrop_TheaCorr > 105 & jet2_puppi_msoftdrop_TheaCorr < 135 
      & jet2bbtag > 0.8" --Cut 0.8 --name HH_TT_Data_Radion --log True --TT)

2)There is one script, Background.c(Background_Radion.c), that creates the background and Obs WS
  from the output of 1). To run for the TT region you must change the variable
  LLregion to false inside of the script. The command to run is:
     
       root -l -b Background.c (root -l -b Background_Radion.c)
        
This is for LL category only (orthogonal to TT): 

3)Create Signal WS :

    bash runSignal_LL_Data.sh (bash runSignal_LL_Radion_Data.sh)

This is for TT category only: 

3)Create Signal WS :

    bash runSignal_TT_Data.sh (bash runSignal_TT_Radion_Data.sh)

TO COMBINE THE CATEGORIES:

    bash runLimits_bump_BothCategories.sh (bash runLimits_bump_BothCategories_Radion.sh)
   
