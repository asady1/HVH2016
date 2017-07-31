from ROOT import *
gStyle.SetOptStat(0)
import os
from math import *

import ROOT
import sys

from array import *

from optparse import OptionParser
parser = OptionParser()

#input files
q3 = ROOT.TFile.Open("QCD_300_finaldEta1.root", "READ")
q5 = ROOT.TFile.Open("QCD500_finaldEta1.root", "READ")
q7 = ROOT.TFile.Open("QCD700_finaldEta1.root", "READ")
q10 = ROOT.TFile.Open("QCD1000_finaldEta1.root", "READ")
q15 = ROOT.TFile.Open("QCD1500_finaldEta1.root", "READ")
q20 = ROOT.TFile.Open("QCD2000_finaldEta1.root", "READ")
jb = ROOT.TFile.Open("Jet_finaldEta1.root", "READ")

outfile = ROOT.TFile("trigHistos.root", 'recreate')
outfile.cd()

#QCDBaseHT = ROOT.TH1F("QCDBaseHT", "QCD After Event Selection", 60, 0, 3000)
#QCD260HT = ROOT.TH1F("QCD260HT", "QCD After Event Selection + 260", 60, 0, 3000)
#QCDBoostHT = ROOT.TH1F("QCDBoostHT", "QCD After Event Selection + 260 + OR", 60, 0, 3000)
#QCDBEfHT = ROOT.TH1F("QCDBEfHT", "QCD Efficiency Boosted", 60, 0, 3000)
#QCD260EfHT = ROOT.TH1F("QCD260EfHT", "QCD Efficiency 260", 60, 0, 3000)
#QCD260SubEfHT = ROOT.TH1F("QCD260SubEfHT", "QCD Efficiency 260", 60, 0, 3000)

#DataBEfHT = ROOT.TH1F("DataBEfHT", "Data Boosted", 60, 0, 3000)

#SFBEfHT = ROOT.TH1F("SFBEfHT", "SF Efficiency Boosted", 60, 0, 3000)

#QCDBaseInvM = ROOT.TH1F("QCDBaseInvM", "QCD After Event Selection", 60, 0, 3000)
#QCD260InvM = ROOT.TH1F("QCD260InvM", "QCD After Event Selection + 260", 60, 0, 3000)
#QCDBoostInvM = ROOT.TH1F("QCDBoostInvM", "QCD After Event Selection + 260 + OR", 60, 0, 3000)
#QCDBEfInvM = ROOT.TH1F("QCDBEfInvM", "QCD Efficiency Boosted", 60, 0, 3000)
#QCD260EfInvM = ROOT.TH1F("QCD260EfInvM", "QCD Efficiency 260", 60, 0, 3000)
#QCD260SubEfInvM = ROOT.TH1F("QCD260SubEfInvM", "QCD Efficiency 260", 60, 0, 3000)

#DataBEfInvM = ROOT.TH1F("DataBEfInvM", "Data Boosted", 60, 0, 3000)

#SFBEfInvM = ROOT.TH1F("SFBEfInvM", "SF Efficiency Boosted", 60, 0, 3000)

QCDBaseRedM = ROOT.TH1F("QCDBaseRedM", "QCD After Event Selection", 60, 0, 3000)
QCD260RedM = ROOT.TH1F("QCD260RedM", "", 60, 0, 3000)
QCDBoostRedM = ROOT.TH1F("QCDBoostRedM", "", 60, 0, 3000)
QCDBEfRedM = ROOT.TH1F("QCDBEfRedM", "QCD Efficiency Boosted", 60, 0, 3000)
QCD260EfRedM = ROOT.TH1F("QCD260EfRedM", "QCD Efficiency 260", 60, 0, 3000)
QCD260SubEfRedM = ROOT.TH1F("QCD260SubEfRedM", "QCD Efficiency 260", 60, 0, 3000)

