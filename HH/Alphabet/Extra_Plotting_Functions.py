import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy

import Alphabet_Header
from Alphabet_Header import *
import Plotting_Header
from Plotting_Header import *
import Converters
from Converters import *
import Distribution_Header
from Distribution_Header import *
import Alphabet
from Alphabet import *

def GetQuantileProfiles(Th2f, cut, name):
        q1 = []
        nxbins = Th2f.GetXaxis().GetNbins();
        xlo = Th2f.GetXaxis().GetBinLowEdge(1);
        xhi = Th2f.GetXaxis().GetBinUpEdge(Th2f.GetXaxis().GetNbins() );
        for i in range(nxbins):
                H = Th2f.ProjectionY("ProjY"+str(i),i+1,i+1)
                probSum = array('d', [cut])
                q = array('d', [0.0]*len(probSum))
                H.GetQuantiles(len(probSum), q, probSum)
                q1.append(q[0])
        H1 = TH1F(name, "", nxbins,xlo,xhi)
        for i in range(nxbins):
                H1.SetBinContent(i+1,q1[i])
        return H1

def CorrPlotter(name, Input, V0, V1, Cuts):
        print "making correlation plot ..."
        Vars = [V0[0], V1[0], V0[1],V0[2],V0[3], V1[1], V1[2],V1[3]]
        A = Alphabet.Alphabetizer("A_"+V1[0]+V1[0], Input, [])
        A.SetRegions(Vars, Cuts)
        A.TwoDPlot.SetStats(0)
        A.TwoDPlot.GetYaxis().SetTitle(V1[4])
        A.TwoDPlot.GetXaxis().SetTitle(V0[4])
        ProfsM = []
        for i in [8,6,4,2]:
                ProfsM.append(GetQuantileProfiles(A.TwoDPlot, 0.1*i, name+V1[0]+
V0[0]+str(i)))
        return [A.TwoDPlot, ProfsM]

