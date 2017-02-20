#include <iostream>

#include <TROOT.h>
#include <TSystem.h>
#include <TMath.h>
#include <TFile.h>
#include <TF1.h>
#include <TH1F.h>
#include <TProfile.h>
#include <THStack.h>
#include <TGraphErrors.h>
#include <TStyle.h>
#include <TPaveText.h>
#include <TLegend.h>
#include <TCanvas.h>


/*#include <RooFit.h>
 #include <RooHist.h>
 #include <RooDataHist.h>
 #include <RooGenericPdf.h>
 #include <RooRealVar.h>
 #include <RooPlot.h>
 */

#include "CMS_lumi.C"
#include "tdrstyle.C"

using namespace RooFit;
int iPeriod = 4;    // 1=7TeV, 2=8TeV, 3=7+8TeV, 7=7+8+13TeV
int iPos =11;
bool bias= false;
bool blind = false;
bool LLregion = false;
bool isQCD = true;

double rebin = 1;

std::string tags="nominal"; // MMMM

double SR_lo=1100.;
double SR_hi=3300.;

Double_t ErfExp(Double_t x, Double_t c, Double_t offset, Double_t width){
    if(width<1e-2)width=1e-2;
    if (c==0)c=-1e-7;
    return TMath::Exp(c*x)*(1.+TMath::Erf((x-offset)/width))/2. ;
}

std::string tostr(float t, int precision=0)
{
    std::ostringstream os;
    os<<std::setprecision(precision)<<t;
    return os.str();
}

double quad(double a, double b, double c=0, double d=0, double e=0, double f=0)
{
    return pow(a*a+b*b+c*c+d*d+e*e+f*f, 0.5);
}

std::string itoa(int i)
{
    char res[10];
    sprintf(res, "%d", i);
    std::string ret(res);
    return ret;
}


TCanvas* comparePlots2(RooPlot *plot_bC, RooPlot *plot_bS, TH1F *data, TH1F *qcd, std::string title)
{
    
    RooRealVar x("x", "m_{X} (GeV)", SR_lo, SR_hi);
    TCanvas *c=new TCanvas(("c_RooFit_"+title).c_str(), "c", 700, 700);
    TPad *p_1=new TPad("p_1", "p_1", 0, 0.35, 1, 1);
    gStyle->SetPadGridX(0);
    gStyle->SetPadGridY(0);
    gROOT->SetStyle("Plain");
    p_1->SetFrameFillColor(0);
    TPad *p_2 = new TPad("p_2", "p_2",0,0.003740648,0.9975278,0.3391022);
    p_2->Range(160.1237,-0.8717948,1008.284,2.051282);
    p_2->SetFillColor(0);
    p_2->SetBorderMode(0);
    p_2->SetBorderSize(2);
    p_2->SetTopMargin(0.02);
    p_2->SetBottomMargin(0.3);
    p_2->SetFrameBorderMode(0);
    p_2->SetFrameBorderMode(0);
    
    p_1->Draw();
    p_2->Draw();
    p_1->cd();
    double maxdata=data->GetMaximum();
    double maxqcd=qcd->GetMaximum();
    double maxy=(maxdata>maxqcd) ? maxdata : maxqcd;
    
    title=";m_{X} (GeV); Events / "+itoa(data->GetBinWidth(1))+" GeV";
    p_1->DrawFrame(SR_lo, 0, SR_hi, maxy*1., title.c_str());
    plot_bS->SetMarkerStyle(20);
    plot_bS->Draw("same");
    // plot_bS->Draw("same");
    CMS_lumi( p_1, iPeriod, iPos );
    p_2->cd();
    

    RooHist* hpull;
    hpull = plot_bS->pullHist();
    hpull->GetXaxis()->SetRangeUser(SR_lo, SR_hi);
    RooPlot* frameP = x.frame() ;
    frameP->SetTitle("");
    frameP->GetYaxis()->SetTitle("Pull");
    frameP->GetXaxis()->SetRangeUser(SR_lo, SR_hi);
    
    frameP->addPlotable(hpull,"P");
    frameP->GetYaxis()->SetTitle("Pull");
    
    frameP->GetYaxis()->SetTitleSize(0.07);
    frameP->GetYaxis()->SetTitleOffset(0.5);
    frameP->GetXaxis()->SetTitleSize(0.09);
    frameP->GetXaxis()->SetTitleOffset(1.0);
    frameP->GetXaxis()->SetLabelSize(0.07);
    frameP->GetYaxis()->SetLabelSize(0.06);
    
    frameP->Draw();
    
    
    //  TLine *m_one_line = new TLine(SR_lo,1,SR_hi,1);
    
    
    // h_ratio->Draw("");
    // m_one_line->Draw("same");
    p_1->cd();
    return c;
}

