from ROOT import *
import array, os, sys, copy
file1=TFile("JetHT_V24_HT_Histos_Real.root", "R")

hCom = file1.Get("h7")
h1 = file1.Get("h8")
h2 = file1.Get("h3")

Prescale = h1.GetEntries()/hCom.GetEntries()

PreScaledTrig = TH1F("PrescaledTrig", "", 150, 0., 1500.)
PFHT800 = TH1F("PFHT800", "", 150, 0., 1500.)

PreScaledTrig.Add(h2,Prescale)
PFHT800.Add(h1)

h=[]
h.append(PreScaledTrig)
#h.append(copy.copy(file1.Get("h0")))
h.append(copy.copy(file1.Get("h8")))

#newFile=TFile("trigger_objects_60Bins.root", "RECREATE")
newFile=TFile("trigger_object_HT_V24.root", "RECREATE")
#newFile=TFile("trigger_object_HT.root", "RECREATE")
graph=TGraphErrors(150)

for i in range(1, 151):
	if h[0].GetBinContent(i)>0:
		if h[1].GetBinContent(i)>0:
			eff=h[1].GetBinContent(i)/h[0].GetBinContent(i)
			if eff > 1:
			   print "bin: " 
			   print i
			else:
			   graph.SetPoint(i, 10*i-5, h[1].GetBinContent(i)/(h[0].GetBinContent(i)))
			   graph.SetPointError(i, 0., (eff*(1.-eff)/h[0].GetBinContent(i))**0.5)
#	else:
#		graph.SetPoint(i, 780+(2220/60)*i-(2220/120), 0.)


turnonPt2= TF1("turnonPt2", "1/(1+exp(-[1]*(x-[0])))", 1, 1300)
#turnonPt2= TF1("turnonPt2", "1/(1+exp(-[1]*(x-[0])))", 700, 900)
turnonPt2.SetLineColor(kBlue)
turnonPt2.SetParameter(0, 872.5)
turnonPt2.SetParameter(1, 0.0457)

c=TCanvas("c", "c")
plot = TPad("pad1", "The pad 80% of the height",0,0,1,1)
plot.Draw()
plot.cd()

graph.SetMarkerStyle(20)
graph.Draw()
graph.Fit(turnonPt2)
c.Print("log_trigger.pdf")

fitter = TVirtualFitter.GetFitter()

ErrorBars=TGraphErrors(750)
ErrorBars_2sigma=TGraphErrors(750)

for i in range(0,750):
#	ErrorBars.SetPoint(i,graph.GetX()[i],0)
	ErrorBars.SetPoint(i,500+1*i,0)
        ErrorBars_2sigma.SetPoint(i,500+1*i,0)

fitter.GetConfidenceIntervals(ErrorBars,.68)
fitter.GetConfidenceIntervals(ErrorBars_2sigma,.95)

x=Double()
y=Double()
x1=Double()
y1=Double()
y_naught=Double()
y1_naught=Double()
function=TF1("function", "0", 0, 800)
function.SetLineColor(kBlue)
f=[function ]
histo=TH1F("histo_efficiency", "histo_efficiency", 5000, 0, 5000)
histo_low=TH1F("histo_efficiency_lower", "histo_efficiency_lower", 5000, 0, 5000)
histo_high=TH1F("histo_efficiency_upper", "histo_efficiency_upper", 5000, 0, 5000)
histo_2low=TH1F("histo_efficiency_lower_2sigma", "histo_efficiency_lower_2sigma", 5000, 0, 5000)
histo_2high=TH1F("histo_efficiency_upper_2sigma", "histo_efficiency_upper_2sigma", 5000, 0, 5000)
histo.Add(turnonPt2)

