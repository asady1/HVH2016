import os
#import numpy
import glob
import math    
from math import *

import ROOT 
#ROOT.gROOT.Macro("rootlogon.C")
from ROOT import *

import FWCore.ParameterSet.Config as cms

import sys
from DataFormats.FWLite import Events, Handle

from array import *

from optparse import OptionParser
parser = OptionParser()

parser.add_option("-o", "--outName", dest="outName",
                  help="output file name")
parser.add_option("-t", "--saveTrig", dest="saveTrig",
                  help="trigger info saved")
parser.add_option("-b", "--ttbar", dest="ttbar",
                  help="isttbar")
parser.add_option("-d", "--data", dest="data",
                  help="isdata")
parser.add_option("-j", "--JERUp", dest="JERUp",
                  help="JERUp")
parser.add_option("-q", "--JERDown", dest="JERDown",
                  help="JERDown")
parser.add_option("-k", "--JECUp", dest="JECUp",
                  help="JECUp")
parser.add_option("-l", "--JECDown", dest="JECDown",
                  help="JECDown")
parser.add_option("-r", "--useReg", dest="useReg",
                  help="use regression for AK4 jets")
(options, args) = parser.parse_args()
outputfilename = options.outName

#AK4 btag SF calculation loaded here
ROOT.gSystem.Load('libCondFormatsBTauObjects') 
ROOT.gSystem.Load('libCondToolsBTau') 
calib = ROOT.BTagCalibration('DeepCSV', 'DeepCSV_Moriond17_B_H.csv')
v_sys = getattr(ROOT, 'vector<string>')()
v_sys.push_back('up')
v_sys.push_back('down')
readerb = ROOT.BTagCalibrationReader(
    1,             
    "central",      
    v_sys,          
)
readerb.load(
    calib, 
    0,          
    "comb"     
)
readerc = ROOT.BTagCalibrationReader(
    1,             
    "central",      
    v_sys,          
)
readerc.load(
    calib, 
    1,          
    "comb"     
)
readerl = ROOT.BTagCalibrationReader(
    1,             
    "central",      
    v_sys,          
)
readerl.load(
    calib, 
    2,          
    "incl"     
)

#FJER
def ApplyJERp4(eta, jerShift):

  eta = abs(eta) 
  if (eta >= 4.7):
      eta = 4.699 
  jerscale = 0 

  if (eta >= 3.2 and eta < 5.0):
    if (jerShift == 1): 
        jerscale = 1.16    
    elif (jerShift == 2): 
        jerscale = 1.16 + 0.029   
    elif (jerShift == -1): 
        jerscale = 1.16 - 0.029   
  
  elif (eta >= 3.0 and eta < 3.2):
    if (jerShift == 1): 
        jerscale = 1.328    
    elif (jerShift == 2): 
        jerscale = 1.328 + 0.022  
    elif (jerShift == -1): 
        jerscale = 1.328 - 0.022  
  
  elif (eta >= 2.8 and eta < 3.0):
    if (jerShift == 1): 
        jerscale =  1.857   
    elif (jerShift == 2): 
        jerscale =  1.857 + 0.071  
    elif (jerShift == -1): 
        jerscale =  1.857 - 0.071  
  
  elif (eta >= 2.5 and eta < 2.8):
    if (jerShift == 1): 
        jerscale = 1.364    
    elif (jerShift == 2): 
        jerscale = 1.364 + 0.039  
    elif (jerShift == -1): 
        jerscale = 1.364 - 0.039  
  
  elif (eta >= 2.3 and eta < 2.5):
    if (jerShift == 1): 
        jerscale = 1.177   
    elif (jerShift == 2): 
        jerscale = 1.177 + 0.041  
    elif (jerShift == -1): 
        jerscale = 1.177 - 0.041  
  
  elif (eta >= 2.1 and eta < 2.3):
    if (jerShift == 1): 
        jerscale = 1.067   
    elif (jerShift == 2): 
        jerscale = 1.067 + 0.053  
    elif (jerShift == -1): 
        jerscale = 1.067 - 0.053   
  
  elif (eta >= 1.9 and eta < 2.1):
    if (jerShift == 1): 
        jerscale = 1.140    
    elif (jerShift == 2): 
        jerscale = 1.140 + 0.047  
    elif (jerShift == -1): 
        jerscale = 1.140 - 0.047  
  
  elif (eta >= 1.7 and eta < 1.9):
    if (jerShift == 1): 
        jerscale = 1.082    
    elif (jerShift == 2): 
        jerscale = 1.082 + 0.035  
    elif (jerShift == -1): 
        jerscale = 1.082 - 0.035   
  
  elif (eta >= 1.3 and eta < 1.7):
    if (jerShift == 1): 
        jerscale = 1.084    
    elif (jerShift == 2): 
        jerscale = 1.084 + 0.011  
    elif (jerShift == -1): 
        jerscale = 1.084 - 0.011   
  
  elif (eta >= 1.1 and eta < 1.3):
    if (jerShift == 1): 
        jerscale = 1.123    
    elif (jerShift == 2): 
        jerscale = 1.123 + 0.024  
    elif (jerShift == -1): 
        jerscale = 1.123 - 0.024  
  
  elif (eta >= 0.8 and eta < 1.1):
    if (jerShift == 1): 
        jerscale = 1.114    
    elif (jerShift == 2): 
        jerscale = 1.114 + 0.013  
    elif (jerShift == -1): 
        jerscale = 1.114 - 0.013  
  
  elif (eta >= 0.5 and eta < 0.8):
    if (jerShift == 1): 
        jerscale = 1.138    
    elif (jerShift == 2): 
        jerscale = 1.138 + 0.013  
    elif (jerShift == -1): 
        jerscale = 1.138 - 0.013  
  
  elif (eta >= 0.0 and eta < 0.5):
    if (jerShift == 1): 
        jerscale = 1.109    
    elif (jerShift == 2): 
        jerscale = 1.109 + 0.008  
    elif (jerShift == -1): 
        jerscale = 1.109 - 0.008  
  
  return jerscale  

#tmva regression AK4
this_pt=array( 'f', [ 0 ] )
this_pv=array( 'f', [ 0 ] )
this_eta=array( 'f', [ 0 ] )
this_mt=array( 'f', [ 0 ] )
this_leadTrackPt=array( 'f', [ 0 ] )
this_leptonPtRel=array( 'f', [ 0 ] )
this_leptonPt=array( 'f', [ 0 ] )
this_LeptonDeltaR=array( 'f', [ 0 ] )
this_neHEF=array( 'f', [ 0 ] )
this_neEmEF=array( 'f', [ 0 ] )
this_vtxPt=array( 'f', [ 0 ] )
this_vtxMass=array( 'f', [ 0 ] )
this_vtx3dL=array( 'f', [ 0 ] )
this_vtxNtrk=array( 'f', [ 0 ] )
this_vtx3deL=array( 'f', [ 0 ] )

reader = ROOT.TMVA.Reader("!Color:!Silent" )
reader.AddVariable( "Jet_pt", this_pt)
reader.AddVariable( "nPVs", this_pv)
reader.AddVariable( "Jet_eta", this_eta)
reader.AddVariable( "Jet_mt", this_mt)
reader.AddVariable( "Jet_leadTrackPt", this_leadTrackPt)
reader.AddVariable( "Jet_leptonPtRel", this_leptonPtRel)
reader.AddVariable( "Jet_leptonPt", this_leptonPt)
reader.AddVariable( "Jet_leptonDeltaR", this_LeptonDeltaR)
reader.AddVariable( "Jet_neHEF", this_neHEF)
reader.AddVariable( "Jet_neEmEF", this_neEmEF)
reader.AddVariable( "Jet_vtxPt", this_vtxPt)
reader.AddVariable( "Jet_vtxMass", this_vtxMass)
reader.AddVariable( "Jet_vtx3dL", this_vtx3dL)
reader.AddVariable( "Jet_vtxNtrk", this_vtxNtrk)
reader.AddVariable( "Jet_vtx3deL", this_vtx3deL)
reader.BookMVA("BDTG method", "gravall-v25.weights.xml")

