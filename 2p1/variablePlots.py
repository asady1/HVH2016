#! /usr/bin/env python
import os
from math import *

from optparse import OptionParser


import ROOT

import sys

#input files
fData = ROOT.TFile("V25miniTrees/Jet_MC.root")

fTopMC = ROOT.TFile("V25miniTrees/TT_MC.root")
fQCD300MC = ROOT.TFile("V25miniTrees/QCD_300_MC.root")
fQCD500MC = ROOT.TFile("V25miniTrees/QCD500_MC.root")
fQCD700MC = ROOT.TFile("V25miniTrees/QCD700_MC.root")
fQCD1000MC = ROOT.TFile("V25miniTrees/QCD1000_MC.root")
fQCD1500MC = ROOT.TFile("V25miniTrees/QCD1500_MC.root")
fQCD2000MC = ROOT.TFile("V25miniTrees/QCD2000_MC.root")
#fBG600 = ROOT.TFile("V25miniTrees/BG_600_MC.root")
#fBG800 = ROOT.TFile("V25miniTrees/BG_800_shape.root")
#fBG1000 = ROOT.TFile("V25miniTrees/BG_1000_shape.root")
#fBG1200 = ROOT.TFile("V25miniTrees/BG_1200_shape.root")


#t1axis = ["Softdrop Corrected Jet Mass (GeV)","AK8 Jet p_{T}/CA15 Jet p_{T}", "p_{T} AK8 Jet (GeV)", "p_{T} AK4 Jet 1 (GeV)", "#eta AK4 Jet 1 (GeV)", "p_{T} AK4 Jet 2 (GeV)", "Dijet Mass AK4 Jets (GeV)", "Deep CSV AK4 Jet 1", "Deep CSV AK4 Jet 2","#eta AK8 Jet (GeV)","#tau_{2}/#tau_{1}","AK Jet p_{T}/CA15 Jet p_{T} with CA15 cuts", "Puppi #tau_{2}/#tau_{1}", "#DeltaR Fatjet and AK4 Jet1","#DeltaR Fatjet and AK4 Jet2","#DeltaR Fatjet and Nearest AK4 Jet","p_{T} AK4 Jet Nearest to Fatjet (GeV)", "#DeltaR AK Jet1 and Nearest Rejected AK4 Jet","#DeltaR AK Jet2 and Nearest Rejected AK4 Jet","p_{T} AK4 Jet Nearest to AK4 Jet1 (GeV)","p_{T} AK4 Jet Nearest to AK4 Jet2 (GeV)", "Number of AK4 jets within #DeltaR 1.5 of AK4 Jet1","Number of AK4 jets within #DeltaR 1.5 of AK4 Jet2","#DeltaR AK Jet1 and AK Jet2", "Number AK4 Jets"
#t1axis = ["Dijet Mass AK4 Jets (GeV)","#DeltaR Fatjet and Matched CA15 Jet", "p_{T} nearest AK4 Jet to AK4 Jet1/p_{T} (AK4 Jet1 + AK4 Jet2)","Softdrop Corrected Jet Mass (GeV)"]
i=0		    
#t1hists = ["jetmass","akca","ptFJ","ptJ1","etaJ1","ptJ2","dijetmass","btag1","btag2","etaFJ","tau21","akcac","ptau21","dRfjAK1","dRfjAK2","dRfjnAK","pTnAKfj","dRAK1nAK","dRAK2nAK","pTnAKAK1","pTnAKAK2","numnAKAK1","numnAKAK2","dRAK1AK2","numAK4",
#t1hists = ["dijetmass1","dRfjCA", "pTAK4AKs", "jetmass1"]

#print len(t1hists)
#print len(t1axis)
#t1axis = ["#tau_{3}/#tau_{2}","Double B Tagger","#eta AK4 Jet 2 (GeV)"]
#t1hists = ["tau32","doubleb","etaJ2"]
#t1axis = ["Invariant Mass (GeV)"]
#t1hists = ["invmass"]
#t1axis = ["#Delta R Fatjet and Second Nearest AK4 Jet","Invariant Mass Fatjet and Second Nearest AK4 Jet (GeV)"]
#t1hists = ["dRsnAK4fj","invmsnAK4fj"]
#t1axis = ["#Delta R AK4 Selected and Nearest AK4 Unselected Jet","Invariant Mass AK4 Selected and Nearest AK4 Unselected Jet (GeV)"]
#t1hists = ["dRsnAK4cl","invmsnAK4cl"]

