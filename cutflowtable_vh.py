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
    comparecutflow = [array[1]/array[0], array[2]/array[1], array[3]/array[2], array[4]/array[2], array[5]/array[1], array[6]/array[5],array[7]/array[5],array[8]/array[1], array[9]/array[8], array[10]/array[8]]
    
    return comparecutflow

#input files
WP600 = ROOT.TFile("tree_WP_600_VH.root")
WP800 = ROOT.TFile("tree_WP_800_VH.root")
WP1000 = ROOT.TFile("tree_WP_1000_VH.root")
WP1200 = ROOT.TFile("tree_WP_1200_VH.root")
WP1400 = ROOT.TFile("tree_WP_1400_VH.root")
WP1600 = ROOT.TFile("tree_WP_1600_VH.root")
WP1800 = ROOT.TFile("tree_WP_1800_VH.root")
WP2000 = ROOT.TFile("tree_WP_2000_VH.root")
WP2500 = ROOT.TFile("tree_WP_2500_VH.root")
WP3000 = ROOT.TFile("tree_WP_3000_VH.root")
WP3500 = ROOT.TFile("tree_WP_3500_VH.root")
WP4000 = ROOT.TFile("tree_WP_4000_VH.root")
WP4500 = ROOT.TFile("tree_WP_4500_VH.root")

ZP600 = ROOT.TFile("tree_ZP_600_DDT_VH.root")
ZP800 = ROOT.TFile("tree_ZP_800_DDT_VH.root")
ZP1000 = ROOT.TFile("tree_ZP_1000_DDT_VH.root")
ZP1200 = ROOT.TFile("tree_ZP_1200_DDT_VH.root")
ZP1400 = ROOT.TFile("tree_ZP_1400_DDT_VH.root")
ZP1600 = ROOT.TFile("tree_ZP_1600_DDT_VH.root")
ZP1800 = ROOT.TFile("tree_ZP_1800_DDT_VH.root")
#ZP2000 = ROOT.TFile("tree_ZP_2000_DDT_VH.root")
ZP2500 = ROOT.TFile("tree_ZP_2500_DDT_VH.root")
ZP3000 = ROOT.TFile("tree_ZP_3000_DDT_VH.root")
ZP3500 = ROOT.TFile("tree_ZP_3500_DDT_VH.root")
ZP4000 = ROOT.TFile("tree_ZP_4000_DDT_VH.root")
ZP4500 = ROOT.TFile("tree_ZP_4500_DDT_VH.root")

ttbar = ROOT.TFile("tree_ttbar_DDT_VH.root")

#sample names
sample1name = "WP 600"
sample2name = "WP 800"
sample3name = "WP 1000"
sample4name = "WP 1200"
sample5name = "WP 1400"
sample6name = "WP 1600"
sample7name = "WP 1800"
sample8name = "WP 2000"
sample9name = "WP 2500"
sample10name = "WP 3000"
sample11name = "WP 3500"
sample12name = "WP 4000"
sample13name = "WP 4500"

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

sample14name = "ttbar"
#histograms for cutflow
histograms = ["c1","c2","c3","c3a","c3b","c4","c4a","c4b","c5","c5a","c5b"]

#initializing cutflow arrays
myn1 = []
myn2 = []
myn3 = []
myn4 = []
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

#writing cutflow arrays
myn1 = getIntegral(WP600,histograms)
myn2 = getIntegral(WP800,histograms)
myn3 = getIntegral(WP1000,histograms)
myn4 = getIntegral(WP1200,histograms)
myn5 = getIntegral(WP1400,histograms)
myn6 = getIntegral(WP1600,histograms)
myn7 = getIntegral(WP1800,histograms)
myn8 = getIntegral(WP2000,histograms)
myn9 = getIntegral(WP2500,histograms)
myn10 = getIntegral(WP3000,histograms)
myn11 = getIntegral(WP3500,histograms)
myn12 = getIntegral(WP4000,histograms)
myn13 = getIntegral(WP4500,histograms)

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
myn14 = getIntegral(ttbar,histograms)

