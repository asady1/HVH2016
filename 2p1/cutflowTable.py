import os
import glob
import math    

import ROOT 
#ROOT.gROOT.Macro("rootlogon.C")

import FWCore.ParameterSet.Config as cms

import sys
from DataFormats.FWLite import Events, Handle

from array import array

#function to get integral of all the histograms
def getIntegral(filename,hists):
    cthisto = filename.Get(hists[0])
    c0histo = filename.Get(hists[1])
    c1histo = filename.Get(hists[2])
    c2histo = filename.Get(hists[3])
    c3histo = filename.Get(hists[4])
    c4histo = filename.Get(hists[5])
    c5histo = filename.Get(hists[6])
    c6histo = filename.Get(hists[7])
    c7histo = filename.Get(hists[8])
    c8histo = filename.Get(hists[9])
    c9histo = filename.Get(hists[10])
    
    nevents = []
    first = cthisto.Integral()
    nevents.append(first/2.0)
    nevents.append(c0histo.Integral())
    nevents.append(c1histo.Integral()) 
    nevents.append(c2histo.Integral()) 
    nevents.append(c3histo.Integral()) 
    nevents.append(c4histo.Integral()) 
    nevents.append(c5histo.Integral()) 
    nevents.append(c6histo.Integral()) 
    nevents.append(c7histo.Integral()) 
    nevents.append(c8histo.Integral())
    nevents.append(c9histo.Integral())

    return nevents

#function to get cutflow normalized to (nevents passed * xsec * lumi)/nevents total    
def getNormCutflow(array,xsec,lumi,ntotalevents):
    normcutflow = []
    for i in range(len(array)):
        newvalue = (array[i]*xsec*lumi)/ntotalevents
        normcutflow.append(newvalue)

    return normcutflow

#function to get cutflow with comparison to previous cut
def getCompareCutflow(array):
    comparecutflow = [array[1]/array[0], array[2]/array[1], array[3]/array[2], array[4]/array[2], array[5]/array[1], array[6]/array[5],array[7]/array[5],array[8]/array[1], array[9]/array[8], array[10]/array[9]]
    
    return comparecutflow

#input files
#BG500 = ROOT.TFile("BG_500_cutflow.root")
#BG550 = ROOT.TFile("BG_550_cutflow.root")
#BG600 = ROOT.TFile("BG_600_cutflow.root")
#BG650 = ROOT.TFile("BG_650_cutflow.root")
BG750 = ROOT.TFile("BG_750_cutflow.root")
BG800 = ROOT.TFile("BG_800_cutflow.root")
BG900 = ROOT.TFile("BG_900_cutflow.root")
BG1000 = ROOT.TFile("BG_1000_cutflow.root")
BG1200 = ROOT.TFile("BG_1200_cutflow.root")
BG1600 = ROOT.TFile("BG_1600_cutflow.root")
BG2000 = ROOT.TFile("BG_2000_cutflow.root")
Rad750 = ROOT.TFile("Rad_750_cutflow.root")
Rad800 = ROOT.TFile("Rad_800_cutflow.root")
Rad1000 = ROOT.TFile("Rad_1000_cutflow.root")
Rad1200 = ROOT.TFile("Rad_1200_cutflow.root")
Rad1400 = ROOT.TFile("Rad_1400_cutflow.root")
Rad1600 = ROOT.TFile("Rad_1600_cutflow.root")
#NR2 = ROOT.TFile("NR_2_cutflow.root")
#NR3 = ROOT.TFile("NR_3_cutflow.root")
#NR4 = ROOT.TFile("NR_4_cutflow.root")
#NR5 = ROOT.TFile("NR_5_cutflow.root")
#NR6 = ROOT.TFile("NR_6_cutflow.root")
#NR7 = ROOT.TFile("NR_7_cutflow.root")
#NR8 = ROOT.TFile("NR_8_cutflow.root")
#NR9 = ROOT.TFile("NR_9_cutflow.root")
#NR10 = ROOT.TFile("NR_10_cutflow.root")
#NR11 = ROOT.TFile("NR_11_cutflow.root")
#NR12 = ROOT.TFile("NR_12_cutflow.root")
#NR13 = ROOT.TFile("NR_13_cutflow.root")
#NRSM = ROOT.TFile("NR_SM_cutflow.root")
#NRbox = ROOT.TFile("NR_box_cutflow.root")

#ZP600 = ROOT.TFile("tree_ZP_600_DDT_VH.root")
#ZP800 = ROOT.TFile("tree_ZP_800_DDT_VH.root")
#ZP1000 = ROOT.TFile("tree_ZP_1000_DDT_VH.root")
#ZP1200 = ROOT.TFile("tree_ZP_1200_DDT_VH.root")
#ZP1400 = ROOT.TFile("tree_ZP_1400_DDT_VH.root")
#ZP1600 = ROOT.TFile("tree_ZP_1600_DDT_VH.root")
#ZP1800 = ROOT.TFile("tree_ZP_1800_DDT_VH.root")
#ZP2000 = ROOT.TFile("tree_ZP_2000_DDT_VH.root")
#ZP2500 = ROOT.TFile("tree_ZP_2500_DDT_VH.root")
#ZP3000 = ROOT.TFile("tree_ZP_3000_DDT_VH.root")
#ZP3500 = ROOT.TFile("tree_ZP_3500_DDT_VH.root")
#ZP4000 = ROOT.TFile("tree_ZP_4000_DDT_VH.root")
#ZP4500 = ROOT.TFile("tree_ZP_4500_DDT_VH.root")

