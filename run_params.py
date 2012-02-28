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
This module defines a single class, C{RunParams} which is used to keep track
of parameters affecting the post processing.
"""
__docformat__ = 'epytext en'


class RunParams:
    """
Stores variables that are needed to perform post processing.

Variables that always need to be defined in the class before a run are:

- B{N} (int) E{-} The number of nodes in a path.
- B{beta} (float) E{-} Euclidian time difference between first and
last node in the path.
- B{nbrOfWalkers} (int) E{-} The number of paths that should be worked on
simultaneously.

"""
    def __init__(self, plotStyle, observables, printInfo=False,
                       drawPlot=False, hwDependence=True,
                       nmaxDependence=True, nmaxInvDependence=False,
                       nmaxExcludeZero=False, printSummary=True):
        """
Creates a new C{RunParams}. Sets most options to False.
"""

        self.plotStyle = plotStyle
        self.observables = observables

        self.printInfo = printInfo
        self.drawPlot = drawPlot
        self.hwDependence = hwDependence
        self.nmaxDependence = nmaxDependence
        self.nmaxInvDependence = nmaxInvDependence
        self.nmaxExcludeZero = nmaxExcludeZero
        self.printSummary = printSummary