#writing normalized cutflow arrays
mync1 = getNormCutflow(myn1, 1, 2700, 48666)
mync2 = getNormCutflow(myn2, 1, 2700, 49560)
mync3 = getNormCutflow(myn3, 1, 2700, 49774)
mync4 = getNormCutflow(myn4, 1, 2700, 49853)
mync5 = getNormCutflow(myn5, 1, 2700, 49686)
mync6 = getNormCutflow(myn6, 1, 2700, 49916)
mync7 = getNormCutflow(myn7, 1, 2700, 49943)
mync8 = getNormCutflow(myn8, 1, 2700, 49945)
mync9 = getNormCutflow(myn9, 1, 2700, 49956)
mync10 = getNormCutflow(myn10, 1, 2700, 48369)
mync11 = getNormCutflow(myn11, 1, 2700, 47582)
mync12 = getNormCutflow(myn12, 1, 2700, 49971)
mync13 = getNormCutflow(myn13, 1, 2700, 49974)

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
mync14 = getNormCutflow(myn14, 831.8,2700, 9552643)

#get comparative cutflows
mycc1 = getCompareCutflow(myn1)
mycc2 = getCompareCutflow(myn2)
mycc3 = getCompareCutflow(myn3)
mycc4 = getCompareCutflow(myn4)
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


