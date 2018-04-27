#include "TStyle.h"

/*void SetStyle();
TStyle* Style();

void addbin(TH1D *h);
*/
void limitplot()
{

  /*  //Style options
   gROOT->SetBatch();
   gROOT->SetStyle("Plain");
   
   gStyle->SetOptStat(0);

   SetStyle();
   
   //drawing canvas 1, setting more style options
   TCanvas *c1 = new TCanvas("c1","c1",0,0,600,500);
   c1->Draw();
   c1->cd();
   
   gStyle->SetHistTopMargin(0);
   
   c1->SetLogx(0);
   
  */
  TCanvas *c1 = new TCanvas("c1","c1",0,0,600,500); 

  c1->SetLogy(1);

  double x[6] = {0.75,0.8,1.0,1.2,1.4,1.6};
  double both[6] = {149.0,140.6,55.62,27.89,15.23,11.67};
  double boost[6] = {70.31,70.31,33.59,19.76,12.14,9.88};
  double none[6] = {48.59,40.15,15.27,8.82,6.66,6.77};
  //double both[11] = {856., 493., 353., 235., 100., 99., 82., 69., 36., 23., 29.};
  //  double boost[11] = {341., 195., 113., 82., 37., 39., 36., 32., 21., 18., 23.};
  //double none[11] = {303., 169., 98., 73., 25., 21., 16., 13., 8., 11., 20.};
  //BGLIM
/*
  double both[7] = {93.43,90.31,62.50,39.84,17.57,8.55,9.96};
  double boost[7] = {43.90,45.15,33.90,24.29,12.61,7.75,9.21};
  double none[7] = {29.76,25.23,15.70,10.03,5.33,4.98,7.44};
*/
  /*   TGraph *graph = new TGraph(54, trigSF, y);
   TGraph *gr1 = new TGraph(54, trigSFUp, y);
   TGraph *gr2 = new TGraph(54, trigSFDown, y);

   graph->Draw("AP");
   graph1->Draw("AP");
   graph2->Draw("AP");
   */
   //   c1->Print("graph.pdf");
   //}
   //gApplication->Terminate();*/
   /*TCanvas *c1 = new TCanvas("c1","A Simple Graph Example",200,10,700,500);
  Double_t x[100], y[100];
  Int_t n = 20;
  for (Int_t i=0;i<n;i++) {
    x[i] = i*0.1;
    y[i] = 10*sin(x[i]+0.2);
    }*/
   Int_t n = 6;
   gr = new TGraph(n,x, both);
   gr1 = new TGraph(n,x, boost);
   gr2 = new TGraph(n,x, none);
   gr->SetLineColor(kRed);
   gr->GetXaxis()->SetTitle("Reduced Mass (GeV)");
   gr->GetYaxis()->SetTitle("#sigma #times B(G_{Rad} #rightarrow HH to b#bar{b}b#bar{b}) (fb)"); 
   gr1->SetLineColor(kBlue);
   gr2->SetLineColor(kGreen);
   TMultiGraph *mg = new TMultiGraph();
   
   mg->Add(gr);
   mg->Add(gr1);
   mg->Add(gr2);

   TLegend *leg_cMVAv2L;
   leg_cMVAv2L = new TLegend(0.4, 0.85, 0.6, 0.65);
   leg_cMVAv2L->SetFillColor(253);
   leg_cMVAv2L->SetBorderSize(0);
   leg_cMVAv2L->AddEntry(gr,"Reject Both","l");
   leg_cMVAv2L->AddEntry(gr1,"Reject Boosted","l");
   leg_cMVAv2L->AddEntry(gr2, "Retain Both", "l");
   
   mg->Draw("AL");
   leg_cMVAv2L->Draw();
   mg->GetXaxis()->SetTitle("Reduced Mass (GeV)");
   mg->GetYaxis()->SetTitle("#sigma #times B(G_{Rad} #rightarrow HH to b#bar{b}b#bar{b}) (fb)");

   //gr->Draw("AC");
   //gr1->Draw("PS");
   //gr2->Draw("PS");

   /*   const int bins = 54;
   TGraphAsymmErrors *plot = new TGraphAsymmErrors(bins,y,trigSF,width,width, Down, Up);
   plot->GetXaxis()->SetTitle("Reduced Mass (GeV)");
   plot->GetYaxis()->SetTitle("SF");
   plot->Draw("AP");*/
  c1->Print("test.pdf");
}
/*
void SetStyle()
{
  static TStyle* style = 0;
  if( style==0 ) style = Style();
  gROOT->SetStyle("STYLE");
  gROOT->ForceStyle();
}
*/
 /*
TStyle* Style() 
{
  TStyle *style = new TStyle("STYLE","User style");

  // use plain black on white colors
  Int_t icol=0; // WHITE
  style->SetFrameBorderMode(icol);
  style->SetFrameFillColor(icol);
  style->SetCanvasBorderMode(icol);
  style->SetCanvasColor(icol);
  style->SetPadBorderMode(icol);
  style->SetPadColor(icol);
  style->SetStatColor(icol);
  //style->SetFillColor(icol); // don't use: white fill color for *all* objects

  // set the paper & margin sizes
  style->SetPaperSize(20,26);

  // set margin sizes
  style->SetPadTopMargin(0.05);
  style->SetPadRightMargin(0.05);
  style->SetPadBottomMargin(0.16);
  style->SetPadLeftMargin(0.16);

  // set title offsets (for axis label)
  style->SetTitleXOffset(1.4);
  style->SetTitleYOffset(1.4);

  // use large fonts
  //Int_t font=72; // Helvetica italics
  Int_t font=42; // Helvetica
  Double_t tsize=0.05;
  style->SetTextFont(font);

  style->SetTextSize(tsize);
  style->SetLabelFont(font,"x");
  style->SetTitleFont(font,"x");
  style->SetLabelFont(font,"y");
  style->SetTitleFont(font,"y");
  style->SetLabelFont(font,"z");
  style->SetTitleFont(font,"z");
  
  style->SetLabelSize(tsize,"x");
  style->SetTitleSize(tsize,"x");
  style->SetLabelSize(tsize,"y");
  style->SetTitleSize(tsize,"y");
  style->SetLabelSize(tsize,"z");
  style->SetTitleSize(tsize,"z");

  // use bold lines and markers
  style->SetMarkerStyle(20);
  style->SetMarkerSize(1.2);
  style->SetHistLineWidth(2.);
  style->SetLineStyleString(2,"[12 12]"); // postscript dashes

  // get rid of X error bars 
  //style->SetErrorX(0.001);
  // get rid of error bar caps
  style->SetEndErrorSize(0.);

  // do not display any of the standard histogram decorations
  style->SetOptTitle(0);
  //style->SetOptStat(1111);
  style->SetOptStat(0);
  //style->SetOptFit(1111);
  style->SetOptFit(0);

  // put tick marks on top and RHS of plots
  style->SetPadTickX(1);
  style->SetPadTickY(1);


  return style;
}
/*
/*
void addbin(TH1D *h)
{   
   // Add overflow and underflow bins
   Int_t x_nbins = h->GetXaxis()->GetNbins();
   h->SetBinContent(1,h->GetBinContent(0)+h->GetBinContent(1));
   h->SetBinError(1,TMath::Sqrt(pow(h->GetBinError(0),2)+pow(h->GetBinError(1),2)));
   h->SetBinContent(x_nbins,h->GetBinContent(x_nbins)+h->GetBinContent(x_nbins+1));
   h->SetBinError(x_nbins,TMath::Sqrt(pow(h->GetBinError(x_nbins),2)+
				      pow(h->GetBinError(x_nbins+1),2)));
   // Set overflow and underflow bins to 0
   h->SetBinContent(0,0.);
   h->SetBinError(0,0.);
   h->SetBinContent(x_nbins+1,0.);
   h->SetBinError(x_nbins+1,0.);
}
*/
