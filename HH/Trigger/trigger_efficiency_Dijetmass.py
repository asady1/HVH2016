from ROOT import *
gStyle.SetOptStat(0)
import os
from math import *

import ROOT
import sys

f="JetHT_TriggerComparisons_BigBins_AllTriggers.root"

trigEf_PFHT800orWidejet = ROOT.TH1F("trigEf_PFHT800 or widejet", "", 300, 0., 3000.)
trigEf_PFHT800 = ROOT.TH1F("trigEf_PFHT800", "", 300, 0., 3000.)
trigEf_PFHT800orWidejetorDijet250 = ROOT.TH1F("trigEf_PFHT800 or widejet or dijet250", "", 300, 0., 3000.)
trigEf_PFHT800orWidejetorDijet280 = ROOT.TH1F("trigEf_PFHT800 or widejet or dijet280", "", 300, 0., 3000.)

legend = ROOT.TLegend(0.1,0.15,0.88,0.55)
text = ROOT.TPaveText(0.55,0.5,0.9,0.65,"NDC")
text.AddText("PFJet260   #||{#eta} < 2.4")
text.AddText("#||{#Delta#eta} < 1.3  jet pt > 200")
text.AddText("jet mass > 50")

fin = ROOT.TFile.Open(f, "READ")

h = fin.Get("h0")
h1 = fin.Get("h25")
h8 = fin.Get("h8")
#h.Sumw2()
#h1.Sumw2()
trigEf_PFHT800.Sumw2()
#trigEf_PFHT800.Divide(h1,h,1,1,"B")
#trigEf.Rebin(20)
trigEf_PFHT800.GetXaxis().SetRangeUser(800.,2000.)
#trigEf.Rebin(20)
trigEf_PFHT800.GetXaxis().SetTitle("Dijet Mass (GeV)")
trigEf_PFHT800.GetYaxis().SetTitle("Efficiency")
trigEf_PFHT800.SetMarkerStyle(7)
trigEf_PFHT800.SetMarkerColor( ROOT.kBlue )

#h2 = fin.Get("h28")
#h2.Sumw2()
trigEf_PFHT800orWidejet.Sumw2()
#trigEf_PFHT800orWidejet.Divide(h2,h,1,1,"B")
trigEf_PFHT800orWidejet.SetMarkerStyle(7)
trigEf_PFHT800orWidejet.SetMarkerColor( ROOT.kRed )
trigEf_PFHT800orWidejet.SetLineColor( ROOT.kRed )

h3 = fin.Get("h17")
trigEf_PFHT800orWidejetorDijet250.Sumw2()
trigEf_PFHT800orWidejetorDijet250.Divide(h3,h,1,1,"B")
trigEf_PFHT800orWidejetorDijet250.SetMarkerStyle(7)
trigEf_PFHT800orWidejetorDijet250.SetMarkerColor( ROOT.kBlue )
trigEf_PFHT800orWidejetorDijet250.SetLineColor( ROOT.kBlue )
trigEf_PFHT800orWidejetorDijet250.GetXaxis().SetRangeUser(800.,2000.)
trigEf_PFHT800orWidejetorDijet250.GetXaxis().SetTitle("Dijet Mass (GeV)")
trigEf_PFHT800orWidejetorDijet250.GetYaxis().SetTitle("Efficiency")

h4 = fin.Get("h21")
trigEf_PFHT800orWidejetorDijet280.Sumw2()
#trigEf_PFHT800orWidejetorDijet280.Divide(h4,h,1,1,"B")
trigEf_PFHT800orWidejetorDijet280.SetMarkerStyle(7)
trigEf_PFHT800orWidejetorDijet280.SetMarkerColor( ROOT.kBlack )
trigEf_PFHT800orWidejetorDijet280.SetLineColor( ROOT.kBlack )


#legend.AddEntry(trigEf_PFHT800,"PFHT800","p")
#legend.AddEntry(trigEf_PFHT800orWidejet,"PFHT800 OR PFHT650_WideJetMJJ900DEtaJJ1p5 OR Dijet","p")
legend.AddEntry(trigEf_PFHT800orWidejetorDijet250,"#splitline{PFHT800 OR AK8PFHT650_TrimR0p1PT0p03Mass50 OR AK8PFJet360 OR}{PFHT650_WideJetMJJ900DEtaJJ1p5 OR AK8DiPFJet280_200_TrimMass30_BTagCSV_p20}","p")
#legend.AddEntry(trigEf_PFHT800orWidejetorDijet280,"#splitline{PFHT800 OR AK8PFHT700_TrimR0p1PT0p03Mass50 OR AK8PFJet360 OR}{PFHT650_WideJetMJJ900DEtaJJ1p5 OR AK8DiPFJet280_200_TrimMass30_BTagCSV_p20}","p")

legend.SetBorderSize(0)
legend.SetFillStyle(0)

text.SetFillStyle(0)
text.SetBorderSize(0)
text.SetTextSize(0.03)

c = ROOT.TCanvas('c1')
#trigEf_PFHT800.Draw("P")
#trigEf_PFHT800orWidejet.Draw("P SAME")
trigEf_PFHT800orWidejetorDijet250.Draw("P")
#trigEf_PFHT800orWidejetorDijet280.Draw("SAME")
legend.Draw("same")
text.Draw("same")
c1.Print('trigEf_Data_DijetMass_ORTrigger.pdf')


fin.Close()


#fout = ROOT.TFile("trig_eff_plot.root", "RECREATE")
#fout.cd()
#trigEf.Write()
#fout.Close()
