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

import numpy as np


def fitFunction(func):
    """
    Determines what fitting function is used.

    :type func: string
    :param func: What fitting function to use. Currently 'reciprocal' and
                 'exponential' is implemented.
    """
    if func == 'reciprocal':
        def fitfunc(O_inf, p, nMax): 
            return O_inf + p[0]/nMax + p[1] / nMax ** 2
        return fitfunc

    if func == 'exponential':
        def fitfunc(O_inf, p, nMax):
            return O_inf + p[0] * np.exp(-p[1] * nMax)
        return fitfunc

def errFunc(p, X, Y, fitFunc):
    """
    Returns an array of the difference between the data and the fitting
    function for the current parameters p.

    :type p: list
    :param p: The parameters used in the fitting

    :type X: list of nd arrays
    :param X: The x-values for the runs with different hO


    :type Y: list of nd arrays
    :param Y: The y-values for the runs with different hO

    :type fitFunc: function
    :param fitFunc: What fitting function to use.

    """
   

    total = []
    for i in range(len(X)):
        total.append(fitFunc(p[0], p[2 * i+1:2 * i+3], X[i]) - Y[i])
    total2 = total[0]
    for i in range(len(total) - 1):
        total2 = np.concatenate((total2, total[i+1]))
    return total2.tolist()