DataBEfRedM = ROOT.TH1F("DataBEfRedM", "Data Boosted", 60, 0, 3000)

SFBEfRedM = ROOT.TH1F("SFBEfRedM", "SF Efficiency Boosted", 60, 0, 3000)

#unitary = ROOT.TH1F("unitary", "Unitary", 60, 0, 3000)

#for i in range(0,60):
#    unitary.SetBinContent(i, 1.)

#unitary.Draw()


#getting histograms
qcd300HTBase = q3.Get("htes")
qcd300HT260 = q3.Get("htes260")
qcd300HTBoost = q3.Get("htes260B")

qcd500HTBase = q5.Get("htes")
qcd500HT260 = q5.Get("htes260")
qcd500HTBoost = q5.Get("htes260B")

qcd700HTBase = q7.Get("htes")
qcd700HT260 = q7.Get("htes260")
qcd700HTBoost = q7.Get("htes260B")

qcd1000HTBase = q10.Get("htes")
qcd1000HT260 = q10.Get("htes260")
qcd1000HTBoost = q10.Get("htes260B")

qcd1500HTBase = q15.Get("htes")
qcd1500HT260 = q15.Get("htes260")
qcd1500HTBoost = q15.Get("htes260B")

qcd2000HTBase = q20.Get("htes")
qcd2000HT260 = q20.Get("htes260")
qcd2000HTBoost = q20.Get("htes260B")

dataHTBase = jb.Get("htes")
dataHT260 = jb.Get("htes260")
dataHTBoost = jb.Get("htes260B") 

qcd300InvMBase = q3.Get("invmes")
qcd300InvM260 = q3.Get("invmes260")
qcd300InvMBoost = q3.Get("invmes260B")

qcd500InvMBase = q5.Get("invmes")
qcd500InvM260 = q5.Get("invmes260")
qcd500InvMBoost = q5.Get("invmes260B")

qcd700InvMBase = q7.Get("invmes")
qcd700InvM260 = q7.Get("invmes260")
qcd700InvMBoost = q7.Get("invmes260B")

qcd1000InvMBase = q10.Get("invmes")
qcd1000InvM260 = q10.Get("invmes260")
qcd1000InvMBoost = q10.Get("invmes260B")

qcd1500InvMBase = q15.Get("invmes")
qcd1500InvM260 = q15.Get("invmes260")
qcd1500InvMBoost = q15.Get("invmes260B")

qcd2000InvMBase = q20.Get("invmes")
qcd2000InvM260 = q20.Get("invmes260")
qcd2000InvMBoost = q20.Get("invmes260B")

dataInvMBase = jb.Get("invmes")
dataInvM260 = jb.Get("invmes260")
dataInvMBoost = jb.Get("invmes260B") 

qcd300RedMBase = q3.Get("redmes")
qcd300RedM260 = q3.Get("redmes260")
qcd300RedMBoost = q3.Get("redmes260B")

qcd500RedMBase = q5.Get("redmes")
qcd500RedM260 = q5.Get("redmes260")
qcd500RedMBoost = q5.Get("redmes260B")

qcd700RedMBase = q7.Get("redmes")
qcd700RedM260 = q7.Get("redmes260")
qcd700RedMBoost = q7.Get("redmes260B")

qcd1000RedMBase = q10.Get("redmes")
qcd1000RedM260 = q10.Get("redmes260")
qcd1000RedMBoost = q10.Get("redmes260B")

qcd1500RedMBase = q15.Get("redmes")
qcd1500RedM260 = q15.Get("redmes260")
qcd1500RedMBoost = q15.Get("redmes260B")

qcd2000RedMBase = q20.Get("redmes")
qcd2000RedM260 = q20.Get("redmes260")
qcd2000RedMBoost = q20.Get("redmes260B")

dataRedMBase = jb.Get("redmes")
dataRedM260 = jb.Get("redmes260")
dataRedMBoost = jb.Get("redmes260B") 

