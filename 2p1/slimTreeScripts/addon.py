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
parser.add_option("-d", "--data", dest="data",
                  help="isdata")
parser.add_option("-b", "--ttbar", dest="ttbar",
                  help="isttbar")
(options, args) = parser.parse_args()
outputfilename = options.outName



#trigger SFs
#trigSFdEta0 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0108459869848156, 1.0135635018495686, 0.976682622570351, 1.0211962438758846, 0.9827501516946459, 1.123758744179627, 0.9734683598949527, 0.8994249353773404, 0.9689032105317371, 0.9577702390496463, 0.9823622336517268, 0.9890812290700821, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFUpdEta0 = [1.0939849624060152, 1.0751879699248121, 1.0565804795968703, 1.0378019428465677, 1.0394817403026815, 1.0407346027815376, 1.0568945333685424, 1.0864103466592585, 1.0940166406336427, 1.156386177248416, 1.3413086236608123, 1.3419215079158664, 1.5256913366408837, 1.3062412129543783, 1.142232902778897, 1.1323328572968094, 1.0478832227259216, 1.0307550573849393, 1.0088764155710892, 1.010666206420435, 1.003410020914795, 1.0012693577050014, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095, 2.414213562373095]
#trigSFDowndEta0 = [0.13950946755530114, 0.15518159814116494, 0.8064698743836028, 0.8848682499740125, 0.9085302006365152, 0.923164539539495, 0.9292715871923337, 0.9311383761232073, 0.9314350800255777, 0.7966703916051777, 0.7008959381678028, 0.6233727241325318, 0.7216443412498479, 0.6403873070853199, 0.6562731391783462, 0.8049046408763654, 0.8654884420808598, 0.9279839737149949, 0.9484160156351846, 0.9648188387959707, 0.9471718312930084, 0.9197032590439469, 0.7357655683286832, 0.7944197899369732, 0.8318164994392157, 0.5413390577390398, 0.7356857216118726, 0.15861284069096604, 0.630955589899722, 0.3980547855171185, 0.15839473811466598, 0.39750489232149333, 0.15756289309327043, 0.15700587460312931, 0.1564097492861095, 0.9197229440674958, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.0, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]

#trigSFdEta1 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0273224043715847, 1.014335145823035, 0.7796143250688705, 0.8976925687139464, 0.8577763239196016, 0.8954837328767123, 0.9947652347652347, 0.9162004579467933, 0.9851987447698745, 1.00065528661312, 1.037318490129878, 0.9398525359508609, 0.9812667261373773, 0.9765548719061419, 0.9505225741418643, 0.9234091995165054, 0.9826625225725795, 0.9483444844741808, 0.9485409886054602, 0.9928433268858802, 1.0112293987214565, 0.9627766599597586, 0.9874451754385964, 0.9048509955900039, 0.9888111635305388, 0.9638991552270328, 0.9628682856487398, 1.0707417582417582, 0.9653716216216216, 1.0274949083503055, 0.9166666666666666, 0.875, 1.0439739413680782, 1.0091603053435114, 1.0098199672667758, 1.0425531914893618, 0.8675450762829403, 1.014018691588785, 1.0146198830409356, 1.0, 1.0, 0.9059174116645381, 1.030456852791878, 0.6666666666666666, 0.33333333333333326, 0., 0., 0., 0., 0.]
#trigSFUpdEta1 = [1.0, 1.0, 1.1190311523320813, 1.1457650703072844, 1.1146887958281324, 1.090913241370335, 1.0861291853901271, 1.0804121728649845, 1.0684515060395492, 1.0386937235464984, 1.0856417054417045, 1.159820428236897, 1.0106454116165227, 1.2214509754047855, 1.1591545786164001, 1.221171174182325, 1.3368881960159174, 1.1843119399583533, 1.2389347597772624, 1.2123634104268621, 1.2309192895360315, 1.0793806963787713, 1.1270258295992834, 1.098758185368669, 1.0697552012922398, 1.0244113768392922, 1.0927072823245434, 1.0366800666473397, 1.0126484632504067, 1.0914456955629257, 1.0876002290030917, 1.0701299455578965, 1.0965416634887404, 0.9645363593375753, 1.0474364050639295, 1.0191275883383686, 1.008703192439878, 1.206083730115986, 0.98998810768447, 1.1243823196452327, 1.0037292651642264, 0.9235592315901815, 1.1485978322755201, 1.0765466206311187, 1.3049709346357923, 1.1077127659574468, 1.8799144097208624, 2.028743042834847, 2.0297316765712408, 2.003891903689068, 2.000198842253103, 1.9252332221472828, 2.0610988522404403, 1.868546224371884, 1.387438361117068, 0.9999999999999999, 0.7753344614935782, 0.5351837584879965, 0.41476799288047594, 0.33362445415069186]
#trigSFDowndEta1 = [0.7238449712716393, 0.3981229310642277, 0.7422751286395539, 0.8026864763113837, 0.8340745138431198, 0.8879378256848235, 0.8978894847399698, 0.9082489828955099, 0.9238237060822352, 0.9551509446265528, 0.9645305437579014, 0.8665539246480662, 0.5474834532107302, 0.5729817468177147, 0.555230012553001, 0.5683423579752227, 0.6495795104885598, 0.6457966574451199, 0.7269256767923283, 0.7858271994142076, 0.8395159435873418, 0.7922586165741006, 0.8223838278076301, 0.8337423265994243, 0.8094894090924887, 0.7967857216265004, 0.8431772055081057, 0.8173960900127831, 0.846466396779694, 0.836077092779216, 0.8547864659061508, 0.7744191893422723, 0.8226483350322025, 0.717565168890499, 0.7696711624920567, 0.8413570503352874, 0.7245743531210806, 0.791335342274439, 0.7731982962245784, 0.6964417932635785, 0.537594011231508, 0.2713379374172121, 0.8192156244847545, 0.1573832046234348, 0.5808018400779169, 0.9768345008679075, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]