#axis labels
t1axis = ["Softdrop Corrected Jet Mass (GeV)","Reduced Mass (GeV)","Puppi #tau_{21}","TriAK4jet Mass (GeV)","Double B Tagger","p_{T} AK8 Jet (GeV)", "#eta AK8 Jet","p_{T} AK4 Jet 1 (GeV)","#eta AK4 Jet 1","p_{T} AK4 Jet 2 (GeV)","#eta AK4 Jet 2","Dijet Mass AK4 Jets (GeV)","Deep CSV AK4 Jet 1","Deep CSV AK4 Jet 2", "#Delta#eta"]

#histo names from variableHistos.py
t1hists = ["jetmass","redmass","ptau21","invmsnAK4cl","doubleb","ptFJ","etaFJ","ptJ1","etaJ1","ptJ2","etaJ2","dijetmass","btag1","btag2","deta"] 
for t1hist in t1hists:
	#getting histos
	t1data= fData.Get(t1hist)
	t1data.Sumw2()
	t1ttbarMC= fTopMC.Get(t1hist)	
	t1QCD300MC= fQCD300MC.Get(t1hist)	
	t1QCD500MC= fQCD500MC.Get(t1hist)	
	t1QCD700MC= fQCD700MC.Get(t1hist)	
	t1QCD1000MC= fQCD1000MC.Get(t1hist)	
	t1QCD1500MC= fQCD1500MC.Get(t1hist)	
	t1QCD2000MC= fQCD2000MC.Get(t1hist)
#	t1BG600 = fBG600.Get(t1hist)
#        t1BG800 = fBG800.Get(t1hist)
#        t1BG1000 = fBG1000.Get(t1hist)
#        t1BG1200 = fBG1200.Get(t1hist)
	t1ttbarMC.Sumw2()
	t1QCD300MC.Sumw2()
	t1QCD500MC.Sumw2()
	t1QCD700MC.Sumw2()
	t1QCD1000MC.Sumw2()
	t1QCD1500MC.Sumw2()
	t1QCD2000MC.Sumw2()
#        t1BG600.Sumw2()
#        t1BG800.Sumw2()
#        t1BG1000.Sumw2()
#        t1BG1200.Sumw2()
#	t1ttbarMC.Rebin(5)
#	t1QCD300MC.Rebin(5)
#	t1QCD500MC.Rebin(5)
#	t1QCD700MC.Rebin(5)
#	t1QCD1000MC.Rebin(5)
#	t1QCD1500MC.Rebin(5)
#	t1QCD2000MC.Rebin(5)
 #       t1BG600.Rebin(5)
  #      t1BG800.Rebin(5)
   #     t1BG1000.Rebin(5)
    #    t1BG1200.Rebin(5)

	#scaling
	t1ttbarMC.Scale(831.8*35876/71480770)
#	t1ttbarMC.Scale(1/t1ttbarMC.Integral())
	t1QCD300MC.Scale(347700*35876/39598300)
#	t1QCD300MC.Scale((347700/39598300)/(t1QCD300MC.Integral()+t1QCD500MC.Integral()+t1QCD700MC.Integral()+t1QCD1000MC.Integral()+t1QCD1500MC.Integral()+t1QCD2000MC.Integral()))
	t1QCD500MC.Scale(32100*35876/42837570)
#	t1QCD500MC.Scale(1/(t1QCD300MC.Integral()+t1QCD500MC.Integral()+t1QCD700MC.Integral()+t1QCD1000MC.Integral()+t1QCD1500MC.Integral()+t1QCD2000MC.Integral()))
	t1QCD700MC.Scale(6831*35876/44384120)
#	t1QCD700MC.Scale(1/(t1QCD300MC.Integral()+t1QCD500MC.Integral()+t1QCD700MC.Integral()+t1QCD1000MC.Integral()+t1QCD1500MC.Integral()+t1QCD2000MC.Integral()))
	t1QCD1000MC.Scale(1207*35876/14977450)
#	t1QCD1000MC.Scale(1/(t1QCD300MC.Integral()+t1QCD500MC.Integral()+t1QCD700MC.Integral()+t1QCD1000MC.Integral()+t1QCD1500MC.Integral()+t1QCD2000MC.Integral()))
	t1QCD1500MC.Scale(119.9*35876/11777410) 