qcd300HTBase.Sumw2()
qcd300HT260.Sumw2()
qcd300HTBoost.Sumw2()
qcd500HTBase.Sumw2()
qcd500HT260.Sumw2()
qcd500HTBoost.Sumw2()
qcd700HTBase.Sumw2()
qcd700HT260.Sumw2()
qcd700HTBoost.Sumw2()
qcd1000HTBase.Sumw2()
qcd1000HT260.Sumw2()
qcd1000HTBoost.Sumw2()
qcd1500HTBase.Sumw2()
qcd1500HT260.Sumw2()
qcd1500HTBoost.Sumw2()
qcd2000HTBase.Sumw2()
qcd2000HT260.Sumw2()
qcd2000HTBoost.Sumw2()
dataHTBase.Sumw2()
dataHT260.Sumw2()
dataHTBoost.Sumw2()
qcd300InvMBase.Sumw2()
qcd300InvM260.Sumw2()
qcd300InvMBoost.Sumw2()
qcd500InvMBase.Sumw2()
qcd500InvM260.Sumw2()
qcd500InvMBoost.Sumw2()
qcd700InvMBase.Sumw2()
qcd700InvM260.Sumw2()
qcd700InvMBoost.Sumw2()
qcd1000InvMBase.Sumw2()
qcd1000InvM260.Sumw2()
qcd1000InvMBoost.Sumw2()
qcd1500InvMBase.Sumw2()
qcd1500InvM260.Sumw2()
qcd1500InvMBoost.Sumw2()
qcd2000InvMBase.Sumw2()
qcd2000InvM260.Sumw2()
qcd2000InvMBoost.Sumw2()
dataInvMBase.Sumw2()
dataInvM260.Sumw2()
dataInvMBoost.Sumw2()
qcd300RedMBase.Sumw2()
qcd300RedM260.Sumw2()
qcd300RedMBoost.Sumw2()
qcd500RedMBase.Sumw2()
qcd500RedM260.Sumw2()
qcd500RedMBoost.Sumw2()
qcd700RedMBase.Sumw2()
qcd700RedM260.Sumw2()
qcd700RedMBoost.Sumw2()
qcd1000RedMBase.Sumw2()
qcd1000RedM260.Sumw2()
qcd1000RedMBoost.Sumw2()
qcd1500RedMBase.Sumw2()
qcd1500RedM260.Sumw2()
qcd1500RedMBoost.Sumw2()
qcd2000RedMBase.Sumw2()
qcd2000RedM260.Sumw2()
qcd2000RedMBoost.Sumw2()
dataRedMBase.Sumw2()
dataRedM260.Sumw2()
dataRedMBoost.Sumw2()

