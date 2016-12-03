Synopsis

    How to create miniTrees from Heppy Ntuples
    
Procedure

    For each type of Heppy Ntuples(QCD500,QCD1000,TT..) there is a set of .sh files that run over all of the Heppy files. Each 
    .sh file has a .jdl file associated to it. There is an executalbe for each type of Heppy Ntuple that will submit every 
    .jdl file to condor. For example, ./condorSubmit_TT.sh will submit all of the TT MC jobs
