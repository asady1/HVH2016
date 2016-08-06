#! /usr/bin/env python
from ROOT import *
gStyle.SetOptStat(0000)
import os
from math import *

from optparse import OptionParser
parser = OptionParser()

parser.add_option('--pt', metavar='F', type='string', action='store',
                  default='low',
                  dest='pt',
                  help='low or high')

(options, args) = parser.parse_args()

argv = []




import ROOT
ROOT.gROOT.Macro("rootlogon.C")




import sys


#fData = ROOT.TFile("data_SUSYana.root")
#fData = ROOT.TFile("TTSemilepAnalyzer_v9_19invfb_antibtag_w_mucut_withDR_type1_FULL_withPU.root")
#fQCD = ROOT.TFile("TTSemilepAnalyzer_v9_19invfb_antibtag_w_mucut_qcd_withDR_type1_fix_FULL_withPU.root")

#fTopSLMC = ROOT.TFile("ttbar_sl_2.root")
#fTopFLMC = ROOT.TFile("ttbar_fl_2.root")
#fTopFHMC = ROOT.TFile("ttbar_fh_2.root")
fQCD500MC = ROOT.TFile("tree_QCD_500_VH_alphPlots.root")
fQCD700MC = ROOT.TFile("tree_QCD_700_VH_alphPlots.root")
fQCD1000MC = ROOT.TFile("tree_QCD_1000_VH_alphPlots.root")
fQCD1500MC = ROOT.TFile("tree_QCD_1500_VH_alphPlots.root")
fQCD2000MC = ROOT.TFile("tree_QCD_2000_VH_alphPlots.root")
fWP600 = ROOT.TFile("tree_WP_600_VH_alphPlots.root")
fWP1000 = ROOT.TFile("tree_WP_1000_VH_alphPlots.root")
fWP1400 = ROOT.TFile("tree_WP_1400_VH_alphPlots.root")
fWP2000 = ROOT.TFile("tree_WP_2000_VH_alphPlots.root")
fWP3000 = ROOT.TFile("tree_WP_3000_VH_alphPlots.root")
fWP4000 = ROOT.TFile("tree_WP_4000_VH_alphPlots.root")
fZP600 = ROOT.TFile("tree_ZP_600_VH_alphPlots.root") 
fZP1000 = ROOT.TFile("tree_ZP_1000_VH_alphPlots.root")
fZP1400 = ROOT.TFile("tree_ZP_1400_VH_alphPlots.root")
fZP1800 = ROOT.TFile("tree_ZP_1800_VH_alphPlots.root")
fZP3000 = ROOT.TFile("tree_ZP_3000_VH_alphPlots.root")
fZP4000 = ROOT.TFile("tree_ZP_4000_VH_alphPlots.root")
#fQCD300MC = ROOT.TFile("BG_1p2_v9_pt_0_tree.root")
#fQCD470MC = ROOT.TFile("BG_1p6_v9_pt_0_tree.root")
#fQCD600MC = ROOT.TFile("BG_2_v9_pt_0_tree.root")
#fQCD800MC = ROOT.TFile("BG_3_v9_pt_0_tree.root")
#fQCD1000MC = ROOT.TFile("QCD_1000_2.root")
#fQCD1400MC = ROOT.TFile("QCD_1400_2.root")
#fQCD1800MC = ROOT.TFile("QCD_1800_2.root")
#fW1MC = ROOT.TFile("w1jets_2.root")
#fW2MC = ROOT.TFile("w2jets_2.root")
#fW3MC = ROOT.TFile("w3jets_2.root")
#fW4MC = ROOT.TFile("w4jets_2.root")
#fZJetsMC = ROOT.TFile("TTSemilepAnalyzert_ZJets_SUSYana.root")
#fSignal = ROOT.TFile("Gluino_Stop_1000_250_SUSYana.root")
#fSingletop = [
#ROOT.TFile("TTSemilepAnalyzert_ST_t_SUSYana.root"),
#ROOT.TFile("TTSemilepAnalyzert_ST_tB_SUSYana.root"),
#ROOT.TFile("TTSemilepAnalyzert_ST_tW_SUSYana.root"),
#ROOT.TFile("TTSemilepAnalyzert_ST_tWB_SUSYana.root"),
#ROOT.TFile("TTSemilepAnalyzert_ST_s_SUSYana.root"),
#ROOT.TFile("TTSemilepAnalyzert_ST_sB_SUSYana.root"),
#]

hists = []
canvs = []

