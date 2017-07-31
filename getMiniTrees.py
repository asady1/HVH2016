import os
import glob
import math
import ROOT
import pdb

from ROOT import *

#ROOT.gROOT.Macro("rootlogon.C")

import FWCore.ParameterSet.Config as cms
import miniTreeFunctions
from miniTreeFunctions import *

import miniTreeProducer
from miniTreeProducer import *

import sys
from DataFormats.FWLite import Events, Handle

from array import *

#ROOT.gSystem.Load('libCondFormatsBTagObjects') 
#command line options 
from optparse import OptionParser
parser = OptionParser()

parser.add_option("-f", "--pathIn", dest="inputFile",
                  help="inputFile path")

parser.add_option("-o", "--outName", dest="outName",
                  help="output file name")

parser.add_option("-i", "--min", dest="min", 
		  help="input index low end")

parser.add_option("-j", "--max", dest="max", 
		  help="input index high end")

parser.add_option("-l", "--file", dest="txt", 
		  help="input txt file")

parser.add_option("-m", "--isMC", dest="isMC", 
		  help="bool for is MC")

parser.add_option("-y", "--saveTrig", dest="saveTrig",
                  help="bool to not save triggers for background")

parser.add_option("-x", "--xsec", dest="xsec", 
		  help="cross section")

parser.add_option("-S", "--syst", dest="syst",
                  help="Systematic")


(options, args) = parser.parse_args()

inputfile = options.txt 

ff_n = 1000

num1 = int(options.min)
num2 = int(options.max)

d1 = options.outName 
d2 = '_'
print(options.outName)
outputfilename = d1 + d2 + options.min + '.root'

print outputfilename

import copy
#important files and histograms
File_tr=ROOT.TFile.Open("trigger_objects.root", "R")
histo_efficiency=copy.copy(File_tr.Get("histo_efficiency"))
histo_efficiency_up=copy.copy(File_tr.Get("histo_efficiency_upper"))
histo_efficiency_down=copy.copy(File_tr.Get("histo_efficiency_lower"))
histo_efficiency_2up=copy.copy(File_tr.Get("histo_efficiency_upper_2sigma"))
histo_efficiency_2down=copy.copy(File_tr.Get("histo_efficiency_lower_2sigma"))
File_tr.Close()

PuppiWeightFile = ROOT.TFile.Open("puppiCorr.root","R")
puppisd_corrGEN      = PuppiWeightFile.Get("puppiJECcorr_gen")
puppisd_corrRECO_cen = PuppiWeightFile.Get("puppiJECcorr_reco_0eta1v3")
puppisd_corrRECO_for = PuppiWeightFile.Get("puppiJECcorr_reco_1v3eta2v5")
PuppiWeightFile.Close()


print sys.argv[1]

f =  ROOT.TFile(outputfilename, 'recreate')

f.cd()

myTree =  ROOT.TTree('myTree', 'myTree')
#running miniTree Producer
test = miniTreeProducer(options.isMC, options.saveTrig, options.syst, myTree, options.xsec)
test.runProducer(options.inputFile, inputfile, num1, num2,histo_efficiency, histo_efficiency_up, histo_efficiency_down, histo_efficiency_2up, histo_efficiency_2down, puppisd_corrGEN, puppisd_corrRECO_cen, puppisd_corrRECO_for)

f.cd()
f.Write()
f.Close()



