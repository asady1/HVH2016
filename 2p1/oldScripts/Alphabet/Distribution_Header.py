# Dist def
import os
import math
from array import array
import optparse
import ROOT
from ROOT import *
import scipy

import Plotting_Header
from Plotting_Header import *

class DIST:
	def __init__(self, name, File, Tree, weight):
		self.name = name
		self.File = File
		self.Tree = Tree
		self.weight = weight
