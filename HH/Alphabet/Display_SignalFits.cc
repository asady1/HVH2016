// Creates the images and HTML
// for displaying changes in Signal MC
// due to JEC+1-1, and JER+1-1

#include <TH1D.h>
#include <TH2F.h>
#include <TROOT.h>
#include <TFile.h>
#include <TTree.h>
#include <TSystem.h>
#include <TChain.h>
#include <TLorentzVector.h>
#include <TLegend.h>
#include <TCanvas.h>
#include <TProfile.h>
#include <iostream>
#include <TFractionFitter.h>
#include <TStyle.h>
#include <TPaveText.h>
#include <THStack.h>
#include <TArrow.h>
#include <TColor.h>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
#include "CMS_lumi.C"
#include "tdrstyle.C"

//#include "RooRealVar.h"
//#include "RooArgList.h"
//#include "RooChebychev.h"
/*#include "RooDataHist.h"
 #include "RooAbsPdf.h"
 #include "RooWorkspace.h"
 #include "RooPlot.h"
 #include "RooFitResult.h"
 #include "RooCBShape.h"
 #include "RooGaussian.h"
 */
int iPeriod = 4;    // 1=7TeV, 2=8TeV, 3=7+8TeV, 7=7+8+13TeV
int iPos =11;

bool _antitag=false;

int rebin=1;
ofstream outfile;

std::string tostr(float t, int precision=0)
{
    std::ostringstream os;
    os<<std::setprecision(precision)<<t;
    return os.str();
}

double quad(double a, double b, double c=0, double d=0, double e=0, double f=0, double g=0, double h=0, double i=0, double j=0, double k=0)
{
    return pow(a*a+b*b+c*c+d*d+e*e+f*f+g*g+h*h+i*i+j*j+k*k, 0.5);
}

struct Params
{
    double sg_p0;
    double sg_p1;
    double sg_p2;
    double sg_p3;
    double sg_p4;
    double sg_p5;
    double sg_p6;
    double sg_p0_err;
    double sg_p1_err;
    double sg_p2_err;
    double sg_p3_err;
    double sg_p4_err;
    double sg_p5_err;
    double sg_p6_err;
};