#scaling QCD appropriately
qcd300HTBase.Scale(35876.*347700./39598300.)
qcd300HT260.Scale(35876.*347700./39598300.)
qcd300HTBoost.Scale(35876.*347700./39598300.)
qcd300InvMBase.Scale(35876.*347700./39598300.)
qcd300InvM260.Scale(35876.*347700./39598300.)
qcd300InvMBoost.Scale(35876.*347700./39598300.)
qcd300RedMBase.Scale(35876.*347700./39598300.)
qcd300RedM260.Scale(35876.*347700./39598300.)
qcd300RedMBoost.Scale(35876.*347700./39598300.)
qcd500HTBase.Scale(35876.*32100./42837570.)
qcd500HT260.Scale(35876.*32100./42837570.)
qcd500HTBoost.Scale(35876.*32100./42837570.)
qcd500InvMBase.Scale(35876.*32100./42837570.)
qcd500InvM260.Scale(35876.*32100./42837570.)
qcd500InvMBoost.Scale(35876.*32100./42837570.)
qcd500RedMBase.Scale(35876.*32100./42837570.)
qcd500RedM260.Scale(35876.*32100./42837570.)
qcd500RedMBoost.Scale(35876.*32100./42837570.)
qcd700HTBase.Scale(35876.*6831./44384120.)
qcd700HT260.Scale(35876.*6831./44384120.) 
qcd700HTBoost.Scale(35876.*6831./44384120.) 
qcd700InvMBase.Scale(35876.*6831./44384120.)
qcd700InvM260.Scale(35876.*6831./44384120.) 
qcd700InvMBoost.Scale(35876.*6831./44384120.) 
qcd700RedMBase.Scale(35876.*6831./44384120.)
qcd700RedM260.Scale(35876.*6831./44384120.) 
qcd700RedMBoost.Scale(35876.*6831./44384120.) 
qcd1000HTBase.Scale(35876.*1207./14977450.)
qcd1000HT260.Scale(35876.*1207./14977450.)
qcd1000HTBoost.Scale(35876.*1207./14977450.)
qcd1000InvMBase.Scale(35876.*1207./14977450.)
qcd1000InvM260.Scale(35876.*1207./14977450.)
qcd1000InvMBoost.Scale(35876.*1207./14977450.)
qcd1000RedMBase.Scale(35876.*1207./14977450.)
qcd1000RedM260.Scale(35876.*1207./14977450.)
qcd1000RedMBoost.Scale(35876.*1207./14977450.)
qcd1500HTBase.Scale(35876.*119.9/11777410.)
qcd1500HT260.Scale(35876.*119.9/11777410.) 
qcd1500HTBoost.Scale(35876.*119.9/11777410.) 
qcd1500InvMBase.Scale(35876.*119.9/11777410.)
qcd1500InvM260.Scale(35876.*119.9/11777410.) 
qcd1500InvMBoost.Scale(35876.*119.9/11777410.) 
qcd1500RedMBase.Scale(35876.*119.9/11777410.)
qcd1500RedM260.Scale(35876.*119.9/11777410.) 
qcd1500RedMBoost.Scale(35876.*119.9/11777410.) 
qcd2000HTBase.Scale(35876.*25.24/5740311.)
qcd2000HT260.Scale(35876.*25.24/5740311.) 
qcd2000HTBoost.Scale(35876.*25.24/5740311.) 
qcd2000InvMBase.Scale(35876.*25.24/5740311.)
qcd2000InvM260.Scale(35876.*25.24/5740311.) 
qcd2000InvMBoost.Scale(35876.*25.24/5740311.) 
qcd2000RedMBase.Scale(35876.*25.24/5740311.)
qcd2000RedM260.Scale(35876.*25.24/5740311.) 
qcd2000RedMBoost.Scale(35876.*25.24/5740311.) 

#QCDBaseHT.Add(qcd300HTBase)
#QCDBaseHT.Add(qcd500HTBase)
#QCDBaseHT.Add(qcd700HTBase)
#QCDBaseHT.Add(qcd1000HTBase)
#QCDBaseHT.Add(qcd1500HTBase)
#QCDBaseHT.Add(qcd2000HTBase)
#QCDBaseHT.GetXaxis().SetTitle("HT (GeV)")
#QCDBaseHT.SetTitle("QCD with Preselction")

#QCD260HT.Add(qcd300HT260)
#QCD260HT.Add(qcd500HT260)
#QCD260HT.Add(qcd700HT260)
#QCD260HT.Add(qcd1000HT260)
#QCD260HT.Add(qcd1500HT260)
#QCD260HT.Add(qcd2000HT260)
#QCD260HT.GetXaxis().SetTitle("HT (GeV)")
#QCD260HT.SetTitle("QCD with Preselection Passing PFJet260")

#QCDBoostHT.Add(qcd300HTBoost)
#QCDBoostHT.Add(qcd500HTBoost)
#QCDBoostHT.Add(qcd700HTBoost)
#QCDBoostHT.Add(qcd1000HTBoost)
#QCDBoostHT.Add(qcd1500HTBoost)
#QCDBoostHT.Add(qcd2000HTBoost)
#QCDBoostHT.GetXaxis().SetTitle("HT (GeV)")
#QCDBoostHT.SetTitle("QCD with Preselection Passing PFJet260 + Boosted OR")