void Background(int rebin_factor=rebin,int model_number = 0,int imass=750, bool plotBands = false)
{
    rebin = rebin_factor;
    std::string fname;
    if (LLregion) {
      if(isQCD){
	fname.assign("outputs/HHSR_LL.root");
	cout << "QCD LL" << endl;
      }
      else{
	fname.assign("outputs/HHSR_LL_Data.root");
	cout << "Data LL" << endl;
      }
    }else{
      if(isQCD){
	fname.assign("outputs/HHSR_TT.root");
	cout << "QCD TT" << endl;
      }
      else{
	fname.assign("outputs/HHSR_TT_Data.root");
	cout << "Data TT" << endl;
      }
    }

    stringstream iimass ;
    iimass << imass;
    std::string dirName = "outputs/datacards/";
    
    
    gStyle->SetOptStat(000000000);
    gStyle->SetPadGridX(0);
    gStyle->SetPadGridY(0);
    
    setTDRStyle();
    gStyle->SetPadGridX(0);
    gStyle->SetPadGridY(0);
    gStyle->SetOptStat(0000);
    
    writeExtraText = true;       // if extra text
    extraText  = "Preliminary";  // default extra text is "Preliminary"
    lumi_13TeV  = "36.8 fb^{-1} (2016)"; // default is "19.7 fb^{-1}"
    lumi_7TeV  = "4.9 fb^{-1}";  // default is "5.1 fb^{-1}"
    
    
    double ratio_tau=-1;
    
    TFile *f=new TFile(fname.c_str());
    TH1F *h_mX_EST=(TH1F*)f->Get("est")->Clone("alphabet");
    double NormOfEst = h_mX_EST->Integral();
    h_mX_EST->Draw("hist");
    double OverAllIntegral = h_mX_EST->Integral();
    TH1F *h_mX_EST_antitag=(TH1F*)f->Get("antitag")->Clone("alphabet_SB");	
    double NormOfEst_AT= h_mX_EST_antitag->Integral();
    double AllOfEst_AT= h_mX_EST_antitag->Integral();
    std::cout<<"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"<<std::endl;
    std::cout<<"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"<<std::endl;
    std::cout<<"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"<<std::endl;
    std::cout<<"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"<<std::endl;
    std::cout<<"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"<<std::endl;
    std::cout<<"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"<<std::endl;
    std::cout<<OverAllIntegral<<std::endl;
    std::cout<<NormOfEst<<std::endl;
    std::cout<<AllOfEst_AT<<std::endl;
    std::cout<<NormOfEst_AT<<std::endl;
    	
    TH1F *h_mX_SR=(TH1F*)f->Get("data")->Clone("The_SR");
    double maxdata = h_mX_SR->GetMaximum();
	 std::cout<<"Open ... "<<std::endl;
    double nEventsSR = h_mX_SR->Integral(h_mX_SR->FindBin(1100),h_mX_SR->FindBin(3300));
//    double nEventsSR = h_mX_SR->Integral(h_mX_SR->FindBin(1200),h_mX_SR->FindBin(2500));
    ratio_tau=(h_mX_SR->GetSumOfWeights()/(h_mX_EST->GetSumOfWeights()));
    //double nEventsSR = h_mX_SR->Integral(600,4000);

    TH1F *LinCalcNum=(TH1F*)f->Get("data")->Clone("numer");
    TH1F *LinCalcDen=(TH1F*)f->Get("antitag")->Clone("denom");
    LinCalcNum->Divide(LinCalcDen);
    TFitResultPtr rLin = LinCalcNum->Fit("pol1", "SQ0");
    double mjjlinINIT = rLin->Parameter(1);
    double mjjlinINITerror = rLin->ParError(1);
    std::cout<<"Linear Rpf term:  "<<mjjlinINIT<<" / "<<mjjlinINITerror<<std::endl;
    
    std::cout<<"ratio tau "<<ratio_tau<<std::endl;
    
    TH1F *h_SR_Prediction;
    TH1F *h_SR_Prediction2;
    
    if(blind) {
        h_SR_Prediction2 = (TH1F*)h_mX_EST->Clone("h_SR_Prediction2");
        h_mX_EST->Rebin(rebin);
	h_mX_EST_antitag->Rebin(rebin);
        h_mX_EST->SetLineColor(kBlack);
        h_SR_Prediction=(TH1F*)h_mX_EST_antitag->Clone("h_SR_Prediction");
//        h_SR_Prediction=(TH1F*)h_mX_EST->Clone("h_SR_Prediction");

    } else {
        h_SR_Prediction2=(TH1F*)h_mX_EST_antitag->Clone("h_SR_Prediction2");
	h_SR_Prediction2->Rebin(rebin);
        h_mX_SR->Rebin(rebin);
        h_mX_SR->SetLineColor(kBlack);
        h_SR_Prediction=(TH1F*)h_mX_SR->Clone("h_SR_Prediction");
        
    }
    h_SR_Prediction->SetMarkerSize(0.7);
    h_SR_Prediction->GetYaxis()->SetTitleOffset(1.2);
    
     

     RooRealVar x("x", "m_{X} (GeV)", SR_lo, SR_hi);

     TRandom3 R;	
     double normWeight, normWeight2, rnd, intPart, resid;

     for (int i = 1; i <  h_mX_EST_antitag->GetNbinsX()+1; i++){
       double N= h_mX_EST_antitag->GetBinContent(i);
       int intPart = TMath::Nint(N);
       double resid = intPart - N;
       double rnd = R.Uniform(1.);
       if (resid > 0) normWeight = rnd > resid ? intPart : intPart-1; 
       else normWeight = rnd > fabs(resid) ?  intPart+0. : intPart+1.; 
       h_mX_EST_antitag->SetBinContent(i, normWeight);
     }

     cout << "SR integral = " << h_mX_SR->Integral(h_mX_SR->FindBin(1100),h_mX_SR->FindBin(3300)) << endl;
     
     for (int i = 0; i <  h_mX_EST->GetNbinsX()+1; i++){
       double M =  h_mX_EST->GetBinContent(i);
       intPart = TMath::Nint(M);		
       resid = intPart - M;	
       double rnd = R.Uniform(1.);
       if (resid > 0) normWeight2 = rnd > resid ? intPart : intPart-1.;
       else normWeight2 = rnd > fabs(resid) ?  intPart+0. : intPart+1.;	
       h_mX_EST->SetBinContent(i, normWeight2);
     }
     

     normWeight = h_mX_EST_antitag->Integral();
     normWeight2 = h_mX_EST->Integral();
    
     cout << " normWeight = " << normWeight << " normWeight2 = " << normWeight2 << endl;   

 
    RooRealVar nBackgroundSB((std::string("bgSB_")+std::string("_norm")).c_str(),"nbkg",normWeight);
    
    RooRealVar nBackground((std::string("n_exp_binHH4b_proc_EST_")+std::string("_norm")).c_str(),"nbkg",normWeight2);
    
    
    RooRealVar bg_p1_LL((std::string("bg_p1_LL_")).c_str(), "bg_p1",  -10, 10.);
    RooRealVar bg_p2_LL((std::string("bg_p2_LL_")).c_str(), "bg_p2",  -10, 10.);
    RooRealVar bg_p1_TT((std::string("bg_p1_TT_")).c_str(), "bg_p1",  -10, 10.);
    RooRealVar bg_p2_TT((std::string("bg_p2_TT_")).c_str(), "bg_p2",  -10, 10.);
    RooRealVar mjjlin_TT((std::string("mjjlin_TT_")).c_str(), "mjjlin_TT",  -0.1, 0.1);
    RooRealVar mjjlin_LL((std::string("mjjlin_LL_")).c_str(), "mjjlin_LL",  -0.1, 0.1);


//    RooGenericPdf bg = RooGenericPdf((std::string("bg_")).c_str(),"exp(-@0*@2/(1+(@0*@1*@2)))",RooArgList(x,bg_p1,bg_p2));
//    RooGenericPdf bg;
//    RooGenericPdf bgSB;
    RooGenericPdf bg_LL = RooGenericPdf((std::string("bg_")).c_str(),"(1 + @0*@3)*exp(-@0*@2/(1+(@0*@1*@2)))",RooArgList(x,bg_p1_LL,bg_p2_LL,mjjlin_LL));
    RooGenericPdf bg_TT = RooGenericPdf((std::string("bg_")).c_str(),"(1 + @0*@3)*exp(-@0*@2/(1+(@0*@1*@2)))",RooArgList(x,bg_p1_TT,bg_p2_TT,mjjlin_TT));
    RooGenericPdf bgSB_LL = RooGenericPdf((std::string("bgSB_")).c_str(),"exp(-@0*@2/(1+(@0*@1*@2)))",RooArgList(x,bg_p1_LL,bg_p2_LL));
    RooGenericPdf bgSB_TT = RooGenericPdf((std::string("bgSB_")).c_str(),"exp(-@0*@2/(1+(@0*@1*@2)))",RooArgList(x,bg_p1_TT,bg_p2_TT));
/*    if (LLregion){
      bg.RooGenericPdf(bg_LL_temp);
      bgSB.RooGenericPdf(bgSB_LL_temp);
    }
    else{
      bg.RooGenericPdf(bg_TT_temp);
      bgSB.RooGenericPdf(bgSB_TT_temp);
    }*/
//    RooGenericPdf bg = RooGenericPdf((std::string("bg_")).c_str(),"(1 + @0*@3)*exp(-@0*@2/(1+(@0*@1*@2)))",RooArgList(x,bg_p1_LL,bg_p2_LL,mjjlin_LL));
//    RooGenericPdf bgSB = RooGenericPdf((std::string("bgSB_")).c_str(),"exp(-@0*@2/(1+(@0*@1*@2)))",RooArgList(x,bg_p1_LL,bg_p2_LL));
    
    string name_output = "CR_RooFit_Exp";
    
    std::cout<<"Nevents "<<nEventsSR<<std::endl;

    h_mX_EST_antitag->Sumw2();
    h_mX_SR->Sumw2();

    RooDataHist pred2("pred2", "Prediction from SB", RooArgList(x));
    RooDataHist tmp_antitag("tmp","tmp", RooArgList(x),h_mX_EST_antitag);
    RooDataHist tmp_SR("tmp2","tmp2", RooArgList(x), h_mX_SR);
    RooDataHist pred("pred", "Prediction from SB", RooArgList(x), h_SR_Prediction); // MARC I THINK YOU SHOULD LOOK HERE SEARCH FOR ME! SEAACH FOR ME
    if (blind) {
	pred2.add(tmp_antitag);
    } else {
	pred2.add(tmp_SR);
    }

////////////////////////////////////////////////////////////
// Post Fit Info
////////////////////////////////////////////////////////////
    Fit0 = TF1("Fit0","(1 + x*[3])*[2]*exp(-x*[1]/(1+(x*[0]*[1])))",1100.,4000.);
    Fit0.SetParameter(0,0.0303868843789);
    Fit0.SetParameter(1,0.0143760376205);
    Fit0.SetParameter(2,1);
    Fit0.SetParameter(3,0.0000360527817108);

    integral = Fit0.Integral(1100,3300);
    std::cout <<"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << std::endl;
    std::cout <<"integral = " << integral << std::endl;

    Fit0.SetParameter(2,5657.76867962/integral);
    Fit0.SetLineColor(kGreen);

    RooRealVar postfit_1((std::string("postfit_1")).c_str(), "bg_p1",  -10, 10.);
    RooRealVar postfit_2((std::string("postfit_2")).c_str(), "bg_p2",  -10, 10.);
    RooRealVar postfit_3((std::string("postfit_3")).c_str(), "bg_norm",  -10, 30000.);
    RooRealVar postfit_4((std::string("postfit_4")).c_str(), "mjjlin",  -10, 10.);
    postfit_1.setVal(0.0303868843789);
    postfit_2.setVal(0.0143760376205);
    postfit_3.setVal(5657.76867962/integral);
    postfit_4.setVal(0.0000360527817108);


    RooGenericPdf fit0 = RooGenericPdf((std::string("postfit")).c_str(),"(1 + @0*@4)*@3*exp(-@0*@2/(1+(@0*@1*@2)))",RooArgList(x,postfit_1,postfit_2,postfit_3,postfit_4));

/*    Fit0 = TF1("Fit0","[2]*exp(-x*[0]*[1]/(1+(x*[0]*[1])))",1100.,4000.);
    Fit0.SetParameter(0,0.0238711693372);
    Fit0.SetParameter(1,0.00938185642235);
    Fit0.SetParameter(2,1);

    integral = Fit0.Integral(1100,3300);

    Fit0.SetParameter(2,8158.98838689/integral);
    Fit0.SetLineColor(kGreen);

    RooRealVar postfit_1((std::string("postfit_1")).c_str(), "bg_p1",  -10, 10.);
    RooRealVar postfit_2((std::string("postfit_2")).c_str(), "bg_p2",  -10, 10.);
    RooRealVar postfit_3((std::string("postfit_3")).c_str(), "bg_norm",  -10, 30000.);
    RooRealVar postfit_4((std::string("postfit_4")).c_str(), "mjjlin",  -10, 10.);
    postfit_1.setVal(0.0238711693372);
    postfit_2.setVal(0.00938185642235);
    postfit_3.setVal(8158.98838689/integral);
    postfit_4.setVal(-0.0000328167316498);

    RooGenericPdf fit0 = RooGenericPdf((std::string("postfit")).c_str(),"@3*exp(-@0*@2/(1+(@0*@1*@2)))",RooArgList(x,postfit_1,postfit_2,postfit_3));*/

///////////////////////////////////////////////////////////
// Post Fit With No Correction
///////////////////////////////////////////////////////////
    Fit1 = TF1("Fit1","[2]*exp(-x*[1]/(1+(x*[0]*[1])))",1100.,4000.);
    Fit1.SetParameter(0,0.030408080199);
    Fit1.SetParameter(1,0.0143763150691);
    Fit1.SetParameter(2,1);

    integral2 = Fit1.Integral(1100,3300);

    Fit1.SetParameter(2,5657.82088054/integral2);
    Fit1.SetLineColor(kGreen);

    RooRealVar postfit1_1((std::string("postfit1_1")).c_str(), "bg_p1",  -10, 10.);
    RooRealVar postfit1_2((std::string("postfit1_2")).c_str(), "bg_p2",  -10, 10.);
    RooRealVar postfit1_3((std::string("postfit1_3")).c_str(), "bg_norm",  -10, 30000.);
    postfit1_1.setVal(0.030408080199);
    postfit1_2.setVal(0.0143763150691);
    postfit1_3.setVal(5657.82088054/integral2);

    RooGenericPdf fit1 = RooGenericPdf((std::string("postfit1")).c_str(),"@3*exp(-@0*@2/(1+(@0*@1*@2)))",RooArgList(x,postfit1_1,postfit1_2,postfit1_3));

    RooFitResult *r_bg;
    if (LLregion){
      r_bg = bg_LL.fitTo(pred, RooFit::Minimizer("Minuit2"), RooFit::Range(SR_lo, SR_hi), RooFit::SumW2Error(kTRUE), RooFit::Save());
    }else{
      r_bg = bg_TT.fitTo(pred, RooFit::Minimizer("Minuit2"), RooFit::Range(SR_lo, SR_hi), RooFit::SumW2Error(kTRUE), RooFit::Save());
    }
//    RooFitResult *r_bg=bg.fitTo(pred, RooFit::Minimizer("Minuit2"), RooFit::Range(SR_lo, SR_hi), RooFit::SumW2Error(kTRUE), RooFit::Save());

    const TMatrixDSym& cor = r_bg->covarianceMatrix();
 
    std::cout<<"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << std::endl;
    std::cout<<"Covariance Matrix = " <<  endl;
    cor.Print();
    
    RooPlot *aC_plot=x.frame();

    pred2.plotOn(aC_plot, RooFit::MarkerColor(kBlack));


//  PLOTTING THE POST FIT

    if (LLregion){
      bg_LL.plotOn(aC_plot, RooFit::LineColor(kBlue));
    }else{
      bg_TT.plotOn(aC_plot, RooFit::LineColor(kBlue));
    }
    
    TGraph* error_curve[5]; //correct error bands
    TGraphAsymmErrors* dataGr = new TGraphAsymmErrors(h_SR_Prediction->GetNbinsX()); //data w/o 0 entries MARC ALSO LOOK HERE!!!

    for (int i=2; i!=5; ++i) {
        error_curve[i] = new TGraph();
    }
    error_curve[2] = (TGraph*)aC_plot->getObject(1)->Clone("errs");
    int nPoints = error_curve[2]->GetN();
    
    error_curve[0] = new TGraph(2*nPoints);
    error_curve[1] = new TGraph(2*nPoints);
    
    error_curve[0]->SetFillStyle(1001);
    error_curve[1]->SetFillStyle(1001);
    
    error_curve[0]->SetFillColor(kGreen);
    error_curve[1]->SetFillColor(kYellow);
    
    error_curve[0]->SetLineColor(kGreen);
    error_curve[1]->SetLineColor(kYellow);
    
/*    if (plotBands) {
        RooDataHist pred2("pred2", "Prediction from SB", RooArgList(x), h_SR_Prediction2);

        error_curve[3]->SetFillStyle(1001);
        error_curve[4]->SetFillStyle(1001);
        
        error_curve[3]->SetFillColor(kGreen);
        error_curve[4]->SetFillColor(kYellow);
        
        error_curve[3]->SetLineColor(kGreen);
        error_curve[4]->SetLineColor(kYellow);
        
        error_curve[2]->SetLineColor(kBlue+1);
        error_curve[2]->SetLineWidth(3);
        
        double binSize = rebin;
        
        for (int i=0; i!=nPoints; ++i) {
            double x0,y0, x1,y1;
            error_curve[2]->GetPoint(i,x0,y0);
            
            RooAbsReal* nlim = new RooRealVar("nlim","y0",y0,-100000,100000);
            //double lowedge = x0 - (SR_hi - SR_lo)/double(2*nPoints);
            //double upedge = x0 + (SR_hi - SR_lo)/double(2*nPoints);
            
            double lowedge = x0 - binSize/2.;
            double upedge = x0 + binSize/2.;
            
            x.setRange("errRange",lowedge,upedge);
            
            RooExtendPdf* epdf = new RooExtendPdf("epdf","extpdf",bg, *nlim,"errRange");
            
            // Construct unbinned likelihood
            RooAbsReal* nll = epdf->createNLL(pred2,NumCPU(2));
            // Minimize likelihood w.r.t all parameters before making plots
            RooMinimizer* minim = new RooMinimizer(*nll);
            minim->setMinimizerType("Minuit2");
            minim->setStrategy(2);
            minim->setPrintLevel(-1);
            minim->migrad();
            
            minim->hesse();
            RooFitResult* result = minim->lastMinuitFit();
            double errm = nlim->getPropagatedError(*result);
            
            //std::cout<<x0<<" "<<lowedge<<" "<<upedge<<" "<<y0<<" "<<nlim->getVal()<<" "<<errm<<std::endl;
            
            error_curve[0]->SetPoint(i,x0,(y0-errm));
            error_curve[0]->SetPoint(2*nPoints-i-1,x0,y0+errm);
            
            error_curve[1]->SetPoint(i,x0,(y0-2*errm));
            error_curve[1]->SetPoint(2*nPoints-i-1,x0,(y0+2*errm));
            
            error_curve[3]->SetPoint(i,x0,-errm/sqrt(y0));
            error_curve[3]->SetPoint(2*nPoints-i-1,x0,errm/sqrt(y0));
            
            error_curve[4]->SetPoint(i,x0,-2*errm/sqrt(y0));
            error_curve[4]->SetPoint(2*nPoints-i-1,x0,2*errm/sqrt(y0));
            
        }
        
        int npois = 0;
        dataGr->SetMarkerSize(1.0);
        dataGr->SetMarkerStyle (20);
        
        const double alpha = 1 - 0.6827;
        
        for (int i=0; i!=h_SR_Prediction->GetNbinsX(); ++i){
            if (h_SR_Prediction->GetBinContent(i+1) > 0) {
                
                int N = h_SR_Prediction->GetBinContent(i+1);
                double L =  (N==0) ? 0  : (ROOT::Math::gamma_quantile(alpha/2,N,1.));
                double U =  ROOT::Math::gamma_quantile_c(alpha/2,N+1,1) ;
                
                dataGr->SetPoint(npois,h_SR_Prediction->GetBinCenter(i+1),h_SR_Prediction->GetBinContent(i+1));
                dataGr->SetPointEYlow(npois, N-L);
                dataGr->SetPointEYhigh(npois, U-N);
                npois++;
            }
        }
    }*/
    
    double xG[2] = {-10,4000};
    double yG[2] = {0.0,0.0};
    TGraph* unityG = new TGraph(2, xG, yG);
    unityG->SetLineColor(kBlue);
    unityG->SetLineWidth(1);

    double xPad = 0.3;
    TCanvas *c_rooFit=new TCanvas("c_rooFit", "c_rooFit", 800*(1.-xPad), 600);
    c_rooFit->SetFillStyle(4000);
    c_rooFit->SetFrameFillColor(0);
    
    TPad *p_1=new TPad("p_1", "p_1", 0, xPad, 1, 1);
    p_1->SetFillStyle(4000);
    p_1->SetFrameFillColor(0);
    p_1->SetBottomMargin(0.02);
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
    
    int nbins = (int) (SR_hi- SR_lo)/rebin;
    x.setBins(nbins);
   
    std::cout << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << std::endl; 
    std::cout << "chi2(data) " <<  aC_plot->chiSquare()<<std::endl;
    
    //std::cout << "p-value: data     under hypothesis H0:  " << TMath::Prob(chi2_data->getVal(), nbins - 1) << std::endl;
    
    aC_plot->GetXaxis()->SetRangeUser(SR_lo, SR_hi);
    aC_plot->GetXaxis()->SetLabelOffset(0.02);
    aC_plot->GetYaxis()->SetRangeUser(0.001, 1000.);
    h_SR_Prediction->GetXaxis()->SetRangeUser(SR_lo, SR_hi);
    string rebin_ = itoa(rebin);
    
    aC_plot->GetXaxis()->SetTitle("M_{X} [GeV] ");
    aC_plot->GetYaxis()->SetTitle(("Events / "+rebin_+" GeV ").c_str());
    aC_plot->SetMarkerSize(0.7);
    aC_plot->GetYaxis()->SetTitleOffset(1.2);
    aC_plot->Draw();
    
    if (plotBands) {
        error_curve[1]->Draw("Fsame");
        error_curve[0]->Draw("Fsame");
        error_curve[2]->Draw("Lsame");
        dataGr->Draw("p e1 same");
    }
    
    aC_plot->SetTitle("");
    TPaveText *pave = new TPaveText(0.85,0.55,0.67,0.65,"NDC");
    pave->SetBorderSize(0);
    pave->SetTextSize(0.05);
    pave->SetTextFont(42);
    pave->SetLineColor(1);
    pave->SetLineStyle(1);
    pave->SetLineWidth(2);
    pave->SetFillColor(0);
    pave->SetFillStyle(0);
    char name[1000];
    sprintf(name,"#chi^{2}/n = %.2f",1.47569);
    pave->AddText(name);
    //pave->Draw();
    
    TLegend *leg = new TLegend(0.88,0.65,0.55,0.90,NULL,"brNDC");
    leg->SetBorderSize(0);
    leg->SetTextSize(0.05);
    leg->SetTextFont(42);
    leg->SetLineColor(1);
    leg->SetLineStyle(1);
    leg->SetLineWidth(2);
    leg->SetFillColor(0);
    leg->SetFillStyle(0);
    h_SR_Prediction->SetMarkerColor(kBlack);
    h_SR_Prediction->SetLineColor(kBlack);
    h_SR_Prediction->SetMarkerStyle(20);
    h_SR_Prediction->SetMarkerSize(1.0);
    //h_mMMMMa_3Tag_SR->GetXaxis()->SetTitleSize(0.09);
    if (blind)
	if(isQCD){
          leg->AddEntry(h_SR_Prediction, "QCD MC: sideband", "ep");
	}
	else{
          leg->AddEntry(h_SR_Prediction, "Data: sideband", "ep");
	}
    else{
        if(isQCD){
          leg->AddEntry(h_SR_Prediction, "QCD MC: SR", "ep");
        }
        else{
          leg->AddEntry(h_SR_Prediction, "Data: SR", "ep");
        }
    }
    
    Fake1 = new TLine(0,1,0,1);
    Fake1->SetLineColor(kBlue);
    Fake1->SetLineWidth(2);

    Fake2 = new TLine(0,1,0,1);
    Fake2->SetLineColor(kGreen);
    Fake2->SetLineWidth(2);

    Fake3 = new TLine(0,1,0,1);
    Fake3->SetLineColor(kRed);
    Fake3->SetLineWidth(2);

    leg->AddEntry(Fake1, "Pre-Fit", "l");
//    leg->AddEntry(Fake2, "Post-Fit", "l");
//    leg->AddEntry(Fake3, "Post-Fit No Mjj Corr", "l");
//    leg->AddEntry(error_curve[0], "Fit #pm1#sigma", "f");
//    leg->AddEntry(error_curve[1], "Fit #pm2#sigma", "f");
    leg->Draw();
//    pave->Draw("SAME"); 
    aC_plot->Draw("axis same");
    
    
    CMS_lumi( p_1, iPeriod, iPos );
    
    p_2->cd();

   
    RooHist* hpull;
    hpull = aC_plot->pullHist();
    RooPlot* frameP = x.frame() ;
    frameP->SetTitle("");
    frameP->GetXaxis()->SetRangeUser(SR_lo, SR_hi);
    pave->Draw();
    
    frameP->addPlotable(hpull,"P");
    frameP->GetYaxis()->SetRangeUser(-7,7);
    frameP->GetYaxis()->SetNdivisions(505);
    frameP->GetYaxis()->SetTitle("#frac{(data-fit)}{#sigma_{stat}}");
    
    frameP->GetYaxis()->SetTitleSize((1.-xPad)/xPad*0.06);
    frameP->GetYaxis()->SetTitleOffset(1.0/((1.-xPad)/xPad));
    frameP->GetXaxis()->SetTitleSize((1.-xPad)/xPad*0.06);
    //frameP->GetXaxis()->SetTitleOffset(1.0);
    frameP->GetXaxis()->SetLabelSize((1.-xPad)/xPad*0.05);
    frameP->GetYaxis()->SetLabelSize((1.-xPad)/xPad*0.05);
    frameP->GetXaxis()->SetNdivisions(505,kTRUE); 
    
    frameP->Draw();
    if (plotBands) {
        error_curve[4]->Draw("Fsame");
        error_curve[3]->Draw("Fsame");
        unityG->Draw("same");
        hpull->Draw("psame");
        
        frameP->Draw("axis same");
    }
    
    
    c_rooFit->SaveAs((dirName+"/"+name_output+".pdf").c_str());
    
    const int nModels = 9;
    TString models[nModels] = {
        "env_pdf_0_13TeV_dijet2", //0
        "env_pdf_0_13TeV_exp1", //1
        "env_pdf_0_13TeV_expow1", //2
        "env_pdf_0_13TeV_expow2", //3 => skip
        "env_pdf_0_13TeV_pow1", //4
        "env_pdf_0_13TeV_lau1", //5
        "env_pdf_0_13TeV_atlas1", //6
        "env_pdf_0_13TeV_atlas2", //7 => skip
        "env_pdf_0_13TeV_vvdijet1" //8
    };
    
    int nPars[nModels] = {
        2, 1, 2, 3, 1, 1, 2, 3, 2
    };
    
    TString parNames[nModels][3] = {
        "env_pdf_0_13TeV_dijet2_log1","env_pdf_0_13TeV_dijet2_log2","",
        "env_pdf_0_13TeV_exp1_p1","","",
        "env_pdf_0_13TeV_expow1_exp1","env_pdf_0_13TeV_expow1_pow1","",
        "env_pdf_0_13TeV_expow2_exp1","env_pdf_0_13TeV_expow2_pow1","env_pdf_0_13TeV_expow2_exp2",
        "env_pdf_0_13TeV_pow1_p1","","",
        "env_pdf_0_13TeV_lau1_l1","","",
        "env_pdf_0_13TeV_atlas1_coeff1","env_pdf_0_13TeV_atlas1_log1","",
        "env_pdf_0_13TeV_atlas2_coeff1","env_pdf_0_13TeV_atlas2_log1","env_pdf_0_13TeV_atlas2_log2",
        "env_pdf_0_13TeV_vvdijet1_coeff1","env_pdf_0_13TeV_vvdijet1_log1",""
    };
    
        p_1->SetLogy();
        c_rooFit->Update();
        c_rooFit->SaveAs((dirName+"/"+name_output+"_log.pdf").c_str());


    RooDataHist predSB("predSB", "Data from SB", RooArgList(x), h_mX_EST_antitag);
    RooFitResult *r_bgSB;
    if(LLregion){
      r_bgSB=bgSB_LL.fitTo(predSB, RooFit::Range(SR_lo, SR_hi), RooFit::Save());
    }else{
      r_bgSB=bgSB_TT.fitTo(predSB, RooFit::Range(SR_lo, SR_hi), RooFit::Save());
    }
//    RooFitResult *r_bgSB=bgSB.fitTo(predSB, RooFit::Range(SR_lo, SR_hi), RooFit::Save());
    std::cout<<" --------------------- Building Envelope --------------------- "<<std::endl;
    if (LLregion){
      std::cout<< "bg_p1_LL_   param   "<<bg_p1_LL.getVal() <<  " "<<bg_p1_LL.getError()<<std::endl;
      std::cout<< "bg_p2_LL_   param   "<<bg_p2_LL.getVal() <<  " "<<bg_p2_LL.getError()<<std::endl;
      std::cout<< "mjjlin_LL_  param   "<<mjjlin_LL.getVal() <<  " "<<mjjlin_LL.getError()<<std::endl;
    }else{
      std::cout<< "bg_p1_TT_   param   "<<bg_p1_TT.getVal() <<  " "<<bg_p1_TT.getError()<<std::endl;
      std::cout<< "bg_p2_TT_   param   "<<bg_p2_TT.getVal() <<  " "<<bg_p2_TT.getError()<<std::endl;
      std::cout<< "mjjlin_TT_  param   "<<mjjlin_TT.getVal() <<  " "<<mjjlin_TT.getError()<<std::endl;
    }

    
    RooWorkspace *w=new RooWorkspace("HH4b");
    if(LLregion){
      w->import(bg_LL);
      w->import(bgSB_LL);
    }else{
      w->import(bg_TT);
      w->import(bgSB_TT);
    }
//    w->import(bg);
//    w->import(bgSB);
//    w->import(bg_p1);
//    w->import(bg_p2);
//    w->import(mjjlin);
//    w->import(nBackgroundSB);	
//    w->import(nBackground);
    if(LLregion){    
	w->SaveAs((dirName+"/w_background_LL.root").c_str());
    }
    else{
	w->SaveAs((dirName+"/w_background_TT.root").c_str());
    }
    w->Print();
    
    TH1F *h_mX_SR_fakeData=(TH1F*)h_mX_EST->Clone("h_mX_SR_fakeData");
    //h_mX_SR_fakeData->Scale(nEventsSR/h_mX_SR_fakeData->GetSumOfWeights());
    RooDataHist data_obs("data_obs", "Data", RooArgList(x), h_mX_EST);
    RooDataHist data_obs_sb("data_obs_sb", "Data", RooArgList(x), h_mX_EST_antitag);	
    std::cout<<" Background number of events = "<<nEventsSR<<std::endl;
    RooWorkspace *w_data=new RooWorkspace("HH4b");
    w_data->import(data_obs);
    w_data->import(data_obs_sb);
   // w->import(nBackground);
    if(LLregion){
	w_data->SaveAs((dirName+"/w_data_LL.root").c_str());
    }
    else{
        w_data->SaveAs((dirName+"/w_data_TT.root").c_str());
    }

    FILE *passtxt;
    if(LLregion){
	passtxt=fopen("outputs/datacards/HH_mX_1200_HH_LL_QCD_13TeV.txt", "a");
        fprintf(passtxt,("#bg_p1_LL_ param " + tostr(bg_p1_LL.getVal(),4) + " " + tostr(bg_p1_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt,("#bg_p2_LL_ param " + tostr(bg_p2_LL.getVal(),4) + " " + tostr(bg_p2_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt,("mjjlin_LL_ param " + tostr(mjjlin_LL.getVal(),4) + " " + tostr(mjjlin_LL.getError(),4) +"\n").c_str());
    }
    else{
        passtxt=fopen("outputs/datacards/HH_mX_1200_HH_TT_QCD_13TeV.txt", "a");
        fprintf(passtxt,("#bg_p1_TT_ param " + tostr(bg_p1_TT.getVal(),4) + " " + tostr(bg_p1_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt,("#bg_p2_TT_ param " + tostr(bg_p2_TT.getVal(),4) + " " + tostr(bg_p2_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt,("mjjlin_TT_ param " + tostr(mjjlin_TT.getVal(),4) + " " + tostr(mjjlin_TT.getError(),4) +"\n").c_str());
    }

    FILE *passtxt2;
    if(LLregion){
        passtxt2=fopen("outputs/datacards/HH_mX_1400_HH_LL_QCD_13TeV.txt", "a");
        fprintf(passtxt2,("#bg_p1_LL_ param " + tostr(bg_p1_LL.getVal(),4) + " " + tostr(bg_p1_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt2,("#bg_p2_LL_ param " + tostr(bg_p2_LL.getVal(),4) + " " + tostr(bg_p2_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt2,("mjjlin_LL_ param " + tostr(mjjlin_LL.getVal(),4) + " " + tostr(mjjlin_LL.getError(),4) +"\n").c_str());
    }
    else{
        passtxt2=fopen("outputs/datacards/HH_mX_1400_HH_TT_QCD_13TeV.txt", "a");
        fprintf(passtxt2,("#bg_p1_TT_ param " + tostr(bg_p1_TT.getVal(),4) + " " + tostr(bg_p1_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt2,("#bg_p2_TT_ param " + tostr(bg_p2_TT.getVal(),4) + " " + tostr(bg_p2_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt2,("mjjlin_TT_ param " + tostr(mjjlin_TT.getVal(),4) + " " + tostr(mjjlin_TT.getError(),4) +"\n").c_str());
    }

    FILE *passtxt3;
    if(LLregion){
        passtxt3=fopen("outputs/datacards/HH_mX_1600_HH_LL_QCD_13TeV.txt", "a");
        fprintf(passtxt3,("#bg_p1_LL_ param " + tostr(bg_p1_LL.getVal(),4) + " " + tostr(bg_p1_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt3,("#bg_p2_LL_ param " + tostr(bg_p2_LL.getVal(),4) + " " + tostr(bg_p2_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt3,("mjjlin_LL_ param " + tostr(mjjlin_LL.getVal(),4) + " " + tostr(mjjlin_LL.getError(),4) +"\n").c_str());
    }
    else{
        passtxt3=fopen("outputs/datacards/HH_mX_1600_HH_TT_QCD_13TeV.txt", "a");
        fprintf(passtxt3,("#bg_p1_TT_ param " + tostr(bg_p1_TT.getVal(),4) + " " + tostr(bg_p1_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt3,("#bg_p2_TT_ param " + tostr(bg_p2_TT.getVal(),4) + " " + tostr(bg_p2_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt3,("mjjlin_TT_ param " + tostr(mjjlin_TT.getVal(),4) + " " + tostr(mjjlin_TT.getError(),4) +"\n").c_str());
    }

    FILE *passtxt4;
    if(LLregion){
        passtxt4=fopen("outputs/datacards/HH_mX_1800_HH_LL_QCD_13TeV.txt", "a");
        fprintf(passtxt4,("#bg_p1_LL_ param " + tostr(bg_p1_LL.getVal(),4) + " " + tostr(bg_p1_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt4,("#bg_p2_LL_ param " + tostr(bg_p2_LL.getVal(),4) + " " + tostr(bg_p2_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt4,("mjjlin_LL_ param " + tostr(mjjlin_LL.getVal(),4) + " " + tostr(mjjlin_LL.getError(),4) +"\n").c_str());
    }
    else{
        passtxt4=fopen("outputs/datacards/HH_mX_1800_HH_TT_QCD_13TeV.txt", "a");
        fprintf(passtxt4,("#bg_p1_TT_ param " + tostr(bg_p1_TT.getVal(),4) + " " + tostr(bg_p1_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt4,("#bg_p2_TT_ param " + tostr(bg_p2_TT.getVal(),4) + " " + tostr(bg_p2_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt4,("mjjlin_TT_ param " + tostr(mjjlin_TT.getVal(),4) + " " + tostr(mjjlin_TT.getError(),4) +"\n").c_str());
    }

    FILE *passtxt5;
    if(LLregion){
        passtxt5=fopen("outputs/datacards/HH_mX_2000_HH_LL_QCD_13TeV.txt", "a");
        fprintf(passtxt5,("#bg_p1_LL_ param " + tostr(bg_p1_LL.getVal(),4) + " " + tostr(bg_p1_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt5,("#bg_p2_LL_ param " + tostr(bg_p2_LL.getVal(),4) + " " + tostr(bg_p2_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt5,("mjjlin_LL_ param " + tostr(mjjlin_LL.getVal(),4) + " " + tostr(mjjlin_LL.getError(),4) +"\n").c_str());
    }
    else{
        passtxt5=fopen("outputs/datacards/HH_mX_2000_HH_TT_QCD_13TeV.txt", "a");
        fprintf(passtxt5,("#bg_p1_TT_ param " + tostr(bg_p1_TT.getVal(),4) + " " + tostr(bg_p1_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt5,("#bg_p2_TT_ param " + tostr(bg_p2_TT.getVal(),4) + " " + tostr(bg_p2_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt5,("mjjlin_TT_ param " + tostr(mjjlin_TT.getVal(),4) + " " + tostr(mjjlin_TT.getError(),4) +"\n").c_str());
    }

    FILE *passtxt6;
    if(LLregion){
        passtxt6=fopen("outputs/datacards/HH_mX_2500_HH_LL_QCD_13TeV.txt", "a");
        fprintf(passtxt6,("#bg_p1_LL_ param " + tostr(bg_p1_LL.getVal(),4) + " " + tostr(bg_p1_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt6,("#bg_p2_LL_ param " + tostr(bg_p2_LL.getVal(),4) + " " + tostr(bg_p2_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt6,("mjjlin_LL_ param " + tostr(mjjlin_LL.getVal(),4) + " " + tostr(mjjlin_LL.getError(),4) +"\n").c_str());
    }
    else{
        passtxt6=fopen("outputs/datacards/HH_mX_2500_HH_TT_QCD_13TeV.txt", "a");        fprintf(passtxt6,("#bg_p1_TT_ param " + tostr(bg_p1_TT.getVal(),4) + " " + tostr(bg_p1_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt6,("#bg_p2_TT_ param " + tostr(bg_p2_TT.getVal(),4) + " " + tostr(bg_p2_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt6,("mjjlin_TT_ param " + tostr(mjjlin_TT.getVal(),4) + " " + tostr(mjjlin_TT.getError(),4) +"\n").c_str());

    }

    FILE *passtxt7;
    if(LLregion){
        passtxt7=fopen("outputs/datacards/HH_mX_3000_HH_LL_QCD_13TeV.txt", "a");
        fprintf(passtxt7,("#bg_p1_LL_ param " + tostr(bg_p1_LL.getVal(),4) + " " + tostr(bg_p1_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt7,("#bg_p2_LL_ param " + tostr(bg_p2_LL.getVal(),4) + " " + tostr(bg_p2_LL.getError(),4) +"\n").c_str());
        fprintf(passtxt7,("mjjlin_LL_ param " + tostr(mjjlin_LL.getVal(),4) + " " + tostr(mjjlin_LL.getError(),4) +"\n").c_str());
    }
    else{
        passtxt7=fopen("outputs/datacards/HH_mX_3000_HH_TT_QCD_13TeV.txt", "a");
        fprintf(passtxt7,("#bg_p1_TT_ param " + tostr(bg_p1_TT.getVal(),4) + " " + tostr(bg_p1_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt7,("#bg_p2_TT_ param " + tostr(bg_p2_TT.getVal(),4) + " " + tostr(bg_p2_TT.getError(),4) +"\n").c_str());
        fprintf(passtxt7,("mjjlin_TT_ param " + tostr(mjjlin_TT.getVal(),4) + " " + tostr(mjjlin_TT.getError(),4) +"\n").c_str());
    }

    TCanvas *c_rooFit2=new TCanvas("c_rooFit2", "c_rooFit2", 900, 600);
    c_rooFit2->Divide(2,1);
    c_rooFit2->cd(1);
    h_mX_EST_antitag->Draw();
    c_rooFit2->cd(2);
    h_mX_EST->Draw();

    std::cout << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << std::endl;
    std::cout << "chi2(data) " <<  aC_plot->chiSquare()<<std::endl;

    if(LLregion){
      mjjlin_LL.Print();
    }else{
      mjjlin_TT.Print();
    }
    
}




