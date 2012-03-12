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

import pickle
import numpy as np
import pylab as pl
import itertools as it
from matplotlib import rc
from matplotlib.ticker import *
import matplotlib.pyplot as plt
from scipy import optimize
from fit_functions import fitFunction
from fit_functions import errFunc

#try:
#    pf = open('../runs/'+rp.dataFile)
#except IOError:
#    raise Exception("Unable to open the data file 'runs/"
#                    ""+str(rp.dataFile)+"', make sure that it lies in the "
#                    "correct folder with read premission.")




def unpickleDataFile(dataFile):
    """
    Unpickle NCSM data file and return the data structure in it.

    :type dataFile: string
    :param dataFile: Data file containing NCSM runs.

    :type allRuns: dict
    :param allRuns: Dictionary containing the NCSM runs and all the associated
                    data for each run. The dictionary is in a very specific
                    format, described in the file
                    `currentDictionaryStructure.txt`.
    """
    pf = open('runs/'+dataFile)
    allRuns = pickle.load(pf)

    return allRuns





def printInfo(dataFile, dataStructure=None):
    """
    Print info about the runs and observables measured in a NCSM run data file.

    :type dataFile: string
    :param dataFile: Data file containing NCSM runs.
    
    :type dataStructure: dict
    :param dataStructure: Dictionary containing the NCSM runs and all the
                          associated data for each run. The dictionary is in a
                          very specific format, described in the file
                          `currentDictionaryStructure.txt`.
    """

    if dataStructure == None:
        dataStructure = unpickleDataFile(dataFile)
    
    print 'Number of runs in datafile \''+str(dataFile)+'\': ',
    print str(len(dataStructure))

    for ncsmrun in dataStructure:
        print '\n------------ NCSM-Run: ' + str(ncsmrun),
        print ' ------------'
        print 'Fields/Observables:',
        print '\'' + '\', \''.join(dataStructure[ncsmrun]) + '\''
        print '-'*len('------------ NCSM-Run: ' + str(ncsmrun)+' ------------ ')





def journalStylePlot(figureWidthPt):
    """
    Fix figure proportions to match journal-style. Provide 

    :type figureWidthPt: float
    :param figureWidthPt: Figure width in pt.

    :type figureSize: list
    :param figureSize: List of floats describing width and height of figure.
    """
    
    inchesPerPt = 1.0/72.27 # Convert pt to inch
    goldenMean = (np.sqrt(5)-1.0)/2.0 # Aesthetic ratio
    figureWidth = figureWidthPt*inchesPerPt # width in inches
    figureHeight = figureWidth*goldenMean # height in inches
    figureHeight = figureHeight + 40 * inchesPerPt # Add space for title
    figureSize =  [figureWidth,figureHeight]
    return figureSize





def plotObservable(dataSeries, groupBy, xLabel, yLabel, plotStyle):
    """
    Plot an observable 

    :type rp: :class:`run_params.RunParams` class
    :param rp: An instance of RunParams containing which file, observables and
               fitting function to use.
    """




def performFit(func, X, Y):
    """
Perform a chi-squared fit procedure on observables in a NCSM run. The
fitting functions are defined in the fit_functions.py file.

:type observable: tuple
:param observable: Tuple containing info about the observable of interest.

:type runData: ndarray
:param runData: Numpy 2D-array containing a sorted list of O(hw,Nmax).
"""
    #print X
    #print Y
    #X = X[:,1:]
    #Y = Y[:,1:]


    fitFunc = fitFunction(func, X, Y)


    p = [-60]
    for i in range(2 * len(X)):
        p.append(1.0)



    p, success = optimize.leastsq(errFunc, p, args = (X, Y, fitFunc))

    #print p

    for i in range(len(X)):
        nMax_interp = np.linspace(X[i,:].min(), X[i,:].max() + 20)
        pl.plot(nMax_interp, fitFunc(p[0], p[2 * i + 1: 2 * i + 3], nMax_interp))