for i in range(1,750):
        ErrorBars.GetPoint(i-1, x, y_naught)
        ErrorBars.GetPoint(i, x1, y1_naught)
	ErrorY = ErrorBars.GetErrorYhigh(i-1)
	ErrorY1 = ErrorBars.GetErrorYhigh(i)
	y = ErrorY + y_naught
	y1 = ErrorY1 + y1_naught
        if y1 > 1.0:
                miniLine=TF1("miniLine", "1", x, x1)
                histo_high.Add(miniLine)
        else:
                f1=TF1("f1"+str(i), "pol1", x, x1)
                f1.SetParameter(0, y1+(y-y1)*(-x1)/(x-x1))
                f1.SetParameter(1, (y-y1)/(x-x1))
                f1.SetLineColor(kAzure+i-11)
                f.append(f1)
                histo_high.Add(f1)
        ErrorBars.GetPoint(i-1, x, y_naught)
        ErrorBars.GetPoint(i, x1, y1_naught)
        ErrorY = ErrorBars.GetErrorYlow(i-1)
        ErrorY1 = ErrorBars.GetErrorYlow(i)
        y = y_naught - ErrorY
        y1 = y1_naught - ErrorY1
        f1=TF1("f1"+str(i), "pol1", x, x1)
        f1.SetParameter(0, y1+(y-y1)*(-x1)/(x-x1))
        f1.SetParameter(1, (y-y1)/(x-x1))
        f1.SetLineColor(kAzure+i-11)
        f.append(f1)
        histo_low.Add(f1)
        ErrorBars_2sigma.GetPoint(i-1, x, y_naught)
        ErrorBars_2sigma.GetPoint(i, x1, y1_naught)
        ErrorY = ErrorBars_2sigma.GetErrorYhigh(i-1)
        ErrorY1 = ErrorBars_2sigma.GetErrorYhigh(i)
        y = ErrorY + y_naught
        y1 = ErrorY1 + y1_naught
	if y1 > 1.0:
		miniLine=TF1("miniLine", "1", x, x1)
                histo_2high.Add(miniLine)
	else:
		f1=TF1("f1"+str(i), "pol1", x, x1)
	        f1.SetParameter(0, y1+(y-y1)*(-x1)/(x-x1))
        	f1.SetParameter(1, (y-y1)/(x-x1))
	        f1.SetLineColor(kAzure+i-11)
	     	f.append(f1)
	        histo_2high.Add(f1)
        ErrorBars_2sigma.GetPoint(i-1, x, y_naught)
        ErrorBars_2sigma.GetPoint(i, x1, y1_naught)
        ErrorY = ErrorBars_2sigma.GetErrorYlow(i-1)
        ErrorY1 = ErrorBars_2sigma.GetErrorYlow(i)
        y = y_naught - ErrorY
        y1 = y1_naught - ErrorY1
        f1=TF1("f1"+str(i), "pol1", x, x1)
        f1.SetParameter(0, y1+(y-y1)*(-x1)/(x-x1))
        f1.SetParameter(1, (y-y1)/(x-x1))
        f1.SetLineColor(kAzure+i-11)
        f.append(f1)
        histo_2low.Add(f1)


function=TF1("function", "1", 1300, 10000)
function.SetLineColor(kBlue)
line_high=TF1("line_high", "1", 1249, 10000)
line_high.SetLineColor(kRed)
line_low=TF1("line_low", "1", 1249, 10000)
line_low.SetLineColor(kGreen)
f.append(function)
histo.Add(function)
histo_high.Add(line_high)
histo_low.Add(line_low)
histo_2high.Add(line_high)
histo_2low.Add(line_low)
graph.Write()
histo.Write()
histo_high.Write()
histo_low.Write()
histo_2high.Write()
histo_2low.Write()


#graph.Draw("a4")
#histo.Draw("same")
histo.Draw("")
histo_high.SetLineColor(kRed)
#ErrorBars.Draw("same")
histo_high.Draw("same")
histo_low.Draw("same")
histo_low.SetLineColor(kGreen)
#histo_2high.Draw("same")
#histo_2low.Draw("same")

#graph.Draw("a4 SAME")




c.Print("triiger_check.pdf")
