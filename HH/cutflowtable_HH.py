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
    #c9histo = filename.Get(hists[10])
    #c10histo = filename.Get(hists[11])
    
    nevents = []
    #first = cthisto.Integral()
    #nevents.append(first/2.0)
    nevents.append(cthisto.Integral())
    nevents.append(c0histo.Integral())
    nevents.append(c1histo.Integral()) 
    nevents.append(c2histo.Integral()) 
    nevents.append(c3histo.Integral()) 
    nevents.append(c4histo.Integral()) 
    nevents.append(c5histo.Integral()) 
    nevents.append(c6histo.Integral()) 
    nevents.append(c7histo.Integral()) 
    nevents.append(c8histo.Integral())
    #nevents.append(c9histo.Integral())
    #nevents.append(c10histo.Integral())

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
    comparecutflow = [array[2]/array[0], array[3]/array[2], array[4]/array[3], array[5]/array[4], array[6]/array[5], array[7]/array[6], array[8]/array[7], array[9]/array[8]]
    
    return comparecutflow

#input files
WP600 = ROOT.TFile("plots_WP_600_HH.root")
WP650 = ROOT.TFile("plots_WP_650_HH.root")
WP700 = ROOT.TFile("plots_WP_700_HH.root")
WP750 = ROOT.TFile("plots_WP_750_HH.root")
WP800 = ROOT.TFile("plots_WP_800_HH.root")
WP900 = ROOT.TFile("plots_WP_900_HH.root")
WP1000 = ROOT.TFile("plots_WP_1000_HH.root")
WP1200 = ROOT.TFile("plots_WP_1200_HH.root")
WP1400 = ROOT.TFile("plots_WP_1400_HH.root")
WP1600 = ROOT.TFile("plots_WP_1600_HH.root")
WP1800 = ROOT.TFile("plots_WP_1800_HH.root")
WP2000 = ROOT.TFile("plots_WP_2000_HH.root")
WP2500 = ROOT.TFile("plots_WP_2500_HH.root")
WP3000 = ROOT.TFile("plots_WP_3000_HH.root")
WP4000 = ROOT.TFile("plots_WP_4000_HH.root")
WP4500 = ROOT.TFile("plots_WP_4500_HH.root")

ttbar = ROOT.TFile("plots_TT.root")
QCD300 = ROOT.TFile("plots_QCD300.root")
QCD500 = ROOT.TFile("plots_QCD500.root")
QCD700 = ROOT.TFile("plots_QCD700.root")
QCD1000 = ROOT.TFile("plots_QCD1000.root")
QCD1500 = ROOT.TFile("plots_QCD1500.root")
QCD2000 = ROOT.TFile("plots_QCD2000.root")

#sample names
sample1name = "WP 600"
sample2name = "WP 650"
sample3name = "WP 700"
sample4name = "WP 750"
sample5name = "WP 800"
sample6name = "WP 900"
sample7name = "WP 1000"
sample8name = "WP 1200"
sample9name = "WP 1400"
sample10name = "WP 1600"
sample11name = "WP 1800"
sample12name = "WP 2000"
sample13name = "WP 2500"
sample14name = "WP 3000"
sample15name = "WP 4000"
sample16name = "WP 4500"

sample17name = "ttbar"
sample18name = "QCD HT300-500"
sample19name = "QCD HT500-700"
sample20name = "QCD HT700-1000"
sample21name = "QCD HT1000-1500"
sample22name = "QCD HT1500-2000"
sample23name = "QCD HT2000-Inf"

#histograms for cutflow
#histograms = ["bbj","bb0","bb1","bb2","bb3","bb4","bb5","bb6","bb7","bb8","bb9","bb10"]
histograms = ["bbj","bb3","bb4","bb5","bb6","bb7","bb8","bb9","bb10","bb11"]

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
myn15 = []
myn16 = []
myn17 = []
myn18 = []
myn19 = []
myn20 = []
myn21 = []
myn22 = []
myn23 = []


