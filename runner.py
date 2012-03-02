# This file is part of PostProcessingNCSM.
#
# PostProcessingNCSM is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PostProcessingNCSM is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PostProcessingNCSM. If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import csv
import numpy as np
from datetime import datetime
from time import time

from PostProcessingNCSM.run_params import *
from PostProcessingNCSM.fit_functions import *
from PostProcessingNCSM.post_processing import *


# Journal-style specific (see the scipy/matplotlib cookbook)
# figureWidthPt = 246.0  # Get this from LaTeX using \showthe\columnwidth
figureWidthPt = 512.0  # Get this from LaTeX using \showthe\columnwidth
figureFontSize = 16
inchesPerPt = 1.0/72.27               # Convert pt to inch
goldenMean = (np.sqrt(5)-1.0)/2.0         # Aesthetic ratio
figureWidth = figureWidthPt*inchesPerPt  # width in inches
figureHeight = figureWidth*goldenMean      # height in inches
figureHeight = figureHeight + 40 * inchesPerPt # Add space for title
figureSize =  [figureWidth,figureHeight]


rp = RunParams(dataFile = 'z4a10.pickle',
               plotStyle = [['g^-',10],
                            ['bv-',10],
                            ['r>-',10],
                            ['c<-',10],
                            ['ms-',10],
                            ['yd-',10],
                            ['ko-',10],
                            ['wp-',10]],
               observables = [{'id': 'e', 'drawPlot': True,
                               'ylabel': r'Binding energy [eV]',
                               'xlabel': r'N${_max}$'},
                              {'id': 'rc', 'drawPlot': False,
                               'ylabel': r'r$_c$ []', 'xlabel': r'N${_max}$'},
                              {'id': 'rn', 'drawPlot': False,
                               'ylabel': r'r$_n$ []', 'xlabel': r'N${_max}$'},
                              {'id': 'rp', 'drawPlot': False,
                               'ylabel': r'r$_p$ []', 'xlabel': r'N${_max}$'}],
               rcUserParams = {'backend': 'ps',
                               'axes.labelsize': figureFontSize,
                               'text.fontsize': 2*figureFontSize,
                               'legend.fontsize': 0.8*figureFontSize,
                               'xtick.labelsize': 0.8*figureFontSize,
                               'ytick.labelsize': 0.8*figureFontSize,
                               'text.usetex': True,
                               'figure.figsize': figureSize},
               printInfo = False,
               drawPlot = True,
               xAxisVariable = 0,
               nmaxExcludeZero = False,
               printSummary = True,
               preformFit = True,
               fitFunction = 0)

postProcess(rp)
