#!/usr/bin/env python

### PDF4LHC recommendations for LHC Run II: http://arxiv.org/abs/1510.03865

import os, sys, ROOT
import math
from ROOT import *
from math import *
import glob
import FWCore.ParameterSet.Config as cms
from DataFormats.FWLite import Events, Handle
from array import *
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-n", "--num", dest="num",
                  help="number of files")
(options, args) = parser.parse_args()
nF = int(options.num)

allevt = 0
allevtup = []
allevtlo = []
passevt = 0
passevtup = []
passevtlo = []

for j in range(0, nF):
    f = ROOT.TFile.Open(sys.argv[j+1],"READ")
    treeMine = f.Get('mynewTree')
    nPDF = treeMine.GetEntries();
    allEvtUp = []
    allEvtLo = []
    passEvtUp = []
    passEvtLo = []
    for i in range(0, nPDF):
        treeMine.GetEntry(i)
        allEvt = treeMine.allEvt
#        if i%2 == 1:
        allEvtUp.append(treeMine.allEvtUp)
        passEvtUp.append(treeMine.passEvtUp)
        passEvt = treeMine.passEvt
 #       if i%2 == 0: 
        passEvtLo.append(treeMine.passEvtLo)
        allEvtLo.append(treeMine.allEvtLo)
    allevt += allEvt
    passevt += passEvt
    if j == 0:
        allevtup = allEvtUp
        passevtup = passEvtUp
        allevtlo = allEvtLo
        passevtlo = passEvtLo
    else:
        for k in range(0, 50):
            allevtup[k] += allEvtUp[k]
            passevtup[k] += passEvtUp[k]
            allevtlo[k] += allEvtLo[k]
            passevtlo[k] += passEvtLo[k]

print allevtup
print allevtlo
print passevtup
print passevtlo
            
  #evtwt passing/ all evt wt
aenominal = passevt/allevt
  
allevtup_sum=0
for k in allevtup:
    allevtup_sum += pow(k - allevt,2.)
allevtup_sum = math.sqrt(allevtup_sum/100)

passevtup_sum=0
for k in passevtup:
    passevtup_sum += pow(k - passevt,2.)
passevtup_sum = math.sqrt(passevtup_sum/100)

  #total pdf up passing / total pdf up all
aepdfup = passevtup_sum/allevtup_sum

allevtlo_sum=0
for k in allevtlo:
    allevtlo_sum += pow(k - allevt,2.)
allevtlo_sum = math.sqrt(allevtlo_sum/100)

passevtlo_sum=0
for k in passevtlo:
    passevtlo_sum += pow(k - passevt,2.)
passevtlo_sum = math.sqrt(passevtlo_sum/100)

  #total pdf down passing / total pdf down all
aepdflo = passevtlo_sum/allevtlo_sum

print aepdfup/aenominal
print aepdflo/aenominal