#ttbar = ROOT.TFile("tree_ttbar_DDT_VH.root")

#sample names
#sample1name = "BG 500"
#sample2name = "BG 550"
#sample3name = "BG 600"
#sample4name = "BG 650"
sample5name = "BG 750"
sample6name = "BG 800"
sample7name = "BG 900"
sample8name = "BG 1000"
sample9name = "BG 1200"
sample10name = "BG 1600"
sample11name = "BG 2000"
#sample12name = "NR 2"
#sample13name = "NR 3"
#sample14name = "NR 4"
#sample15name = "NR 5"
#sample16name = "NR 6"
#sample17name = "NR 7"
#sample18name = "NR 8"
#sample19name = "NR 9"
#sample20name = "NR 10"
#sample21name = "NR 11"
#sample22name = "NR 12"
#sample23name = "NR 13"
#sample24name = "NR SM"
#sample25name = "NR box"
sample12name = "Rad 750"
sample13name = "Rad 800"
sample14name = "Rad 1000"
sample15name = "Rad 1200"
sample16name = "Rad 1400"
sample17name = "Rad 1600"


#sample1name = "ZP 600"
#sample2name = "ZP 800"
#sample3name = "ZP 1000"
#sample4name = "ZP 1200"
#sample5name = "ZP 1400"
#sample6name = "ZP 1600"
#sample7name = "ZP 1800"
#sample8name = "ZP 2000"
#sample9name = "ZP 2500"
#sample10name = "ZP 3000"
#sample11name = "ZP 3500"
#sample12name = "ZP 4000"
#sample13name = "ZP 4500"

#sample14name = "ttbar"
#histograms for cutflow
histograms = ["tpo1","tpo2","tpo3","tpo4","tpo5","tpo6","tpo7","tpo8","tpo9","tpo10","tpo12"]
#initializing cutflow arrays
#myn1 = []
#myn2 = []
#myn3 = []
#myn4 = []
myn5 = []
myn6 = []
myn7 = []
myn8 = []
myn9 = []
myn10 = []
myn11 = []
myn12 = []
myn13 = []
myn14 = []
myn15 = []
myn16 = []
myn17 = []
#myn18 = []
#myn19 = []
#myn20 = []
#myn21 = []
#myn22 = []
#myn23 = []
#myn24 = []
#myn25 = []

#writing cutflow arrays
#myn1 = getIntegral(BG500,histograms)
#myn2 = getIntegral(BG550,histograms)
#myn3 = getIntegral(BG600,histograms)
#myn4 = getIntegral(BG650,histograms)
myn5 = getIntegral(BG750,histograms)
myn6 = getIntegral(BG800,histograms)
myn7 = getIntegral(BG900,histograms)
myn8 = getIntegral(BG1000,histograms)
myn9 = getIntegral(BG1200,histograms)
myn10 = getIntegral(BG1600,histograms)
myn11 = getIntegral(BG2000,histograms)
#myn12 = getIntegral(NR2,histograms)
#myn13 = getIntegral(NR3,histograms)
#myn14 = getIntegral(NR4,histograms)
#myn15 = getIntegral(NR5,histograms)
#myn16 = getIntegral(NR6,histograms)
#myn17 = getIntegral(NR7,histograms)
#myn18 = getIntegral(NR8,histograms)
#myn19 = getIntegral(NR9,histograms)
#myn20 = getIntegral(NR10,histograms)
#myn21 = getIntegral(NR11,histograms)
#myn22 = getIntegral(NR12,histograms)
#myn23 = getIntegral(NR13,histograms)
#myn24 = getIntegral(NRSM,histograms)
#myn25 = getIntegral(NRbox,histograms)
myn12 = getIntegral(Rad750,histograms)
myn13 = getIntegral(Rad800,histograms)
myn14 = getIntegral(Rad1000,histograms)
myn15 = getIntegral(Rad1200,histograms)
myn16 = getIntegral(Rad1400,histograms)
myn17 = getIntegral(Rad1600,histograms)

#myn1 = getIntegral(ZP600,histograms)
#myn2 = getIntegral(ZP800,histograms)
#myn3 = getIntegral(ZP1000,histograms)
#myn4 = getIntegral(ZP1200,histograms)
#myn5 = getIntegral(ZP1400,histograms)
#myn6 = getIntegral(ZP1600,histograms)
#myn7 = getIntegral(ZP1800,histograms)
#myn8 = getIntegral(ZP2000,histograms)
#myn9 = getIntegral(ZP2500,histograms)
#myn10 = getIntegral(ZP3000,histograms)
#myn11 = getIntegral(ZP3500,histograms)
#myn12 = getIntegral(ZP4000,histograms)
#myn13 = getIntegral(ZP4500,histograms)
#myn14 = getIntegral(ttbar,histograms)