#numberLimit = float(sys.argv[1])

#trigSFdEta0 = [3.9830958753802994, 4.3559051484897005, 4.923024657534257, 5.889910045490319, 7.909326196806197, 14.752621411737515, 0., 0., 0., 0., 0., 0.14073408061352966, 0.47159121329029186, 0.7100655289054277, 0.8901098901098901, 1.0308550185873606, 0.9132368460726669, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFUpdEta0 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.8108637105181025, 0., 0., 0., 0.23069629610165182, 0.7166077018044468, 0.9939993867272175, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFDowndEta0 = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.5552194175326198, 0.2204566275683444, 0.8480084894939368, 0.09965321097204971, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFdEta1 = [0.34171154300956447, 0.3533532154885635, 0.3664623615509309, 0.3813351158796554, 0.3983530390136312, 0.41801631492461355, 0.44099373443459167, 0.4682002778242589, 0.5009218779095986, 0.5410246129541598, 0.5913234613653321, 0.6562732874349062, 0.7433665637703893, 0.8662544505227938, 1.0527114144861585, 1.3692722371967654, 1.0158607350096711, 0.9635478352414791, 0.9878873966942149, 0.9738893617021276, 1.0328113348247576, 0.9166666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFUpdEta1 = [0.6842929587866644, 0.6933095939646388, 0.7036609217367031, 0.7154938809521858, 0.7296303685901853, 0.7476899863342854, 0.7698696016772315, 0.7982883894348123, 0.832011911120617, 0.8756823134010105, 0.9320228637357391, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#trigSFDowndEta1 = [0.004330742716100844, 0.007797827451695105, 0.028699623392710094, 0.045567088251500076, 0.06636735333482863, 0.08713290749627445, 0.11078073723799148, 0.1362280758880547, 0.16420797568455464, 0.1994889866526544, 0.22499299031812237, 0.12363545297569056, 0.3505855489799618, 0.1793773081151211, 0.4901947418521466, 0.2858550227335308, 0.016377733774347703, 0.3822895112874798, 0.29735039724859, 0.10527087159417081, 0.9379899294181477, 0.08832607678421145, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

trigSFdEta0 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.8901098901098901, 1.0308550185873606, 0.9132368460726669, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
trigSFUpdEta0 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.1600378185993734, 1.2034903288970646, 0.98999980555529,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
trigSFDowndEta0 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.6142752356102305, 0.8506364838283518, 0.8214091884719226, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
trigSFdEta1 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0527114144861585, 1.3692722371967654, 1.0158607350096711, 0.9635478352414791, 0.9878873966942149, 0.9738893617021276, 0.94, 0.9166666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
trigSFUpdEta1 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.4950824529256705, 1.904833956731782, 1.4019437249768507, 1.2112427498411353, 1.2084117379663502, 1.1322268125337909,1.06,1.0031101834020775, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
trigSFDowndEta1 = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5560146262639349, 0.72132854692502, 0.6155413357042459, 0.6861899018877822, 0.7560227590023999, 0.7962104338848723, 0.79, 0.7962543617611338, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

f = ROOT.TFile.Open(sys.argv[1],"READ")

f2 =  ROOT.TFile(outputfilename, 'recreate')
#print outputfilename
f2.cd()

treeMine  = f.Get('mynewTree')

mynewTree = ROOT.TTree('mynewTree', 'mynewTree')

#run = array('f', [-100.0])
#evt = array('f', [-100.0])
#lumi = array('f', [-100.0])
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