#QCDBEfHT.Add(QCDBoostHT)
#QCDBEfHT.Divide(QCD260HT)
#QCDBEfHT.GetXaxis().SetTitle("HT (GeV)")
#QCDBEfHT.SetTitle("QCD Efficiency for Boosted OR")
#c2 = ROOT.TCanvas('c2') 
#QCDBEfHT.Draw("hist p")

#QCD260EfHT.Add(QCD260HT)
#QCD260EfHT.Divide(QCDBaseHT)
#QCD260EfHT.GetXaxis().SetTitle("HT (GeV)")
#QCD260EfHT.SetTitle("QCD Efficiency for PFJet260")

#QCD260SubEfHT.Add(unitary)
#QCD260SubEfHT.Add(QCD260EfHT, -1)
#QCD260SubEfHT.GetXaxis().SetTitle("HT (GeV)")     
#QCD260SubEfHT.SetTitle("1 - QCD Efficiency for PFJet260")                       
#c3 = ROOT.TCanvas('c3')
#QCD260SubEfHT.Draw("hist p")

#DataBEfHT.Add(dataHTBoost)
#DataBEfHT.Divide(dataHT260)
#DataBEfHT.GetXaxis().SetTitle("HT (GeV)")
#DataBEfHT.SetTitle("Data Efficiency for Boosted OR")
#c4 = ROOT.TCanvas('c4')
#DataBEfHT.Draw("hist p")

#SFBEfHT.Add(DataBEfHT)
#SFBEfHT.Divide(QCDBEfHT)                 
#SFBEfHT.GetXaxis().SetTitle("HT (GeV)")     
#SFBEfHT.SetTitle("Data/MC Efficiency for Boosted OR")                       
#c5 = ROOT.TCanvas('c5')
#SFBEfHT.Draw("hist p")

#QCDBaseInvM.Add(qcd300InvMBase)
#QCDBaseInvM.Add(qcd500InvMBase)
#QCDBaseInvM.Add(qcd700InvMBase)
#QCDBaseInvM.Add(qcd1000InvMBase)
#QCDBaseInvM.Add(qcd1500InvMBase)
#QCDBaseInvM.Add(qcd2000InvMBase)
#QCDBaseInvM.GetXaxis().SetTitle("Invariant Mass (GeV)")
#QCDBaseInvM.SetTitle("QCD with Preselction")

#QCD260InvM.Add(qcd300InvM260)
#QCD260InvM.Add(qcd500InvM260)
#QCD260InvM.Add(qcd700InvM260)
#QCD260InvM.Add(qcd1000InvM260)
#QCD260InvM.Add(qcd1500InvM260)
#QCD260InvM.Add(qcd2000InvM260)
#QCD260InvM.GetXaxis().SetTitle("Invariant Mass (GeV)")
#QCD260InvM.SetTitle("QCD with Preselection Passing PFJet260")

#QCDBoostInvM.Add(qcd300InvMBoost)
#QCDBoostInvM.Add(qcd500InvMBoost)
#QCDBoostInvM.Add(qcd700InvMBoost)
#QCDBoostInvM.Add(qcd1000InvMBoost)
#QCDBoostInvM.Add(qcd1500InvMBoost)
#QCDBoostInvM.Add(qcd2000InvMBoost)
#QCDBoostInvM.GetXaxis().SetTitle("Invariant Mass (GeV)")
#QCDBoostInvM.SetTitle("QCD with Preselection Passing PFJet260 + Boosted OR")

