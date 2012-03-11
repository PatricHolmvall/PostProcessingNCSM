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

"""
Fit function description
"""

def fitFunction(func, X, Y):
    if func == 'reciprocal':
        def fitfunc(O_inf, p, nMax): 
            return O_inf + p[0]/nMax + p[1] / nMax ** 2
        return fitfunc

    if func == 'exponential':
        def fitfunc(O_inf, p, nMax):
            return O_inf + p[0] * np.exp(-p[1] * nMax)
        return fitfunc

def errFunc(p, X, Y, fitFunc):
    total = []
    for i in range(len(X)):
        total.append(fitFunc(p[0], p[2 * i+1:2 * i+3], X[i,:]) - Y[i,:])
    return np.array(total).flatten().tolist()

