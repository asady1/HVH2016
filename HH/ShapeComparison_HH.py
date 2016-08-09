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
fQCD300MC = ROOT.TFile("histos_QCD300_SR.root")
fQCD500MC = ROOT.TFile("histos_QCD500_SR.root")
fQCD700MC = ROOT.TFile("histos_QCD700_SR.root")
fQCD1000MC = ROOT.TFile("histos_QCD1000_SR.root")
fQCD1500MC = ROOT.TFile("histos_QCD1500_SR.root")
fQCD2000MC = ROOT.TFile("histos_QCD2000_SR.root")
fTTMC = ROOT.TFile("histos_TT_SR.root")
fWP600 = ROOT.TFile("histos_WP_600_SR.root")
fWP650 = ROOT.TFile("histos_WP_650_SR.root")
fWP700 = ROOT.TFile("histos_WP_700_SR.root")
fWP750 = ROOT.TFile("histos_WP_750_SR.root")
fWP800 = ROOT.TFile("histos_WP_800_SR.root")
fWP900 = ROOT.TFile("histos_WP_900_SR.root")
fWP1000 = ROOT.TFile("histos_WP_1000_SR.root")
fWP1200 = ROOT.TFile("histos_WP_1200_SR.root")
fWP1400 = ROOT.TFile("histos_WP_1400_SR.root")
fWP1600 = ROOT.TFile("histos_WP_1600_SR.root")
fWP1800 = ROOT.TFile("histos_WP_1800_SR.root")
fWP2000 = ROOT.TFile("histos_WP_2000_SR.root")
fWP2500 = ROOT.TFile("histos_WP_2500_SR.root")
fWP3000 = ROOT.TFile("histos_WP_3000_SR.root")
fWP4000 = ROOT.TFile("histos_WP_4000_SR.root")
fWP4500 = ROOT.TFile("histos_WP_4500_SR.root")
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
    16763036.,
    19198108.,
    15616919.,
    4983341.,
    3753851.,
    1959483.,
    32106228.,
    98000.,
    100000.,
    100000.,
    95600.,
    95800.,
    100000.,
    50000.,
    50000.,
    50000.,
    50000.,
    50000.,
    50000.,
    48800.,
    23600.,
    50000.,
    49600.,
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
    347700.,
    32100.,
    6831.,
    1207.,
    119.9,
    25.24,
    831.76,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,	
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
lumi = 9200.
#15379.91 * 1.066
#lumi = 4921.


if options.pt == 'high':
	t1titles = ["t1MinimumPairwiseMasshighpt","t1TopMasshighpt","t1Nsubjetshighpt","t1PairMasshighpt"]
else:
	t1titles = ["hJet1PMass","hJet2PMass","hJet1bbtag","hJet2bbtag","hJet1tau21","hJet2tau21"]
#	t1titles = ["t1MinimumPairwiseMass","t1TopMass","t1Nsubjets","t1PairMass","t1ptleptest","t1leppttest","t1lepetatest","t1lepphitest","t1jet0pttest","t1jet1pttest","t1jet2pt","t1jet3pt","t1jet0etatest","t1jet1etatest","t1nbtags", "t1ptMET3","t1njetst","t1htLep3","t1httot","t1mtopleptonic","t1DRmin", "t1jjinvmass01","t1jjinvmass02","t1jjinvmass03","t1jjinvmass04","t1jjinvmass12","t1jjinvmass13","t1jjinvmass14","t1jjinvmass23","t1jjinvmass24","t1jjinvmass34","t1mtophadronic"]
	t1axis = ["Jet 1 Pruned Mass (GeV)", "Jet 2 Pruned Mass (GeV)", "Jet 1 Double b Discriminant","Jet 2 Double b Discriminant", "Jet 1 #tau_{21}", "Jet 2 #tau_{21}"]
#	t1axis = ["Jet 2 Pruned Mass (GeV)", "Jet 1 Pruned Mass (GeV)"]
#t1axis = ["Minimum Pairwise Mass (GeV/c^{2})","m(top) (GeV/c^{2})","Number of Subjets","M_{t#bar{t}} (GeV/c^{2})","p_{T}(leptonic top) (GeV/c^{2})","p_{T}(lepton) (GeV/c^{2})","#eta(lepton) (GeV/c^{2})","#phi(lepton) (GeV/c^{2})","p_{T}(leading jet) (GeV/c^{2})","p_{T}(subleading jet) (GeV/c^{2})","p_{T}(jet 3) (GeV/c^{2})","p_{T}(jet 4) (GeV/c^{2})","#eta(leading jet) (GeV/c^{2})","#eta(subleading jet) (GeV/c^{2})","N_{btags}","E_{T}^{miss} (GeV/c^{2})","N_{jets}","H_{T}^{lep} (GeV/c^{2})","H_{T}^{tot} (GeV/c^{2})","Mass of Leptonic Top (GeV/c^{2})","#DeltaR_{min}","Invariant Mass of Jet 0 + 1 (GeV/c^{2})","Invariant Mass of Jet 0 + 2 (GeV/c^{2})","Invariant Mass of Jet 0 + 3 (GeV/c^{2})","Invariant Mass of Jet 0 + 4 (GeV/c^{2})","Invariant Mass of Jet 1 + 2 (GeV/c^{2})","Invariant Mass of Jet 1 + 3 (GeV/c^{2})","Invariant Mass of Jet 1 + 4 (GeV/c^{2})","Invariant Mass of Jet 2 + 3 (GeV/c^{2})","Invariant Mass of Jet 2 + 4 (GeV/c^{2})","Invariant Mass of Jet 3 + 4 (GeV/c^{2})","Mass of Hadronic Top (GeV/c^{2})"]
t1int = [[1.,1.,1.],[1.,1.,1.],[1.,1.,1.],[1.,1.,1.],[1.,1.,1.],[1.,1.,1.]]
#t1int = [[50,149.9],[140,249.99],[3.,10.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.],[500.,1000.]]
#t1rebins = [10,5,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
t1rebins = [1,1,1,1,1,1,1,1]
i=0
		    