#writing normalized cutflow arrays
#mync1 = getNormCutflow(myn1, 1, 1, 50000)
#mync2 = getNormCutflow(myn2, 1, 1, 100000)
#mync3 = getNormCutflow(myn3, 1, 1, 100000)
#mync4 = getNormCutflow(myn4, 1, 1, 49200)
mync5 = getNormCutflow(myn5, 1, 1, 50000)
mync6 = getNormCutflow(myn6, 1, 1, 100000)
mync7 = getNormCutflow(myn7, 1, 1, 50000)
mync8 = getNormCutflow(myn8, 1, 1, 49200)
mync9 = getNormCutflow(myn9, 1, 1, 50000)
mync10 = getNormCutflow(myn10, 1, 1, 50000)
mync11 = getNormCutflow(myn11, 1, 1, 50000)
#mync12 = getNormCutflow(myn12, 1, 1, 299600)
#mync13 = getNormCutflow(myn13, 1, 1, 299800)
#mync14 = getNormCutflow(myn14, 1, 1, 265200)
#mync15 = getNormCutflow(myn15, 1, 1, 258000)
#mync16 = getNormCutflow(myn16, 1, 1, 300000)
#mync17 = getNormCutflow(myn17, 1, 1, 192434)
#mync18 = getNormCutflow(myn18, 1, 1, 294000)
#mync19 = getNormCutflow(myn19, 1, 1, 263400)
#mync20 = getNormCutflow(myn20, 1, 1, 16800)
#mync21 = getNormCutflow(myn21, 1, 1, 300000)
#mync22 = getNormCutflow(myn22, 1, 1, 226200)
#mync23 = getNormCutflow(myn23, 1, 1, 300000)
#mync24 = getNormCutflow(myn24, 1, 1, 299800)
#mync25 = getNormCutflow(myn25, 1, 1, 154600)
mync12 = getNormCutflow(myn12, 1, 1, 49800)
mync13 = getNormCutflow(myn13, 1, 1, 100000)
mync14 = getNormCutflow(myn14, 1, 1, 50000)
mync15 = getNormCutflow(myn15, 1, 1, 50000)
mync16 = getNormCutflow(myn16, 1, 1, 50000)
mync17 = getNormCutflow(myn17, 1, 1, 50000)


#mync1 = getNormCutflow(myn1, 1, 2700, 48534)
#mync2 = getNormCutflow(myn2, 1, 2700, 48758)
#mync3 = getNormCutflow(myn3, 1, 2700, 49776)
#mync4 = getNormCutflow(myn4, 1, 2700, 49840)
#mync5 = getNormCutflow(myn5, 1, 2700, 49298)
#mync6 = getNormCutflow(myn6, 1, 2700, 49107)
#mync7 = getNormCutflow(myn7, 1, 2700, 49929)
#mync8 = getNormCutflow(myn8, 1, 1, 1)
#mync9 = getNormCutflow(myn9, 1, 2700, 49164)
#mync10 = getNormCutflow(myn10, 1, 2700, 49971)
#mync11 = getNormCutflow(myn11, 1, 2700, 49976)
#mync12 = getNormCutflow(myn12, 1, 2700, 49983)
#mync13 = getNormCutflow(myn13, 1, 2700, 49977)
#mync14 = getNormCutflow(myn14, 831.8,2700, 9552643)

#get comparative cutflows
#mycc1 = getCompareCutflow(myn1)
#mycc2 = getCompareCutflow(myn2)
#mycc3 = getCompareCutflow(myn3)
#mycc4 = getCompareCutflow(myn4)
mycc5 = getCompareCutflow(myn5)
mycc6 = getCompareCutflow(myn6)
mycc7 = getCompareCutflow(myn7)
mycc8 = getCompareCutflow(myn8)
mycc9 = getCompareCutflow(myn9)
mycc10 = getCompareCutflow(myn10)
mycc11 = getCompareCutflow(myn11)
mycc12 = getCompareCutflow(myn12)
mycc13 = getCompareCutflow(myn13)
mycc14 = getCompareCutflow(myn14)
mycc15 = getCompareCutflow(myn15)
mycc16 = getCompareCutflow(myn16)
mycc17 = getCompareCutflow(myn17)
#mycc18 = getCompareCutflow(myn18)
#mycc19 = getCompareCutflow(myn19)
#mycc20 = getCompareCutflow(myn20)
#mycc21 = getCompareCutflow(myn21)
#mycc22 = getCompareCutflow(myn22)
#mycc23 = getCompareCutflow(myn23)
#mycc24 = getCompareCutflow(myn24)
#mycc25 = getCompareCutflow(myn25)


#writing tex file
target = open("cutflowtable_80X_2p1.tex",'w')
#target = open("cutflowtable_76X_vh_ZP_DDT.tex",'w')
 