RooPlot* fitSignal(std::string dirName, TH1D *h, int massNum, std::string mass, int color, TLegend *leg, Params &params, bool kinFit=false)
{
    
    RooRealVar *x, *sg_p0, *sg_p1, *sg_p2, *sg_p3, *sg_p4, *sg_p5, *sg_p6, *sg_p7, *sg_p8;
    //x=new RooRealVar("x", "m_{X} (GeV)", 600., 3200.);
    
    double massL = double(massNum);
    double rangeLo=TMath::Max(600., massL-0.3*massL), rangeHi=TMath::Min(3600., massL+0.3*massL);
    
    sg_p0=new RooRealVar((std::string("sg_p0")).c_str(), "sg_p0", massL, massL-0.1*massL, massL+0.1*massL);
    sg_p1=new RooRealVar((std::string("sg_p1")).c_str(), "sg_p1", 0.03*massL, 5., 400.);
    sg_p2=new RooRealVar((std::string("sg_p2")).c_str(), "sg_p2", 1.3, 0., 200.);
    sg_p3=new RooRealVar((std::string("sg_p3")).c_str(), "sg_p3", 5, 0., 300.);
    sg_p4=new RooRealVar((std::string("sg_p4")).c_str(), "sg_p4", massL, 500., 800.);
    sg_p5=new RooRealVar((std::string("sg_p5")).c_str(), "sg_p5", 150, 0., 3000.);
    //sg_p6=new RooRealVar((std::string("sg_p6")).c_str(), "sg_p6", 0.99, 0.,1.);
        sg_p6=new RooRealVar((std::string("sg_p6")).c_str(), "sg_p6", 0.99, 0.,1.);
    
    x=new RooRealVar("x", "m_{X} (GeV)", 600., 3600.);
    RooCBShape signalCore((std::string("signalCore")).c_str(), "signalCore", *x, *sg_p0, *sg_p1,*sg_p2, *sg_p3);
    RooGaussian signalComb((std::string("signalComb")).c_str(), "Combinatoric", *x, *sg_p0, *sg_p5);
    RooAddPdf signal((std::string("signal")).c_str(), "signal", RooArgList(signalCore, signalComb), *sg_p6);
    
    RooDataHist signalHistogram((std::string("signalHistogram")).c_str(), "Signal Histogram", RooArgList(*x), h);
    //signal.fitTo(signalHistogram, RooFit::Range(rangeLo, rangeHi), RooFit::Save());
    signal.fitTo(signalHistogram, RooFit::Hesse(false), RooFit::Range(rangeLo, rangeHi), RooFit::Save());

    params.sg_p0=sg_p0->getVal(); params.sg_p0_err=sg_p0->getError();
    params.sg_p1=sg_p1->getVal(); params.sg_p1_err=sg_p1->getError();
    params.sg_p2=sg_p2->getVal(); params.sg_p2_err=sg_p2->getError();
    params.sg_p3=sg_p3->getVal(); params.sg_p3_err=sg_p3->getError();
    params.sg_p4=sg_p0->getVal(); params.sg_p4_err=sg_p0->getError();
    params.sg_p5=sg_p5->getVal(); params.sg_p5_err=sg_p5->getError();
    params.sg_p6=sg_p6->getVal(); params.sg_p6_err=sg_p6->getError();
    RooPlot *plot=x->frame();
    if (color==kBlack)
    {
        signalHistogram.plotOn(plot, RooFit::MarkerColor(color), RooFit::MarkerSize(1.2));
        signal.plotOn(plot, RooFit::LineColor(color), RooFit::LineWidth(3));
    }
    else
    {
        signalHistogram.plotOn(plot, RooFit::MarkerColor(color));
        signal.plotOn(plot, RooFit::LineColor(color), RooFit::LineWidth(0));
    }
    leg->AddEntry((TObject*)0, ("#mu_{CB}= "+tostr(sg_p0->getVal(),4)+" #pm "+tostr(sg_p0->getError(),2)+" GeV").c_str(), "");
    leg->AddEntry((TObject*)0, ("#sigma_{CB}= "+tostr(sg_p1->getVal(),2)+" #pm "+tostr(sg_p1->getError(),2)+" GeV").c_str(), "");
    
    // std::cout<<"chi2/dof = "<<plot->chiSquare()<<std::endl;
    
    if (color==kBlack)
    {
        RooRealVar signal_p0((std::string("signal_p0_")).c_str(), "signal_p0", sg_p0->getVal());
        RooRealVar signal_p1((std::string("signal_p1_")).c_str(), "signal_p1", sg_p1->getVal());
        RooRealVar signal_p2((std::string("signal_p2_")).c_str(), "signal_p2", sg_p2->getVal());
        RooRealVar signal_p3((std::string("signal_p3_")).c_str(), "signal_p3", sg_p3->getVal());
        RooRealVar signal_p4((std::string("signal_p4_")).c_str(), "signal_p4", sg_p0->getVal());
        RooRealVar signal_p5((std::string("signal_p5_")).c_str(), "signal_p5", sg_p5->getVal());
        RooRealVar signal_p6((std::string("signal_p6_")).c_str(), "signal_p6", sg_p6->getVal());
        //RooGaussian signal_fixed("signal_fixed", "Signal Prediction", *x, signal_p0, signal_p1);
        RooCBShape signalCore_fixed((std::string("signalCore_fixed_")).c_str(), "signalCore", *x, signal_p0, signal_p1,signal_p2, signal_p3);
        RooGaussian signalComb_fixed((std::string("signalComb_fixed_")).c_str(), "Combinatoric", *x, signal_p0, signal_p5);
	string WhichString;
	if (_antitag) WhichString = "signal_fixed_antitag_";
	else WhichString = "signal_fixed_";
	RooAddPdf signal_fixed((WhichString).c_str(), "signal", RooArgList(signalCore_fixed, signalComb_fixed), signal_p6);
        RooWorkspace *w=new RooWorkspace("HH4b");
        w->import(signal_fixed);
	if (_antitag) w->SaveAs((dirName+"/w_signal_antitag_"+mass+".root").c_str());
	else w->SaveAs((dirName+"/w_signal_"+mass+".root").c_str());
	w->Print();
    }
    return plot;
}

double lnN(double b, double a, double c)
{
    // std::cout<<"a = "<<a<<", b = "<<b<<", c = "<<c<<std::endl;
    // std::cout<<"1.+(a-c)/(2.*b) = "<<1.+fabs(a-c)/(2.*b)<<std::endl;
    double err=0;
    if (b>0) err=1.+fabs(a-c)/(2.*b);
    return err;
}

