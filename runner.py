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

from PostProcessingNCSM.run_params import *
from PostProcessingNCSM.fit_functions import *
from PostProcessingNCSM.post_processing import *



figureWidthPt = 512.0 # Set figure size width in pt (2 column=512, 1 column=246)
figureFontSize = 16   # Set figure base font size in pt

# Generate proper width and height for rc params (LaTeX support in figures)
titleSpace = True # Enable/Disable extra space for title etc in figures
figureSize = applyGoldenRatio(figureWidthPt, titleSpace)


# Run parameters - check the RunParams class description in the documentation
#                  for information about the different parameters.
rp = RunParams(dataFile = 'ncsmextract_ant_z3a6.pickle',
               plotStyle = [['g^-',10],
                            ['bv-',10],
                            ['r>-',10],
                            ['c<-',10],
                            ['ms-',10],
                            ['yd-',10],
                            ['ko-',10],
                            ['wp-',10]],
               observables = [{'id': 'e', 'drawPlot': True, 'invert': False,
                               'performFit': True, 'fitFunction': 'reciprocal',
                               'ylabel': r'Binding energy [eV]',
                               'xlabel': r'N$_\mathrm{max}$'},
                              {'id': 'rc', 'drawPlot': False, 'invert': False,
                               'performFit': False, 'fitFunction': 'reciprocal',
                               'ylabel': r'r$_c$ []',
                               'xlabel': r'N$_\mathrm{max}$'},
                              {'id': 'rn', 'drawPlot': False, 'invert': False,
                               'performFit': False, 'fitFunction': 'reciprocal',
                               'ylabel': r'r$_n$ []',
                               'xlabel': r'N$_\mathrm{max}$'},
                              {'id': 'rp', 'drawPlot': False, 'invert': False,
                               'performFit': False, 'fitFunction': 'reciprocal',
                               'ylabel': r'r$_p$ []',
                               'xlabel': r'N$_\mathrm{max}$'}],
               rcUserParams = {'backend': 'ps',
                               'axes.labelsize': figureFontSize,
                               'text.fontsize': 2*figureFontSize,
                               'legend.fontsize': 0.8*figureFontSize,
                               'xtick.labelsize': 0.8*figureFontSize,
                               'ytick.labelsize': 0.8*figureFontSize,
                               'text.usetex': True,
                               'figure.figsize': figureSize},
               printInfo = True,
               drawPlot = True,
               xVar = 1,
               nmaxExcludeZero = True,
               printSummary = True,
               performFit = True,
               fitFunction = 0)


# Run the full post processing routine
postProcess(rp)
