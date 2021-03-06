#!/usr/bin/env python

#from version import __version__
#from version import __doc__

import sys

import matplotlib
#print matplotlib.__version__

if sys.platform == 'darwin':
    matplotlib.use('TkAgg')

# load submodules
from colors import *
from graphers import *
from logger import *
from output import *
from patterns import *
from sbaDriver import *
from sync import *
from tools import *
from triangulate import *
from undistort import *
#from clickerWindow import *
from frameFinderPyglet import *
from gui import *

import resources