#writing tex file
target = open("cutflowtable_76X_vh_WP.tex",'w')
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
target.write("Sample & Trigger, Jet Kin., $\Delta\eta$ & Mass & $\\tau_{21}$ DDT 0.55 & bbtag 0.3 & bbtag 0.6 & $\\tau_{21}$ DDT 0.45 & bbtag 0.3 & bbtag 0.6 & $\\tau_{21}$ DDT 0.38 & bbtag 0.3 & bbtag 0.6 \\\ \hline")
target.write("\n")
target.write(sample1name + " & " + str(round(mync1[0],2))+ " & " + str(round(mync1[1],2)) + " & " + str(round(mync1[2],2)) + " & " + str(round(mync1[3],2)) + " & " + str(round(mync1[4],2)) + " & " + str(round(mync1[5],2)) + " & " + str(round(mync1[6],2)) + " & " + str(round(mync1[7],2)) + " & " + str(round(mync1[8],2)) + " & " + str(round(mync1[9],2)) + " & " + str(round(mync1[10],2))+ " \\\ " )
target.write("\n")
target.write(sample2name + " & " + str(round(mync2[0],2))+ " & " + str(round(mync2[1],2)) + " & " + str(round(mync2[2],2)) + " & " + str(round(mync2[3],2)) + " & " + str(round(mync2[4],2)) + " & " + str(round(mync2[5],2)) + " & " + str(round(mync2[6],2)) + " & " + str(round(mync2[7],2)) + " & " + str(round(mync2[8],2)) + " & " + str(round(mync2[9],2)) + " & " + str(round(mync2[10],2)) +" \\\ " )
target.write("\n")
target.write(sample3name + " & " + str(round(mync3[0],2))+ " & " + str(round(mync3[1],2)) + " & " + str(round(mync3[2],2)) + " & " + str(round(mync3[3],2)) + " & " + str(round(mync3[4],2)) + " & " + str(round(mync3[5],2)) + " & " + str(round(mync3[6],2)) + " & " + str(round(mync3[7],2)) + " & " + str(round(mync3[8],2)) + " & " + str(round(mync3[9],2)) + " & " + str(round(mync3[10],2)) + " \\\ " )
target.write("\n")
target.write(sample4name + " & " + str(round(mync4[0],2))+ " & " + str(round(mync4[1],2)) + " & " + str(round(mync4[2],2)) + " & " + str(round(mync4[3],2)) + " & " + str(round(mync4[4],2)) + " & " + str(round(mync4[5],2)) + " & " + str(round(mync4[6],2))+ " & " + str(round(mync4[7],2)) + " & " + str(round(mync4[8],2)) + " & " + str(round(mync4[9],2)) + " & " + str(round(mync4[10],2)) +" \\\ " )
target.write("\n")
target.write(sample5name + " & " + str(round(mync5[0],2))+ " & " + str(round(mync5[1],2)) + " & " + str(round(mync5[2],2)) + " & " + str(round(mync5[3],2)) + " & " + str(round(mync5[4],2)) + " & " + str(round(mync5[5],2)) + " & " + str(round(mync5[6],2)) + " & " + str(round(mync5[7],2)) + " & " + str(round(mync5[8],2)) + " & " + str(round(mync5[9],2)) + " & " + str(round(mync5[10],2)) +" \\\ " )
target.write("\n")
target.write(sample6name + " & " + str(round(mync6[0],2))+ " & " + str(round(mync6[1],2)) + " & " + str(round(mync6[2],2)) + " & " + str(round(mync6[3],2)) + " & " + str(round(mync6[4],2)) + " & " + str(round(mync6[5],2)) + " & " + str(round(mync6[6],2)) + " & " + str(round(mync6[7],2)) + " & " + str(round(mync6[8],2)) + " & " + str(round(mync6[9],2)) + " & " + str(round(mync6[10],2)) +" \\\ " )
target.write("\n")
target.write(sample7name + " & " + str(round(mync7[0],2))+ " & " + str(round(mync7[1],2)) + " & " + str(round(mync7[2],2)) + " & " + str(round(mync7[3],2)) + " & " + str(round(mync7[4],2)) + " & " + str(round(mync7[5],2)) + " & " + str(round(mync7[6],2)) + " & " + str(round(mync7[7],2)) + " & " + str(round(mync7[8],2)) + " & " + str(round(mync7[9],2)) + " & " + str(round(mync7[10],2)) +" \\\ " )
target.write("\n")
target.write(sample8name + " & " + str(round(mync8[0],2))+ " & " + str(round(mync8[1],2)) + " & " + str(round(mync8[2],2)) + " & " + str(round(mync8[3],2)) + " & " + str(round(mync8[4],2)) + " & " + str(round(mync8[5],2)) + " & " + str(round(mync8[6],2)) + " & " + str(round(mync8[7],2)) + " & " + str(round(mync8[8],2)) + " & " + str(round(mync8[9],2)) + " & " + str(round(mync8[10],2)) + " \\\ " )
target.write("\n")
target.write(sample9name + " & " + str(round(mync9[0],2))+ " & " + str(round(mync9[1],2)) + " & " + str(round(mync9[2],2)) + " & " + str(round(mync9[3],2)) + " & " + str(round(mync9[4],2)) + " & " + str(round(mync9[5],2)) + " & " + str(round(mync9[6],2)) + " & " + str(round(mync9[7],2)) + " & " + str(round(mync9[8],2)) + " & " + str(round(mync9[9],2)) + " & " + str(round(mync9[10],2)) +" \\\ " )
target.write("\n")
target.write(sample10name + " & " + str(round(mync10[0],2))+ " & " + str(round(mync10[1],2)) + " & " + str(round(mync10[2],2)) + " & " + str(round(mync10[3],2)) + " & " + str(round(mync10[4],2)) + " & " + str(round(mync10[5],2)) + " & " + str(round(mync10[6],2)) + " & " + str(round(mync10[7],2)) + " & " + str(round(mync10[8],2)) + " & " + str(round(mync10[9],2)) + " & " + str(round(mync10[10],2)) +" \\\ " )
target.write("\n")
target.write(sample11name + " & " + str(round(mync11[0],2))+ " & " + str(round(mync11[1],2)) + " & " + str(round(mync11[2],2)) + " & " + str(round(mync11[3],2)) + " & " + str(round(mync11[4],2)) + " & " + str(round(mync11[5],2)) + " & " + str(round(mync11[6],2)) + " & " + str(round(mync11[7],2)) + " & " + str(round(mync11[8],2)) + " & " + str(round(mync11[9],2)) + " & " + str(round(mync11[10],2)) +" \\\ " )
target.write("\n")
target.write(sample12name + " & " + str(round(mync12[0],2))+ " & " + str(round(mync12[1],2)) + " & " + str(round(mync12[2],2)) + " & " + str(round(mync12[3],2)) + " & " + str(round(mync12[4],2)) + " & " + str(round(mync12[5],2)) + " & " + str(round(mync12[6],2)) + " & " + str(round(mync12[7],2)) + " & " + str(round(mync12[8],2)) + " & " + str(round(mync12[9],2)) + " & " + str(round(mync12[10],2)) + " \\\ " )
target.write("\n")
target.write(sample13name + " & " + str(round(mync13[0],2))+ " & " + str(round(mync13[1],2)) + " & " + str(round(mync13[2],2)) + " & " + str(round(mync13[3],2)) + " & " + str(round(mync13[4],2)) + " & " + str(round(mync13[5],2)) + " & " + str(round(mync13[6],2)) + " & " + str(round(mync13[7],2)) + " & " + str(round(mync13[8],2)) + " & " + str(round(mync13[9],2)) + " & " + str(round(mync13[10],2)) +" \\\ " )
target.write("\n")
target.write(sample14name + " & " + str(round(mync14[0],2))+ " & " + str(round(mync14[1],2)) + " & " + str(round(mync14[2],2)) + " & " + str(round(mync14[3],2)) + " & " + str(round(mync14[4],2)) + " & " + str(round(mync14[5],2)) + " & " + str(round(mync14[6],2)) + " & " + str(round(mync14[7],2)) + " & " + str(round(mync14[8],2)) + " & " + str(round(mync14[9],2)) + " & " + str(round(mync14[10],2)) +" \\\ " )
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
target.write(sample1name + " & " + str(round(mycc1[0],2))+ " & " + str(round(mycc1[1],2)) + " & " + str(round(mycc1[2],2)) + " & " + str(round(mycc1[3],2)) + " & " + str(round(mycc1[4],2)) + " & " + str(round(mycc1[5],2)) + " & " + str(round(mycc1[6],2)) + " & " + str(round(mycc1[7],2)) + " & " + str(round(mycc1[8],2)) + " & " + str(round(mycc1[9],2)) + " \\\ " )
target.write("\n") 
target.write(sample2name + " & " + str(round(mycc2[0],2))+ " & " + str(round(mycc2[1],2)) + " & " + str(round(mycc2[2],2)) + " & " + str(round(mycc2[3],2)) + " & " + str(round(mycc2[4],2)) + " & " + str(round(mycc2[5],2)) + " & " + str(round(mycc2[6],2)) + " & " + str(round(mycc2[7],2)) + " & " + str(round(mycc2[8],2)) + " & " + str(round(mycc2[9],2)) + " \\\ " )
target.write("\n")
target.write(sample3name + " & " + str(round(mycc3[0],2))+ " & " + str(round(mycc3[1],2)) + " & " + str(round(mycc3[2],2)) + " & " + str(round(mycc3[3],2)) + " & " + str(round(mycc3[4],2)) + " & " + str(round(mycc3[5],2)) + " & " + str(round(mycc3[6],2)) + " & " + str(round(mycc3[7],2)) + " & " + str(round(mycc3[8],2)) +  "& " + str(round(mycc3[9],2)) + " \\\ " )
target.write("\n")
target.write(sample4name + " & " + str(round(mycc4[0],2))+ " & " + str(round(mycc4[1],2)) + " & " + str(round(mycc4[2],2)) + " & " + str(round(mycc4[3],2)) + " & " + str(round(mycc4[4],2)) + " & " + str(round(mycc4[5],2)) + " & " + str(round(mycc4[6],2)) + " & " + str(round(mycc4[7],2)) + " & " + str(round(mycc4[8],2)) + " & " + str(round(mycc4[9],2)) + " \\\ " )
target.write("\n")
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
target.write("\hline")
target.write("\n")
target.write("\end{tabular}")
target.write("\n")
target.write("\caption{ Cutflow of N Events After Cut / N Events Before Cut }")
target.write("\n")
target.write("\end{table}")
target.write("\end{document}")

target.close()