#trigger SFs
#trigSF = [0.6357615894039734, 0.6857142857142856, 0.7441860465116279, 0.8135593220338982, 0.8971962616822429, 1.0, 1.1294117647058823, 1.0194552529182879, 1.0136674259681093, 0.9372496662216289, 0.9688644688644689, 0.9646535282898919, 1.1915057300509337, 1.0488215488215489, 0.8915477064713152, 0.9703428418374179, 0.9689652366874557, 0.9762512064977283, 0.973422758855812, 1.0010830128885444, 0.9923695117964079, 0.9075827726095381, 0.9943284508440914, 0.9510941853464571, 0.9546363594807095, 0.9291468202685571, 0.9930416577957561, 0.9386372902227362, 0.9473785412126651, 1.0367265469061875, 0.9665803178715022, 0.9858860428646106, 1.0014807813484563, 0.9412416851441242, 0.9607551787431169, 0.9134463558547329, 1.0055803571428572, 1.0418041804180418, 1.015850144092219, 1.0, 1.0, 0.9601209601209602, 1.072, 1.0150375939849625, 1.026128266033254, 1.0337423312883436, 0.8199170124481329, 1.018450184501845, 1.029126213592233, 1.0, 1.0, 1.0273224043715847, 1.045045045045045, 1.0]
#trigSFUp = [0.6357615894039734, 0.7012422145624967, 0.7487377914200966, 0.8170907637785441, 0.950360728545606, 1.0594836931184717, 1.2088747012541348, 1.1334461813205436, 1.129099697752378, 1.1650376032032344, 1.387935097793835, 1.388115360738331, 1.687166363172731, 1.444361999401587, 1.1658022749442472, 1.1923302056834117, 1.1440416329622523, 1.1357571054715827, 1.1109993594740484, 1.1226493901110293, 1.1094379630441884, 1.0034475251006116, 1.1165599941768225, 1.0380648682573603, 1.0293744160500646, 1.0388840975821427, 1.105279800409969, 1.0246693382428933, 1.0493214496040295, 1.137192509734631, 1.0589652054617855, 1.072788566295079, 1.092218162812897, 1.0014045269793728, 1.022591989549982, 0.954083929953782, 1.1048719969020697, 1.090337836282454, 1.0462950418175787, 1.1037427532522217, 1.1361422143678848, 1.1419038358964453, 1.0955232922994538, 1.1121504759929202, 1.098548849421287, 1.0798416514674183, 0.8398653796244868, 1.0936831747542617, 1.0363061639196207, 1.0837320574162679, 1.0071428571428571, 1.0747546794952945, 1.0707428740215625, 1.0]
#trigSFDown = [1.1716395097179646, 1.0008389926943484, 0.9409477277946691, 1.001777312432118, 1.027974949873889, 1.145852634909245, 1.234859256126339, 1.1395825747220822, 1.1304391790179706, 1.1654439899790363, 1.3882283999387006, 1.388421963604086, 1.6875212748732462, 1.4450361109921563, 1.1666039116055777, 1.1932174008313843, 1.1455751796890385, 1.1376411825464592, 1.113222747966162, 1.1257781757837049, 1.1144688552458206, 1.009289061863386, 1.1353629221225667, 1.0475715870417464, 1.041456773216397, 1.0562518190607557, 1.1341843580729392, 1.0714419076917325, 1.085935693026256, 1.1906753097967395, 1.100230293087276, 1.1560906606286687, 1.1384254634311097, 1.2003987049387523, 1.1795402324670292, 1.104611072139729, 1.1970770625801255, 1.2615703857226783, 1.3918688315559384, 1.1976893889629179, 1.2684914976517743, 1.3060700102604788, 1.3212494449258854, 1.4907626911550749, 1.5024218917076568, 1.904748272532864, 1.2905342250239396, 1.8788943962189897, 1.6485273687688706, 1.8456582275346265, 1.602374549719121, 1.893798600861906, 1.9250059764909548, 1.842037120957264]
#trigSFDown=[0.09988366908998225, 0.3705895787342227, 0.5474243652285867, 0.6253413316356784, 0.7664175734905967, 0.854147365090755, 1.0239642732854257, 0.8993279311144935, 0.896895672918248, 0.7090553424642214, 0.5495005377902371, 0.5408850929756979, 0.6954901852286212, 0.6526069866509413, 0.6164915013370527, 0.7474682828434516, 0.7923552936858728, 0.8148612304489975, 0.833622769745462, 0.8763878499933838, 0.8702701683469951, 0.8058764833556902, 0.853293979565616, 0.8546167836511679, 0.8678159457450219, 0.8020418214763584, 0.8518989575185731, 0.80583267275374, 0.808821389399074, 0.8827777840156354, 0.8329303426557285, 0.8156814251005524, 0.8645360992658028, 0.6820846653494961, 0.7419701250192046, 0.7222816395697366, 0.8140836517055889, 0.8220379751134053, 0.6398314566284995, 0.8023106110370821, 0.7315085023482257, 0.6141719099814416, 0.8227505550741148, 0.5393124968148502, 0.5498346403588512, 0.16273639004382323, 0.34929979987232623, 0.1580059727847003, 0.40972505841559537, 0.15434177246537362, 0.39762545028087903, 0.16084620788126336, 0.16508411359913522, 0.15796287904273543]
#trigSFdEta0=[1.484963670204615, 1.5072994825535715, 1.5355649469022725, 1.572482751621185, 1.6227436987889157, 1.695177290289154, 1.8086079369494683, 2.011579678333788, 2.4792511814039644, 4.699815265623083, 0., 0.055167354947859314, 0.557596521691155, 0.7701404314223599, 0.8875097500593482, 0.9619369814664294, 0.9710612992089115, 1.0012575740253802, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFUpdEta0 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0., 0.08657377954972162, 0.8160534068689946, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFDowndEta0 = [0., 0., 0., 0., 0., 0., 0., 0.014198465638805002, 0.27680815379575474, 0.9773224065092085, 0., 0., 0.17767293333521295, 0., 0.23725768459288066, 0.6736865134259405, 0.3598345925134321, 0.3980684772790841, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFdEta1 = [0.6589837245758327, 0.6669943856968895, 0.6757219007199154, 0.6852670009160687, 0.6957502178069424, 0.7073169996420445, 0.7201445008850427, 0.7344507197175704, 0.7505069888591436, 0.7686553489530904, 0.7893331863419369, 0.8131089444196866, 0.8407351853392928, 0.873229703211642, 0.9120036617461952, 0.9590719637015934, 0.928758418718102, 0.9372576250716054, 0.9617424859242152, 0.9835615023809807, 1.0051458267901705, 0.9646099747479004, 0.9910382483145155, 0.9890499194847022, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFUpdEta1 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFDowndEta1 = [0.12173515695364667, 0.14454801523734562, 0.16883887198757253, 0.1936967611883592, 0.21946433412406996, 0.24604394447332922, 0.27384550850306755, 0.3028884071652762, 0.3338356752905493, 0.3664762146928061, 0.40185455810724047, 0.4388110039255826, 0.4810600852536323, 0.5191822060949968, 0.5752986770358548, 0.6219074555191477, 0.6361219139460541, 0.6828900033501075, 0.6585917850901328, 0.3353249030892579, 0.7795500567750538, 0.771806281274267, 0.3882354085582551, 0.5295907099370317, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
trigSFdEta0 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.8901098901098901, 1.0308550185873606, 0.9132368460726669, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
trigSFUpdEta0 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.1600378185993734, 1.2034903288970646, 0.98999980555529,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
trigSFDowndEta0 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.6142752356102305, 0.8506364838283518, 0.8214091884719226, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
trigSFdEta1 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0527114144861585, 1.3692722371967654, 1.0158607350096711, 0.9635478352414791, 0.9878873966942149, 0.9738893617021276, 0.94, 0.9166666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
trigSFUpdEta1 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.4950824529256705, 1.904833956731782, 1.4019437249768507, 1.2112427498411353, 1.2084117379663502, 1.1322268125337909,1.06,1.0031101834020775, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
trigSFDowndEta1 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5560146262639349, 0.72132854692502, 0.6155413357042459, 0.6861899018877822, 0.7560227590023999, 0.7962104338848723, 0.79, 0.7962543617611338, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

#trigSFdEta0 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0108459869848156, 1.0135635018495686, 0.976682622570351, 1.0211962438758846, 0.9827501516946459, 1.123758744179627, 0.9734683598949527, 0.8994249353773404, 0.9689032105317371, 0.9577702390496463, 0.9823622336517268, 0.9890812290700821, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFUpdEta0 = [1.0939849624060152, 1.0751879699248121, 1.0565804795968703, 1.0378019428465677, 1.0394817403026815, 1.0407346027815376, 1.0568945333685424, 1.0864103466592585, 1.0940166406336427, 1.156386177248416, 1.3413086236608123, 1.3419215079158664, 1.5256913366408837, 1.3062412129543783, 1.142232902778897, 1.1323328572968094, 1.0478832227259216, 1.0307550573849393, 1.0088764155710892, 1.010666206420435, 1.003410020914795, 1.0012693577050014, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095]
#trigSFDowndEta0 = [0.13950946755530114, 0.15518159814116494, 0.8064698743836028, 0.8848682499740125, 0.9085302006365152, 0.923164539539495, 0.9292715871923337, 0.9311383761232073, 0.9314350800255777, 0.7966703916051777, 0.7008959381678028, 0.6233727241325318, 0.7216443412498479, 0.6403873070853199, 0.6562731391783462, 0.8049046408763654, 0.8654884420808598, 0.9279839737149949, 0.9484160156351846, 0.9648188387959707, 0.9471718312930084, 0.9197032590439469, 0.7357655683286832, 0.7944197899369732, 0.8318164994392157, 0.5413390577390398, 0.7356857216118726, 0.15861284069096604, 0.630955589899722, 0.3980547855171185, 0.15839473811466598, 0.39750489232149333, 0.15756289309327043, 0.15700587460312931, 0.1564097492861095, 0.9197229440674958, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.0, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]

#trigSFdEta1 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0273224043715847, 1.014335145823035, 0.7796143250688705, 0.8976925687139464, 0.8577763239196016, 0.8954837328767123, 0.9947652347652347, 0.9162004579467933, 0.9851987447698745, 1.00065528661312, 1.037318490129878, 0.9398525359508609, 0.9812667261373773, 0.9765548719061419, 0.9505225741418643, 0.9234091995165054, 0.9826625225725795, 0.9483444844741808, 0.9485409886054602, 0.9928433268858802, 1.0112293987214565, 0.9627766599597586, 0.9874451754385964, 0.9048509955900039, 0.9888111635305388, 0.9638991552270328, 0.9628682856487398, 1.0707417582417582, 0.9653716216216216, 1.0274949083503055, 0.9166666666666666, 0.875, 1.0439739413680782, 1.0091603053435114, 1.0098199672667758, 1.0425531914893618, 0.8675450762829403, 1.014018691588785, 1.0146198830409356, 1.0, 1.0, 0.9059174116645381, 1.030456852791878, 0.6666666666666666, 0.33333333333333326, 0., 0., 0., 0., 0.]
#trigSFUpdEta1 = [1.0, 1.0, 1.1190311523320813, 1.1457650703072844, 1.1146887958281324, 1.090913241370335, 1.0861291853901271, 1.0804121728649845, 1.0684515060395492, 1.0386937235464984, 1.0856417054417045, 1.159820428236897, 1.0106454116165227, 1.2214509754047855, 1.1591545786164001, 1.221171174182325, 1.3368881960159174, 1.1843119399583533, 1.2389347597772624, 1.2123634104268621, 1.2309192895360315, 1.0793806963787713, 1.1270258295992834, 1.098758185368669, 1.0697552012922398, 1.0244113768392922, 1.0927072823245434, 1.0366800666473397, 1.0126484632504067, 1.0914456955629257, 1.0876002290030917, 1.0701299455578965, 1.0965416634887404, 0.9645363593375753, 1.0474364050639295, 1.0191275883383686, 1.008703192439878, 1.206083730115986, 0.98998810768447, 1.1243823196452327, 1.0037292651642264, 0.9235592315901815, 1.1485978322755201, 1.0765466206311187, 1.3049709346357923, 1.1077127659574468, 1.8799144097208624, 2.028743042834847, 2.0297316765712408, 2.003891903689068, 2.000198842253103, 1.9252332221472828, 2.0610988522404403, 1.868546224371884, 1.387438361117068, 0.9999999999999999, 0.7753344614935782, 0.5351837584879965, 0.41476799288047594, 0.33362445415069186]
#trigSFDowndEta1 = [0.7238449712716393, 0.3981229310642277, 0.7422751286395539, 0.8026864763113837, 0.8340745138431198, 0.8879378256848235, 0.8978894847399698, 0.9082489828955099, 0.9238237060822352, 0.9551509446265528, 0.9645305437579014, 0.8665539246480662, 0.5474834532107302, 0.5729817468177147, 0.555230012553001, 0.5683423579752227, 0.6495795104885598, 0.6457966574451199, 0.7269256767923283, 0.7858271994142076, 0.8395159435873418, 0.7922586165741006, 0.8223838278076301, 0.8337423265994243, 0.8094894090924887, 0.7967857216265004, 0.8431772055081057, 0.8173960900127831, 0.846466396779694, 0.836077092779216, 0.8547864659061508, 0.7744191893422723, 0.8226483350322025, 0.717565168890499, 0.7696711624920567, 0.8413570503352874, 0.7245743531210806, 0.791335342274439, 0.7731982962245784, 0.6964417932635785, 0.537594011231508, 0.2713379374172121, 0.8192156244847545, 0.1573832046234348, 0.5808018400779169, 0.9768345008679075, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]