#QCDBEfInvM.Add(QCDBoostInvM)
#QCDBEfInvM.Divide(QCD260InvM)
#QCDBEfInvM.GetXaxis().SetTitle("Invariant Mass (GeV)")
#QCDBEfInvM.SetTitle("QCD Efficiency for Boosted OR")
#c6 = ROOT.TCanvas('c6')
#QCDBEfInvM.Draw("hist p")

#QCD260EfInvM.Add(QCD260InvM)
#QCD260EfInvM.Divide(QCDBaseInvM)
#QCD260EfInvM.GetXaxis().SetTitle("Invariant Mass (GeV)")
#QCD260EfInvM.SetTitle("QCD Efficiency for PFJet260")

#QCD260SubEfInvM.Add(unitary)
#QCD260SubEfInvM.Add(QCD260EfInvM, -1)
#QCD260SubEfInvM.GetXaxis().SetTitle("Invariant Mass (GeV)")
#QCD260SubEfInvM.SetTitle("1 - QCD Efficiency for PFJet260")
#c13 = ROOT.TCanvas('c13')
#QCD260SubEfInvM.Draw("hist p")

#DataBEfInvM.Add(dataInvMBoost)
#DataBEfInvM.Divide(dataInvM260)
#DataBEfInvM.Add(dataInvM260)
#DataBEfInvM.GetXaxis().SetTitle("Invariant Mass (GeV)")
#DataBEfInvM.SetTitle("Data Efficiency for Boosted OR")
#DataBEfInvM.SetTitle("Data 260")
#c7 = ROOT.TCanvas('c7')
#DataBEfInvM.Draw("hist p")

#SFBEfInvM.Add(DataBEfInvM)
#SFBEfInvM.Divide(QCDBEfInvM)                      
#SFBEfInvM.GetXaxis().SetTitle("Invariant Mass (GeV)")
#SFBEfInvM.SetTitle("Data/MC Efficiency for Boosted OR")
#c8 = ROOT.TCanvas('c8')
#SFBEfInvM.Draw("hist p")

QCDBaseRedM.Add(qcd300RedMBase)
QCDBaseRedM.Add(qcd500RedMBase)
QCDBaseRedM.Add(qcd700RedMBase)
QCDBaseRedM.Add(qcd1000RedMBase)
QCDBaseRedM.Add(qcd1500RedMBase)
QCDBaseRedM.Add(qcd2000RedMBase)
QCDBaseRedM.GetXaxis().SetTitle("Reduced Mass (GeV)")
#QCDBaseRedM.SetTitle("QCD with Preselction")
#QCDBaseRedM.Draw('hist')

#leg = ROOT.TLegend( 0.45, 0.25, 0.6, 0.4)
#leg.AddEntry(QCDeff, "QCD efficiency", 'l')
#leg.AddEntry(Dataeff, "Data efficiency", 'l')
#leg.AddEntry(QCDBaseRedM, "QCD", 'l')
#leg.AddEntry(QCD260RedM, "QCD 260", 'l')
#leg.AddEntry(QCDBoostRedM, "QCD 260 + OR", 'l')
#leg.SetFillColor(0)
#leg.SetBorderSize(0)

QCD260RedM.Add(qcd300RedM260)
QCD260RedM.Add(qcd500RedM260)
QCD260RedM.Add(qcd700RedM260)
QCD260RedM.Add(qcd1000RedM260)
QCD260RedM.Add(qcd1500RedM260)
QCD260RedM.Add(qcd2000RedM260)
QCD260RedM.GetXaxis().SetTitle("Reduced Mass (GeV)")
#QCD260RedM.SetTitle("QCD with Preselection Passing PFJet260")
QCDBaseRedM.GetXaxis().SetTitle("Reduced Mass (GeV)")
#QCDBaseRedM.SetLineColor(603)
#QCDBaseRedM.Draw('hist')
#QCD260RedM.SetLineColor(4)
#QCD260RedM.Draw('same hist')

