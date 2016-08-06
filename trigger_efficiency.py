from ROOT import *
gStyle.SetOptStat(0)
import os
from math import *

import ROOT
import sys

f="tree_data_VH_plots.root"

trigEf = ROOT.TH1F("trigEf", "", 500, 0., 10000.)

fin = ROOT.TFile.Open(f, "READ")

h = fin.Get("c0")
h1 = fin.Get("c1")
h.Sumw2()
h1.Sumw2()

trigEf.Add(h1)
trigEf.Divide(h)
#trigEf.Rebin(20)
trigEf.GetXaxis().SetRangeUser(800.,3000.)
#trigEf.Rebin(20)
trigEf.GetXaxis().SetTitle("m(Vh) (GeV)")
trigEf.GetYaxis().SetTitle("Efficiency")
trigEf.SetMarkerStyle(7)
trigEf.SetMarkerColor( ROOT.kBlue )
c = ROOT.TCanvas('c1')
trigEf.Draw("EP")
c1.Print('trigEf.pdf')


fin.Close()


#fout = ROOT.TFile("trig_eff_plot.root", "RECREATE")
#fout.cd()
#trigEf.Write()
#fout.Close()