#numberLimit = float(sys.argv[1])

f = ROOT.TFile.Open(sys.argv[1],"READ")

f2 =  ROOT.TFile(outputfilename, 'recreate')
#print outputfilename
f2.cd()

treeMine  = f.Get('myTree')

mynewTree = ROOT.TTree('mynewTree', 'mynewTree')

#run = array('f', [-100.0])
evt = array('f', [-100.0])
#lumi = array('f', [-100.0])
#weightSig = array('f', [-100.0])
deltaEta = array('f', [-100.0])
f1 = array('f', [-100.0])
Red_mass = array('f', [-100.0])
g1 = array('f', [-100.0])
h1 = array('f', [-100.0])
i1 = array('f', [-100.0])
l1 = array('f', [-100.0])
o1 = array('f', [-100.0])
u1 = array('f', [-100.0])
LL = array('f', [-100.0])
LT = array('f', [-100.0])
TT = array('f', [-100.0])
MM = array('f', [-100.0])
b1 = array('f', [-100.0])
b2 = array('f', [-100.0])
v1 = array('f', [-100.0])
fatjetPT = array('f', [-100.0])
fatjetETA = array('f', [-100.0])
fatjetPHI = array('f', [-100.0])
fatjetM = array('f', [-100.0])
fatjetN = array('f', [-100.0])
ak4nfatjetPT = array('f', [-100.0])
ak4nfatjetETA = array('f', [-100.0])
ak4nfatjetPHI = array('f', [-100.0])
ak4nfatjetM = array('f', [-100.0])
sak4nfatjetPT = array('f', [-100.0])
sak4nfatjetETA = array('f', [-100.0])
sak4nfatjetPHI = array('f', [-100.0])
sak4nfatjetM = array('f', [-100.0])
#fatjetl1l2l3 = array('f', [-100.0])
#fatjetl2l3 = array('f', [-100.0])
#fatjetl1l2l3Up = array('f', [-100.0])
#fatjetl1l2l3Down = array('f', [-100.0])
#fatjetl2l3Unc = array('f', [-100.0])
fatjetJER = array('f', [-100.0])
fatjetJERUp = array('f', [-100.0])
fatjetJERDown = array('f', [-100.0])
fatjetMatchedHadW = array('f', [-100.0])
fatjettau32 = array('f', [-100.0])
fatjettau21 = array('f', [-100.0])
fatjetptau21 = array('f', [-100.0])
fatjettau31 = array('f', [-100.0])
fatjetAKCAratio = array('f', [-100.0])
fatjetCAPT = array('f', [-100.0])
fatjetCAETA = array('f', [-100.0])
fatjetCAPHI = array('f', [-100.0])
fatjetCAM = array('f', [-100.0])
bjet1PT = array('f', [-100.0])
bjet1ETA = array('f', [-100.0])
bjet1PHI = array('f', [-100.0])
bjet1M = array('f', [-100.0])
bjet2PT = array('f', [-100.0])
bjet2ETA = array('f', [-100.0])
bjet2PHI = array('f', [-100.0])
bjet2M = array('f', [-100.0])
ak4nbjet1PT = array('f', [-100.0])
ak4nbjet1ETA = array('f', [-100.0])
ak4nbjet1PHI = array('f', [-100.0])
ak4nbjet1M = array('f', [-100.0])
ak4nbjet2PT = array('f', [-100.0])
ak4nbjet2ETA = array('f', [-100.0])
ak4nbjet2PHI = array('f', [-100.0])
ak4nbjet2M = array('f', [-100.0])
invmAK4 = array('f', [-100.0])
HT = array('f', [-100.0])
nAK4 = array('f', [-100.0])
nAK4near1 = array('f', [-100.0])
nAK4near2 = array('f', [-100.0])
ak4btag1 = array('f', [-100.0])
ak4btag2 = array('f', [-100.0])
#trigger1 = array('f', [-100.0])
#trigger2 = array('f', [-100.0])
#trigger3 = array('f', [-100.0])
#trigger_pre = array('f', [-100.0])
ak4jetCorr1 = array('f', [-100.0])
ak4jetCorr2 = array('f', [-100.0])
ak4jetCorrJECUp1 = array('f', [-100.0])
ak4jetCorrJECUp2 = array('f', [-100.0])
ak4jetCorrJECDown1 = array('f', [-100.0])
ak4jetCorrJECDown2 = array('f', [-100.0])
ak4jetCorrJER1 = array('f', [-100.0])
ak4jetCorrJER2 = array('f', [-100.0])
ak4jetCorrJERUp1 = array('f', [-100.0])
ak4jetCorrJERUp2 = array('f', [-100.0])
ak4jetCorrJERDown1 = array('f', [-100.0])
ak4jetCorrJERDown2 = array('f', [-100.0])    
ak4jetflav1 = array('f', [-100.0])
ak4jetflav2 = array('f', [-100.0])

if options.ttbar == "True":
    ttHT = array('f', [-100.0])
SF = array('f', [-100.0])
SFup = array('f', [-100.0])
SFdown = array('f', [-100.0])

trigWeight = array('f', [-100.0])
trigWeightUp = array('f', [-100.0])
trigWeightDown = array('f', [-100.0])
    
ak4btag1SF = array('f', [-100.0])
ak4btag1SFup = array('f', [-100.0])
ak4btag1SFdown = array('f', [-100.0])
ak4btag2SF = array('f', [-100.0])
ak4btag2SFup = array('f', [-100.0])
ak4btag2SFdown = array('f', [-100.0])
    
puW_up = array('f', [-100.0])
puW_down = array('f', [-100.0])
hhsm = array('f', [-100.0])
 
if options.saveTrig == 'True':
    HLT2_HT800 = array('f', [-100.0])  
    HLT2_Quad_Triple = array('f', [-100.0])
    HLT2_Double_Triple = array('f', [-100.0])
    HLT2_DiPFJet280 = array('f', [-100.0])
    HLT2_AK8PFHT650 = array('f', [-100.0])
    HLT2_AK8PFJet360 = array('f', [-100.0])
    HLT2_PFHT650 = array('f', [-100.0])
    HLT2_PFHT900 = array('f', [-100.0])
    HLT2_AK8PFHT700 = array('f', [-100.0])  
    trigger800 = array('f', [-100.0])
    triggerBtag = array('f', [-100.0])
    HLT2_PFJet260 = array('f', [-100.0]) 
    HLT2_PFJet200 = array('f', [-100.0])
    HLT2_PFJet140 = array('f', [-100.0])
    HLT2_Mu27 = array('f', [-100.0])