#writing cutflow arrays
myn1 = getIntegral(WP600,histograms)
myn2 = getIntegral(WP650,histograms)
myn3 = getIntegral(WP700,histograms)
myn4 = getIntegral(WP750,histograms)
myn5 = getIntegral(WP800,histograms)
myn6 = getIntegral(WP900,histograms)
myn7 = getIntegral(WP1000,histograms)
myn8 = getIntegral(WP1200,histograms)
myn9 = getIntegral(WP1400,histograms)
myn10 = getIntegral(WP1600,histograms)
myn11 = getIntegral(WP1800,histograms)
myn12 = getIntegral(WP2000,histograms)
myn13 = getIntegral(WP2500,histograms)
myn14 = getIntegral(WP3000,histograms)
myn15 = getIntegral(WP4000,histograms)
myn16 = getIntegral(WP4500,histograms)
myn17 = getIntegral(ttbar,histograms)
myn18 = getIntegral(QCD300,histograms)
myn19 = getIntegral(QCD500,histograms)
myn20 = getIntegral(QCD700,histograms)
myn21 = getIntegral(QCD1000,histograms)
myn22 = getIntegral(QCD1500,histograms)
myn23 = getIntegral(QCD2000,histograms)

#writing normalized cutflow arrays
mync1 = getNormCutflow(myn1, 1, 9200, 98000)
mync2 = getNormCutflow(myn2, 1, 9200, 100000)
mync3 = getNormCutflow(myn3, 1, 9200, 100000)
mync4 = getNormCutflow(myn4, 1, 9200, 95600)
mync5 = getNormCutflow(myn5, 1, 9200, 95800)
mync6 = getNormCutflow(myn6, 1, 9200, 100000)
mync7 = getNormCutflow(myn7, 1, 9200, 50000)
mync8 = getNormCutflow(myn8, 1, 9200, 50000)
mync9 = getNormCutflow(myn9, 1, 9200, 50000)
mync10 = getNormCutflow(myn10, 1, 9200, 50000)
mync11 = getNormCutflow(myn11, 1, 9200, 50000)
mync12 = getNormCutflow(myn12, 1, 9200, 50000)
mync13 = getNormCutflow(myn13, 1, 9200, 48800)
mync14 = getNormCutflow(myn14, 1, 9200, 23600)
mync15 = getNormCutflow(myn15, 1, 9200, 50000)
mync16 = getNormCutflow(myn16, 1, 9200, 49600)
mync17 = getNormCutflow(myn17, 831.76, 9200, 32106228.)
mync18 = getNormCutflow(myn18, 347700., 9200, 16763036.)
mync19 = getNormCutflow(myn19, 32100., 9200, 19198108.)
mync20 = getNormCutflow(myn20, 6831., 9200, 15616919.)
mync21 = getNormCutflow(myn21, 1207., 9200, 4983341.)
mync22 = getNormCutflow(myn22, 119.9, 9200, 3753851.)
mync23 = getNormCutflow(myn23, 25.24, 9200, 1959483.)

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
mycc15 = getCompareCutflow(myn15)
mycc16 = getCompareCutflow(myn16)
mycc17 = getCompareCutflow(myn17)
#mycc18 = getCompareCutflow(myn18)
mycc19 = getCompareCutflow(myn19)
mycc20 = getCompareCutflow(myn20)
mycc21 = getCompareCutflow(myn21)
mycc22 = getCompareCutflow(myn22)
mycc23 = getCompareCutflow(myn23)