QCDBoostRedM.Add(qcd300RedMBoost)
QCDBoostRedM.Add(qcd500RedMBoost)
QCDBoostRedM.Add(qcd700RedMBoost)
QCDBoostRedM.Add(qcd1000RedMBoost)
QCDBoostRedM.Add(qcd1500RedMBoost)
QCDBoostRedM.Add(qcd2000RedMBoost)
#QCDBoostRedM.GetXaxis().SetTitle("Reduced Mass (GeV)")
#QCDBoostRedM.SetTitle("QCD with Preselection Passing PFJet260 + Boosted OR")
#QCDBoostRedM.SetLineColor(870)
#QCDBoostRedM.Draw('same hist')
#leg.Draw()

 
QCDBEfRedM.Add(QCDBoostRedM)
QCDBEfRedM.Divide(QCD260RedM)
QCDBEfRedM.GetXaxis().SetTitle("Reduced Mass (GeV)")
#QCDBEfRedM.SetTitle("QCD Efficiency for Boosted OR")

QCD260EfRedM.Add(QCD260RedM)
QCD260EfRedM.Divide(QCDBaseRedM)
QCD260EfRedM.GetXaxis().SetTitle("Reduced Mass (GeV)")
#QCD260EfRedM.SetTitle("QCD Efficiency for PFJet260")

#QCD260SubEfRedM.Add(unitary)
QCD260SubEfRedM.Add(QCD260EfRedM,)
QCD260SubEfRedM.GetXaxis().SetTitle("Reduced Mass (GeV)")
#QCD260SubEfRedM.SetTitle("QCD Efficiency for PFJet260")

DataBEfRedM.Add(dataRedMBoost)
DataBEfRedM.Divide(dataRedM260)
#DataBEfRedM.SetTitle("Data Efficiency for Boosted OR")

SFBEfRedM.Add(DataBEfRedM)
SFBEfRedM.Divide(QCDBEfRedM)                      
SFBEfRedM.GetXaxis().SetTitle("Reduced Mass (GeV)")
#SFBEfRedM.SetTitle("Data/MC Efficiency for Boosted OR")

#TGraphAsymmErrors objects for QCD efficiency and Data efficiency
QCDeff = ROOT.TGraphAsymmErrors(QCDBoostRedM, QCD260RedM, 'cp')
Dataeff = ROOT.TGraphAsymmErrors(dataRedMBoost, dataRedM260, 'cp')

c = ROOT.TCanvas('c', 'c')

QCDeff.SetLineColor(4)
QCDeff.SetMarkerColor(4)
Dataeff.SetLineColor(8)
Dataeff.SetMarkerColor(8)
QCDeff.GetXaxis().SetTitle("Reduced Mass (GeV)")
QCDeff.GetYaxis().SetTitle("Efficiency")
#QCDeff.Draw("ALP")
#Dataeff.Draw("L")

leg = ROOT.TLegend( 0.25, 0.25, 0.4, 0.4)
leg.AddEntry(QCDeff, "QCD efficiency", 'l')
leg.AddEntry(Dataeff, "Data efficiency", 'l')
leg.SetFillColor(0)
leg.SetBorderSize(0)
#leg.Draw()

#TGraphAsymmErrors object for QCD systematic
QCDsys = ROOT.TGraphAsymmErrors(QCD260RedM, QCDBaseRedM, 'cp')
QCDsys.GetXaxis().SetTitle("Reduced Mass (GeV)")
QCDsys.GetYaxis().SetTitle("Efficiency")
QCDsys.Draw("ALP")

c.Print('QCDDeta1.pdf','pdf')
#stat = ROOT.TGraphAsymmErrors(DataBEfRedM, QCDBEfRedM, 'cp')
#stat.Draw("ALP")

#syst = ROOT.TGraphAsymmErrors(QCD260RedM, QCDBaseRedM, 'cp')

nBins = 60