#mynewTree.Branch("run", run, "run")
mynewTree.Branch("evt", evt, "evt")
#mynewTree.Branch("lumi", lumi, "lumi")
#mynewTree.Branch("weightSig", weightSig, "weightSig")
mynewTree.Branch("deltaEta", deltaEta, "deltaEta")
mynewTree.Branch("Inv_mass", f1, "Invariant mass")
mynewTree.Branch("Red_mass", Red_mass, "Red_mass")
mynewTree.Branch("dijet_mass", g1, "dijet_mass")
mynewTree.Branch("fatjet_mass", h1, "fatjet_mass")
mynewTree.Branch("cross_section", i1, "cross_section")
mynewTree.Branch("fatjet_hbb", l1, "fatjet_hbb")
mynewTree.Branch("puWeight", o1, "puWeight")
mynewTree.Branch("boosted", u1, "boosted")
mynewTree.Branch("LL", LL, "LL")
mynewTree.Branch("LT", LT, "LT")
mynewTree.Branch("TT", TT, "TT")
mynewTree.Branch("MM", MM, "MM")
mynewTree.Branch("b1", b1, "b1")
mynewTree.Branch("b2", b2, "b2")
mynewTree.Branch("resolved", v1, "resolved")
mynewTree.Branch("ak4nfatjetPT", ak4nfatjetPT, "ak4nfatjetPT")
mynewTree.Branch("ak4nfatjetETA", ak4nfatjetETA, "ak4nfatjetETA")
mynewTree.Branch("ak4nfatjetPHI", ak4nfatjetPHI, "ak4nfatjetPHI")
mynewTree.Branch("ak4nfatjetM", ak4nfatjetM, "ak4nfatjetM")
mynewTree.Branch("sak4nfatjetPT", sak4nfatjetPT, "sak4nfatjetPT")
mynewTree.Branch("sak4nfatjetETA", sak4nfatjetETA, "sak4nfatjetETA")
mynewTree.Branch("sak4nfatjetPHI", sak4nfatjetPHI, "sak4nfatjetPHI")
mynewTree.Branch("sak4nfatjetM", sak4nfatjetM, "sak4nfatjetM")
mynewTree.Branch("fatjetPT", fatjetPT, "fatjetPT")
mynewTree.Branch("fatjetETA", fatjetETA, "fatjetETA")
mynewTree.Branch("fatjetPHI", fatjetPHI, "fatjetPHI")
mynewTree.Branch("fatjetM", fatjetM, "fatjetM")
mynewTree.Branch("fatjetN", fatjetN, "fatjetN")
#mynewTree.Branch("fatjetl1l2l3", fatjetl1l2l3, "fatjetl1l2l3")
#mynewTree.Branch("fatjetl2l3", fatjetl2l3, "fatjetl2l3")
#mynewTree.Branch("fatjetl1l2l3Up", fatjetl1l2l3Up, "fatjetl1l2l3Up")
#mynewTree.Branch("fatjetl1l2l3Down", fatjetl1l2l3Down, "fatjetl1l2l3Down")
#mynewTree.Branch("fatjetl2l3Unc", fatjetl2l3Unc, "fatjetl2l3Unc")
mynewTree.Branch("fatjetJER", fatjetJER, "fatjetJER")
mynewTree.Branch("fatjetJERUp", fatjetJERUp, "fatjetJERUp")
mynewTree.Branch("fatjetJERDown", fatjetJERDown, "fatjetJERDown")
mynewTree.Branch("fatjetMatchedHadW", fatjetMatchedHadW, "fatjetMatchedHadW")
mynewTree.Branch("fatjettau32", fatjettau32, "fatjettau32")
mynewTree.Branch("fatjettau21", fatjettau21, "fatjettau21")
mynewTree.Branch("fatjetptau21", fatjetptau21, "fatjetptau21")
mynewTree.Branch("fatjettau31", fatjettau31, "fatjettau31")
mynewTree.Branch("fatjetAKCAratio", fatjetAKCAratio, "fatjetAKCAratio")
mynewTree.Branch("fatjetCAPT", fatjetCAPT, "fatjetCAPT")
mynewTree.Branch("fatjetCAETA", fatjetCAETA, "fatjetCAETA")
mynewTree.Branch("fatjetCAPHI", fatjetCAPHI, "fatjetCAPHI")
mynewTree.Branch("fatjetCAM", fatjetCAM, "fatjetCAM")
mynewTree.Branch("nAK4", nAK4, "nAK4")
mynewTree.Branch("nAK4near1", nAK4near1, "nAK4near1")
mynewTree.Branch("nAK4near2", nAK4near2, "nAK4near2")
mynewTree.Branch("bjet1PT", bjet1PT, "bjet1PT")
mynewTree.Branch("bjet1ETA", bjet1ETA, "bjet1ETA")
mynewTree.Branch("bjet1PHI", bjet1PHI, "bjet1PHI")
mynewTree.Branch("bjet1M", bjet1M, "bjet1M")
mynewTree.Branch("bjet2PT", bjet2PT, "bjet2PT")
mynewTree.Branch("bjet2ETA", bjet2ETA, "bjet2ETA")
mynewTree.Branch("bjet2PHI", bjet2PHI, "bjet2PHI")
mynewTree.Branch("bjet2M", bjet2M, "bjet2M")
mynewTree.Branch("ak4nbjet1PT", ak4nbjet1PT, "ak4nbjet1PT")
mynewTree.Branch("ak4nbjet1ETA", ak4nbjet1ETA, "ak4nbjet1ETA")
mynewTree.Branch("ak4nbjet1PHI", ak4nbjet1PHI, "ak4nbjet1PHI")
mynewTree.Branch("ak4nbjet1M", ak4nbjet1M, "ak4nbjet1M")
mynewTree.Branch("ak4nbjet2PT", ak4nbjet2PT, "ak4nbjet2PT")
mynewTree.Branch("ak4nbjet2ETA", ak4nbjet2ETA, "ak4nbjet2ETA")
mynewTree.Branch("ak4nbjet2PHI", ak4nbjet2PHI, "ak4nbjet2PHI")
mynewTree.Branch("ak4nbjet2M", ak4nbjet2M, "ak4nbjet2M")
mynewTree.Branch("invmAK4", invmAK4, "invmAK4")
mynewTree.Branch("HT", HT, "HT")
mynewTree.Branch("ak4btag1", ak4btag1, "ak4btag1")
mynewTree.Branch("ak4btag2", ak4btag2, "ak4btag2")
mynewTree.Branch("ak4jetCorr1", ak4jetCorr1, "ak4jetCorr1")
mynewTree.Branch("ak4jetCorr2", ak4jetCorr2, "ak4jetCorr2")
mynewTree.Branch("ak4jetCorrJECUp1", ak4jetCorrJECUp1, "ak4jetCorrJECUp1")
mynewTree.Branch("ak4jetCorrJECUp2", ak4jetCorrJECUp2, "ak4jetCorrJECUp2")
mynewTree.Branch("ak4jetCorrJECDown1", ak4jetCorrJECDown1, "ak4jetCorrJECDown1")
mynewTree.Branch("ak4jetCorrJECDown2", ak4jetCorrJECDown2, "ak4jetCorrJECDown2")
mynewTree.Branch("ak4jetCorrJER1", ak4jetCorrJER1, "ak4jetCorrJER1")
mynewTree.Branch("ak4jetCorrJER2", ak4jetCorrJER2, "ak4jetCorrJER2")
mynewTree.Branch("ak4jetCorrJERUp1", ak4jetCorrJERUp1, "ak4jetCorrJERUp1")
mynewTree.Branch("ak4jetCorrJERUp2", ak4jetCorrJERUp2, "ak4jetCorrJERUp2")
mynewTree.Branch("ak4jetCorrJERDown1", ak4jetCorrJERDown1, "ak4jetCorrJERDown1")
mynewTree.Branch("ak4jetCorrJERDown2", ak4jetCorrJERDown2, "ak4jetCorrJERDown2")
mynewTree.Branch("ak4jetflav1", ak4jetflav1, "ak4jetflav1")
mynewTree.Branch("ak4jetflav2", ak4jetflav2, "ak4jetflav2")

#mynewTree.Branch("HLT_ht800", trigger1, "HLT_ht800")
#mynewTree.Branch("HLT_AK08", trigger2, "HLT_AK08")
#mynewTree.Branch("HLT_HH4b", trigger3, "HLT_HH4b")
#mynewTree.Branch("HLT_ht350", trigger_pre, "HLT_ht350")

if options.ttbar == "True":
    mynewTree.Branch("ttHT", ttHT, "ttHT")
mynewTree.Branch("SF", SF, "SF")
mynewTree.Branch("SFup", SFup, "SFup")
mynewTree.Branch("SFdown", SFdown, "SFdown")
mynewTree.Branch("trigWeight", trigWeight, "trigWeight")
mynewTree.Branch("trigWeightUp", trigWeightUp, "trigWeightUp")
mynewTree.Branch("trigWeightDown", trigWeightDown, "trigWeightDown")
mynewTree.Branch("ak4btag1SF", ak4btag1SF, "ak4btag1SF")
mynewTree.Branch("ak4btag1SFup", ak4btag1SFup, "ak4btag1upSF")
mynewTree.Branch("ak4btag1SFdown", ak4btag1SFdown, "ak4btag1downSF")
mynewTree.Branch("ak4btag2SF", ak4btag2SF, "ak4btag2SF")
mynewTree.Branch("ak4btag2SFup", ak4btag2SFup, "ak4btag2SFup")
mynewTree.Branch("ak4btag2SFdown", ak4btag2SFdown, "ak4btag2SFdown")
    
mynewTree.Branch("puWeightUp", puW_up, "puWeightUp")
mynewTree.Branch("puWeightDown", puW_down, "puWeightDown")
mynewTree.Branch("hhsm", hhsm, "hhsm")

if options.saveTrig == 'True':
    mynewTree.Branch('HLT2_HT800', HLT2_HT800, 'HLT2_HT800/F')
    mynewTree.Branch('HLT2_Quad_Triple', HLT2_Quad_Triple, 'HLT2_Quad_Triple/F')
    mynewTree.Branch('HLT2_Double_Triple', HLT2_Double_Triple, 'HLT2_Double_Triple/F')
    mynewTree.Branch('trigger800', trigger800, 'trigger800/F')
    mynewTree.Branch('triggerBtag', triggerBtag, 'triggerBtag/F')
    mynewTree.Branch("HLT2_DiPFJet280", HLT2_DiPFJet280, "HLT2_DiPFJet280")
    mynewTree.Branch("HLT2_AK8PFHT650", HLT2_AK8PFHT650, "HLT2_AK8PFHT650")
    mynewTree.Branch("HLT2_AK8PFJet360", HLT2_AK8PFJet360, "HLT2_AK8PFJet360")
    mynewTree.Branch("HLT2_PFHT650", HLT2_PFHT650, "HLT2_PFHT650")
    mynewTree.Branch("HLT2_PFHT900", HLT2_PFHT900, "HLT2_PFHT900")
    mynewTree.Branch("HLT2_AK8PFHT700", HLT2_AK8PFHT700, "HLT2_AK8PFHT700")
    mynewTree.Branch("HLT2_PFJet260", HLT2_PFJet260, "HLT2_PFJet260")
    mynewTree.Branch("HLT2_PFJet200", HLT2_PFJet200, "HLT2_PFJet200")
    mynewTree.Branch("HLT2_PFJet140", HLT2_PFJet140, "HLT2_PFJet140")
    mynewTree.Branch("HLT2_Mu27", HLT2_Mu27, "HLT2_Mu27")

nevent = treeMine.GetEntries();

tpo1 = ROOT.TH1F("tpo1", "After jet kinematic cuts", 8,-1, 7)
tpo2 = ROOT.TH1F("tpo2", "After trigger", 8, -1, 7)
tpo3 = ROOT.TH1F("tpo3", "After v-type cut", 8, -1, 7)
tpo4 = ROOT.TH1F("tpo4", "After 1 fatjet + 2 AK4 b tagged dR(fj) jets", 8, -1, 7)
tpo5 = ROOT.TH1F("tpo5", "After fatjet pt, mass, AK4 jets dR", 8, -1, 7)
tpo6 = ROOT.TH1F("tpo6", "After mass cuts", 8, -1, 7)
tpo7 = ROOT.TH1F("tpo7", "After double b 0.8", 8, -1, 7)
tpo8 = ROOT.TH1F("tpo8", "After double b 0.9", 8, -1, 7) 
tpo9 = ROOT.TH1F("tpo9", "After double b 0.6", 8, -1, 7)
if options.data == "False":
    CountWeightedmc = ROOT.TH1F("CountWeighted","Count with sign(gen weight) and pu weight",1,0,2)
    CountWeightedmc.Add(f.Get("CountWeighted"))