#writing tex file
target = open("cutflowtable_80X_H_WP.tex",'w')
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
target.write("\\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|}")
target.write("\n")
target.write("\hline")
target.write("\n")
target.write("Sample & All Events & 2 AK8 jets, $\Delta\eta$ & HT, vtype & jet$\eta$, jetID & jetpt & dijet mass & jet pruned mass & $\\tau_{21} < 0.6$ & bbtag $>0.6$ \\\ \hline")
target.write("\n")
target.write(sample1name + " & " + str(round(mync1[0],2)) + " & " + str(round(mync1[2],2)) + " & " + str(round(mync1[3],2)) + " & " + str(round(mync1[4],2)) + " & " + str(round(mync1[5],2)) + " & " + str(round(mync1[6],2)) + " & " + str(round(mync1[7],2)) + " & " + str(round(mync1[8],2)) + " & " + str(round(mync1[9],2)) + " \\\ " )
target.write("\n")
target.write(sample2name + " & " + str(round(mync2[0],2)) + " & " + str(round(mync2[2],2)) + " & " + str(round(mync2[3],2)) + " & " + str(round(mync2[4],2)) + " & " + str(round(mync2[5],2)) + " & " + str(round(mync2[6],2)) + " & " + str(round(mync2[7],2)) + " & " + str(round(mync2[8],2)) + " & " + str(round(mync2[9],2)) + " \\\ " )
target.write("\n")
target.write(sample3name + " & " + str(round(mync3[0],2)) + " & " + str(round(mync3[2],2)) + " & " + str(round(mync3[3],2)) + " & " + str(round(mync3[4],2)) + " & " + str(round(mync3[5],2)) + " & " + str(round(mync3[6],2)) + " & " + str(round(mync3[7],2)) + " & " + str(round(mync3[8],2)) + " & " + str(round(mync3[9],2)) + " \\\ " )
target.write("\n")
target.write(sample4name + " & " + str(round(mync4[0],2)) + " & " + str(round(mync4[2],2)) + " & " + str(round(mync4[3],2)) + " & " + str(round(mync4[4],2)) + " & " + str(round(mync4[5],2)) + " & " + str(round(mync4[6],2))+ " & " + str(round(mync4[7],2)) + " & " + str(round(mync4[8],2)) + " & " + str(round(mync4[9],2)) + " \\\ " )
target.write("\n")
target.write(sample5name + " & " + str(round(mync5[0],2)) + " & " + str(round(mync5[2],2)) + " & " + str(round(mync5[3],2)) + " & " + str(round(mync5[4],2)) + " & " + str(round(mync5[5],2)) + " & " + str(round(mync5[6],2)) + " & " + str(round(mync5[7],2)) + " & " + str(round(mync5[8],2)) + " & " + str(round(mync5[9],2)) + " \\\ " )
target.write("\n")
target.write(sample6name + " & " + str(round(mync6[0],2)) + " & " + str(round(mync6[2],2)) + " & " + str(round(mync6[3],2)) + " & " + str(round(mync6[4],2)) + " & " + str(round(mync6[5],2)) + " & " + str(round(mync6[6],2)) + " & " + str(round(mync6[7],2)) + " & " + str(round(mync6[8],2)) + " & " + str(round(mync6[9],2)) + " \\\ " )
target.write("\n")
target.write(sample7name + " & " + str(round(mync7[0],2)) + " & " + str(round(mync7[2],2)) + " & " + str(round(mync7[3],2)) + " & " + str(round(mync7[4],2)) + " & " + str(round(mync7[5],2)) + " & " + str(round(mync7[6],2)) + " & " + str(round(mync7[7],2)) + " & " + str(round(mync7[8],2)) + " & " + str(round(mync7[9],2)) + " \\\ " )
target.write("\n")
target.write(sample8name + " & " + str(round(mync8[0],2)) + " & " + str(round(mync8[2],2)) + " & " + str(round(mync8[3],2)) + " & " + str(round(mync8[4],2)) + " & " + str(round(mync8[5],2)) + " & " + str(round(mync8[6],2)) + " & " + str(round(mync8[7],2)) + " & " + str(round(mync8[8],2)) + " & " + str(round(mync8[9],2)) + " \\\ " )
target.write("\n")
target.write(sample9name + " & " + str(round(mync9[0],2)) + " & " + str(round(mync9[2],2)) + " & " + str(round(mync9[3],2)) + " & " + str(round(mync9[4],2)) + " & " + str(round(mync9[5],2)) + " & " + str(round(mync9[6],2)) + " & " + str(round(mync9[7],2)) + " & " + str(round(mync9[8],2)) + " & " + str(round(mync9[9],2)) + " \\\ " )
target.write("\n")
target.write(sample10name + " & " + str(round(mync10[0],2)) + " & " + str(round(mync10[2],2)) + " & " + str(round(mync10[3],2)) + " & " + str(round(mync10[4],2)) + " & " + str(round(mync10[5],2)) + " & " + str(round(mync10[6],2)) + " & " + str(round(mync10[7],2)) + " & " + str(round(mync10[8],2)) + " & " + str(round(mync10[9],2)) + " \\\ " )
target.write("\n")
target.write(sample11name + " & " + str(round(mync11[0],2)) + " & " + str(round(mync11[2],2)) + " & " + str(round(mync11[3],2)) + " & " + str(round(mync11[4],2)) + " & " + str(round(mync11[5],2)) + " & " + str(round(mync11[6],2)) + " & " + str(round(mync11[7],2)) + " & " + str(round(mync11[8],2)) + " & " + str(round(mync11[9],2)) + " \\\ " )
target.write("\n")
target.write(sample12name + " & " + str(round(mync12[0],2)) + " & " + str(round(mync12[2],2)) + " & " + str(round(mync12[3],2)) + " & " + str(round(mync12[4],2)) + " & " + str(round(mync12[5],2)) + " & " + str(round(mync12[6],2)) + " & " + str(round(mync12[7],2)) + " & " + str(round(mync12[8],2)) + " & " + str(round(mync12[9],2)) + " \\\ " )
target.write("\n")
target.write(sample13name + " & " + str(round(mync13[0],2)) + " & " + str(round(mync13[2],2)) + " & " + str(round(mync13[3],2)) + " & " + str(round(mync13[4],2)) + " & " + str(round(mync13[5],2)) + " & " + str(round(mync13[6],2)) + " & " + str(round(mync13[7],2)) + " & " + str(round(mync13[8],2)) + " & " + str(round(mync13[9],2)) + " \\\ " )
target.write("\n")
target.write(sample14name + " & " + str(round(mync14[0],2)) + " & " + str(round(mync14[2],2)) + " & " + str(round(mync14[3],2)) + " & " + str(round(mync14[4],2)) + " & " + str(round(mync14[5],2)) + " & " + str(round(mync14[6],2)) + " & " + str(round(mync14[7],2)) + " & " + str(round(mync14[8],2)) + " & " + str(round(mync14[9],2)) + " \\\ " )
target.write("\n")
target.write(sample15name + " & " + str(round(mync15[0],2)) + " & " + str(round(mync15[2],2)) + " & " + str(round(mync15[3],2)) + " & " + str(round(mync15[4],2)) + " & " + str(round(mync15[5],2)) + " & " + str(round(mync15[6],2)) + " & " + str(round(mync15[7],2)) + " & " + str(round(mync15[8],2)) + " & " + str(round(mync15[9],2)) + " \\\ " )
target.write("\n")
target.write(sample16name + " & " + str(round(mync16[0],2)) + " & " + str(round(mync16[2],2)) + " & " + str(round(mync16[3],2)) + " & " + str(round(mync16[4],2)) + " & " + str(round(mync16[5],2)) + " & " + str(round(mync16[6],2)) + " & " + str(round(mync16[7],2)) + " & " + str(round(mync16[8],2)) + " & " + str(round(mync16[9],2)) + " \\\ " )
target.write("\n")
target.write(sample17name + " & " + str(round(mync17[0],2)) + " & " + str(round(mync17[2],2)) + " & " + str(round(mync17[3],2)) + " & " + str(round(mync17[4],2)) + " & " + str(round(mync17[5],2)) + " & " + str(round(mync17[6],2)) + " & " + str(round(mync17[7],2)) + " & " + str(round(mync17[8],2)) + " & " + str(round(mync17[9],2)) + " \\\ " )
target.write("\n")
target.write(sample18name + " & " + str(round(mync18[0],2)) + " & " + str(round(mync18[2],2)) + " & " + str(round(mync18[3],2)) + " & " + str(round(mync18[4],2)) + " & " + str(round(mync18[5],2)) + " & " + str(round(mync18[6],2)) + " & " + str(round(mync18[7],2)) + " & " + str(round(mync18[8],2)) + " & " + str(round(mync18[9],2)) + " \\\ " )
target.write("\n")
target.write(sample19name + " & " + str(round(mync19[0],2)) + " & " + str(round(mync19[2],2)) + " & " + str(round(mync19[3],2)) + " & " + str(round(mync19[4],2)) + " & " + str(round(mync19[5],2)) + " & " + str(round(mync19[6],2)) + " & " + str(round(mync19[7],2)) + " & " + str(round(mync19[8],2)) + " & " + str(round(mync19[9],2)) + " \\\ " )
target.write("\n")
target.write(sample20name + " & " + str(round(mync20[0],2)) + " & " + str(round(mync20[2],2)) + " & " + str(round(mync20[3],2)) + " & " + str(round(mync20[4],2)) + " & " + str(round(mync20[5],2)) + " & " + str(round(mync20[6],2)) + " & " + str(round(mync20[7],2)) + " & " + str(round(mync20[8],2)) + " & " + str(round(mync20[9],2)) + " \\\ " )
target.write("\n")
target.write(sample21name + " & " + str(round(mync21[0],2)) + " & " + str(round(mync21[2],2)) + " & " + str(round(mync21[3],2)) + " & " + str(round(mync21[4],2)) + " & " + str(round(mync21[5],2)) + " & " + str(round(mync21[6],2)) + " & " + str(round(mync21[7],2)) + " & " + str(round(mync21[8],2)) + " & " + str(round(mync21[9],2)) + " \\\ " )
target.write("\n")
target.write(sample22name + " & " + str(round(mync22[0],2)) + " & " + str(round(mync22[2],2)) + " & " + str(round(mync22[3],2)) + " & " + str(round(mync22[4],2)) + " & " + str(round(mync22[5],2)) + " & " + str(round(mync22[6],2)) + " & " + str(round(mync22[7],2)) + " & " + str(round(mync22[8],2)) + " & " + str(round(mync22[9],2)) + " \\\ " )
target.write("\n")
target.write(sample23name + " & " + str(round(mync23[0],2)) + " & " + str(round(mync23[2],2)) + " & " + str(round(mync23[3],2)) + " & " + str(round(mync23[4],2)) + " & " + str(round(mync23[5],2)) + " & " + str(round(mync23[6],2)) + " & " + str(round(mync23[7],2)) + " & " + str(round(mync23[8],2)) + " & " + str(round(mync23[9],2)) + " \\\ " )
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
target.write("\\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|}")
target.write("\n")
target.write("\hline")
target.write("\n")
target.write("Sample & 2 AK8 jets, $\Delta\eta$ & HT, vtype & jet$\eta$, jetID & jetpt & dijet mass & jet pruned mass & $\\tau_{21} < 0.6$ & bbtag $>0.6$ \\\ \hline")
target.write("\n")
target.write(sample1name + " & " + str(round(mycc1[0],2))+ " & " + str(round(mycc1[1],2)) + " & " + str(round(mycc1[2],2)) + " & " + str(round(mycc1[3],2)) + " & " + str(round(mycc1[4],2)) + " & " + str(round(mycc1[5],2)) + " & " + str(round(mycc1[6],2)) + " & " + str(round(mycc1[7],2)) + " \\\ " )
target.write("\n") 
target.write(sample2name + " & " + str(round(mycc2[0],2))+ " & " + str(round(mycc2[1],2)) + " & " + str(round(mycc2[2],2)) + " & " + str(round(mycc2[3],2)) + " & " + str(round(mycc2[4],2)) + " & " + str(round(mycc2[5],2)) + " & " + str(round(mycc2[6],2)) + " & " + str(round(mycc2[7],2)) + " \\\ " )
target.write("\n")
target.write(sample3name + " & " + str(round(mycc3[0],2))+ " & " + str(round(mycc3[1],2)) + " & " + str(round(mycc3[2],2)) + " & " + str(round(mycc3[3],2)) + " & " + str(round(mycc3[4],2)) + " & " + str(round(mycc3[5],2)) + " & " + str(round(mycc3[6],2)) + " & " + str(round(mycc3[7],2)) + " \\\ " )
target.write("\n")
target.write(sample4name + " & " + str(round(mycc4[0],2))+ " & " + str(round(mycc4[1],2)) + " & " + str(round(mycc4[2],2)) + " & " + str(round(mycc4[3],2)) + " & " + str(round(mycc4[4],2)) + " & " + str(round(mycc4[5],2)) + " & " + str(round(mycc4[6],2)) + " & " + str(round(mycc4[7],2)) + " \\\ " )
target.write("\n")
target.write(sample5name + " & " + str(round(mycc5[0],2))+ " & " + str(round(mycc5[1],2)) + " & " + str(round(mycc5[2],2)) + " & " + str(round(mycc5[3],2)) + " & " + str(round(mycc5[4],2)) + " & " + str(round(mycc5[5],2)) + " & " + str(round(mycc5[6],2)) + " & " + str(round(mycc5[7],2)) + " \\\ " )
target.write("\n")
target.write(sample6name + " & " + str(round(mycc6[0],2))+ " & " + str(round(mycc6[1],2)) + " & " + str(round(mycc6[2],2)) + " & " + str(round(mycc6[3],2)) + " & " + str(round(mycc6[4],2)) + " & " + str(round(mycc6[5],2)) + " & " + str(round(mycc6[6],2)) + " & " + str(round(mycc6[7],2)) + " \\\ " )
target.write("\n")
target.write(sample7name + " & " + str(round(mycc7[0],2))+ " & " + str(round(mycc7[1],2)) + " & " + str(round(mycc7[2],2)) + " & " + str(round(mycc7[3],2)) + " & " + str(round(mycc7[4],2)) + " & " + str(round(mycc7[5],2)) + " & " + str(round(mycc7[6],2)) + " & " + str(round(mycc7[7],2)) + " \\\ ")
target.write("\n")
target.write(sample8name + " & " + str(round(mycc8[0],2))+ " & " + str(round(mycc8[1],2)) + " & " + str(round(mycc8[2],2)) + " & " + str(round(mycc8[3],2)) + " & " + str(round(mycc8[4],2)) + " & " + str(round(mycc8[5],2)) + " & " + str(round(mycc8[6],2)) + " & " + str(round(mycc8[7],2)) + " \\\ " )
target.write("\n")
target.write(sample9name + " & " + str(round(mycc9[0],2))+ " & " + str(round(mycc9[1],2)) + " & " + str(round(mycc9[2],2)) + " & " + str(round(mycc9[3],2)) + " & " + str(round(mycc9[4],2)) + " & " + str(round(mycc9[5],2)) + " & " + str(round(mycc9[6],2)) + " & " + str(round(mycc9[7],2)) + " \\\ " )
target.write("\n")
target.write(sample10name + " & " + str(round(mycc10[0],2))+ " & " + str(round(mycc10[1],2)) + " & " + str(round(mycc10[2],2)) + " & " + str(round(mycc10[3],2)) + " & " + str(round(mycc10[4],2)) + " & " + str(round(mycc10[5],2)) + " & " + str(round(mycc10[6],2)) + " & " + str(round(mycc10[7],2)) + " \\\ " )
target.write("\n")
target.write(sample11name + " & " + str(round(mycc11[0],2))+ " & " + str(round(mycc11[1],2)) + " & " + str(round(mycc11[2],2)) + " & " + str(round(mycc11[3],2)) + " & " + str(round(mycc11[4],2)) + " & " + str(round(mycc11[5],2)) + " & " + str(round(mycc11[6],2)) + " & " + str(round(mycc11[7],2)) + " \\\ " )
target.write("\n")
target.write(sample12name + " & " + str(round(mycc12[0],2))+ " & " + str(round(mycc12[1],2)) + " & " + str(round(mycc12[2],2)) + " & " + str(round(mycc12[3],2)) + " & " + str(round(mycc12[4],2)) + " & " + str(round(mycc12[5],2)) + " & " + str(round(mycc12[6],2)) + " & " + str(round(mycc12[7],2)) + " \\\ " )
target.write("\n")
target.write(sample13name + " & " + str(round(mycc13[0],2))+ " & " + str(round(mycc13[1],2)) + " & " + str(round(mycc13[2],2)) + " & " + str(round(mycc13[3],2)) + " & " + str(round(mycc13[4],2)) + " & " + str(round(mycc13[5],2)) + " & " + str(round(mycc13[6],2)) + " & " + str(round(mycc13[7],2)) + " \\\ " )
target.write("\n")
target.write(sample14name + " & " + str(round(mycc14[0],2))+ " & " + str(round(mycc14[1],2)) + " & " + str(round(mycc14[2],2)) + " & " + str(round(mycc14[3],2)) + " & " + str(round(mycc14[4],2)) + " & " + str(round(mycc14[5],2)) + " & " + str(round(mycc14[6],2)) + " & " + str(round(mycc14[7],2)) + " \\\ " )
target.write("\n")
target.write(sample15name + " & " + str(round(mycc15[0],2))+ " & " + str(round(mycc15[1],2)) + " & " + str(round(mycc15[2],2)) + " & " + str(round(mycc15[3],2)) + " & " + str(round(mycc15[4],2)) + " & " + str(round(mycc15[5],2)) + " & " + str(round(mycc15[6],2)) + " & " + str(round(mycc15[7],2)) + " \\\ " )
target.write("\n")
target.write(sample16name + " & " + str(round(mycc16[0],2))+ " & " + str(round(mycc16[1],2)) + " & " + str(round(mycc16[2],2)) + " & " + str(round(mycc16[3],2)) + " & " + str(round(mycc16[4],2)) + " & " + str(round(mycc16[5],2)) + " & " + str(round(mycc16[6],2)) + " & " + str(round(mycc16[7],2)) + " \\\ " )
target.write("\n")
target.write(sample17name + " & " + str(round(mycc17[0],2))+ " & " + str(round(mycc17[1],2)) + " & " + str(round(mycc17[2],2)) + " & " + str(round(mycc17[3],2)) + " & " + str(round(mycc17[4],2)) + " & " + str(round(mycc17[5],2)) + " & " + str(round(mycc17[6],2)) + " & " + str(round(mycc17[7],2)) + " \\\ " )
#target.write("\n")
#target.write(sample18name + " & " + str(round(mycc18[0],2))+ " & " + str(round(mycc18[1],2)) + " & " + str(round(mycc18[2],2)) + " & " + str(round(mycc18[3],2)) + " & " + str(round(mycc18[4],2)) + " & " + str(round(mycc18[5],2)) + " & " + str(round(mycc18[6],2)) + " & " + str(round(mycc18[7],2)) + " \\\ " )
target.write("\n")
target.write(sample19name + " & " + str(round(mycc19[0],2))+ " & " + str(round(mycc19[1],2)) + " & " + str(round(mycc19[2],2)) + " & " + str(round(mycc19[3],2)) + " & " + str(round(mycc19[4],2)) + " & " + str(round(mycc19[5],2)) + " & " + str(round(mycc19[6],2)) + " & " + str(round(mycc19[7],2)) + " \\\ " )
target.write("\n")
target.write(sample20name + " & " + str(round(mycc20[0],2))+ " & " + str(round(mycc20[1],2)) + " & " + str(round(mycc20[2],2)) + " & " + str(round(mycc20[3],2)) + " & " + str(round(mycc20[4],2)) + " & " + str(round(mycc20[5],2)) + " & " + str(round(mycc20[6],2)) + " & " + str(round(mycc20[7],2)) + " \\\ " )
target.write("\n")
target.write(sample21name + " & " + str(round(mycc21[0],2))+ " & " + str(round(mycc21[1],2)) + " & " + str(round(mycc21[2],2)) + " & " + str(round(mycc21[3],2)) + " & " + str(round(mycc21[4],2)) + " & " + str(round(mycc21[5],2)) + " & " + str(round(mycc21[6],2)) + " & " + str(round(mycc21[7],2)) + " \\\ " )
target.write("\n")
target.write(sample22name + " & " + str(round(mycc22[0],2))+ " & " + str(round(mycc22[1],2)) + " & " + str(round(mycc22[2],2)) + " & " + str(round(mycc22[3],2)) + " & " + str(round(mycc22[4],2)) + " & " + str(round(mycc22[5],2)) + " & " + str(round(mycc22[6],2)) + " & " + str(round(mycc22[7],2)) + " \\\ " )
target.write("\n")
target.write(sample23name + " & " + str(round(mycc23[0],2))+ " & " + str(round(mycc23[1],2)) + " & " + str(round(mycc23[2],2)) + " & " + str(round(mycc23[3],2)) + " & " + str(round(mycc23[4],2)) + " & " + str(round(mycc23[5],2)) + " & " + str(round(mycc23[6],2)) + " & " + str(round(mycc23[7],2)) + " \\\ " )
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