nEvents = [
    6909048.,
    57679988.,
    30439523.,
    111885.
    ]
#stnEvents = [
#    3752922.,
#    1932776.,
#    496681.,
#    492545.,
#    259575.,
#    139803.,
#]
xs = [
    225.0,
    37509.0,
    3503.71,
    0.000877261
    ]
#stxs=[
#    56.4,
#    30.7,
#    11.1,
#    11.1,
#    3.79,
#    1.76,
#]
colors = [
    #ROOT.kRed-3,
    ROOT.TColor.GetColor(255, 80, 80),
    ROOT.kGreen,
    ROOT.kYellow,
    ROOT.kCyan
    ]
#qcdFactor = [
#    0.00957248,0.00957248,0.00957248,0.00957248
#    ]

#lumi = 12696.
lumi = 19800.
#15379.91 * 1.066
#lumi = 4921.


if options.pt == 'high':
	t1titles = ["t1MinimumPairwiseMasshighpt","t1TopMasshighpt","t1Nsubjetshighpt","t1PairMasshighpt"]
else:
	t1titles = ["hJetVMass","hJetHMass","hJetVbbtag","hJetHbbtag","hJetVtau21DDT","hJetHtau21DDT","hJetVtau21","hJetHtau21"]
#	t1titles = ["t1MinimumPairwiseMass","t1TopMass","t1Nsubjets","t1PairMass","t1ptleptest","t1leppttest","t1lepetatest","t1lepphitest","t1jet0pttest","t1jet1pttest","t1jet2pt","t1jet3pt","t1jet0etatest","t1jet1etatest","t1nbtags", "t1ptMET3","t1njetst","t1htLep3","t1httot","t1mtopleptonic","t1DRmin", "t1jjinvmass01","t1jjinvmass02","t1jjinvmass03","t1jjinvmass04","t1jjinvmass12","t1jjinvmass13","t1jjinvmass14","t1jjinvmass23","t1jjinvmass24","t1jjinvmass34","t1mtophadronic"]
	t1axis = ["V Jet Pruned Mass (GeV)", "H Jet Pruned Mass (GeV)", "V Jet Double b Discriminant","H Jet Double b Discriminant", "V Jet #tau_{21} DDT","H Jet #tau_{21} DDT","V Jet #tau_{21}", "H Jet #tau_{21}"]
#	t1axis = ["Jet 2 Pruned Mass (GeV)", "Jet 1 Pruned Mass (GeV)"]
#t1axis = ["Minimum Pairwise Mass (GeV/c^{2})","m(top) (GeV/c^{2})","Number of Subjets","M_{t#bar{t}} (GeV/c^{2})","p_{T}(leptonic top) (GeV/c^{2})","p_{T}(lepton) (GeV/c^{2})","#eta(lepton) (GeV/c^{2})","#phi(lepton) (GeV/c^{2})","p_{T}(leading jet) (GeV/c^{2})","p_{T}(subleading jet) (GeV/c^{2})","p_{T}(jet 3) (GeV/c^{2})","p_{T}(jet 4) (GeV/c^{2})","#eta(leading jet) (GeV/c^{2})","#eta(subleading jet) (GeV/c^{2})","N_{btags}","E_{T}^{miss} (GeV/c^{2})","N_{jets}","H_{T}^{lep} (GeV/c^{2})","H_{T}^{tot} (GeV/c^{2})","Mass of Leptonic Top (GeV/c^{2})","#DeltaR_{min}","Invariant Mass of Jet 0 + 1 (GeV/c^{2})","Invariant Mass of Jet 0 + 2 (GeV/c^{2})","Invariant Mass of Jet 0 + 3 (GeV/c^{2})","Invariant Mass of Jet 0 + 4 (GeV/c^{2})","Invariant Mass of Jet 1 + 2 (GeV/c^{2})","Invariant Mass of Jet 1 + 3 (GeV/c^{2})","Invariant Mass of Jet 1 + 4 (GeV/c^{2})","Invariant Mass of Jet 2 + 3 (GeV/c^{2})","Invariant Mass of Jet 2 + 4 (GeV/c^{2})","Invariant Mass of Jet 3 + 4 (GeV/c^{2})","Mass of Hadronic Top (GeV/c^{2})"]
t1int = [[1.,1.,1.],[1.,1.,1.],[1.,1.,1.],[1.,1.,1.],[1.,1.,1.],[1.,1.,1.],[1.,1.,1.],[1.,1.,1.]]
#t1int = [[50,149.9],[140,249.99],[3.,10.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.]]
#t1rebins = [10,5,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
t1rebins = [1,1,1,1,1,1,1,1]
i=0
		    
