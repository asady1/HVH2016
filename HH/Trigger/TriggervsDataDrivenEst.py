from ROOT import *
gStyle.SetOptStat(0)
import os
from math import *

import ROOT
import sys

f="plots_BulkGrav_M-1000_0.root"
DataFile="JetHT_TurnOnPlot_SR.root"

trigEf = ROOT.TH1F("trigEf", "", 80, 800., 3000.)
DataEf = ROOT.TH1F("DataEf", "", 80, 800., 3000.)
DataDrivenEf = ROOT.TH1F("DataDrivenEf", "", 80, 800., 3000.)
Pull = ROOT.TH1F("Pull", "", 80, 800., 3000.)
legend = ROOT.TLegend(0.55,0.65,0.9,0.8)
text = ROOT.TPaveText(0.55,0.8,0.9,0.9,"NDC")
text.AddText("Jet p_{T} > 200    #||{#eta} < 2.4")
text.AddText("#||{#Delta#eta} < 1.3       pruned mass > 50")

fin = ROOT.TFile.Open(f, "READ")

h1 = fin.Get("h1")
h1.Sumw2()
h2 = fin.Get("h0")
h2.Sumw2()

trigEf.Add(h1)
trigEf.GetXaxis().SetRangeUser(800.,1400.)
trigEf.GetXaxis().SetTitle("Dijet Mass (GeV)")
trigEf.GetYaxis().SetTitle("Events")
trigEf.GetYaxis().SetTitleOffset(1.4)
trigEf.SetMarkerStyle(7)
trigEf.SetMarkerColor( ROOT.kBlue )
trigEf.SetTitle("BulkGrav_M-1000")
trigEf.SetFillColor( ROOT.kBlue - 7)


fin2 = ROOT.TFile.Open(DataFile, "READ")

h1_Data = fin2.Get("h1")
h2_Data = fin2.Get("h0")
h1_Data.Sumw2()
h2_Data.Sumw2()

DataEf.Add(h1_Data)
DataEf.Divide(h2_Data)

text.SetFillStyle(0)
text.SetBorderSize(0)
text.SetTextSize(0.03)
text.SetTextFont(42)

for i in range(1,81):
    weight = DataEf.GetBinContent(i)
    MCevents = h2.GetBinContent(i)
    DataDrivenEf.SetBinContent(i,weight*MCevents)

DataDrivenEf.SetMarkerStyle(7)
DataDrivenEf.SetMarkerColor(ROOT.kRed)
DataDrivenEf.SetLineColor(ROOT.kRed)
DataDrivenEf.SetFillColor(ROOT.kRed - 6)
DataDrivenEf.SetAxisRange(800.,1400.)

legend.AddEntry(trigEf,"PFHT800 Trigger")
legend.AddEntry(DataDrivenEf,"Data-Driven Estimate")
legend.SetBorderSize(0)
legend.SetFillStyle(0)

c = ROOT.TCanvas('c1',"",800,800)
plot = ROOT.TPad("pad1", "The pad 80% of the height",0,0.15,1,1)
pull = ROOT.TPad("pad2", "The pad 20% of the height",0,0,1.0,0.15)
plot.Draw()
pull.Draw()
plot.cd()

trigEf.Draw("E BAR")
legend.Draw("same")
DataDrivenEf.Draw("E BAR SAME")

pull.cd()
Pull.Add(trigEf)
Pull.Divide(DataDrivenEf)
Pull.SetLineColor(1)
Pull.SetFillColor(0)
Pull.SetMarkerColor(1)
Pull.SetMarkerStyle(20)
Pull.SetMarkerSize(0.5)
Pull.GetXaxis().SetTitle("")
Pull.GetXaxis().SetNdivisions(0)
Pull.GetYaxis().SetNdivisions(5)
Pull.GetYaxis().SetTitle("#frac{Trigger Bit}{Data Est.}")
Pull.GetYaxis().SetLabelSize(85/15*Pull.GetYaxis().GetLabelSize())
Pull.GetYaxis().SetTitleSize(4.2*Pull.GetYaxis().GetTitleSize())
Pull.GetYaxis().SetTitleOffset(0.225)
Pull.GetXaxis().SetRangeUser(800.,1400.)
Pull.GetYaxis().SetRangeUser(-1.,4.)

T1 = ROOT.TLine(800.,1.,1400.,1.)
T1.SetLineColor(kBlue)
T1.SetLineStyle(3)

Pull.Draw("EP")
#T1.Draw("same")

c1.Print('trigEf_BulkGrav_M-1000_TriggervsDataDriven.pdf')


fin2.Close()
fin.Close()


