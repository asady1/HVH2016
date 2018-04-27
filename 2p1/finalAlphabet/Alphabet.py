# Class def for full Alphabetization.
# Does everything except the pretty plots, but makes all components available.

import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy

# Our functions:
import Alphabet_Header
from Alphabet_Header import *
import Plotting_Header
from Plotting_Header import *
import Converters
from Converters import *
import Distribution_Header
from Distribution_Header import *

class Alphabetizer:
    def __init__(self, name, Dist_Plus, Dist_Minus):
	self.name = name
	self.DP = Dist_Plus
	self.DM = Dist_Minus
    def SetRegions(self, var_array, presel):
	# var_array = [x var, y var, x n bins, x min, x max, y n bins, y min, y max]
	self.X = var_array[0]
	self.Pplots = TH2F("added"+self.name, "", var_array[2],var_array[3],var_array[4],var_array[5],var_array[6],var_array[7])
	self.Mplots = TH2F("subbed"+self.name, "", var_array[2],var_array[3],var_array[4],var_array[5],var_array[6],var_array[7])
	for i in self.DP:
		 quick2dplot(i.File, i.Tree, self.Pplots, var_array[0], var_array[1], presel, i.weight)
                 print "DEBUG: weight: " + str(i.weight)
	for j in self.DM:
		 quick2dplot(j.File, j.Tree, self.Mplots, var_array[0], var_array[1], presel, j.weight)
                 print "DEBUG: weight: " + str(j.weight)
	self.TwoDPlot = self.Pplots.Clone("TwoDPlot_"+self.name)
	self.TwoDPlot.Add(self.Mplots, -1.)
    def GetRates(self, cut, bins, truthbins, center, FIT):
	self.center = center
	self.G = AlphabetSlicer(self.TwoDPlot, bins, cut[0], cut[1], center) # makes the A/B slices
	if len(truthbins)>0:
	    self.truthG = AlphabetSlicer(self.TwoDPlot, truthbins, cut[0], cut[1], center) # makes the A/B slices
	else:
	    self.truthG = None
	self.Fit = FIT # reads the right class in, should be initialized and set up already
	AlphabetFitter(self.G, self.Fit) # creates all three distributions (nominal, up, down)
    def MakeEst(self, var_array, antitag, tag):
	# makes an estimate in a region, based on an anti-tag region, of that variable in all dists
	self.Fit.MakeConvFactor(self.X, self.center)
	self.hists_EST = []
	self.hists_EST_SUB = []
	self.hists_EST_UP = []
	self.hists_EST_SUB_UP = []
	self.hists_EST_DN = []
	self.hists_EST_SUB_DN = []
	self.hists_MSR = []
	self.hists_MSR_SUB = []
	for i in self.DP:
		temphist = TH1F("Hist_VAL"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
		temphistN = TH1F("Hist_NOMINAL"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
		temphistU = TH1F("Hist_UP"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
		temphistD = TH1F("Hist_DOWN"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
		quickplot(i.File, i.Tree, temphist, var_array[0], tag, i.weight)
		quickplot(i.File, i.Tree, temphistN, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFact+")")
		quickplot(i.File, i.Tree, temphistU, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFactUp+")")
		quickplot(i.File, i.Tree, temphistD, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFactDn+")")
		self.hists_MSR.append(temphist)
		self.hists_EST.append(temphistN)
		self.hists_EST_UP.append(temphistU)
		self.hists_EST_DN.append(temphistD)
	for i in self.DM:
		temphist = TH1F("Hist_SUB_VAL"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
		temphistN = TH1F("Hist_SUB_NOMINAL"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
		temphistU = TH1F("Hist_SUB_UP"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
		temphistD = TH1F("Hist_SUB_DOWN"+self.name+"_"+i.name, "", var_array[1], var_array[2], var_array[3])
		quickplot(i.File, i.Tree, temphist, var_array[0], tag, i.weight)
		quickplot(i.File, i.Tree, temphistN, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFact+")")
		quickplot(i.File, i.Tree, temphistU, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFactUp+")")
		quickplot(i.File, i.Tree, temphistD, var_array[0], antitag, "("+i.weight+"*"+self.Fit.ConvFactDn+")")
		self.hists_MSR_SUB.append(temphist)
		self.hists_EST_SUB.append(temphistN)
		self.hists_EST_SUB_UP.append(temphistU)
		self.hists_EST_SUB_DN.append(temphistD)
    def MakeEstVariable(self, variable, binBoundaries, antitag, tag):
        # makes an estimate in a region, based on an anti-tag region, of that variable in all dists
	self.Fit.MakeConvFactor(self.X, self.center)
	self.hists_EST = []
	self.hists_EST_SUB = []
	self.hists_EST_UP = []
	self.hists_EST_SUB_UP = []
	self.hists_EST_DN = []
	self.hists_EST_SUB_DN = []
	self.hists_MSR = []
	self.hists_MSR_SUB = []
	self.hists_ATAG = []
	for i in self.DP:
		print "in self.DP"
                temphist = TH1F("Hist_VAL"+self.name+"_"+i.name, "", len(binBoundaries)-1, array('d',binBoundaries))
                temphistN = TH1F("Hist_NOMINAL"+self.name+"_"+i.name, "", len(binBoundaries)-1, array('d',binBoundaries))
                temphistU = TH1F("Hist_UP"+self.name+"_"+i.name, "", len(binBoundaries)-1, array('d',binBoundaries))
                temphistD = TH1F("Hist_DOWN"+self.name+"_"+i.name, "", len(binBoundaries)-1, array('d',binBoundaries))
                temphistA = TH1F("Hist_ATAG"+self.name+"_"+i.name, "", len(binBoundaries)-1, array('d',binBoundaries))
                quickplot(i.File, i.Tree, temphist, variable, tag, i.weight)
                quickplot(i.File, i.Tree, temphistN, variable, antitag, "("+i.weight+"*"+self.Fit.ConvFact+")")
		print "temphistN info"
		temphistN.Print("all")
		print "Weight:"
		print i.weight
		print "ConvFact:"
		print self.Fit.ConvFact
                quickplot(i.File, i.Tree, temphistU, variable, antitag, "("+i.weight+"*"+self.Fit.ConvFactUp+")")
                print "temphistU info"
                temphistU.Print("all")
                print "Weight:"
                print i.weight
                print "ConvFact:"
                print self.Fit.ConvFact
                quickplot(i.File, i.Tree, temphistD, variable, antitag, "("+i.weight+"*"+self.Fit.ConvFactDn+")")
                print "temphistD info"
                temphistD.Print("all")
                print "Weight:"
                print i.weight
                print "ConvFact:"
                print self.Fit.ConvFact
                quickplot(i.File, i.Tree, temphistA, variable, antitag, i.weight)
                self.hists_MSR.append(temphist)
                self.hists_EST.append(temphistN)
                self.hists_EST_UP.append(temphistU)
                self.hists_EST_DN.append(temphistD)
                self.hists_ATAG.append(temphistA)
	for i in self.DM:
                print "in self.DM"
                temphist = TH1F("Hist_SUB_VAL"+self.name+"_"+i.name, "", len(binBoundaries)-1, array('d',binBoundaries))
                temphistN = TH1F("Hist_SUB_NOMINAL"+self.name+"_"+i.name, "", len(binBoundaries)-1, array('d',binBoundaries))
                temphistU = TH1F("Hist_SUB_UP"+self.name+"_"+i.name, "",len(binBoundaries)-1, array('d',binBoundaries))
                temphistD = TH1F("Hist_SUB_DOWN"+self.name+"_"+i.name, "", len(binBoundaries)-1, array('d',binBoundaries))
                quickplot(i.File, i.Tree, temphist, variable, tag, i.weight)
                quickplot(i.File, i.Tree, temphistN, variable, antitag, "("+i.weight+"*"+self.Fit.ConvFact+")")
                print "temphistN info"
                temphistN.Print("all")
                print "Weight:"
                print i.weight
                print "ConvFact:"
                print self.Fit.ConvFact
                quickplot(i.File, i.Tree, temphistU, variable, antitag, "("+i.weight+"*"+self.Fit.ConvFactUp+")")
                quickplot(i.File, i.Tree, temphistD, variable, antitag, "("+i.weight+"*"+self.Fit.ConvFactDn+")")
                self.hists_MSR_SUB.append(temphist)
                self.hists_EST_SUB.append(temphistN)
                self.hists_EST_SUB_UP.append(temphistU)
                self.hists_EST_SUB_DN.append(temphistD)