if options.pt == 'high':
	t1hists = ["minPairHisthighpt","topTagMassHistpremasshighpt","nsjhighpt","pairmasshightpt"]
else:
	t1hists = ["hJetVMass","hJetHMass","hJetVbbtag","hJetHbbtag","hJetVtau21DDT","hJetHtau21DDT","hJetVtau21","hJetHtau21"]
	t1bin = [20,30,20,20,20,20,20,20]
	t1min = [60,0,-1,-1,0,0,0,0]
	t1max = [110,250,1,1,1,1,1,1]
#	t1hists = ["jet2mass","jet1mass"]
#	t1hists = ["leppttest","lepetatest","lepphitest","jet0pttest","jet1pttest","jet2pt","jet3pt","jet0etatest","jet1etatest","nbtags", "ptMET3","njetst","htLep3","httot"]
for t1hist in t1hists:
#	t1data= fData.Get(t1hist)
#	t1data.Sumw2()
#	t1ttbar= fTopMC.Get(t1hist)		
#	t1sig=fSignal.Get(t1hist)
#	t1wjets= fWMC.Get(t1hist)
#	t1wjets.Scale(xs[1]*lumi/nEvents[1])
#	t1zjets= fZJetsMC.Get(t1hist)

#	singletopt1temp = fSingletop[0].Get(t1hist)
#	singletopt1temp.Scale((stxs[0] / stnEvents[0]) * lumi)
#	singletopt1temp.Rebin(t1rebins[i])
#	singletopt1 = singletopt1temp.Clone("singletopt1")
#	for ifile in range(1,len(fSingletop)):
#		singletopt1temp = fSingletop[ifile].Get(t1hist)
#		singletopt1temp.Scale((stxs[ifile] / stnEvents[ifile]) * lumi)
 #      	        singletopt1temp.Rebin(t1rebins[i])
#		singletopt1.Add(singletopt1temp)
#	singletopt1.SetMarkerStyle( 0 )
#	singletopt1.SetFillColor( 6 )


	#t1ttbar.Scale(xs[0]*lumi/nEvents[0])
#        t1zjets.Scale(xs[2]*lumi/nEvents[2])
#	t1sig.Scale(xs[3]*lumi/nEvents[3])
#	t1wjets.Rebin(t1rebins[i])
#	t1zjets.Rebin(t1rebins[i])
#	t1ttbar.Rebin(t1rebins[i])
#	t1data.Rebin(t1rebins[i])
#	t1sig.Rebin(t1rebins[i])
#	t1ttbar.SetFillColor( colors[0] )
#	t1wjets.SetFillColor( colors[1] )
	t1QCD500=fQCD500MC.Get(t1hist)
	t1QCD500.SetLineColor(ROOT.kMagenta)
	t1QCD700=fQCD700MC.Get(t1hist)
	t1QCD700.SetLineColor(ROOT.kMagenta - 3)
	t1QCD1000=fQCD1000MC.Get(t1hist)
	t1QCD1000.SetLineColor(ROOT.kRed)
	t1QCD1500=fQCD1500MC.Get(t1hist)
	t1QCD1500.SetLineColor(ROOT.kRed - 3)
	t1QCD2000=fQCD2000MC.Get(t1hist)
	t1QCD2000.SetLineColor(ROOT.kRed + 2)
	t1WP600=fWP600.Get(t1hist)
	t1WP600.SetLineColor( ROOT.kGreen - 7)
	t1WP1000=fWP1000.Get(t1hist)
	t1WP1000.SetLineColor( ROOT.kGreen)
	t1WP1400=fWP1400.Get(t1hist)
	t1WP1400.SetLineColor( ROOT.kGreen + 1)
	t1WP2000=fWP2000.Get(t1hist)
	t1WP2000.SetLineColor( ROOT.kGreen + 2)
	t1WP3000=fWP3000.Get(t1hist)
	t1WP3000.SetLineColor( ROOT.kGreen + 3)
	t1WP4000=fWP4000.Get(t1hist)
	t1WP4000.SetLineColor( ROOT.kGreen + 4)
	t1ZP600=fZP600.Get(t1hist)
	t1ZP600.SetLineColor( ROOT.kAzure + 10)
	t1ZP1000=fZP1000.Get(t1hist)
	t1ZP1000.SetLineColor( ROOT.kBlue - 7)
	t1ZP1400=fZP1400.Get(t1hist)
	t1ZP1400.SetLineColor( ROOT.kAzure - 3)
	t1ZP1800=fZP1800.Get(t1hist)
	t1ZP1800.SetLineColor( ROOT.kBlue)
	t1ZP3000=fZP3000.Get(t1hist)
	t1ZP3000.SetLineColor( ROOT.kAzure + 2)
	t1ZP4000=fZP4000.Get(t1hist)
	t1ZP4000.SetLineColor( ROOT.kBlue + 2)
	