def postProcess(rp):
    """
    Post Process NCSM runs in a file and plot observables versus hw or Nmax. All
    post processing settings, including data file and what observables to plot
    are set by the user in the runner-file through the :class:`RunParams` class.

    :type rp: :class:`run_params.RunParams` class
    :param rp: An instance of RunParams with different settings for the post
               processing.
    """
    
    # List of dictionaries containing different quantities that observables can
    # be plotted against. If the user plots observables vs one quantity, the
    # data will be grouped by another into dataseries, hence all the group
    # parameters.
    xDict = [{'id': 'hw', 'gNum': 1, 'gid': 'nmax',
              'gLabel': r'N$_{max}$'},
             {'id': 'nmax', 'gNum': 0, 'gid': 'hw',
              'gLabel': r'$\hbar\Omega$'}]

                  
    # Unpickle
    allRuns = unpickleDataFile(rp.dataFile)


    # Print info
    if rp.printInfo:
        printInfo(rp.dataFile, allRuns)


    # Set rc parameters for LaTeX support in figures
    pl.rcParams.update(rp.rcUserParams)


    ncsmRunList = []

    figureNumber = 1
    
    # Loop through runs
    for ncsmrun in allRuns:
        ncsmRunList.append(ncsmrun)

        # Loop through observables provided by the user
        for observable in rp.observables:
            # Make list of tuples into numpy array
            runData = np.array(allRuns[ncsmrun][observable['id']])
            
            runData = runData[runData[:,1] != 14.0]

            # Remove zeros to prevent divsion by zero etc
            if observable['invert']:
                runData = runData[runData[:,rp.xVar] != 0]
            if rp.nmaxExcludeZero:
                runData = runData[runData[:,1] != 0]
                
            # Create a view of runData in order to enable sorting without
            # changing the shape or integrity of runData. The view will be a
            # structured array with specified labels, which is good for sorting,
            # while runData will remain a numpy 2D ndarray which is good for
            # plotting and doing math.
            dt = [('hw',float), ('nmax',float), (observable['id'],float)]
            runDataView = runData.ravel().view(dt)

            # Group the data 
            runDataView.sort(order=xDict[rp.xVar]['gid'])
            
            groupList = []

        
            if observable['drawPlot']:
                pl.figure(figureNumber)
                pl.title(r'NCSM run: '+str(ncsmrun))
                pl.xlabel(observable['xlabel'])
                pl.ylabel(observable['ylabel'])

            # Group data by distinct values to create data series
            keynum = 0
            X = []
            Y = []
            for key, group in it.groupby(runData,
                                         lambda x: x[xDict[rp.xVar]['gNum']]):
                styleNum = keynum%len(rp.plotStyle)
                groupList.append(key)
                dataSeries = np.array(list(group))

                X.append(dataSeries[:, rp.xVar])
                Y.append(dataSeries[:, 2])
                if observable['drawPlot']:
                    if observable['invert']:
                        pl.plot(np.reciprocal(dataSeries[:,rp.xVar].astype(np.float32)),
                                dataSeries[:,2],
                                rp.plotStyle[styleNum][0],
                                markersize=rp.plotStyle[styleNum][1],
                                label=str(key))
                    else:
                        pl.plot(dataSeries[:,rp.xVar],dataSeries[:,2],
                                rp.plotStyle[styleNum][0],
                                markersize=rp.plotStyle[styleNum][1],
                                label=str(key))
                keynum += 1
            figureNumber += 1

            if observable['drawPlot']:
                pl.legend(loc=4, title=xDict[rp.xVar]['gLabel'])

            # Perform chi-squared fit procedure
            if observable['performFit']:
                performFit(observable['fitFunction'], np.array(X), np.array(Y))

            # Print results
            if rp.printSummary:
                print('Summary.')
    # Show plots
    if rp.drawPlot:
        pl.show()