#	t1QCD1500MC.Scale(1/(t1QCD300MC.Integral()+t1QCD500MC.Integral()+t1QCD700MC.Integral()+t1QCD1000MC.Integral()+t1QCD1500MC.Integral()+t1QCD2000MC.Integral()))
	t1QCD2000MC.Scale(25.24*35876/5740311)
#	t1QCD2000MC.Scale(1/(t1QCD300MC.Integral()+t1QCD500MC.Integral()+t1QCD700MC.Integral()+t1QCD1000MC.Integral()+t1QCD1500MC.Integral()+t1QCD2000MC.Integral()))
#        t1BG600.Scale(50*35876./100000)	###
#	t1BG800.Scale(50*35876./100000)
#        t1BG1000.Scale(50*35876./49200)
#        t1BG1200.Scale(50*35876./50000)
	
	#aesthetics
	t1ttbarMC.SetFillColor( ROOT.kRed )
	t1QCD300MC.SetFillColor( ROOT.kYellow )
	t1QCD500MC.SetFillColor( ROOT.kYellow )
	t1QCD700MC.SetFillColor( ROOT.kYellow )
	t1QCD1000MC.SetFillColor( ROOT.kYellow )
	t1QCD1500MC.SetFillColor( ROOT.kYellow )
	t1QCD2000MC.SetFillColor( ROOT.kYellow) 
	t1QCD300MC.SetLineColor( ROOT.kYellow )
	t1QCD500MC.SetLineColor( ROOT.kYellow )
	t1QCD700MC.SetLineColor( ROOT.kBlack )
	t1QCD1000MC.SetLineColor( ROOT.kYellow )
	t1QCD1500MC.SetLineColor( ROOT.kYellow )
	t1QCD2000MC.SetLineColor( ROOT.kYellow )
#        t1BG600.SetLineStyle( 1 )
#        t1BG800.SetLineStyle( 2 )
#        t1BG1000.SetLineStyle( 3 )
#        t1BG1200.SetLineStyle( 4 )
	t1data.SetMarkerStyle( 8 ) 

	t1ttbarMC.SetMarkerStyle( 0 )
	t1QCD300MC.SetMarkerStyle( 0 )
	t1QCD500MC.SetMarkerStyle( 0 )
	t1QCD700MC.SetMarkerStyle( 0 )
	t1QCD1000MC.SetMarkerStyle( 0 )
	t1QCD1500MC.SetMarkerStyle( 0 )
	t1QCD2000MC.SetMarkerStyle( 0 )
	leg = ROOT.TLegend( 0.65, 0.65, 0.84, 0.84)
#	leg = ROOT.TLegend( 0.12, 0.65, 0.31, 0.84)
	leg.AddEntry( t1data,  'Data', 'p')
	leg.AddEntry( t1ttbarMC, 't#bar{t}', 'f')
	leg.AddEntry( t1QCD700MC, 'QCD', 'f')
#        leg.AddEntry( t1BG600, 'M 600', 'l')###
#	leg.AddEntry( t1BG800, 'M 800','l')
#        leg.AddEntry( t1BG1000, 'M 1000','l')
#        leg.AddEntry( t1BG1200, 'M 1200','l')
	leg.SetFillColor(0)
	leg.SetBorderSize(0)

	#stacking background
	hs = ROOT.THStack( 't1 BkgStack', 't1')
	
	hs.Add( t1ttbarMC )
	hs.Add( t1QCD300MC )
	hs.Add( t1QCD500MC )
	hs.Add( t1QCD2000MC )
	hs.Add( t1QCD1000MC )
	hs.Add( t1QCD1500MC )
	hs.Add( t1QCD700MC )
	
	#plotting
	c = ROOT.TCanvas('ct1'+t1hist, 'ct1'+t1hist)
	t1data.SetTitle(';'+t1axis[i]+';Events')
	hs.SetTitle(';'+t1axis[i]+';Events') 
	t1data.SetStats(0)
	t1data.Draw('e')
        

	t1data.SetMaximum( 2. * t1data.GetMaximum() )
#	hs.SetMaximum( 1.1 * t1BG1200.GetMaximum() )
	t1data.Draw('e')
	hs.Draw('hist')
#        t1BG600.Draw('same hist')
#        t1BG800.Draw('same hist')
#        t1BG1000.Draw('same hist')
#        t1BG1200.Draw('same hist')
	t1data.GetYaxis().SetTitleOffset(0.8)
	t1data.Draw('e same')

		
	leg.Draw()
	c.Print( 'MC'+t1hists[i]+'.pdf', 'pdf')
	i +=1

