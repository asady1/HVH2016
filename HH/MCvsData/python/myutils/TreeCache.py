from __future__ import print_function
import os,sys,subprocess,hashlib
import ROOT
from samplesclass import Sample

class TreeCache:
    def __init__(self, cutList, sampleList, path, config):
        ROOT.gROOT.SetBatch(True)
        self.path = path
        self._cutList = []
        for cut in cutList:
            self._cutList.append('(%s)'%cut.replace(' ',''))
        try:
            self.__tmpPath = os.environ["TMPDIR"]
        except KeyError:
            print("\x1b[32;5m %s \x1b[0m" %open('%s/data/vhbb.txt' %config.get('Directories','vhbbpath')).read())
            print("\x1b[31;5;1m\n\t>>> %s: Please set your TMPDIR and try again... <<<\n\x1b[0m" %os.getlogin())
            sys.exit(-1)

        self.__doCache = True
        if config.has_option('Directories','tmpSamples'):
            self.__tmpPath = config.get('Directories','tmpSamples')
        self.__hashDict = {}
        self.minCut = None
        self.__find_min_cut()
        self.__sampleList = sampleList
        print('\n\t>>> Caching FILES <<<\n')
        self.__cache_samples()
    
    def __find_min_cut(self):
        effective_cuts = []
        for cut in self._cutList:
            if not cut in effective_cuts:
                effective_cuts.append(cut)
        self._cutList = effective_cuts
        self.minCut = '||'.join(self._cutList)

    def __trim_tree(self, sample):
        theName = sample.name
        print('Reading sample <<<< %s' %sample)
        source = '%s/%s' %(self.path,sample.get_path)
	print('%s/%s' %(self.path,sample.get_path))
	print('%s' %self.path)
        checksum = self.get_checksum(source)
        theHash = hashlib.sha224('%s_s%s_%s' %(sample,checksum,self.minCut)).hexdigest()
        self.__hashDict[theName] = theHash
        tmpSource = '%stmp_%s.root'%(self.__tmpPath,theHash)
        print('From: %s' %tmpSource)
        if self.__doCache and self.file_exists(tmpSource):
            return
        output = ROOT.TFile.Open(tmpSource,'create')
        input = ROOT.TFile.Open(source,'read')
        output.cd()
        tree = input.Get("myTree")
	#tree = input.Get(sample.tree)
        try:
            CountWithPU = input.Get("CountWeighted")
            sample.count_with_PU = CountWithPU.GetBinContent(1) 
        except:
            print('WARNING: No Count with PU histograms available. Using 1.')
            sample.count_with_PU = 1.
            sample.count_with_PU2011B = 1.
        input.cd()
        obj = ROOT.TObject
        for key in ROOT.gDirectory.GetListOfKeys():
            input.cd()
            obj = key.ReadObj()
            if obj.GetName() == 'myTree':
                continue
            output.cd()
            obj.Write(key.GetName())
        output.cd()
        theCut = self.minCut
        if sample.subsample:
            theCut += '&& (%s)' %(sample.subcut)
	print('addtreecut: %s' %(sample.addtreecut))
	print('subCut: %s' %(sample.subcut))
        theCut += '&& (%s)' %(sample.addtreecut)
	print('theCut: %s' %theCut)
        cuttedTree=tree.CopyTree(theCut)
        cuttedTree.Write()
        output.Write()
        input.Close()
        del input
        output.Close()
#        tmpSourceFile = ROOT.TFile.Open(tmpSource,'read')
#        if tmpSourceFile.IsZombie():
#            print("@ERROR: Zombie file")
        del output

    def __cache_samples(self):
        for job in self.__sampleList:
            self.__trim_tree(job)

    def get_tree(self, sample, cut):
        input = ROOT.TFile.Open('%s/tmp_%s.root'%(self.__tmpPath,self.__hashDict[sample.name]),'read')
        tree = input.Get("myTree")
        try:
            CountWithPU = input.Get("CountWeighted")
            sample.count_with_PU = CountWithPU.GetBinContent(1) 
        except:
            print('WARNING: No Count with PU histograms available. Using 1.')
            sample.count_with_PU = 1.
            sample.count_with_PU2011B = 1.
        if sample.subsample:
            cut += '& (%s)' %(sample.subcut)
        ROOT.gROOT.cd()
        cuttedTree=tree.CopyTree(cut)
        cuttedTree.SetDirectory(0)
        input.Close()
        del input
        del tree
        return cuttedTree

    @staticmethod
    def get_scale(sample, config, lumi = None):
        anaTag=config.get('Analysis','tag')
        theScale = 0.
        if not lumi:
            lumi = float(sample.lumi)
        if anaTag == '7TeV':
            theScale = lumi*sample.xsec*sample.sf/(0.46502*sample.count_with_PU+0.53498*sample.count_with_PU2011B)
        elif anaTag == '8TeV':
            theScale = lumi*sample.xsec*sample.sf/(sample.count_with_PU)
        elif anaTag == '13TeV':
	    theScale = lumi*sample.xsec*sample.sf/(sample.count_with_PU)
	    #print ('lumi:')
	    #print (lumi)
	    #print ('xsec:')
	    #print (sample.xsec)
	    #print ('sample.sf:')
	    #print (sample.sf)
	    #print ('sample.count_with_PU:')
	    #print (sample.count_with_PU)
	    #print ('theScale:')
	    #print (theScale)
        return theScale

    @staticmethod
    def get_checksum(file):
        # If file is remote
        if ':' in file:
            srmPath = 'srm://t3se01.psi.ch:8443/srm/managerv2?SFN=//pnfs/psi.ch/cms/trivcat/'
            command = 'lcg-ls -b -D srmv2 -l %s' %file.replace('root://cms-xrd-global.cern.ch//','%s/'%srmPath)
            print(command)
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
            lines = p.stdout.readlines()
            print(lines)
            if any('No such' in line for line in lines):
                print('File not found')
                print(command)
            line = lines[1].replace('\t* Checksum: ','')
            checksum = line.replace(' (adler32)\n','')
        else:
            command = 'md5sumi %s' %file
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
            lines = p.stdout.readlines()
            checksum = lines[0]
        return checksum
    
    @staticmethod
    def file_exists(file):
        # If file is remote
        if ':' in file:
            srmPath = 'srm://t3se01.psi.ch:8443/srm/managerv2?SFN=//pnfs/psi.ch/cms/trivcat/'
            command = 'lcg-ls %s' %file.replace('root://cms-xrd-global.cern.ch//','%s/'%srmPath)
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
            line = p.stdout.readline()
            return not 'No such file or directory' in line
        else:
            return os.path.exists(file)