if options.pt == 'high':
	t1hists = ["minPairHisthighpt","topTagMassHistpremasshighpt","nsjhighpt","pairmasshightpt"]
else:
	t1hists = ["hJet1PMass","hJet2PMass","hJet1bbtag","hJet2bbtag","hJet1tau21","hJet2tau21"]
	t1bin = [30,30,20,20,20,20]
	t1min = [50,50,-1,-1,0,0]
	t1max = [300,300,1,1,1,1]
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
	t1TT=fTTMC.Get(t1hist)
        #t1TT.Scale(xs[6]*lumi/nEvents[6])
	t1TT.SetLineColor(ROOT.kMagenta + 7)
        t1QCD300=fQCD300MC.Get(t1hist)
	#t1QCD300.Scale(xs[0]*lumi/nEvents[0])
        t1QCD300.SetLineColor(ROOT.kMagenta + 3)
	t1QCD500=fQCD500MC.Get(t1hist)
        #t1QCD500.Scale(xs[1]*lumi/nEvents[1])
	t1QCD500.SetLineColor(ROOT.kMagenta)
	t1QCD700=fQCD700MC.Get(t1hist)
        #t1QCD700.Scale(xs[2]*lumi/nEvents[2])
	t1QCD700.SetLineColor(ROOT.kMagenta - 3)
	t1QCD1000=fQCD1000MC.Get(t1hist)
        #t1QCD1000.Scale(xs[3]*lumi/nEvents[3])
	t1QCD1000.SetLineColor(ROOT.kRed)
	t1QCD1500=fQCD1500MC.Get(t1hist)
        #t1QCD1500.Scale(xs[4]*lumi/nEvents[4])
	t1QCD1500.SetLineColor(ROOT.kRed - 3)
	t1QCD2000=fQCD2000MC.Get(t1hist)
        #t1QCD2000.Scale(xs[5]*lumi/nEvents[5])
	t1QCD2000.SetLineColor(ROOT.kRed + 2)
	t1WP600=fWP600.Get(t1hist)
        #t1WP600.Scale(xs[7]*lumi/nEvents[7])
	t1WP600.SetLineColor( ROOT.kGreen - 7)
        t1WP650=fWP600.Get(t1hist)
        #t1WP650.Scale(xs[8]*lumi/nEvents[8])
        t1WP650.SetLineColor( ROOT.kGreen - 6)
        t1WP700=fWP600.Get(t1hist)
        #t1WP700.Scale(xs[9]*lumi/nEvents[9])
        t1WP700.SetLineColor( ROOT.kGreen - 5)
        t1WP750=fWP600.Get(t1hist)
        #t1WP750.Scale(xs[10]*lumi/nEvents[10])
        t1WP750.SetLineColor( ROOT.kGreen - 4)
        t1WP800=fWP600.Get(t1hist)
        #t1WP800.Scale(xs[11]*lumi/nEvents[11])
        t1WP800.SetLineColor( ROOT.kGreen - 3)
        t1WP900=fWP600.Get(t1hist)
        #t1WP900.Scale(xs[12]*lumi/nEvents[12])
        t1WP900.SetLineColor( ROOT.kGreen - 2)
	t1WP1000=fWP1000.Get(t1hist)
        #t1WP1000.Scale(xs[13]*lumi/nEvents[13])
	t1WP1000.SetLineColor( ROOT.kGreen)
        t1WP1200=fWP1000.Get(t1hist)
        #t1WP1200.Scale(xs[14]*lumi/nEvents[14])
        t1WP1200.SetLineColor( ROOT.kGreen - 1)
	t1WP1400=fWP1400.Get(t1hist)
        #t1WP1400.Scale(xs[15]*lumi/nEvents[15])
	t1WP1400.SetLineColor( ROOT.kGreen + 1)
        t1WP1600=fWP1000.Get(t1hist)
        #t1WP1600.Scale(xs[16]*lumi/nEvents[16])
        t1WP1600.SetLineColor( ROOT.kAzure - 3)
        t1WP1800=fWP1000.Get(t1hist)
        #t1WP1800.Scale(xs[17]*lumi/nEvents[17])
        t1WP1800.SetLineColor( ROOT.kAzure + 10)
	t1WP2000=fWP2000.Get(t1hist)
        #t1WP2000.Scale(xs[18]*lumi/nEvents[18])
	t1WP2000.SetLineColor( ROOT.kGreen + 2)
        t1WP2500=fWP2000.Get(t1hist)
        #t1WP2500.Scale(xs[19]*lumi/nEvents[19])
        t1WP2500.SetLineColor( ROOT.kBlue - 7)
	t1WP3000=fWP3000.Get(t1hist)
        #t1WP3000.Scale(xs[20]*lumi/nEvents[20])
	t1WP3000.SetLineColor( ROOT.kGreen + 3)
	t1WP4000=fWP4000.Get(t1hist)
        #t1WP4000.Scale(xs[21]*lumi/nEvents[21])
	t1WP4000.SetLineColor( ROOT.kGreen + 4)
        t1WP4500=fWP4000.Get(t1hist)
        #t1WP4500.Scale(xs[22]*lumi/nEvents[22])
        t1WP4500.SetLineColor( ROOT.kBlue)
	