target.write("\documentclass{article}")
target.write("\n")
target.write("\usepackage[a4paper,margin=1in,landscape]{geometry}")
target.write("\n")
target.write("\oddsidemargin=0in")
target.write("\n")
target.write("\evensidemargin=0in")
target.write("\n")
target.write("\n")
target.write("\\begin{document}")
target.write("\n")
target.write("\n")
#first table, normalized cutflow
target.write("\\begin{table}[h]")
target.write("\n")
target.write("\small")
target.write("\n")
target.write("\\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|}")
target.write("\n")
target.write("\hline")
target.write("\n")
target.write("Sample & Presel & Trig & AK4btag & AK4dijetmass & Tau21 & TriAK4Jetmass & AK8mass & AK8btag & Boosted & Resolved\\\ \hline")
target.write("\n")
#target.write(sample1name + " & " + str(round(mync1[0],3))+ " & " + str(round(mync1[1],3)) + " & " + str(round(mync1[2],3)) + " & " + str(round(mync1[3],3)) + " & " + str(round(mync1[4],3)) + " & " + str(round(mync1[5],3)) + " & " + str(round(mync1[6],3)) + " & " + str(round(mync1[7],3)) + " & " + str(round(mync1[8],3)) + " & " + str(round(mync1[9],3)) + " & " + str(round(mync1[10],3))+ " \\\ " )
#target.write("\n")
#target.write(sample2name + " & " + str(round(mync2[0],3))+ " & " + str(round(mync2[1],3)) + " & " + str(round(mync2[2],3)) + " & " + str(round(mync2[3],3)) + " & " + str(round(mync2[4],3)) + " & " + str(round(mync2[5],3)) + " & " + str(round(mync2[6],3)) + " & " + str(round(mync2[7],3)) + " & " + str(round(mync2[8],3)) + " & " + str(round(mync2[9],3)) + " & " + str(round(mync2[10],3)) +" \\\ " )
#target.write("\n")
#target.write(sample3name + " & " + str(round(mync3[0],3))+ " & " + str(round(mync3[1],3)) + " & " + str(round(mync3[2],3)) + " & " + str(round(mync3[3],3)) + " & " + str(round(mync3[4],3)) + " & " + str(round(mync3[5],3)) + " & " + str(round(mync3[6],3)) + " & " + str(round(mync3[7],3)) + " & " + str(round(mync3[8],3)) + " & " + str(round(mync3[9],3)) + " & " + str(round(mync3[10],3)) + " \\\ " )
#target.write("\n")
#target.write(sample4name + " & " + str(round(mync4[0],3))+ " & " + str(round(mync4[1],3)) + " & " + str(round(mync4[2],3)) + " & " + str(round(mync4[3],3)) + " & " + str(round(mync4[4],3)) + " & " + str(round(mync4[5],3)) + " & " + str(round(mync4[6],3))+ " & " + str(round(mync4[7],3)) + " & " + str(round(mync4[8],3)) + " & " + str(round(mync4[9],3)) + " & " + str(round(mync4[10],3)) +" \\\ " )
#target.write("\n")
target.write(sample5name + " & " + str(round(mync5[0],3))+ " & " + str(round(mync5[1],3)) + " & " + str(round(mync5[2],3)) + " & " + str(round(mync5[3],3)) + " & " + str(round(mync5[4],3)) + " & " + str(round(mync5[5],3)) + " & " + str(round(mync5[6],3)) + " & " + str(round(mync5[7],3)) + " & " + str(round(mync5[8],3)) + " & " + str(round(mync5[9],3)) + " & " + str(round(mync5[10],3)) +" \\\ " )
target.write("\n")
target.write(sample6name + " & " + str(round(mync6[0],3))+ " & " + str(round(mync6[1],3)) + " & " + str(round(mync6[2],3)) + " & " + str(round(mync6[3],3)) + " & " + str(round(mync6[4],3)) + " & " + str(round(mync6[5],3)) + " & " + str(round(mync6[6],3)) + " & " + str(round(mync6[7],3)) + " & " + str(round(mync6[8],3)) + " & " + str(round(mync6[9],3)) + " & " + str(round(mync6[10],3)) +" \\\ " )
target.write("\n")
target.write(sample7name + " & " + str(round(mync7[0],3))+ " & " + str(round(mync7[1],3)) + " & " + str(round(mync7[2],3)) + " & " + str(round(mync7[3],3)) + " & " + str(round(mync7[4],3)) + " & " + str(round(mync7[5],3)) + " & " + str(round(mync7[6],3)) + " & " + str(round(mync7[7],3)) + " & " + str(round(mync7[8],3)) + " & " + str(round(mync7[9],3)) + " & " + str(round(mync7[10],3)) +" \\\ " )
target.write("\n")
target.write(sample8name + " & " + str(round(mync8[0],3))+ " & " + str(round(mync8[1],3)) + " & " + str(round(mync8[2],3)) + " & " + str(round(mync8[3],3)) + " & " + str(round(mync8[4],3)) + " & " + str(round(mync8[5],3)) + " & " + str(round(mync8[6],3)) + " & " + str(round(mync8[7],3)) + " & " + str(round(mync8[8],3)) + " & " + str(round(mync8[9],3)) + " & " + str(round(mync8[10],3)) + " \\\ " )
target.write("\n")
target.write(sample9name + " & " + str(round(mync9[0],3))+ " & " + str(round(mync9[1],3)) + " & " + str(round(mync9[2],3)) + " & " + str(round(mync9[3],3)) + " & " + str(round(mync9[4],3)) + " & " + str(round(mync9[5],3)) + " & " + str(round(mync9[6],3)) + " & " + str(round(mync9[7],3)) + " & " + str(round(mync9[8],3)) + " & " + str(round(mync9[9],3)) + " & " + str(round(mync9[10],3)) +" \\\ " )
target.write("\n")
target.write(sample10name + " & " + str(round(mync10[0],3))+ " & " + str(round(mync10[1],3)) + " & " + str(round(mync10[2],3)) + " & " + str(round(mync10[3],3)) + " & " + str(round(mync10[4],3)) + " & " + str(round(mync10[5],3)) + " & " + str(round(mync10[6],3)) + " & " + str(round(mync10[7],3)) + " & " + str(round(mync10[8],3)) + " & " + str(round(mync10[9],3)) + " & " + str(round(mync10[10],3)) +" \\\ " )
target.write("\n")
target.write(sample11name + " & " + str(round(mync11[0],3))+ " & " + str(round(mync11[1],3)) + " & " + str(round(mync11[2],3)) + " & " + str(round(mync11[3],3)) + " & " + str(round(mync11[4],3)) + " & " + str(round(mync11[5],3)) + " & " + str(round(mync11[6],3)) + " & " + str(round(mync11[7],3)) + " & " + str(round(mync11[8],3)) + " & " + str(round(mync11[9],3)) + " & " + str(round(mync11[10],3)) +" \\\ " )
target.write("\n")
target.write(sample12name + " & " + str(round(mync12[0],3))+ " & " + str(round(mync12[1],3)) + " & " + str(round(mync12[2],3)) + " & " + str(round(mync12[3],3)) + " & " + str(round(mync12[4],3)) + " & " + str(round(mync12[5],3)) + " & " + str(round(mync12[6],3)) + " & " + str(round(mync12[7],3)) + " & " + str(round(mync12[8],3)) + " & " + str(round(mync12[9],3)) + " & " + str(round(mync12[10],3)) + " \\\ " )
target.write("\n")
target.write(sample13name + " & " + str(round(mync13[0],3))+ " & " + str(round(mync13[1],3)) + " & " + str(round(mync13[2],3)) + " & " + str(round(mync13[3],3)) + " & " + str(round(mync13[4],3)) + " & " + str(round(mync13[5],3)) + " & " + str(round(mync13[6],3)) + " & " + str(round(mync13[7],3)) + " & " + str(round(mync13[8],3)) + " & " + str(round(mync13[9],3)) + " & " + str(round(mync13[10],3)) +" \\\ " )
target.write("\n")
target.write(sample14name + " & " + str(round(mync14[0],3))+ " & " + str(round(mync14[1],3)) + " & " + str(round(mync14[2],3)) + " & " + str(round(mync14[3],3)) + " & " + str(round(mync14[4],3)) + " & " + str(round(mync14[5],3)) + " & " + str(round(mync14[6],3)) + " & " + str(round(mync14[7],3)) + " & " + str(round(mync14[8],3)) + " & " + str(round(mync14[9],3)) + " & " + str(round(mync14[10],3)) +" \\\ " )
target.write("\n")
target.write(sample15name + " & " + str(round(mync15[0],3))+ " & " + str(round(mync15[1],3)) + " & " + str(round(mync15[2],3)) + " & " + str(round(mync15[3],3)) + " & " + str(round(mync15[4],3)) + " & " + str(round(mync15[5],3)) + " & " + str(round(mync15[6],3)) + " & " + str(round(mync15[7],3)) + " & " + str(round(mync15[8],3)) + " & " + str(round(mync15[9],3)) + " & " + str(round(mync15[10],3)) +" \\\ " )
target.write("\n")
target.write(sample16name + " & " + str(round(mync16[0],3))+ " & " + str(round(mync16[1],3)) + " & " + str(round(mync16[2],3)) + " & " + str(round(mync16[3],3)) + " & " + str(round(mync16[4],3)) + " & " + str(round(mync16[5],3)) + " & " + str(round(mync16[6],3)) + " & " + str(round(mync16[7],3)) + " & " + str(round(mync16[8],3)) + " & " + str(round(mync16[9],3)) + " & " + str(round(mync16[10],3)) +" \\\ " )
target.write("\n")
target.write(sample17name + " & " + str(round(mync17[0],3))+ " & " + str(round(mync17[1],3)) + " & " + str(round(mync17[2],3)) + " & " + str(round(mync17[3],3)) + " & " + str(round(mync17[4],3)) + " & " + str(round(mync17[5],3)) + " & " + str(round(mync17[6],3)) + " & " + str(round(mync17[7],3)) + " & " + str(round(mync17[8],3)) + " & " + str(round(mync17[9],3)) + " & " + str(round(mync17[10],3)) +" \\\ " )
#target.write("\n")
#target.write(sample18name + " & " + str(round(mync18[0],3))+ " & " + str(round(mync18[1],3)) + " & " + str(round(mync18[2],3)) + " & " + str(round(mync18[3],3)) + " & " + str(round(mync18[4],3)) + " & " + str(round(mync18[5],3)) + " & " + str(round(mync18[6],3)) + " & " + str(round(mync18[7],3)) + " & " + str(round(mync18[8],3)) + " & " + str(round(mync18[9],3)) + " & " + str(round(mync18[10],3)) +" \\\ " )
#target.write("\n")
#target.write(sample19name + " & " + str(round(mync19[0],3))+ " & " + str(round(mync19[1],3)) + " & " + str(round(mync19[2],3)) + " & " + str(round(mync19[3],3)) + " & " + str(round(mync19[4],3)) + " & " + str(round(mync19[5],3)) + " & " + str(round(mync19[6],3)) + " & " + str(round(mync19[7],3)) + " & " + str(round(mync19[8],3)) + " & " + str(round(mync19[9],3)) + " & " + str(round(mync19[10],3)) +" \\\ " )
#target.write("\n")
#target.write(sample20name + " & " + str(round(mync20[0],3))+ " & " + str(round(mync20[1],3)) + " & " + str(round(mync20[2],3)) + " & " + str(round(mync20[3],3)) + " & " + str(round(mync20[4],3)) + " & " + str(round(mync20[5],3)) + " & " + str(round(mync20[6],3)) + " & " + str(round(mync20[7],3)) + " & " + str(round(mync20[8],3)) + " & " + str(round(mync20[9],3)) + " & " + str(round(mync20[10],3)) +" \\\ " )
#target.write("\n")
#target.write(sample21name + " & " + str(round(mync21[0],3))+ " & " + str(round(mync21[1],3)) + " & " + str(round(mync21[2],3)) + " & " + str(round(mync21[3],3)) + " & " + str(round(mync21[4],3)) + " & " + str(round(mync21[5],3)) + " & " + str(round(mync21[6],3)) + " & " + str(round(mync21[7],3)) + " & " + str(round(mync21[8],3)) + " & " + str(round(mync21[9],3)) + " & " + str(round(mync21[10],3)) +" \\\ " )
#target.write("\n")
#target.write(sample22name + " & " + str(round(mync22[0],3))+ " & " + str(round(mync22[1],3)) + " & " + str(round(mync22[2],3)) + " & " + str(round(mync22[3],3)) + " & " + str(round(mync22[4],3)) + " & " + str(round(mync22[5],3)) + " & " + str(round(mync22[6],3)) + " & " + str(round(mync22[7],3)) + " & " + str(round(mync22[8],3)) + " & " + str(round(mync22[9],3)) + " & " + str(round(mync22[10],3)) +" \\\ " )
#target.write("\n")
#target.write(sample23name + " & " + str(round(mync23[0],3))+ " & " + str(round(mync23[1],3)) + " & " + str(round(mync23[2],3)) + " & " + str(round(mync23[3],3)) + " & " + str(round(mync23[4],3)) + " & " + str(round(mync23[5],3)) + " & " + str(round(mync23[6],3)) + " & " + str(round(mync23[7],3)) + " & " + str(round(mync23[8],3)) + " & " + str(round(mync23[9],3)) + " & " + str(round(mync23[10],3)) +" \\\ " )
#target.write("\n")
#target.write(sample24name + " & " + str(round(mync24[0],3))+ " & " + str(round(mync24[1],3)) + " & " + str(round(mync24[2],3)) + " & " + str(round(mync24[3],3)) + " & " + str(round(mync24[4],3)) + " & " + str(round(mync24[5],3)) + " & " + str(round(mync24[6],3)) + " & " + str(round(mync24[7],3)) + " & " + str(round(mync24[8],3)) + " & " + str(round(mync24[9],3)) + " & " + str(round(mync24[10],3)) +" \\\ " )
#target.write("\n")
#target.write(sample25name + " & " + str(round(mync25[0],3))+ " & " + str(round(mync25[1],3)) + " & " + str(round(mync25[2],3)) + " & " + str(round(mync25[3],3)) + " & " + str(round(mync25[4],3)) + " & " + str(round(mync25[5],3)) + " & " + str(round(mync25[6],3)) + " & " + str(round(mync25[7],3)) + " & " + str(round(mync25[8],3)) + " & " + str(round(mync25[9],3)) + " & " + str(round(mync25[10],3)) +" \\\ " )
target.write("\n")
target.write("\hline")
target.write("\n")
target.write("\end{tabular}")
target.write("\n")
target.write("\caption{ Cutflow Raw Number of Events }")
target.write("\n")
target.write("\end{table}")

