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

"""
This module defines a single class, :class:`RunParams` which is used to keep
track of parameters affecting the post processing.
"""
__docformat__ = 'epytext en'

import numpy as np

class RunParams:

    # Default rc parameter generation
    l_figureWidthPt = 512.0
    l_figureFontSize = 16
    l_inchesPerPt = 1.0/72.27 
    l_goldenMean = (np.sqrt(5)-1.0)/2.0
    l_figureWidth = l_figureWidthPt * l_inchesPerPt
    l_figureHeight = 2 * l_figureWidth * l_goldenMean
    l_figureHeight = l_figureHeight + 40 * l_inchesPerPt
    l_figureSize =  [l_figureWidth,l_figureHeight]
    
    def __init__(self,
                 dataFile,
                 observables,
                 plotStyle, 
                 rcUserParams={'backend': 'ps',
                               'axes.labelsize': l_figureFontSize,
                               'text.fontsize': 2*l_figureFontSize,
                               'legend.fontsize': 0.8*l_figureFontSize,
                               'xtick.labelsize': 0.8*l_figureFontSize,
                               'ytick.labelsize': 0.8*l_figureFontSize,
                               'text.usetex': True,
                               'figure.figsize': l_figureSize},
                 printInfo=False,
                 drawPlot=False,
                 xAxisVariable=0,
                 nmaxExcludeZero=False,
                 printSummary=True,
                 preformFit=True,
                 fitFunction=0):
        """
        Creates an instance of a class that contains different parameters for
        the post processing. Those parameters that have default values does not
        necessarily need to be defined.


        Variables that always need to be defined before a run are:

        :type dataFile: string
        :param dataFile: Name of the data file to post process, which should
                         in turnlie in the 'runs' directory.

        :type observables: tuple
        :param observables: Tuple containing the observables to include in the
                            post processing.



        Variables that are optional to define before a run are:
        
        :type plotStyle: list
        :param plotStyle: List of lists, where the inner list contain a string
                          and an integer. The string is the style markup, and
                          the integer is the marker size. 
                          
        :type rcUserParams: tuple
        :param rcUserParams: Tuple containing text rendering options for using
                             LaTeX as a plugin for handling text in the plots.
                         
        :type printInfo: boolean
        :param printInfo: Set to True to print info about the runs and 
                          observables in the data file.
        
        :type drawPlot: boolean
        :param drawPlot: Enable or disable all plots.
        
        :type xAxisVariable: int
        :param xAxisVariable: 0 - Nmax,
                              1 - 1/Nmax,
                              2 - hw
        
        :type nmaxExcludeZero: boolean
        :param nmaxExcludeZero: Turn to True to exclude Nmax = 0 in different
                                situations, for example as a form of weighting.
                                This is automatically done in all the cases
                                where 1/Nmax is encountered.
        
        :type printSummary: boolean
        :param printSummary: Turn to True to display a summary/results table.
        
        :type preformFit: boolean
        :param preformFit: True will preform a chi-squared fit procedure.
        
        :type fitFunction: int
        :param fitFunction: 0 - Exponential,
                            1 - Reciprocal
        """

        self.dataFile = dataFile
        self.plotStyle = plotStyle
        self.observables = observables
        self.rcUserParams = rcUserParams

        self.printInfo = printInfo
        self.drawPlot = drawPlot
        self.xAxisVariable = xAxisVariable
        self.nmaxExcludeZero = nmaxExcludeZero
        self.printSummary = printSummary
        self.preformFit = preformFit
        self.fitFunction = fitFunction

