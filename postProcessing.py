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

# ['style','markersize']
plotStyle = [['g^-',10],
             ['bv-',10],
             ['r>-',10],
             ['c<-',10],
             ['ms-',10],
             ['yd-',10],
             ['ko-',10],
             ['wp-',10]]

dataFile = 'z4a10.pickle'
printInfo = True
drawPlot = True
hwDependence = True
nmaxDependence = True
nmaxInvDependence = True
# ['identifier', 'ytitle']
observables = ({'id': 'e', 'drawPlot': True, 'ytitle': r'Binding energy [eV]'},
               {'id': 'rc', 'drawPlot': True, 'ytitle': r'r$_c$ []'},
               {'id': 'rn', 'drawPlot': True, 'ytitle': r'r$_n$ []'},
               {'id': 'rp', 'drawPlot': True, 'ytitle': r'r$_p$ []'})


pf = open(dataFile,'r')
allRuns = pickle.load(pf)

# -----------------------
# Plot layouts (line widths, marker size, dash length, etc)
# plw=2; pms=6; pdl=6;
plw=3; pms=9; pdl=9;
# Journal-style specific (see the scipy/matplotlib cookbook)
# fig_width_pt = 246.0  # Get this from LaTeX using \showthe\columnwidth
fig_width_pt = 512.0  # Get this from LaTeX using \showthe\columnwidth
fsize=16
inches_per_pt = 1.0/72.27               # Convert pt to inch
golden_mean = (np.sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_width = fig_width_pt*inches_per_pt  # width in inches
fig_height = 2*fig_width*golden_mean      # height in inches
fig_height = fig_height + 40 * inches_per_pt # Add space for title
fig_size =  [fig_width,fig_height]
# fsize=10
params = {'backend': 'ps',
         'axes.labelsize': fsize,
         'text.fontsize': 2*fsize,
         'legend.fontsize': 0.8*fsize,
         'xtick.labelsize': 0.8*fsize,
         'ytick.labelsize': 0.8*fsize,
         'text.usetex': True,
         'figure.figsize': fig_size}
pl.rcParams.update(params)


if printInfo:
    print 'Number of runs in datafile \''+str(dataFile)+'\': '+str(len(allRuns))

ncsmRunList = []
figureNum = 1

for ncsmrun in allRuns:
    ncsmRunList.append(ncsmrun)

    for observable in observables:
        # Make list of tuples into numpy array
        runData = np.array(allRuns[ncsmrun][observable['id']])

        # Create a view of runData in order to enable sorting without changing
        # the shape or integrity of runData. The view will be a structured array
        # with specified labels, which is good for sorting, while runData will
        # remain a numpy 2D ndarray which is good for plotting and doing math.
        dt = [('hw',float), ('nmax',float), (observable['id'],float)]
        runDataView = runData.ravel().view(dt)


        ########################################################################
        # Nmax dependence for different hw
        ########################################################################
        runDataView.sort(order='hw')

        if observable['drawPlot']:
            pl.figure(figureNum)
            pl.subplot(211)
            pl.title(r'NCSM run: '+str(ncsmrun))
            pl.xlabel(r'N$_{max}$')
            pl.ylabel(observable['ytitle'])

        hwList = []

        # Group data by distinct hw values
        keynum = 0
        for key, group in it.groupby(runData, lambda x: x[0]):
            styleNum = keynum%len(plotStyle)
            hwList.append(key)
            dataSeries = np.array(list(group))
            if drawPlot:
                pl.plot(dataSeries[:,1],dataSeries[:,2],plotStyle[styleNum][0],
                        markersize=plotStyle[styleNum][1],label=str(key))
            keynum += 1

        if observable['drawPlot']:
            pl.legend(loc=4,title=r'$\hbar\Omega$')


        ########################################################################
        # hw dependence for different Nmax
        ########################################################################
        runDataView.sort(order='nmax')

        if observable['drawPlot']:
            pl.subplot(212)
            pl.xlabel(r'$\hbar\Omega$ []')
            pl.ylabel(observable['ytitle'])

        nmaxList = []

        # Group data by distinct nmax values
        keynum = 0
        for key, group in it.groupby(runData, lambda x: x[1]):
            styleNum = keynum%len(plotStyle)
            nmaxList.append(key)
            dataSeries = np.array(list(group))
            if observable['drawPlot']:
                pl.plot(dataSeries[:,0],dataSeries[:,2],plotStyle[styleNum][0],
                        markersize=plotStyle[styleNum][1],label=str(key))
            keynum += 1

        if observable['drawPlot']:
            pl.legend(loc=4,title=r'N$_{max}$')
            figureNum += 1

    ############################################################################
    # Print Info
    ############################################################################
    if printInfo:
        print '\n################# NCSM-Run: ' + str(ncsmrun),
        print ' #################'
        print 'Fields/Observables:',
        print '\'' + '\', \''.join(allRuns[ncsmrun]) + '\''


if drawPlot:
    pl.show()