counter = 0
#for i in range(0, nevent) :
for i in range(32000000, 48000000) :
    counter = counter + 1
    treeMine.GetEntry(i)
    triggerpass = 1
    #weightSig[0] = treeMine.weightSig
    if options.saveTrig == 'True':
        triggerpass = treeMine.HLT_PFHT800_v + treeMine.HLT_QuadJet45_TripleBTagCSV_p087_v + treeMine.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
        btagtrigs = treeMine.HLT_QuadJet45_TripleBTagCSV_p087_v + treeMine.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
        value800 = 0
        valuebtag = 0
        if treeMine.HLT_PFHT800_v > 0 and btagtrigs < 1:
            value800 = 1
        if treeMine.HLT_PFHT800_v < 1 and btagtrigs > 0:
            valuebtag = 1
        trigger800[0] = value800
        triggerBtag[0] = valuebtag

    tpo1.Fill(triggerpass)
    if triggerpass > 0:
        tpo2.Fill(triggerpass) 

    passesVtype = 0
    if treeMine.vtype == -1 or treeMine.vtype == 4:
        passesVtype = 1

    if passesVtype < 1:
      continue
    if triggerpass > 0:
        tpo3.Fill(triggerpass)

    ak8Jet1 = TLorentzVector()
    ak8Jet1.SetPtEtaPhiM(treeMine.jet1pt, treeMine.jet1eta, treeMine.jet1phi, treeMine.jet1mass)

    ak8Jet2 = TLorentzVector()
    ak8Jet2.SetPtEtaPhiM(treeMine.jet2pt, treeMine.jet2eta, treeMine.jet2phi, treeMine.jet2mass)

    if treeMine.isData < 1:
        jer1scale = ApplyJERp4(ak8Jet1.Eta(), 1)
        jer1scaleUp = ApplyJERp4(ak8Jet1.Eta(), 2)
        jer1scaleDown = ApplyJERp4(ak8Jet1.Eta(), -1)
        if treeMine.jet1JER > 0:
            pt1smear = (treeMine.jet1JER + jer1scale*(ak8Jet1.Pt() - treeMine.jet1JER))/ak8Jet1.Pt()
            if pt1smear < 0:
                pt1smear = 0.001
            pt1smearUp = (treeMine.jet1JER + jer1scaleUp*(ak8Jet1.Pt() -treeMine.jet1JER))/ak8Jet1.Pt()
            if pt1smearUp < 0:
                pt1smearUp = 0.001
            pt1smearDown = (treeMine.jet1JER + jer1scaleDown*(ak8Jet1.Pt() -treeMine.jet1JER))/ak8Jet1.Pt()
            if pt1smearDown < 0:
                pt1smearDown = 0.001
        elif jer1scale > 1:
            rand1 = TRandom()
            rand1Up = TRandom()
            rand1Down = TRandom()
            pt1smear = (rand1.Gaus(ak8Jet1.Pt(), sqrt(jer1scale*jer1scale - 1)*0.2))/ak8Jet1.Pt()
            pt1smearUp = rand1Up.Gaus(ak8Jet1.Pt(), sqrt(jer1scaleUp*jer1scaleUp -1)*0.2)/ak8Jet1.Pt()
            pt1smearDown = rand1Down.Gaus(ak8Jet1.Pt(), sqrt(jer1scaleDown*jer1scaleDown -1)*0.2)/ak8Jet1.Pt()
        else:
          pt1smear = -100.
          pt1smearUp = -100.
          pt1smearDown = -100.

        jer2scale = ApplyJERp4(ak8Jet2.Eta(), 1)
        jer2scaleUp = ApplyJERp4(ak8Jet2.Eta(), 2)
        jer2scaleDown = ApplyJERp4(ak8Jet2.Eta(), -1)
        if treeMine.jet2JER > 0:
            pt2smear = (treeMine.jet2JER + jer2scale*(ak8Jet2.Pt() - treeMine.jet2JER))/ak8Jet2.Pt()
            if pt2smear < 0:
                pt2smear = 0.001
            pt2smearUp = (treeMine.jet2JER + jer2scaleUp*(ak8Jet2.Pt() -treeMine.jet2JER))/ak8Jet2.Pt()
            if pt2smearUp < 0:
                pt2smearUp = 0.001
            pt2smearDown = (treeMine.jet2JER + jer2scaleDown*(ak8Jet2.Pt() -treeMine.jet2JER))/ak8Jet2.Pt()
            if pt2smearDown < 0:
                pt2smearDown = 0.001
        elif jer2scale > 1 and ak8Jet2.Pt() > 0:
          rand2 = TRandom()
          rand2Up = TRandom()
          rand2Down = TRandom()
          pt2smear = rand2.Gaus(ak8Jet2.Pt(), sqrt(jer2scale*jer2scale - 1)*0.2)/ak8Jet2.Pt()
          pt2smearUp = rand2Up.Gaus(ak8Jet2.Pt(), sqrt(jer2scaleUp*jer2scaleUp -1)*0.2)/ak8Jet2.Pt()
          pt2smearDown = rand2Down.Gaus(ak8Jet2.Pt(), sqrt(jer2scaleDown*jer2scaleDown -1)*0.2)/ak8Jet2.Pt()
        else:
          pt2smear = -100.
          pt2smearUp = -100.
          pt2smearDown = -100.

    if options.JERUp == "True":
      ak8Jet1*=pt1smearUp/pt1smear
      ak8Jet2*=pt2smearUp/pt2smear
    if options.JERDown == "True":
      ak8Jet1*=pt1smearDown/pt1smear
      ak8Jet2*=pt2smearDown/pt2smear
    if options.JECUp == "True":
      ak8Jet1*=(treeMine.jet1l1l2l3Unc + treeMine.jet1l1l2l3)/treeMine.jet1l1l2l3
      ak8Jet2*=(treeMine.jet2l1l2l3Unc + treeMine.jet2l1l2l3)/treeMine.jet2l1l2l3
    if options.JECDown == "True":
      ak8Jet1*=(treeMine.jet1l1l2l3 - treeMine.jet1l1l2l3Unc)/treeMine.jet1l1l2l3
      ak8Jet2*=(treeMine.jet2l1l2l3 - treeMine.jet2l1l2l3Unc)/treeMine.jet2l1l2l3
    

    ca15Jet1 = TLorentzVector()
    ca15Jet1.SetPtEtaPhiM(treeMine.CA15jet1pt, treeMine.CA15jet1eta, treeMine.CA15jet1phi, treeMine.CA15jet1mass)

    ca15Jet2 = TLorentzVector()
    ca15Jet2.SetPtEtaPhiM(treeMine.CA15jet2pt, treeMine.CA15jet2eta, treeMine.CA15jet2phi, treeMine.CA15jet2mass)
    
    ak4jets1Pre = []
    ak4jets2Pre = []
    ak4jets1csv = []
    ak4jets2csv = []
    ak4jet1ID = []
    ak4jet2ID = []
    ak4corr1 = []
    ak4jecup1 = []
    ak4jecdown1 = []
    ak4jer1 = []
    ak4jerup1 = []
    ak4jerdown1 = []
    ak4flav1 = []
    ak4corr2 = []
    ak4jecup2 = []
    ak4jecdown2 = []
    ak4jer2 = []
    ak4jerup2 = []
    ak4jerdown2 = []
    ak4flav2 = []
    ak4ptreg1 = []
    ak4ptreg2 = []

    nAK4jets = 0 
    
    for j in range(len(treeMine.ak4jet_pt)):
        if treeMine.ak4jet_pt[j] > 25 and abs(treeMine.ak4jet_eta[j]) < 2.4 and treeMine.ak4jetCMVA[j] > 0.4432:
          nAK4jets += 1 
        prej_p4=TLorentzVector()
        prej_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[j], treeMine.ak4jet_eta[j], treeMine.ak4jet_phi[j], treeMine.ak4jet_mass[j])
        if treeMine.isData < 1:
          if treeMine.ak4jetCorrJER[j] < 2 and treeMine.ak4jetCorrJER[j] > 0:
            ak4ptJER = treeMine.ak4jetCorrJER[j]
            ak4ptJERUp = treeMine.ak4jetCorrJERUp[j]
            ak4ptJERDown = treeMine.ak4jetCorrJERDown[j]          
          else:
            jerscale = ApplyJERp4(treeMine.ak4jet_eta[j], 1)
            jerscaleUp = ApplyJERp4(treeMine.ak4jet_eta[j], 2)
            jerscaleDown = ApplyJERp4(treeMine.ak4jet_eta[j], -1)
            rand = TRandom()
            randUp = TRandom()
            randDown = TRandom()
            ak4ptJER = rand.Gaus(treeMine.ak4jet_pt[j], sqrt(jerscale*jerscale - 1)*0.2)/treeMine.ak4jet_pt[j]
            ak4ptJERUp = randUp.Gaus(treeMine.ak4jet_pt[j], sqrt(jerscaleUp*jerscaleUp -1)*0.2)/treeMine.ak4jet_pt[j]
            ak4ptJERDown = randDown.Gaus(treeMine.ak4jet_pt[j], sqrt(jerscaleDown*jerscaleDown -1)*0.2)/treeMine.ak4jet_pt[j] 
        if options.JERUp == "True":
          prej_p4*=ak4ptJERUp/ak4ptJER
        if options.JERDown == "True":
          prej_p4*=ak4ptJERDown/ak4ptJER
        if options.JECUp == "True":
          prej_p4*=(treeMine.ak4jetCorrJECUp[j]/treeMine.ak4jetCorr[j])
        if options.JECDown == "True":
          prej_p4*=(treeMine.ak4jetCorrJECDown[j]/treeMine.ak4jetCorr[j])
        
        this_pt[0] = prej_p4.Pt()
        this_pv[0] = treeMine.nPVs
        this_eta[0] = prej_p4.Eta()
        this_mt[0] = prej_p4.Mt()
        this_leadTrackPt[0] = treeMine.ak4jetLeadTrackPt[j]
        this_leptonPtRel[0] = treeMine.ak4jetLeadTrackPt[j]
        this_leptonPt[0] = treeMine.ak4jetLeptonPt[j]
        this_LeptonDeltaR[0] = treeMine.ak4jetLeptonDeltaR[j]
        this_neHEF[0] = treeMine.ak4jetNeHEF[j]
        this_neEmEF[0] = treeMine.ak4jetNeEmEF[j]
        this_vtxPt[0] = treeMine.ak4jetVtxPt[j]
        this_vtxMass[0] = treeMine.ak4jetVtxMass[j]
        this_vtx3dL[0] = treeMine.ak4jetVtx3dL[j]
        this_vtxNtrk[0] = treeMine.ak4jetVtxNtrk[j]
        this_vtx3deL[0] = treeMine.ak4jetVtx3deL[j]
        ptreg = (reader.EvaluateRegression("BDTG method"))[0]
        
        j_p4=TLorentzVector()
        if options.useReg == "True":
          j_p4.SetPtEtaPhiM(ptreg, prej_p4.Eta(), prej_p4.Phi(), prej_p4.M())
        else:
          j_p4.SetPtEtaPhiM(prej_p4.Pt(), prej_p4.Eta(), prej_p4.Phi(), prej_p4.M())
          
        deltaR1=j_p4.DeltaR(ak8Jet1)
        deltaR2=j_p4.DeltaR(ak8Jet2)
        deepCSV = treeMine.ak4jetDeepCSVb[j] + treeMine.ak4jetDeepCSVbb[j]
        if deltaR1 > 0.8 and deepCSV > 0.2219 and j_p4.Pt() > 30:
            ak4jets1Pre.append(j_p4)
            ak4jets1csv.append(deepCSV)
            ak4jet1ID.append(j)
            if treeMine.isData < 1:
                ak4corr1.append(treeMine.ak4jetCorr[j])
                ak4jecup1.append(treeMine.ak4jetCorrJECUp[j])
                ak4jecdown1.append(treeMine.ak4jetCorrJECDown[j])
                ak4jer1.append(ak4ptJER)
                ak4jerup1.append(ak4ptJERUp)
                ak4jerdown1.append(ak4ptJERDown)
                ak4flav1.append(treeMine.ak4jetMCflavour[j])
                ak4ptreg1.append(ptreg)
        if deltaR2 > 0.8 and deepCSV > 0.2219 and j_p4.Pt() > 30:
            ak4jets2Pre.append(j_p4)
            ak4jets2csv.append(deepCSV)
            ak4jet2ID.append(j)
            if treeMine.isData < 1:
                ak4corr2.append(treeMine.ak4jetCorr[j])
                ak4jecup2.append(treeMine.ak4jetCorrJECUp[j])
                ak4jecdown2.append(treeMine.ak4jetCorrJECDown[j])
                ak4jer2.append(ak4ptJER)
                ak4jerup2.append(ak4ptJERUp)
                ak4jerdown2.append(ak4ptJERDown)
                ak4flav2.append(treeMine.ak4jetMCflavour[j])
                ak4ptreg2.append(ptreg)

    hhres = 0
    if nAK4jets > 3 and (treeMine.HLT_QuadJet45_TripleBTagCSV_p087_v + treeMine.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v) > 0:
      hhres = 1
    nAK4[0] = hhres

    ak4jet1 = TLorentzVector()
    ak4jet2 = TLorentzVector()

    fatjet = TLorentzVector()
    if len(ak4jets1Pre) < 2 and len(ak4jets2Pre) < 2:
        continue

    if triggerpass > 0:
        tpo4.Fill(triggerpass)
    b1[0] = treeMine.jet1bbtag
    b2[0] = treeMine.jet2bbtag
    b_min = 0
    if len(ak4jets1Pre) > 1 and ak8Jet1.Pt() > 250 and treeMine.jet1_puppi_msoftdrop_raw*treeMine.jet1_puppi_TheaCorr > 40:
        fatjet = ak8Jet1
        pmass = treeMine.jet1_puppi_msoftdrop_raw*treeMine.jet1_puppi_TheaCorr
        bbtag = treeMine.jet1bbtag
        order = 1
        if treeMine.jet1tau2 > 0:
            fatjet32 = treeMine.jet1tau3/treeMine.jet1tau2
        else:
            fatjet32 = -100.
        fatjetp21 = treeMine.jet1_puppi_tau21    
        if treeMine.jet1tau1 > 0:
            fatjet21 = treeMine.jet1tau2/treeMine.jet1tau1
            fatjet31 = treeMine.jet1tau3/treeMine.jet1tau1
        else:
            fatjet21 = -100.
            fatjet31 = -100.
        fatjetptCA = treeMine.CA15jet1pt
        fatjetetaCA = treeMine.CA15jet1eta
        fatjetphiCA = treeMine.CA15jet1phi
        fatjetmCA = treeMine.CA15jet1mass
        if treeMine.CA15jet1pt > 0:
            fatjetAKCA = fatjet.Pt()/treeMine.CA15jet1pt
        else:
            fatjetAKCA = -100.
        if treeMine.isData < 1:
           # l1l2l3 = treeMine.jet1l1l2l3
           # l2l3 = treeMine.jet1l2l3
           # l1l2l3Up = treeMine.jet1l1l2l3Unc + treeMine.jet1l1l2l3
           # l1l2l3Down = treeMine.jet1l1l2l3 - treeMine.jet1l1l2l3Unc
           # l2l3Unc = treeMine.jet1l2l3Unc
            ak8jer = pt1smear
            ak8jerUp = pt1smearUp
            ak8jerDown = pt1smearDown
            hadw = treeMine.LeadingAK8Jet_MatchedHadW
        jet3_p4=TLorentzVector()
        jet4_p4=TLorentzVector()
        for k in range(len(ak4jets1Pre)):
            jet3_p4.SetPtEtaPhiM(ak4jets1Pre[k].Pt(), ak4jets1Pre[k].Eta(), ak4jets1Pre[k].Phi(), ak4jets1Pre[k].M())
            for l in range(len(ak4jets1Pre)):
                if (l!=k):
                    jet4_p4.SetPtEtaPhiM(ak4jets1Pre[l].Pt(), ak4jets1Pre[l].Eta(), ak4jets1Pre[l].Phi(), ak4jets1Pre[l].M())
                    deltaRak4=jet3_p4.DeltaR(jet4_p4)
                    b_add = ak4jets1csv[k] + ak4jets1csv[l]
                    if b_min < b_add and deltaRak4 < 1.5:
                        ak4jet1 = ak4jets1Pre[k]
                        ak4jet1btag = ak4jets1csv[k]
                        ak4jet1i = ak4jet1ID[k]
                        if treeMine.isData < 1:
                            ak4jet1corr = ak4corr1[k]
                            ak4jet1jecup = ak4jecup1[k]
                            ak4jet1jecdown = ak4jecdown1[k]
                            ak4jet1jer = ak4jer1[k]
                            ak4jet1jerup = ak4jerup1[k]
                            ak4jet1jerdown = ak4jerdown1[k]
                            ak4jet1flav = ak4flav1[k]
                        ak4jet2 = ak4jets1Pre[l]
                        ak4jet2btag = ak4jets1csv[l]
                        ak4jet2i = ak4jet1ID[l]
                        if treeMine.isData < 1:
                            ak4jet2corr = ak4corr1[l]
                            ak4jet2jecup = ak4jecup1[l]
                            ak4jet2jecdown = ak4jecdown1[l]
                            ak4jet2jer = ak4jer1[l]
                            ak4jet2jerup = ak4jerup1[l]
                            ak4jet2jerdown = ak4jerdown1[l]
                            ak4jet2flav = ak4flav1[l]
                        b_min = b_add
    if b_min==0 and len(ak4jets2Pre) > 1 and ak8Jet2.Pt() > 250 and treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr > 40:
        fatjet = ak8Jet2
        pmass = treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr
        bbtag = treeMine.jet2bbtag
        order = 2
        if treeMine.jet2tau2 > 0:
            fatjet32 = treeMine.jet2tau3/treeMine.jet2tau2
        else:
            fatjet32 = -100.
        fatjetp21 = treeMine.jet2_puppi_tau21
        if treeMine.jet2tau1 > 0:
            fatjet21 = treeMine.jet2tau2/treeMine.jet2tau1
            fatjet31 = treeMine.jet2tau3/treeMine.jet2tau1
        else:
            fatjet21 = -100.
            fatjet31 = -100.
        fatjetptCA = treeMine.CA15jet2pt
        fatjetetaCA = treeMine.CA15jet2eta
        fatjetphiCA = treeMine.CA15jet2phi
        fatjetmCA = treeMine.CA15jet2mass
        if treeMine.CA15jet2pt > 0:
            fatjetAKCA = fatjet.Pt()/treeMine.CA15jet2pt
        else:
            fatjetAKCA = -100.
        if treeMine.isData < 1:
            #l1l2l3 = treeMine.jet2l1l2l3 
            #l2l3 = treeMine.jet2l2l3
            #l1l2l3Up = treeMine.jet2l1l2l3Unc + treeMine.jet2l1l2l3
            #l1l2l3Down = treeMine.jet2l1l2l3 - treeMine.jet2l1l2l3Unc
            #l2l3Unc = treeMine.jet2l2l3Unc
            ak8jer = pt2smear
            ak8jerUp = pt2smearUp
            ak8jerDown = pt2smearDown
            hadw = -1.
        b_min = 0.
        jet3_p4=TLorentzVector()
        jet4_p4=TLorentzVector()
        for k in range(len(ak4jets2Pre)):
            jet3_p4.SetPtEtaPhiM(ak4jets2Pre[k].Pt(), ak4jets2Pre[k].Eta(), ak4jets2Pre[k].Phi(), ak4jets2Pre[k].M())
            for l in range(len(ak4jets2Pre)):
                if (l!=k):
                    jet4_p4.SetPtEtaPhiM(ak4jets2Pre[l].Pt(), ak4jets2Pre[l].Eta(), ak4jets2Pre[l].Phi(), ak4jets2Pre[l].M())
                    deltaRak4=jet3_p4.DeltaR(jet4_p4)
                    b_add = ak4jets2csv[k] + ak4jets2csv[l]
                    if b_min < b_add and deltaRak4 < 1.5:
                        ak4jet1 = ak4jets2Pre[k]
                        ak4jet1btag= ak4jets2csv[k]
                        ak4jet1i = ak4jet2ID[k]
                        if treeMine.isData < 1:
                            ak4jet1corr = ak4corr2[k]
                            ak4jet1jecup = ak4jecup2[k]
                            ak4jet1jecdown = ak4jecdown2[k]
                            ak4jet1jer = ak4jer2[k]
                            ak4jet1jerup = ak4jerup2[k]
                            ak4jet1jerdown = ak4jerdown2[k]
                            ak4jet1flav = ak4flav2[k]
                        ak4jet2 = ak4jets2Pre[l]
                        ak4jet2btag= ak4jets2csv[l]
                        ak4jet2i = ak4jet2ID[l]
                        if treeMine.isData < 1:
                            ak4jet2corr = ak4corr2[l]
                            ak4jet2jecup = ak4jecup2[l]
                            ak4jet2jecdown = ak4jecdown2[l]
                            ak4jet2jer = ak4jer2[l]
                            ak4jet2jerup = ak4jerup2[l]
                            ak4jet2jerdown = ak4jerdown2[l]
                            ak4jet2flav = ak4flav2[l]
                        b_min = b_add
    if b_min == 0:
        continue
    
    if triggerpass > 0:
        tpo5.Fill(triggerpass)

    pTH1=(fatjet).Pt()
    pTH2=(ak4jet1+ak4jet2).Pt()
    mH1=pmass
    mH2=(ak4jet1+ak4jet2).M()
    f1[0]=(ak4jet1+ak4jet2+fatjet).M()
    Red_mass[0] = (ak4jet1+ak4jet2+fatjet).M() - mH2 - mH1 + 250
    deltaEta[0] = abs(fatjet.Eta() - (ak4jet1+ak4jet2).Eta())
    g1[0]=mH2
    h1[0]=mH1
    i1[0]=treeMine.xsec
    l1[0]=bbtag
    o1[0]=treeMine.puWeights
    puW_up[0] = treeMine.puWeightsUp
    puW_down[0] = treeMine.puWeightsDown
    jet1_ungroomed_TL = ROOT.TLorentzVector()
    jet2_ungroomed_TL = ROOT.TLorentzVector()
    jet1_ungroomed_TL.SetPtEtaPhiM(treeMine.jet1pt, treeMine.jet1eta, treeMine.jet1phi, treeMine.jet1mass)
    jet2_ungroomed_TL.SetPtEtaPhiM(treeMine.jet2pt, treeMine.jet2eta, treeMine.jet2phi, treeMine.jet2mass)
    dijetmass_softdrop_corr = (jet1_ungroomed_TL + jet2_ungroomed_TL).M() - (treeMine.jet1_puppi_msoftdrop_raw*treeMine.jet1_puppi_TheaCorr - 125) - (treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr - 125)
    if (treeMine.HLT_PFHT900_v==1 or treeMine.HLT_PFHT800_v==1 or treeMine.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v==1 or treeMine.HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v==1 or treeMine.HLT_AK8PFJet360_TrimMass30_v==1 or treeMine.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v==1 or treeMine.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v==1) and (treeMine.jet1pt > 300 and treeMine.jet2pt > 300 and abs(treeMine.jet1eta) < 2.4 and abs(treeMine.jet2eta) < 2.4) and (abs(treeMine.jet1eta - treeMine.jet2eta) < 1.3) and (treeMine.jet1ID == 1 and treeMine.jet2ID == 1) and (dijetmass_softdrop_corr > 750) and (treeMine.jet1_puppi_tau21 < 0.55 and treeMine.jet2_puppi_tau21 < 0.55) and (105 < treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr < 135):
        u1[0] = 1.
        if (105 < treeMine.jet1_puppi_msoftdrop_raw*treeMine.jet1_puppi_TheaCorr < 135):
          MM[0] = 1.
        else:
          MM[0] = 0.
        if (treeMine.jet1bbtag > 0.8 and treeMine.jet2bbtag > 0.8):
            TT[0] = 1.
        else:
          TT[0] = 0.
        if (treeMine.jet1bbtag > 0.3 and treeMine.jet2bbtag > 0.3 and treeMine.jet1bbtag < 0.8 and treeMine.jet2bbtag < 0.8):
            LL[0] = 1.
        else:
          LL[0] = 0.
        if (treeMine.jet1bbtag > 0.8 and treeMine.jet2bbtag > 0.3 and treeMine.jet2bbtag < 0.8):
            LT[0] = 1.
        elif (treeMine.jet1bbtag > 0.3 and treeMine.jet1bbtag < 0.8 and treeMine.jet2bbtag > 0.8):
            LT[0] = 1.
        else:
          LT[0] = 0.
    else:
        u1[0] = 0.
        LL[0] = 0.
        TT[0] = 0.
        LT[0] = 0.
        MM[0] = 0.

    nCMVAM = 0
    ak4res = []
    chi2_olda = 200
    chi2_oldb = 200
    foundResa = False
    foundResb = False
    v1[0] = 0
    for j in range(len(treeMine.ak4jet_pt)):
        if treeMine.ak4jetCMVA[j] > 0.4432:
            nCMVAM +=1
        if (treeMine.ak4jetDeepCSVb[j] + treeMine.ak4jetDeepCSVbb[j]) > 0.6324 and treeMine.ak4jet_pt[j] > 30 and (treeMine.ak4jet_eta[j]) < 2.4:
            prejv1_p4=TLorentzVector()
            prejv1_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[j], treeMine.ak4jet_eta[j], treeMine.ak4jet_phi[j], treeMine.ak4jet_mass[j])
            this_pt[0] = prejv1_p4.Pt()
            this_pv[0] = treeMine.nPVs
            this_eta[0] = prejv1_p4.Eta()
            this_mt[0] = prejv1_p4.Mt()
            this_leadTrackPt[0] = treeMine.ak4jetLeadTrackPt[j]
            this_leptonPtRel[0] = treeMine.ak4jetLeadTrackPt[j]
            this_leptonPt[0] = treeMine.ak4jetLeptonPt[j]
            this_LeptonDeltaR[0] = treeMine.ak4jetLeptonDeltaR[j]
            this_neHEF[0] = treeMine.ak4jetNeHEF[j]
            this_neEmEF[0] = treeMine.ak4jetNeEmEF[j]
            this_vtxPt[0] = treeMine.ak4jetVtxPt[j]
            this_vtxMass[0] = treeMine.ak4jetVtxMass[j]
            this_vtx3dL[0] = treeMine.ak4jetVtx3dL[j]
            this_vtxNtrk[0] = treeMine.ak4jetVtxNtrk[j]
            this_vtx3deL[0] = treeMine.ak4jetVtx3deL[j]
            ptregv1 = (reader.EvaluateRegression("BDTG method"))[0]
            jv1_p4 = TLorentzVector()
            jv1_p4.SetPtEtaPhiM(ptregv1, prejv1_p4.Eta(), prejv1_p4.Phi(), prejv1_p4.M())
            ak4res.append(jv1_p4)
            if len(ak4res) > 3:
                    jet1=TLorentzVector()
                    jet2=TLorentzVector()
                    jet3=TLorentzVector()
                    jet4=TLorentzVector()
                    for l in range(len(ak4res)):
                        jet1.SetPtEtaPhiM(ak4res[l].Pt(), ak4res[l].Eta(), ak4res[l].Phi(), ak4res[l].M())
                        for m in range(len(ak4res)):
                            if m!=l:
                                jet2.SetPtEtaPhiM(ak4res[m].Pt(), ak4res[m].Eta(), ak4res[m].Phi(),ak4res[m].M())
                                for n in range(len(ak4res)):
                                    if (n!=l and n!=m):
                                        jet3.SetPtEtaPhiM(ak4res[n].Pt(), ak4res[n].Eta(), ak4res[n].Phi(),ak4res[n].M())
                                        for k in range(len(ak4res)):
                                            if (k!=l and k!=m and k!=n):
                                                jet4.SetPtEtaPhiM(ak4res[k].Pt(),ak4res[k].Eta(), ak4res[k].Phi(),ak4res[k].M())

                                                dijet1=jet1+jet2
                                                dijet2=jet3+jet4
                                            
                                                deltar1=jet1.DeltaR(jet2)
                                                deltar2=jet3.DeltaR(jet4)
                                        
                                                mHig1=dijet1.M()
                                                mHig2=dijet2.M()
                                            
                                                chi2a=((mHig1-120)/20)**2+((mHig2-120)/20)**2
                                                chi2b=((mHig1-125)/20)**2+((mHig2-125)/20)**2
                                                if (chi2a<chi2_olda and deltar1<1.5 and deltar2<1.5):
                                                    chi2_olda=chi2a
                                                    foundResa=True
                                                if (chi2b<chi2_oldb and deltar1<1.5 and deltar2<1.5):
                                                    chi2_oldb=chi2b
                                                    foundResb=True

    if foundResa:
        chi=chi2_olda**0.5
        if chi<1:
            if treeMine.HLT_QuadJet45_TripleBTagCSV_p087_v + treeMine.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v > 0:
                v1[0] = 1

    if foundResb:
        chi=chi2_oldb**0.5
        if chi<1:
            if treeMine.HLT_QuadJet45_TripleBTagCSV_p087_v + treeMine.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v > 0:
                v1[0] = 1
                
    if nCMVAM > 3:
        hhsm[0] = 1

    fjak4 = 1000
    ak1ak4 = 1000
    ak2ak4 = 1000
    fjak4s = 1000
    n1 = 0
    n2 = 0
    fjak4spt = -100.
    fjak4seta = -100.
    fjak4sphi = -100.
    fjak4sm = -100.
    fjak4pt = -100.
    fjak4eta = -100.
    fjak4phi = -100.
    fjak4m = -100.
    for j in range(len(treeMine.ak4jet_pt)):
        j_p4=TLorentzVector()
        j_p4.SetPtEtaPhiM(treeMine.ak4jet_pt[j], treeMine.ak4jet_eta[j], treeMine.ak4jet_phi[j], treeMine.ak4jet_mass[j])
        deltaRFJ = fatjet.DeltaR(j_p4)
        if deltaRFJ < fjak4:
            fjak4 = deltaRFJ
            fjak4pt = j_p4.Pt()
            fjak4eta = j_p4.Eta()
            fjak4phi = j_p4.Phi()
            fjak4m = j_p4.M()
            fjak4index = j
        deltaRFJs = fatjet.DeltaR(j_p4)
        if (deltaRFJs < fjak4s) and (deltaRFJs > 0.8) and (j != ak4jet1i) and (j != ak4jet2i):
            fjak4s = deltaRFJs
            fjak4spt = j_p4.Pt()
            fjak4seta = j_p4.Eta()
            fjak4sphi = j_p4.Phi()
            fjak4sm = j_p4.M()
        deltaRAK1 = ak4jet1.DeltaR(j_p4)
        if deltaRAK1 < 1.5 and (j != ak4jet1i):
            n1 += 1
        if (deltaRAK1 < ak1ak4) and (j != ak4jet1i) and (j != ak4jet2i):
            ak1ak4 = deltaRAK1
            ak1ak4pt = j_p4.Pt()
            ak1ak4eta = j_p4.Eta()
            ak1ak4phi = j_p4.Phi()
            ak1ak4m = j_p4.M()
        deltaRAK2 = ak4jet2.DeltaR(j_p4)
        if deltaRAK2 < 1.5 and (j != ak4jet2i):
            n2 += 1
        if (deltaRAK2 < ak2ak4) and (j != ak4jet1i) and (j != ak4jet2i):
            ak2ak4 = deltaRAK2
            ak2ak4pt = j_p4.Pt()
            ak2ak4eta = j_p4.Eta()
            ak2ak4phi = j_p4.Phi()
            ak2ak4m = j_p4.M()
    
    nAK4near1[0] = n1
    nAK4near2[0] = n2
    ak4nfatjetPT[0] = fjak4pt
    ak4nfatjetETA[0] = fjak4eta
    ak4nfatjetPHI[0] = fjak4phi
    ak4nfatjetM[0] = fjak4m
    sak4nfatjetPT[0] = fjak4spt
    sak4nfatjetETA[0] = fjak4seta
    sak4nfatjetPHI[0] = fjak4sphi
    sak4nfatjetM[0] = fjak4sm
    ak4nbjet1PT[0] = ak1ak4pt
    ak4nbjet1ETA[0] = ak1ak4eta
    ak4nbjet1PHI[0] = ak1ak4phi
    ak4nbjet1M[0] = ak1ak4m
    ak4nbjet2PT[0] = ak2ak4pt
    ak4nbjet2ETA[0] = ak2ak4eta
    ak4nbjet2PHI[0] = ak2ak4phi
    ak4nbjet2M[0] = ak2ak4m
    ak4nbjet1 = TLorentzVector()
    ak4nbjet1.SetPtEtaPhiM(ak1ak4pt, ak1ak4eta, ak1ak4phi, ak1ak4m)
    ak4nbjet2 = TLorentzVector()
    ak4nbjet2.SetPtEtaPhiM(ak2ak4pt, ak2ak4eta, ak2ak4phi, ak2ak4m)
    if ak4nbjet1.DeltaR(ak4jet1) < ak4nbjet2.DeltaR(ak4jet2):
        invmAK4[0] = (ak4jet1 + ak4jet2 + ak4nbjet1).M()
    else:
        invmAK4[0] = (ak4jet1 + ak4jet2+ ak4nbjet2).M()


