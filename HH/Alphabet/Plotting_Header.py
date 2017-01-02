#
import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy

#import Alphabet_Header
#from Alphabet_Header import *
#import Alphabet
#from Alphabet import *

def quickplot(File, tree, plot, var, Cut, Weight): # Fills  a plot from a file (needs to have a TTree called "tree"...)
        temp = plot.Clone("temp") # Allows to add multiple distributions to the plot
        chain = ROOT.TChain(tree)
        chain.Add(File)
        chain.Draw(var+">>"+"temp", "("+Weight+")*("+Cut+")", "goff") # Actual plotting (and making of the cut + Weighing if necsr)
	print "quickplot draw:"
	print  chain.Draw(var+">>"+"temp", "("+Weight+")*("+Cut+")", "goff")
	print "Weight:"
	print Weight
	print "Cut:"
	print Cut
        plot.Add(temp)

def quick2dplot(File, tree, plot, var, var2, Cut, Weight): # Same as above, but 2D plotter
        temp = plot.Clone("temp")
        chain = ROOT.TChain(tree)
        chain.Add(File)
        chain.Draw(var2+":"+var+">>"+"temp", "("+Weight+")*("+Cut+")", "goff")
	plot.GetYaxis().SetTitleOffset(1.45)
        plot.Add(temp)

def quickprofiles(name, plot):
	X = plot.ProfileX(name+"_X")
	Y = plot.ProfileY(name+"_Y")
	X.SetLineWidth(2)
	Y.SetLineWidth(2)
	X.SetLineColor(kRed)
	Y.SetLineColor(kGreen)
	return [X,Y]

def FindAndSetMax(someset):
        maximum = 0.0
        for i in someset:
                i.SetStats(0)
                t = i.GetMaximum()
                if t > maximum:
                        maximum = t
        for j in someset:
                j.GetYaxis().SetRangeUser(0,maximum*1.35)