int Display_SignalFits(std::string dir_preselection="outputs/datacards/",
                       std::string dir_selection="",
                       std::string file_histograms="HH_mX_HH_LL_",
                       int imass=1600,
                       int rebin_factor = 1,
		       bool antitag = false,
                       bool focus=false)
{
    _antitag = antitag;  
     
    writeExtraText = true;       // if extra text
    extraText  = "Simulation";  // default extra text is "Preliminary"
    lumi_13TeV  = "27.2 fb^{-1} (2016)"; // default is "19.7 fb^{-1}"
    
    rebin = rebin_factor;
    
    std::vector<std::string> masses;
    std::cout<<" starting with "<<imass<<std::endl;
    stringstream iimass ;
    iimass << imass;
    masses.push_back(iimass.str());
    
    std::string dirName = "outputs/datacards/";
    
    std::string file_postfix = std::string("_13TeV.root");
    std::cout<< " file input "<< file_postfix<<std::endl;
    
    //gROOT->SetStyle("Plain");
    gStyle->SetOptStat(000000000);
    gStyle->SetPadGridX(0);
    gStyle->SetPadGridY(0);
    gStyle->SetOptStat(0000);
    setTDRStyle();
    
    // Calculate nSignal events given production cross section, branching fractions and efficiency
    //double totalLumi=2.690; // /fb
    //double prodXsec_1=1.; // fb
    
    // Interpolation Plots
    std::vector<double> v_sg_p0, v_sg_p0_err;
    std::vector<double> v_sg_p1, v_sg_p1_err;
    std::vector<double> v_sg_p2, v_sg_p2_err;
    std::vector<double> v_sg_p3, v_sg_p3_err;
    std::vector<double> v_sg_p4, v_sg_p4_err;
    std::vector<double> v_sg_p5, v_sg_p5_err;
    std::vector<double> v_sg_p6, v_sg_p6_err;
    
    
    for (unsigned int i=0; i<masses.size(); ++i) {
        std::cout<<" OPENING FILE: " << (dir_preselection+"/"+file_histograms+masses.at(i)+file_postfix).c_str() <<std::endl;
        TFile *file = new TFile((dir_preselection+"/"+file_histograms+masses.at(i)+file_postfix).c_str());
	TH1D *h_mX_SR;
	std::cout<<"Loading histograms"<<std::endl;
	if (antitag)
		{
			std::cout<<"looking for "<<("vh/Signal_mX_antitag_"+masses.at(i)+"_test").c_str()<<std::endl;
			h_mX_SR=(TH1D*)file->Get(("vh/Signal_mX_antitag_"+masses.at(i)+"_test").c_str());
			h_mX_SR->SetTitle(("m_{X} Peak in Signal MC (m_{X}="+masses.at(i)+" GeV); m_{X} (GeV)").c_str());
		}
	else
		{
			std::cout<<"looking for "<<("Signal_mX_"+masses.at(i)+"_").c_str()<<std::endl;
			h_mX_SR=(TH1D*)file->Get(("vh/Signal_mX_"+masses.at(i)+"_test").c_str());
			h_mX_SR->SetTitle(("m_{X} Peak in Signal MC (m_{X}="+masses.at(i)+" GeV); m_{X} (GeV)").c_str());
		}
	std::cout<<" FILE OPENED, DONE!: "<<std::endl;
        std::cout<< "distribs_5_10_0__x"<<std::endl;
        
        double nSignal_init=1.0;
        double xPad = 0.3;
        TCanvas *c_mX_SR=new TCanvas(("c_mX_SR_"+masses.at(i)).c_str(), ("c_mX_SR_"+masses.at(i)+"HH_TT").c_str(), 700*(1.-xPad), 700);
        TPad *p_1=new TPad("p_1", "p_1", 0, xPad, 1, 1);
        p_1->SetFillStyle(4000);
        p_1->SetFrameFillColor(0);
        p_1->SetBottomMargin(0.02);
        p_1->SetTopMargin(0.06);

        TPad* p_2 = new TPad("p_2", "p_2",0,0,1,xPad);
        p_2->SetBottomMargin((1.-xPad)/xPad*0.13);
        p_2->SetTopMargin(0.03);
        p_2->SetFillColor(0);
        p_2->SetBorderMode(0);
        p_2->SetBorderSize(2);
        p_2->SetFrameBorderMode(0);
        p_2->SetFrameBorderMode(0);
        
        p_1->Draw();
        p_2->Draw();
        p_1->cd();
	std::cout<<"first"<<std::endl;
        	
	std::cout<<"Title"<<std::endl;
        h_mX_SR->Rebin(rebin);
	std::cout<<"rebin"<<std::endl;
        std::cout<<" norm = "<<h_mX_SR->Integral(h_mX_SR->FindBin(1200),h_mX_SR->FindBin(2500))<<std::endl;	
        
        TLegend *leg = new TLegend(0.75,0.75,0.5,0.9,NULL,"brNDC");
        leg->SetBorderSize(0);
        leg->SetTextSize(0.035);
        leg->SetTextFont(42);
        leg->SetLineColor(1);
        leg->SetLineStyle(1);
        leg->SetLineWidth(2);
        leg->SetFillColor(0);
        leg->SetFillStyle(0);
        leg->SetTextFont(42);

        
        leg->AddEntry(h_mX_SR, "Signal MC");
	h_mX_SR->Sumw2();
        Params params_vg;
        RooPlot *plot_vg=fitSignal(dirName,h_mX_SR, imass, masses.at(i), kBlack, leg, params_vg,true);
        v_sg_p0.push_back(params_vg.sg_p0); v_sg_p0_err.push_back(params_vg.sg_p0_err);
        v_sg_p1.push_back(params_vg.sg_p1); v_sg_p1_err.push_back(params_vg.sg_p1_err);
        v_sg_p2.push_back(params_vg.sg_p2); v_sg_p2_err.push_back(params_vg.sg_p2_err);
        v_sg_p3.push_back(params_vg.sg_p3); v_sg_p3_err.push_back(params_vg.sg_p3_err);
        v_sg_p4.push_back(params_vg.sg_p4); v_sg_p4_err.push_back(params_vg.sg_p4_err);
        v_sg_p5.push_back(params_vg.sg_p5); v_sg_p5_err.push_back(params_vg.sg_p5_err);
        v_sg_p6.push_back(params_vg.sg_p6); v_sg_p6_err.push_back(params_vg.sg_p6_err);
        

        
        plot_vg->SetTitle("");
        plot_vg->GetYaxis()->SetRangeUser(0.01, 100);
        plot_vg->GetXaxis()->SetRangeUser(imass-400, imass+400);
        plot_vg->GetXaxis()->SetLabelOffset(0.03);
        plot_vg->GetXaxis()->SetNdivisions(505);
	std::cout<<"middle"<<std::endl;

        
        plot_vg->Draw("same");
        leg->SetFillColor(0);
        leg->Draw();
        
        CMS_lumi(p_1, iPeriod, iPos );
        
        p_2->cd();
        RooHist* hpull;
        hpull = plot_vg->pullHist();
        RooRealVar* x=new RooRealVar("x", "m_{X} (GeV)", 1000, 3000);

        RooPlot* frameP = x->frame() ;
        frameP->SetTitle("");
        frameP->GetXaxis()->SetRangeUser(1000,3000);

        frameP->addPlotable(hpull,"P");
        frameP->GetYaxis()->SetRangeUser(-5,5);
        frameP->GetYaxis()->SetNdivisions(505);
        frameP->GetXaxis()->SetNdivisions(505);
        frameP->GetYaxis()->SetTitle("Pull");
        
        frameP->GetYaxis()->SetTitleSize((1.-xPad)/xPad*0.06);
        frameP->GetYaxis()->SetTitleOffset(1.2/((1.-xPad)/xPad));
        frameP->GetXaxis()->SetTitleSize((1.-xPad)/xPad*0.06);
        frameP->GetXaxis()->SetLabelSize((1.-xPad)/xPad*0.05);
        frameP->GetYaxis()->SetLabelSize((1.-xPad)/xPad*0.05);
        
        
        frameP->Draw();
        
        
        c_mX_SR->SaveAs((dirName+"/c_mX_SR_"+masses.at(i)+".png").c_str());
        c_mX_SR->SaveAs((dirName+"/c_mX_SR_"+masses.at(i)+".root").c_str());
        p_1->SetLogy();
        
        c_mX_SR->SaveAs((dirName+"/c_mX_SR_"+masses.at(i)+"Log.png").c_str());
        c_mX_SR->SaveAs((dirName+"/c_mX_SR_"+masses.at(i)+"Log.root").c_str());
	std::cout<<"last"<<std::endl;
        
    }
    
    return 0;
}