#    run[0] = treeMine.run
    evt[0] = treeMine.evt
#    lumi[0] = treeMine.lumi
    if options.ttbar == "True":
        ttHT[0] = treeMine.tPtsum
    fatjetPT[0] = fatjet.Pt()
    fatjetETA[0] = fatjet.Eta()
    fatjetPHI[0] = fatjet.Phi()
    fatjetM[0] = fatjet.M()
    fatjetN[0] = order
    if treeMine.isData < 1:
       # fatjetl1l2l3[0] = l1l2l3
       # fatjetl2l3[0] = l2l3
       # fatjetl1l2l3Up[0] = l1l2l3Up
       # fatjetl1l2l3Down[0] = l1l2l3Down
       # fatjetl2l3Unc[0] = l2l3Unc
        fatjetJER[0] = ak8jer
        fatjetJERUp[0] = ak8jerUp
        fatjetJERDown[0] = ak8jerDown
        fatjetMatchedHadW[0] = hadw
    fatjettau32[0] = fatjet32
    fatjettau21[0] = fatjet21
    fatjetptau21[0] = fatjetp21
    fatjettau31[0] = fatjet31
    fatjetAKCAratio[0] = fatjetAKCA
    fatjetCAPT[0] = fatjetptCA
    fatjetCAETA[0] = fatjetetaCA
    fatjetCAPHI[0] = fatjetphiCA
    fatjetCAM[0] = fatjetmCA
    bjet1PT[0] = ak4jet1.Pt()
    bjet1ETA[0] = ak4jet1.Eta()
    bjet1PHI[0] = ak4jet1.Phi()
    bjet1M[0] = ak4jet1.M()
    bjet2PT[0] = ak4jet2.Pt()
    bjet2ETA[0] = ak4jet2.Eta()
    bjet2PHI[0] = ak4jet2.Phi()
    bjet2M[0] = ak4jet2.M()
    HT[0] = treeMine.ht
    ak4btag1[0] = ak4jet1btag
    ak4btag2[0] = ak4jet2btag
    if treeMine.isData < 1:
        ak4jetCorr1[0] = ak4jet1corr
        ak4jetCorrJECUp1[0] = ak4jet1jecup 
        ak4jetCorrJECDown1[0] = ak4jet1jecdown
        ak4jetCorrJER1[0] = ak4jet1jer
        ak4jetCorrJERUp1[0] = ak4jet1jerup
        ak4jetCorrJERDown1[0] = ak4jet1jerdown
        ak4jetflav1[0] = ak4jet1flav
        ak4jetCorr2[0] = ak4jet2corr
        ak4jetCorrJECUp2[0] = ak4jet2jecup 
        ak4jetCorrJECDown2[0] = ak4jet2jecdown
        ak4jetCorrJER2[0] = ak4jet2jer
        ak4jetCorrJERUp2[0] = ak4jet2jerup
        ak4jetCorrJERDown2[0] = ak4jet2jerdown
        ak4jetflav2[0] = ak4jet2flav

    if treeMine.isData < 1:
      if options.ttbar == "True":
        if fatjetPT[0] <= 250:
          SF[0] = 1.050
          SFup[0] = 1.138
          SFdown[0] = 0.962
        elif fatjetPT[0] > 250 and fatjetPT[0] <= 350:
          SF[0] = 1.050
          SFup[0] = 1.094
          SFdown[0] = 1.006
        elif fatjetPT[0] > 350 and fatjetPT[0] <= 700:
          SF[0] = 1.086
          SFup[0] = 1.164
          SFdown[0] = 1.008
        elif fatjetPT[0] > 700:
          SF[0] = 1.086
          SFup[0] = 1.242
          SFdown[0] = 0.93
      else:
        if fatjetPT[0] <= 250:
            SF[0] = 0.92
            SFup[0] = 0.98
            SFdown[0] = 0.86
        elif fatjetPT[0] > 250 and fatjetPT[0] <= 350:
            SF[0] = 0.92 
            SFup[0] = 0.95
            SFdown[0] = 0.89
        elif fatjetPT[0] > 350 and fatjetPT[0] <= 430:
            SF[0] = 1.01
            SFup[0] = 1.04
            SFdown[0] = 0.97
        elif fatjetPT[0] > 430 and fatjetPT[0] <= 840:
            SF[0] = 0.92
            SFup[0] = 0.95
            SFdown[0] = 0.87
        elif fatjetPT[0] > 840:
            SF[0] = 0.92
            SFup[0] = 0.98
            SFdown[0] = 0.82

        if abs(ak4jetflav1[0]) == 5:
            ak4jet1sf = readerb.eval_auto_bounds(
                'central',      
                0,             
                bjet1ETA[0],           
                bjet1PT[0]            
                )
            ak4jet1sfup = readerb.eval_auto_bounds(
                'up',
                0,
                bjet1ETA[0],
                bjet1PT[0]
                )
            ak4jet1sfdown = readerb.eval_auto_bounds(
                'down',
                0,
                bjet1ETA[0],
                bjet1PT[0]
                )
        elif abs(ak4jetflav1[0]) == 4:
            ak4jet1sf = readerc.eval_auto_bounds(
                'central',      
                1,             
                bjet1ETA[0],           
                bjet1PT[0]            
                )
            ak4jet1sfup = readerc.eval_auto_bounds(
                'up',
                1,
                bjet1ETA[0],
                bjet1PT[0]
                )
            ak4jet1sfdown = readerc.eval_auto_bounds(
                'down',
                1,
                bjet1ETA[0],
                bjet1PT[0]
                )
        else:
            ak4jet1sf = readerl.eval_auto_bounds(
                'central',      
                2,             
                bjet1ETA[0],           
                bjet1PT[0]            
                )
            ak4jet1sfup = readerl.eval_auto_bounds(
                'up',
                2,
                bjet1ETA[0],
                bjet1PT[0]
                )
            ak4jet1sfdown = readerl.eval_auto_bounds(
                'down',
                2,
                bjet1ETA[0],
                bjet1PT[0]
                )
        if abs(ak4jetflav2[0]) == 5:
            ak4jet2sf = readerb.eval_auto_bounds(
                'central',      
                0,             
                bjet2ETA[0],           
                bjet2PT[0]            
                )
            ak4jet2sfup = readerb.eval_auto_bounds(
                'up',
                0,
                bjet2ETA[0],
                bjet2PT[0]
                )
            ak4jet2sfdown = readerb.eval_auto_bounds(
                'down',
                0,
                bjet2ETA[0],
                bjet2PT[0]
                )
        elif abs(ak4jetflav2[0]) == 4:
            ak4jet2sf = readerc.eval_auto_bounds(
                'central',      
                1,             
                bjet2ETA[0],           
                bjet2PT[0]            
                )
            ak4jet2sfup = readerc.eval_auto_bounds(
                'up',
                1,
                bjet2ETA[0],
                bjet2PT[0]
                )
            ak4jet2sfdown = readerc.eval_auto_bounds(
                'down',
                1,
                bjet2ETA[0],
                bjet2PT[0]
                )
        else:
            ak4jet2sf = readerl.eval_auto_bounds(
                'central',      
                2,             
                bjet2ETA[0],           
                bjet2PT[0]            
                )
            ak4jet2sfup = readerl.eval_auto_bounds(
                'up',
                2,
                bjet2ETA[0],
                bjet2PT[0]
                )
            ak4jet2sfdown = readerl.eval_auto_bounds(
                'down',
                2,
                bjet2ETA[0],
                bjet2PT[0]
                )
        ak4btag1SF[0] = ak4jet1sf
        ak4btag1SFup[0] = ak4jet1sfup
        ak4btag1SFdown[0] = ak4jet1sfdown
        ak4btag2SF[0] = ak4jet2sf
        ak4btag2SFup[0] = ak4jet2sfup
        ak4btag2SFdown[0] = ak4jet2sfdown

        #trigger efficiencies based off of reduced mass
        for i in range(0, 53):
            lowmass = i*50.
            highmass = lowmass + 50.
            if Red_mass[0] <= highmass and Red_mass[0] > lowmass:
              if deltaEta[0] < 1.0:
                trigWeight[0] = trigSFdEta0[i]
                trigWeightUp[0] = trigSFUpdEta0[i]
                trigWeightDown[0] = trigSFDowndEta0[i]
              else:
                trigWeight[0] = trigSFdEta1[i]
                trigWeightUp[0] = trigSFUpdEta1[i]
                trigWeightDown[0] = trigSFDowndEta1[i]
                
    if options.saveTrig == 'True':
        HLT2_HT800[0]= treeMine.HLT_PFHT800_v
        HLT2_PFJet260[0] = treeMine.HLT_PFJet260_v
        HLT2_PFJet200[0] = treeMine.HLT_PFJet200_v
        HLT2_PFJet140[0] = treeMine.HLT_PFJet140_v
        HLT2_Quad_Triple[0] = treeMine.HLT_QuadJet45_TripleBTagCSV_p087_v
        HLT2_Double_Triple[0] = treeMine.HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v
        HLT2_DiPFJet280[0] = treeMine.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v
        HLT2_AK8PFHT650[0] = treeMine.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v
        HLT2_AK8PFJet360[0] = treeMine.HLT_AK8PFJet360_TrimMass30_v
        HLT2_PFHT650[0] = treeMine.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v
        HLT2_PFHT900[0] = treeMine.HLT_PFHT900_v
        HLT2_AK8PFHT700[0] = treeMine.HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v
        HLT2_Mu27[0] = treeMine.HLT_Mu27_v
        
    if triggerpass > 0 and 105 < mH1 < 135 and 105 < mH2 < 135:
        tpo6.Fill(triggerpass)

    if triggerpass > 0 and 105 < mH1 < 135 and 105 < mH2 < 135 and bbtag > 0.8:
        tpo7.Fill(triggerpass) 

    if triggerpass > 0 and 105 < mH1 < 135 and 105 < mH2 < 135 and bbtag > 0.9:
        tpo8.Fill(triggerpass) 

    if triggerpass > 0 and 105 < mH1 < 135 and 105 < mH2 < 135 and bbtag > 0.6:
        tpo9.Fill(triggerpass) 


    mynewTree.Fill()

f2.cd()
f2.Write()
f2.Close()

f.Close()