#second table, comparison cutflow
target.write("\n")
target.write("\\newpage")
target.write("\\begin{table}[h]")
target.write("\n")
target.write("\small")
target.write("\n")
target.write("\\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|}")
target.write("\n")
target.write("\hline")
target.write("\n")
target.write("Sample & Mass & $\\tau_{21}$ DDT 0.55 & bbtag 0.3 & bbtag 0.6 & $\\tau_{21}$ DDT 0.45 & bbtag 0.3 & bbtag 0.6 & $\\tau_{21}$ DDT 0.38 & bbtag 0.3 & bbtag 0.6 \\\ \hline")
target.write("\n")
#target.write(sample1name + " & " + str(round(mycc1[0],2))+ " & " + str(round(mycc1[1],2)) + " & " + str(round(mycc1[2],2)) + " & " + str(round(mycc1[3],2)) + " & " + str(round(mycc1[4],2)) + " & " + str(round(mycc1[5],2)) + " & " + str(round(mycc1[6],2)) + " & " + str(round(mycc1[7],2)) + " & " + str(round(mycc1[8],2)) + " & " + str(round(mycc1[9],2)) + " \\\ " )
#target.write("\n") 
#target.write(sample2name + " & " + str(round(mycc2[0],2))+ " & " + str(round(mycc2[1],2)) + " & " + str(round(mycc2[2],2)) + " & " + str(round(mycc2[3],2)) + " & " + str(round(mycc2[4],2)) + " & " + str(round(mycc2[5],2)) + " & " + str(round(mycc2[6],2)) + " & " + str(round(mycc2[7],2)) + " & " + str(round(mycc2[8],2)) + " & " + str(round(mycc2[9],2)) + " \\\ " )
#target.write("\n")
#target.write(sample3name + " & " + str(round(mycc3[0],2))+ " & " + str(round(mycc3[1],2)) + " & " + str(round(mycc3[2],2)) + " & " + str(round(mycc3[3],2)) + " & " + str(round(mycc3[4],2)) + " & " + str(round(mycc3[5],2)) + " & " + str(round(mycc3[6],2)) + " & " + str(round(mycc3[7],2)) + " & " + str(round(mycc3[8],2)) +  "& " + str(round(mycc3[9],2)) + " \\\ " )
#target.write("\n")
#target.write(sample4name + " & " + str(round(mycc4[0],2))+ " & " + str(round(mycc4[1],2)) + " & " + str(round(mycc4[2],2)) + " & " + str(round(mycc4[3],2)) + " & " + str(round(mycc4[4],2)) + " & " + str(round(mycc4[5],2)) + " & " + str(round(mycc4[6],2)) + " & " + str(round(mycc4[7],2)) + " & " + str(round(mycc4[8],2)) + " & " + str(round(mycc4[9],2)) + " \\\ " )
#target.write("\n")
target.write(sample5name + " & " + str(round(mycc5[0],2))+ " & " + str(round(mycc5[1],2)) + " & " + str(round(mycc5[2],2)) + " & " + str(round(mycc5[3],2)) + " & " + str(round(mycc5[4],2)) + " & " + str(round(mycc5[5],2)) + " & " + str(round(mycc5[6],2)) + " & " + str(round(mycc5[7],2)) + " & " + str(round(mycc5[8],2)) + " & " + str(round(mycc5[9],2)) +" \\\ " )
target.write("\n")
target.write(sample6name + " & " + str(round(mycc6[0],2))+ " & " + str(round(mycc6[1],2)) + " & " + str(round(mycc6[2],2)) + " & " + str(round(mycc6[3],2)) + " & " + str(round(mycc6[4],2)) + " & " + str(round(mycc6[5],2)) + " & " + str(round(mycc6[6],2)) + " & " + str(round(mycc6[7],2)) + " & " + str(round(mycc6[8],2)) + " & " + str(round(mycc6[9],2)) +" \\\ " )
target.write("\n")
target.write(sample7name + " & " + str(round(mycc7[0],2))+ " & " + str(round(mycc7[1],2)) + " & " + str(round(mycc7[2],2)) + " & " + str(round(mycc7[3],2)) + " & " + str(round(mycc7[4],2)) + " & " + str(round(mycc7[5],2)) + " & " + str(round(mycc7[6],2)) + " & " + str(round(mycc7[7],2)) + " & " + str(round(mycc7[8],2)) + " & " + str(round(mycc7[9],2)) + " \\\ ")
target.write("\n")
target.write(sample8name + " & " + str(round(mycc8[0],2))+ " & " + str(round(mycc8[1],2)) + " & " + str(round(mycc8[2],2)) + " & " + str(round(mycc8[3],2)) + " & " + str(round(mycc8[4],2)) + " & " + str(round(mycc8[5],2)) + " & " + str(round(mycc8[6],2)) + " & " + str(round(mycc8[7],2)) + " & " + str(round(mycc8[8],2)) + " & " + str(round(mycc8[9],2)) +" \\\ " )
target.write("\n")
target.write(sample9name + " & " + str(round(mycc9[0],2))+ " & " + str(round(mycc9[1],2)) + " & " + str(round(mycc9[2],2)) + " & " + str(round(mycc9[3],2)) + " & " + str(round(mycc9[4],2)) + " & " + str(round(mycc9[5],2)) + " & " + str(round(mycc9[6],2)) + " & " + str(round(mycc9[7],2)) + " & " + str(round(mycc9[8],2)) + " & " + str(round(mycc9[9],2)) + " \\\ " )
target.write("\n")
target.write(sample10name + " & " + str(round(mycc10[0],2))+ " & " + str(round(mycc10[1],2)) + " & " + str(round(mycc10[2],2)) + " & " + str(round(mycc10[3],2)) + " & " + str(round(mycc10[4],2)) + " & " + str(round(mycc10[5],2)) + " & " + str(round(mycc10[6],2)) + " & " + str(round(mycc10[7],2)) + " & " + str(round(mycc10[8],2)) + " & " + str(round(mycc10[9],2)) +" \\\ " )
target.write("\n")
target.write(sample11name + " & " + str(round(mycc11[0],2))+ " & " + str(round(mycc11[1],2)) + " & " + str(round(mycc11[2],2)) + " & " + str(round(mycc11[3],2)) + " & " + str(round(mycc11[4],2)) + " & " + str(round(mycc11[5],2)) + " & " + str(round(mycc11[6],2)) + " & " + str(round(mycc11[7],2)) + " & " + str(round(mycc11[8],2)) + " & " + str(round(mycc11[9],2)) +" \\\ " )
target.write("\n")
target.write(sample12name + " & " + str(round(mycc12[0],2))+ " & " + str(round(mycc12[1],2)) + " & " + str(round(mycc12[2],2)) + " & " + str(round(mycc12[3],2)) + " & " + str(round(mycc12[4],2)) + " & " + str(round(mycc12[5],2)) + " & " + str(round(mycc12[6],2)) + " & " + str(round(mycc12[7],2)) + " & " + str(round(mycc12[8],2)) + " & " + str(round(mycc12[9],2)) + " \\\ " )
target.write("\n")
target.write(sample13name + " & " + str(round(mycc13[0],2))+ " & " + str(round(mycc13[1],2)) + " & " + str(round(mycc13[2],2)) + " & " + str(round(mycc13[3],2)) + " & " + str(round(mycc13[4],2)) + " & " + str(round(mycc13[5],2)) + " & " + str(round(mycc13[6],2)) + " & " + str(round(mycc13[7],2)) + " & " + str(round(mycc13[8],2)) + " & " + str(round(mycc13[9],2)) + " \\\ " )
target.write("\n")
target.write(sample14name + " & " + str(round(mycc14[0],2))+ " & " + str(round(mycc14[1],2)) + " & " + str(round(mycc14[2],2)) + " & " + str(round(mycc14[3],2)) + " & " + str(round(mycc14[4],2)) + " & " + str(round(mycc14[5],2)) + " & " + str(round(mycc14[6],2)) + " & " + str(round(mycc14[7],2)) + " & " + str(round(mycc14[8],2)) + " & " + str(round(mycc14[9],2)) + " \\\ " )
target.write("\n")
target.write(sample15name + " & " + str(round(mycc15[0],2))+ " & " + str(round(mycc15[1],2)) + " & " + str(round(mycc15[2],2)) + " & " + str(round(mycc15[3],2)) + " & " + str(round(mycc15[4],2)) + " & " + str(round(mycc15[5],2)) + " & " + str(round(mycc15[6],2)) + " & " + str(round(mycc15[7],2)) + " & " + str(round(mycc15[8],2)) + " & " + str(round(mycc15[9],2)) + " \\\ " )
target.write("\n")
target.write(sample16name + " & " + str(round(mycc16[0],2))+ " & " + str(round(mycc16[1],2)) + " & " + str(round(mycc16[2],2)) + " & " + str(round(mycc16[3],2)) + " & " + str(round(mycc16[4],2)) + " & " + str(round(mycc16[5],2)) + " & " + str(round(mycc16[6],2)) + " & " + str(round(mycc16[7],2)) + " & " + str(round(mycc16[8],2)) + " & " + str(round(mycc16[9],2)) + " \\\ " )
target.write("\n")
target.write(sample17name + " & " + str(round(mycc17[0],2))+ " & " + str(round(mycc17[1],2)) + " & " + str(round(mycc17[2],2)) + " & " + str(round(mycc17[3],2)) + " & " + str(round(mycc17[4],2)) + " & " + str(round(mycc17[5],2)) + " & " + str(round(mycc17[6],2)) + " & " + str(round(mycc17[7],2)) + " & " + str(round(mycc17[8],2)) + " & " + str(round(mycc17[9],2)) + " \\\ " )
#target.write("\n")
#target.write(sample18name + " & " + str(round(mycc18[0],2))+ " & " + str(round(mycc18[1],2)) + " & " + str(round(mycc18[2],2)) + " & " + str(round(mycc18[3],2)) + " & " + str(round(mycc18[4],2)) + " & " + str(round(mycc18[5],2)) + " & " + str(round(mycc18[6],2)) + " & " + str(round(mycc18[7],2)) + " & " + str(round(mycc18[8],2)) + " & " + str(round(mycc18[9],2)) + " \\\ " )
#target.write("\n")
#target.write(sample19name + " & " + str(round(mycc19[0],2))+ " & " + str(round(mycc19[1],2)) + " & " + str(round(mycc19[2],2)) + " & " + str(round(mycc19[3],2)) + " & " + str(round(mycc19[4],2)) + " & " + str(round(mycc19[5],2)) + " & " + str(round(mycc19[6],2)) + " & " + str(round(mycc19[7],2)) + " & " + str(round(mycc19[8],2)) + " & " + str(round(mycc19[9],2)) + " \\\ " )
#target.write("\n")
#target.write(sample20name + " & " + str(round(mycc20[0],2))+ " & " + str(round(mycc20[1],2)) + " & " + str(round(mycc20[2],2)) + " & " + str(round(mycc20[3],2)) + " & " + str(round(mycc20[4],2)) + " & " + str(round(mycc20[5],2)) + " & " + str(round(mycc20[6],2)) + " & " + str(round(mycc20[7],2)) + " & " + str(round(mycc20[8],2)) + " & " + str(round(mycc20[9],2)) + " \\\ " )
#target.write("\n")
#target.write(sample21name + " & " + str(round(mycc21[0],2))+ " & " + str(round(mycc21[1],2)) + " & " + str(round(mycc21[2],2)) + " & " + str(round(mycc21[3],2)) + " & " + str(round(mycc21[4],2)) + " & " + str(round(mycc21[5],2)) + " & " + str(round(mycc21[6],2)) + " & " + str(round(mycc21[7],2)) + " & " + str(round(mycc21[8],2)) + " & " + str(round(mycc21[9],2)) + " \\\ " )
#target.write("\n")
#target.write(sample22name + " & " + str(round(mycc22[0],2))+ " & " + str(round(mycc22[1],2)) + " & " + str(round(mycc22[2],2)) + " & " + str(round(mycc22[3],2)) + " & " + str(round(mycc22[4],2)) + " & " + str(round(mycc22[5],2)) + " & " + str(round(mycc22[6],2)) + " & " + str(round(mycc22[7],2)) + " & " + str(round(mycc22[8],2)) + " & " + str(round(mycc22[9],2)) + " \\\ " )
#target.write("\n")
#target.write(sample23name + " & " + str(round(mycc23[0],2))+ " & " + str(round(mycc23[1],2)) + " & " + str(round(mycc23[2],2)) + " & " + str(round(mycc23[3],2)) + " & " + str(round(mycc23[4],2)) + " & " + str(round(mycc23[5],2)) + " & " + str(round(mycc23[6],2)) + " & " + str(round(mycc23[7],2)) + " & " + str(round(mycc23[8],2)) + " & " + str(round(mycc23[9],2)) + " \\\ " )
#target.write("\n")
#target.write(sample24name + " & " + str(round(mycc24[0],2))+ " & " + str(round(mycc24[1],2)) + " & " + str(round(mycc24[2],2)) + " & " + str(round(mycc24[3],2)) + " & " + str(round(mycc24[4],2)) + " & " + str(round(mycc24[5],2)) + " & " + str(round(mycc24[6],2)) + " & " + str(round(mycc24[7],2)) + " & " + str(round(mycc24[8],2)) + " & " + str(round(mycc24[9],2)) + " \\\ " )
#target.write("\n")
#target.write(sample25name + " & " + str(round(mycc25[0],2))+ " & " + str(round(mycc25[1],2)) + " & " + str(round(mycc25[2],2)) + " & " + str(round(mycc25[3],2)) + " & " + str(round(mycc25[4],2)) + " & " + str(round(mycc25[5],2)) + " & " + str(round(mycc25[6],2)) + " & " + str(round(mycc25[7],2)) + " & " + str(round(mycc25[8],2)) + " & " + str(round(mycc25[9],2)) + " \\\ " )
target.write("\n")
target.write("\hline")
target.write("\n")
target.write("\end{tabular}")
target.write("\n")
target.write("\caption{ Cutflow of N Events After Cut / N Events Before Cut }")
target.write("\n")
target.write("\end{table}")
target.write("\end{document}")

target.close()