#	t1data.SetMarkerStyle( 8 ) 
#
#	t1ttbar.SetMarkerStyle( 0 )
#	t1wjets.SetMarkerStyle( 0 )
#	t1sig.SetMarkerStyle( 0 )
#	t1zjets.SetFillColor( 30 )
#	t1zjets.SetMarkerStyle( 0 )
	happy = 0
	if happy==0:
		leg = ROOT.TLegend( 0.55, 0.41, 0.84, 0.89)
		leg.AddEntry( t1QCD500,  'QCD HT 500-700', 'l')
		leg.AddEntry( t1QCD700,  'QCD HT 700-1000', 'l')
		leg.AddEntry( t1QCD1000,  'QCD HT 1000-1500', 'l')
		leg.AddEntry( t1QCD1500,  'QCD HT 1500-2000', 'l')
		leg.AddEntry( t1QCD2000,  'QCD HT 2000-Inf', 'l')
		leg.AddEntry( t1WP600, 'Wp 600', 'l')
		leg.AddEntry( t1WP1000, 'Wp 1000', 'l')
		leg.AddEntry( t1WP1400, 'Wp 1400', 'l')
		leg.AddEntry( t1WP2000, 'Wp 2000', 'l')
		leg.AddEntry( t1WP3000, 'Wp 3000', 'l')
		leg.AddEntry( t1WP4000, 'Wp 4000', 'l')
		leg.AddEntry( t1ZP600, 'Zp 600', 'l')
		leg.AddEntry( t1ZP1000, 'Zp 1000', 'l')
		leg.AddEntry( t1ZP1400, 'Zp 1400', 'l')
		leg.AddEntry( t1ZP1800, 'Zp 1800', 'l')
		leg.AddEntry( t1ZP3000, 'Zp 3000', 'l')
		leg.AddEntry( t1ZP4000, 'Zp 4000', 'l')
		leg.SetFillColor(0)
		leg.SetBorderSize(0)

#	hs = ROOT.THStack( 't1 BkgStack', 't1')#
#	hs.Add( t1BG1 )
##	hs.Add( t1BG1p2 )
#	hs.Add( t1BG1p6 )
#	hs.Add( t1BG2 )
#	hs.Add( t1BG3 )
	
		
#	print t1hist
#	if True:
#    		t1bin1 = t1data.GetXaxis().FindBin(t1int[i][0])
#    		t1bin2 = t1data.GetXaxis().FindBin(t1int[i][1]) 

#    		at1 = float(t1data.Integral( t1bin1, t1bin2))
#    		bt1 = float(t1data.Integral())

#		temp=0.
	#print "Data"
    	#for ibin in range(t1bin1,t1bin2+1):
	#	print str(t1data.GetBinLowEdge(ibin)) + " To " + str(t1data.GetBinLowEdge(ibin)+t1data.GetBinWidth(ibin))
	#	print "Content " + str(float(t1data.GetBinContent(ibin)))
	#	temp+=float(t1data.GetBinContent(ibin))
	#print "total" + str(temp)

 #  		ft1 = at1 / bt1
  #  		dft1 = sqrt(ft1 * (1-ft1) / bt1)

	#print "lbin " + str(t1bin1)
	#print "hbin " + str(t1bin2)
	#print "data int 1 "+str(at1)
	#print "data int 2 "+str(bt1)

   # 		at2 = float(hs.GetStack().Last().Integral( t1bin1, t1bin2))
    #		bt2 = float(hs.GetStack().Last().Integral())

    #		ft2 = at2 / bt2
    #		dft2 = sqrt(ft2 * (1-ft2) / bt2)

	#print "mc int 1 "+str(at2)
	#print "mc int 2 "+str(bt2)