#mynewTree.Branch("run", run, "run")
#mynewTree.Branch("evt", evt, "evt")
#mynewTree.Branch("lumi", lumi, "lumi")
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

    
nevent = treeMine.GetEntries();

if options.data == "False":
    CountWeightedmc = ROOT.TH1F("CountWeighted","Count with sign(gen weight) and pu weight",1,0,2)
    CountWeightedmc.Add(f.Get("CountWeighted"))

counter = 0
for i in range(0, nevent) :
    counter = counter + 1
    treeMine.GetEntry(i)

    bjet1 = TLorentzVector()
    bjet2 = TLorentzVector()
    bjet1.SetPtEtaPhiM(treeMine.bjet1PT, treeMine.bjet1ETA, treeMine.bjet1PHI, treeMine.bjet1M)
    bjet2.SetPtEtaPhiM(treeMine.bjet2PT, treeMine.bjet2ETA, treeMine.bjet2PHI, treeMine.bjet2M)

#    deltaEta[0] = abs(treeMine.fatjetETA - (bjet1 + bjet2).Eta())
    deltaEta[0] = treeMine.deltaEta
    f1[0] = treeMine.Inv_mass
    Red_mass[0] = treeMine.Red_mass
    g1[0] = treeMine.dijet_mass
    h1[0] = treeMine.fatjet_mass
    i1[0] = treeMine.cross_section
    l1[0] = treeMine.fatjet_hbb
    o1[0] = treeMine.puWeight
    u1[0] = treeMine.boosted
    LL[0] = treeMine.LL
    LT[0] = treeMine.LT
    TT[0] = treeMine.TT
    b1[0] = treeMine.b1
    b2[0] = treeMine.b2
    MM[0] = treeMine.MM
    v1[0] = treeMine.resolved
    fatjetPT[0] = treeMine.fatjetPT
    fatjetETA[0] = treeMine.fatjetETA
    fatjetPHI[0] = treeMine.fatjetPHI
    fatjetM[0] = treeMine.fatjetM
    ak4nfatjetPT[0] = treeMine.ak4nfatjetPT
    ak4nfatjetETA[0] = treeMine.ak4nfatjetETA
    ak4nfatjetPHI[0] = treeMine.ak4nfatjetPHI
    ak4nfatjetM[0] = treeMine.ak4nfatjetM
    sak4nfatjetPT[0] = treeMine.sak4nfatjetPT
    sak4nfatjetETA[0] = treeMine.sak4nfatjetETA
    sak4nfatjetPHI[0] = treeMine.sak4nfatjetPHI
    sak4nfatjetM[0] = treeMine.sak4nfatjetM
    #fatjetl1l2l3[0] = treeMine.fatjetl1l2l3
    #fatjetl2l3[0] = treeMine.fatjetl2l3
    #fatjetl1l2l3Up[0] = treeMine.fatjetl1l2l3Up
    #fatjetl1l2l3Down[0] = treeMine.fatjetl1l2l3Down
    #fatjetl2l3Unc[0] = treeMine.fatjetl2l3Unc
    fatjetJER[0] = treeMine.fatjetJER
    fatjetJERUp[0] = treeMine.fatjetJERUp
    fatjetJERDown[0] = treeMine.fatjetJERDown
    fatjetMatchedHadW[0] = treeMine.fatjetMatchedHadW
    fatjettau32[0] = treeMine.fatjettau32
    fatjettau21[0] = treeMine.fatjettau21
    fatjetptau21[0] = treeMine.fatjetptau21
    fatjettau31[0] = treeMine.fatjettau31
    fatjetAKCAratio[0] = treeMine.fatjetAKCAratio
    fatjetCAPT[0] = treeMine.fatjetCAPT
    fatjetCAETA[0] = treeMine.fatjetCAETA
    fatjetCAPHI[0] = treeMine.fatjetCAPHI
    fatjetCAM[0] = treeMine.fatjetCAM
    bjet1PT[0] = treeMine.bjet1PT
    bjet1ETA[0] = treeMine.bjet1ETA
    bjet1PHI[0] = treeMine.bjet1PHI
    bjet1M[0] = treeMine.bjet1M
    bjet2PT[0] = treeMine.bjet2PT
    bjet2ETA[0] = treeMine.bjet2ETA
    bjet2PHI[0] = treeMine.bjet2PHI
    bjet2M[0] = treeMine.bjet2M
    ak4nbjet1PT[0] = treeMine.ak4nbjet1PT
    ak4nbjet1ETA[0] = treeMine.ak4nbjet1ETA
    ak4nbjet1PHI[0] = treeMine.ak4nbjet1PHI
    ak4nbjet1M[0] = treeMine.ak4nbjet1M
    ak4nbjet2PT[0] = treeMine.ak4nbjet2PT
    ak4nbjet2ETA[0] = treeMine.ak4nbjet2ETA
    ak4nbjet2PHI[0] = treeMine.ak4nbjet2PHI
    ak4nbjet2M[0] = treeMine.ak4nbjet2M
    invmAK4[0] = treeMine.invmAK4
    HT[0] = treeMine.HT
    nAK4[0] = treeMine.nAK4
    nAK4near1[0] = treeMine.nAK4near1
    nAK4near2[0] = treeMine.nAK4near2
    ak4btag1[0] = treeMine.ak4btag1
    ak4btag2[0] = treeMine.ak4btag2