#calculating and printing SFs
SF =[]
SFUp = []
SFDown = []
Up = []
Down = []
for i in range(0, 60):
    print "Bin number " + str(i*50)
    SF.append( Dataeff.Eval(i*50 + 25)/QCDeff.Eval(i*50 + 25))
    sysEr = (Dataeff.Eval(i*50 + 25)/QCDeff.Eval(i*50 + 25))*(1 - QCDsys.Eval(i*50 + 25))/2
    statErUp = (Dataeff.Eval(i*50 + 25)/QCDeff.Eval(i*50 + 25))*sqrt((Dataeff.GetErrorYhigh(i)/Dataeff.Eval(i*50 + 25))*(Dataeff.GetErrorYhigh(i)/Dataeff.Eval(i*50 + 25)) + (QCDeff.GetErrorYhigh(i)/QCDeff.Eval(i*50 + 25))*(QCDeff.GetErrorYhigh(i)/QCDeff.Eval(i*50 + 25)))
    statErDown = (Dataeff.Eval(i*50 + 25)/QCDeff.Eval(i*50 + 25))*sqrt((Dataeff.GetErrorYlow(i)/Dataeff.Eval(i*50 + 25))*(Dataeff.GetErrorYlow(i)/Dataeff.Eval(i*50 + 25)) + (QCDeff.GetErrorYlow(i)/QCDeff.Eval(i*50 + 25))*(QCDeff.GetErrorYlow(i)/QCDeff.Eval(i*50 + 25)))
    if Dataeff.Eval(i*50 + 25)/QCDeff.Eval(i*50 + 25) == 1.:
        SFUp.append(1.0)
        Up.append(0.)
    else:
        if Dataeff.Eval(i*50 + 25)/QCDeff.Eval(i*50 + 25) + sqrt( statErUp*statErUp + sysEr*sysEr ) > 1:
            SFUp.append(1.0)
            Up.append(0.)
        else:
            SFUp.append(Dataeff.Eval(i*50 + 25)/QCDeff.Eval(i*50 + 25) + sqrt( statErUp*statErUp + sysEr*sysEr ))
            Up.append(sqrt( statErUp*statErUp + sysEr*sysEr ))
    if Dataeff.Eval(i*50 + 25)/QCDeff.Eval(i*50 + 25) == 1.:
        SFDown.append(1.0)
        Down.append(0.)
    else:
        SFDown.append(Dataeff.Eval(i*50 + 25)/QCDeff.Eval(i*50 + 25) - sqrt( statErDown*statErDown + sysEr*sysEr ))
        Down.append(sqrt( statErDown*statErDown + sysEr*sysEr ))
    
    #DataUp = Dataeff.Eval(i*50 + 25) + Dataeff.GetErrorYhigh(i)
    #QCDUp = QCDeff.Eval(i*50 + 25) + sqrt( QCDeff.GetErrorYhigh(i)*QCDeff.GetErrorYhigh(i) + sysEr*sysEr )
    #if QCDUp > 1.0:
    #    QCDUp = 1.0
    #SFUp.append(DataUp/QCDUp)
    #DataDown = Dataeff.Eval(i*50 + 25) - Dataeff.GetErrorYlow(i)
    #QCDDown = QCDeff.Eval(i*50 + 25) - sqrt( QCDeff.GetErrorYlow(i)*QCDeff.GetErrorYlow(i) + sysEr*sysEr )
    #if QCDDown <= 0.0:
    #    SFDown.append(-100.)
    #else:
    #    SFDown.append(DataDown/QCDDown)
#    print "SF " + str(SF) + " SFUp " + str(SFUp) + " SFDown " + str(SFDown)
#    print "stat " + str(stat.Eval[i])
   # print "sys " + str(syst.Eval[i])
#c20 = ROOT.TCanvas('c21')
#trigJetpre.Draw("hist CE")
#c21.Print("trigJetpre.pdf")
print SF
print SFUp
print SFDown
print Up
print Down
outfile.cd()
outfile.Write()
outfile.Close()