#		temp=0.
	#print "Monte Carlo"
    	#for ibin in range(t1bin1,t1bin2+1):
	#	print str(hs.GetStack().Last().GetBinLowEdge(ibin)) + " To " + str(hs.GetStack().Last().GetBinLowEdge(ibin)+hs.GetStack().Last().GetBinWidth(ibin))
	#	print "Content " + str(float(hs.GetStack().Last().GetBinContent(ibin)))
	#	temp+=float(hs.GetStack().Last().GetBinContent(ibin))
	#print "total" + str(temp)
	#	SF = ft1/ft2
	#	SFerror = sqrt((dft1/ft1)**2+(dft2/ft2)**2)*SF
		#print t1hist
#		print "-----------------------------------------"
	#	print "Data = "+str(ft1) +" +/- "+str(dft1)
	#	print "MC = "+str(ft2) +" +/- "+str(dft2)
	#	print "SF = "+str(SF)+" +/- "+str(SFerror)

	c = ROOT.TCanvas('ct1'+t1hist, 'ct1'+t1hist)
	frame = ROOT.TH1F("frame", "", t1bin[i], t1min[i], t1max[i])
	frame.SetMaximum(0.5)
	frame.SetTitle(';'+t1axis[i]+';Events')
#	t1WP600.SetMaximum(5.0*t1WP1400.GetMaximum())
#	t1BG2.SetStats(0)
#	t1BG3.Smooth(100)
#	t1BG2.Smooth(100)
#	t1BG1.Smooth(100)
#	t1BG1p2.Smooth(100)
#	t1BG1p6.Smooth(100)
#	t1QCD.Draw('hist')
	
#	integ = float(t1sig.Integral())
#	print integ
#	t1data.SetMaximum( 1.8 * t1data.GetMaximum() )
	frame.Draw()
	t1QCD500.DrawNormalized('hist sames')
	t1QCD700.DrawNormalized('hist sames')
	t1QCD1000.DrawNormalized('hist sames')
	t1QCD1500.DrawNormalized('hist sames')
	t1QCD2000.DrawNormalized('hist sames')
	t1WP600.DrawNormalized('hist sames')
	t1WP1000.DrawNormalized('hist sames')
	t1WP1400.DrawNormalized('hist sames')
	t1WP2000.DrawNormalized('hist sames')
	t1WP3000.DrawNormalized('hist sames')
	t1WP4000.DrawNormalized('hist sames')
	t1ZP600.DrawNormalized('hist sames')
	t1ZP1000.DrawNormalized('hist sames')
	t1ZP1400.DrawNormalized('hist sames')
	t1ZP1800.DrawNormalized('hist sames')
	t1ZP3000.DrawNormalized('hist sames')
	t1ZP4000.DrawNormalized('hist sames')
	
	leg.Draw()

#	prelim = ROOT.TLatex()#
#	prelim.SetTextFont(42)
#	prelim.SetNDC()
 #       prelim.DrawLatex( 0.15, 0.91, "#scale[1.0]{CMS Preliminary #sqrt{s} = 8 TeV, 19.6 fb^{-1}}" )


#	c.Print( 'SUSYsemiLepMass_'+t1titles[i]+'.root', 'root')
	c.Print( 'AN16254_'+t1titles[i]+'.pdf', 'pdf')
	i+=1
#if options.pt=='high':
#	hists = ['mWCandhighpt', 'muHisthighpt', 'mTopCandhighpt']
#else:
#	hists = ['mWCand', 'muHist', 'mTopCand']

#func0 = ROOT.TF1('func0', 'gaus(0) + gaus(3)', 20, 200)
#func0.SetParameter(1, 90.0)
#func0.SetParameter(2, 10)
#func0.SetParameter(4, 20)
#func0.SetParameter(5, 100)
#func0.SetLineColor(ROOT.kBlue)
#func0.SetLineWidth(3)


#func0MC = ROOT.TF1('func0MC', 'gaus(0) + gaus(3)', 20, 200)
#func0MC.SetParameter(1, 90.0)
#func0MC.SetParameter(2, 10)
#func0MC.SetParameter(4, 20)
#func0MC.SetParameter(5, 100)
#func0MC.SetLineColor(ROOT.TColor.GetColor(103))
#func0MC.SetLineWidth(5)
#func0MC.SetLineStyle(7)

#funcs = [[func0, func0MC], [None, None], [None,None] ]

#titles = [
#    ';m(W-jet) (GeV/c^{2});Events / 5 GeV/c^{2}',
#    ';Subjet Mass Drop (#mu = m_{1} / m_{jet});Events / 0.05',
#    ';m(W+b) (GeV/c^{2});Events / 10 GeV/c^{2}'
#    ]