#	t1data.SetMarkerStyle( 8 ) 
#
#	t1ttbar.SetMarkerStyle( 0 )
#	t1wjets.SetMarkerStyle( 0 )
#	t1sig.SetMarkerStyle( 0 )
#	t1zjets.SetFillColor( 30 )
#	t1zjets.SetMarkerStyle( 0 )
	happy = 0
	if happy==0:
		leg = ROOT.TLegend( 0.35, 0.41, 0.64, 0.89)
		leg.AddEntry( t1TT, 'TT', 'l')
                #leg.AddEntry( t1QCD300,  'QCD HT 300-500', 'l')
		leg.AddEntry( t1QCD500,  'QCD HT 500-700', 'l')
		leg.AddEntry( t1QCD700,  'QCD HT 700-1000', 'l')
		leg.AddEntry( t1QCD1000,  'QCD HT 1000-1500', 'l')
		leg.AddEntry( t1QCD1500,  'QCD HT 1500-2000', 'l')
		leg.AddEntry( t1QCD2000,  'QCD HT 2000-Inf', 'l')
		leg.AddEntry( t1WP600, 'Wp 600', 'l')
                leg.AddEntry( t1WP650, 'Wp 650', 'l')
                leg.AddEntry( t1WP700, 'Wp 700', 'l')
                leg.AddEntry( t1WP750, 'Wp 750', 'l')
                leg.AddEntry( t1WP800, 'Wp 800', 'l')
                leg.AddEntry( t1WP900, 'Wp 900', 'l')
		leg.AddEntry( t1WP1000, 'Wp 1000', 'l')
                leg.AddEntry( t1WP1200, 'Wp 1200', 'l')
		leg.AddEntry( t1WP1400, 'Wp 1400', 'l')
                leg.AddEntry( t1WP1600, 'Wp 1600', 'l')
                leg.AddEntry( t1WP1800, 'Wp 1800', 'l')
		leg.AddEntry( t1WP2000, 'Wp 2000', 'l')
                leg.AddEntry( t1WP2500, 'Wp 2500', 'l')
		leg.AddEntry( t1WP3000, 'Wp 3000', 'l')
                leg.AddEntry( t1WP4000, 'Wp 4000', 'l')
		leg.AddEntry( t1WP4500, 'Wp 4500', 'l')
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
	frame.SetMaximum(1.02)
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
        #t1QCD300.DrawNormalized('hist sames')
	t1QCD500.DrawNormalized('hist sames')
	t1QCD700.DrawNormalized('hist sames')
	t1QCD1000.DrawNormalized('hist sames')
	t1QCD1500.DrawNormalized('hist sames')
	t1QCD2000.DrawNormalized('hist sames')
        t1WP600.DrawNormalized('hist sames')
        t1WP650.DrawNormalized('hist sames')
        t1WP700.DrawNormalized('hist sames')
        t1WP750.DrawNormalized('hist sames')
        t1WP800.DrawNormalized('hist sames')
	t1WP900.DrawNormalized('hist sames')
	t1WP1000.DrawNormalized('hist sames')
        t1WP1200.DrawNormalized('hist sames')
	t1WP1400.DrawNormalized('hist sames')
        t1WP1600.DrawNormalized('hist sames')
        t1WP1800.DrawNormalized('hist sames')
	t1WP2000.DrawNormalized('hist sames')
        t1WP2500.DrawNormalized('hist sames')
	t1WP3000.DrawNormalized('hist sames')
        t1WP4000.DrawNormalized('hist sames')
	t1WP4500.DrawNormalized('hist sames')
	
	leg.Draw()

#	prelim = ROOT.TLatex()#
#	prelim.SetTextFont(42)
#	prelim.SetNDC()
 #       prelim.DrawLatex( 0.15, 0.91, "#scale[1.0]{CMS Preliminary #sqrt{s} = 8 TeV, 19.6 fb^{-1}}" )


#	c.Print( 'SUSYsemiLepMass_'+t1titles[i]+'.root', 'root')
	c.Print( 'SR_'+t1titles[i]+'.pdf', 'pdf')
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