#trigger1[0] = treeMine.
#trigger2[0] = treeMine.
#trigger3[0] = treeMine.
#trigger_pre[0] = treeMine.
    ak4jetCorr1[0] = treeMine.ak4jetCorr1
    ak4jetCorr2[0] = treeMine.ak4jetCorr2
    ak4jetCorrJECUp1[0] = treeMine.ak4jetCorrJECUp1
    ak4jetCorrJECUp2[0] = treeMine.ak4jetCorrJECUp2
    ak4jetCorrJECDown1[0] = treeMine.ak4jetCorrJECDown1
    ak4jetCorrJECDown2[0] = treeMine.ak4jetCorrJECDown2
    ak4jetCorrJER1[0] = treeMine.ak4jetCorrJER1
    ak4jetCorrJER2[0] = treeMine.ak4jetCorrJER2
    ak4jetCorrJERUp1[0] = treeMine.ak4jetCorrJERUp1
    ak4jetCorrJERUp2[0] = treeMine.ak4jetCorrJERUp2
    ak4jetCorrJERDown1[0] = treeMine.ak4jetCorrJERDown1
    ak4jetCorrJERDown2[0] = treeMine.ak4jetCorrJERDown2    
    ak4jetflav1[0] = treeMine.ak4jetflav1
    ak4jetflav2[0] = treeMine.ak4jetflav2
    
    if options.ttbar == "True":
      ttHT[0] = treeMine.ttHT
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
        SF[0] = treeMine.SF
        SFup[0] = treeMine.SFup
        SFdown[0] = treeMine.SFdown
        
    ak4btag1SF[0] = treeMine.ak4btag1SF
    ak4btag1SFup[0] = treeMine.ak4btag1SFup
    ak4btag1SFdown[0] = treeMine.ak4btag1SFdown
    ak4btag2SF[0] = treeMine.ak4btag2SF
    ak4btag2SFup[0] = treeMine.ak4btag2SFup
    ak4btag2SFdown[0] = treeMine.ak4btag2SFdown
    
    puW_up[0] = treeMine.puWeightUp
    puW_down[0] = treeMine.puWeightDown
    hhsm[0] = treeMine.hhsm
    
    HLT2_HT800[0] = treeMine.HLT2_HT800  
    HLT2_Quad_Triple[0] = treeMine.HLT2_Quad_Triple
    HLT2_Double_Triple[0] = treeMine.HLT2_Double_Triple
    HLT2_DiPFJet280[0] = treeMine.HLT2_DiPFJet280
    HLT2_AK8PFHT650[0] = treeMine.HLT2_AK8PFHT650
    HLT2_AK8PFJet360[0] = treeMine.HLT2_AK8PFJet360
    HLT2_PFHT650[0] = treeMine.HLT2_PFHT650
    HLT2_PFHT900[0] = treeMine.HLT2_PFHT900
    HLT2_AK8PFHT700[0] = treeMine.HLT2_AK8PFHT700  
    trigger800[0] = treeMine.trigger800
    triggerBtag[0] = treeMine.triggerBtag
    HLT2_PFJet260[0] = treeMine.HLT2_PFJet260 


    for i in range(0, 53):
      lowmass = i*50.
      highmass = lowmass + 50.
      if Red_mass[0] <= highmass and Red_mass[0] > lowmass:
        if deltaEta[0] < 1.:
            trigWeight[0] = trigSFdEta0[i]
            trigWeightUp[0] = trigSFUpdEta0[i]
            trigWeightDown[0] = trigSFDowndEta0[i]
        else:
            trigWeight[0] = trigSFdEta1[i]
            trigWeightUp[0] = trigSFUpdEta1[i]
            trigWeightDown[0] = trigSFDowndEta1[i]
#    trigWeight[0] = treeMine.trigWeight
#    trigWeightUp[0] = treeMine.trigWeightUp
#    trigWeightDown[0] = treeMine.trigWeightDown
#        else:
#    trigWeight[0] = treeMine.trigWeight
#    trigWeightUp[0] = treeMine.trigWeightUp
#    trigWeightDown[0] = treeMine.trigWeightDown

    mynewTree.Fill()

f2.cd()
f2.Write()
f2.Close()

f.Close()


