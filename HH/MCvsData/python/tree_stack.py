#!/usr/bin/env python
import pickle
import ROOT 
from array import array
import sys, os
from optparse import OptionParser
from copy import copy,deepcopy
from math import sqrt
ROOT.gROOT.SetBatch(True)

#CONFIGURE
argv = sys.argv
parser = OptionParser()
parser.add_option("-R", "--region", dest="region", default="",
                      help="region to plot")
parser.add_option("-C", "--config", dest="config", default=[], action="append",
                      help="configuration file")
(opts, args) = parser.parse_args(argv)
if opts.config =="":
        opts.config = "config"
        
from myutils import BetterConfigParser, printc, ParseInfo, mvainfo, StackMaker, HistoMaker

print opts.config
config = BetterConfigParser()
config.read(opts.config)

#path = opts.path
region = opts.region

# additional blinding cut:
addBlindingCut = None
if config.has_option('Plot_general','addBlindingCut'):
    addBlindingCut = config.get('Plot_general','addBlindingCut')
    print 'adding add. blinding cut'

#get locations:
Wdir=config.get('Directories','Wdir')
samplesinfo=config.get('Directories','samplesinfo')

path = config.get('Directories','plottingSamples')

section='Plot:%s'%region

info = ParseInfo(samplesinfo,path)

if os.path.exists("../interface/DrawFunctions_C.so"):
    print 'ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")'
    ROOT.gROOT.LoadMacro("../interface/DrawFunctions_C.so")

#----------Histo from trees------------
def doPlot():
    vars = (config.get(section, 'vars')).split(',')
    data = config.get(section,'Datas')
    mc = eval(config.get('Plot_general','samples'))

    SignalRegion = False
    if config.has_option(section,'Signal'):
        mc.append(config.get(section,'Signal'))
        SignalRegion = True
            
    datasamples = info.get_samples(data)
    #print datasamples
    mcsamples = info.get_samples(mc)
    #print mcsamples
    #print path

    GroupDict = eval(config.get('Plot_general','Group'))

    #GETALL AT ONCE
    options = []
    Stacks = []
    for i in range(len(vars)):
        Stacks.append(StackMaker(config,vars[i],region,SignalRegion))
        options.append(Stacks[i].options)
    #print options

    Plotter=HistoMaker(mcsamples+datasamples,path,config,options,GroupDict)

    #print '\nProducing Plot of %s\n'%vars[v]
    Lhistos = [[] for _ in range(0,len(vars))]
    Ltyps = [[] for _ in range(0,len(vars))]
    Ldatas = [[] for _ in range(0,len(vars))]
    Ldatatyps = [[] for _ in range(0,len(vars))]
    Ldatanames = [[] for _ in range(0,len(vars))]

    #Find out Lumi:
    lumicounter=0.
    lumi=0.
    for job in datasamples:
        lumi+=float(job.lumi)
        lumicounter+=1.
	print 'lumicounter: '
	print lumicounter

    if lumicounter > 0:
        lumi=lumi/lumicounter

    Plotter.lumi=lumi
    mass = Stacks[0].mass

    for job in mcsamples:
        #hTempList, typList = Plotter.get_histos_from_tree(job)
        if addBlindingCut:
            hDictList = Plotter.get_histos_from_tree(job,config.get('Cuts',region)+' & ' + addBlindingCut)
        else:
            hDictList = Plotter.get_histos_from_tree(job)
        if job.name == mass:
            print job.name
            Overlaylist= deepcopy([hDictList[v].values()[0] for v in range(0,len(vars))])
        for v in range(0,len(vars)):
            Lhistos[v].append(hDictList[v].values()[0])
            Ltyps[v].append(hDictList[v].keys()[0])

    for job in datasamples:
        #hTemp, typ = Plotter.get_histos_from_tree(job)
        if addBlindingCut:
            dDictList = Plotter.get_histos_from_tree(job,config.get('Cuts',region)+' & ' + addBlindingCut)
        else:
            dDictList = Plotter.get_histos_from_tree(job)
        for v in range(0,len(vars)):
	    print 'dDictList: '
	    print dDictList
            Ldatas[v].append(dDictList[v].values()[0])
            Ldatatyps[v].append(dDictList[v].keys()[0])
            Ldatanames[v].append(job.name)
	    print Ldatanames[v]
	    print Ldatas[v]

    for v in range(0,len(vars)):

        histos = Lhistos[v]
        typs = Ltyps[v]
        Stacks[v].histos = Lhistos[v]
        Stacks[v].typs = Ltyps[v]
        Stacks[v].datas = Ldatas[v]
        Stacks[v].datatyps = Ldatatyps[v]
        Stacks[v].datanames= Ldatanames[v]
        #if SignalRegion:
        #    Stacks[v].overlay = Overlaylist[v]
        Stacks[v].lumi = lumi
        Stacks[v].doPlot()
        Stacks[v].histos = Lhistos[v]
        Stacks[v].typs = Ltyps[v]
        Stacks[v].datas = Ldatas[v]
        Stacks[v].datatyps = Ldatatyps[v]
        Stacks[v].datanames= Ldatanames[v]
        Stacks[v].normalize = True
        Stacks[v].options['pdfName'] = Stacks[v].options['pdfName'].replace('.pdf','_norm.pdf')
        Stacks[v].doPlot()
        print 'i am done!\n'
#----------------------------------------------------
doPlot()
sys.exit(0)
