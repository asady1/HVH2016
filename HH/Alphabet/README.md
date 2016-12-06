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
