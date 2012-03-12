Guide
=====
This guide will describe some of the functionality and how to do some basic
post processing. Most of this is accomplished by setting the variables in the
:py:class:`RunParams` class, in the runner.py file.

Installing the package
----------------------
The program is hosted on github and can easily be downloaded by::

   $ git clone git@github.com:PatricHolmvall/PostProcessingNCSM.git


The program is installed by simply running setup.py with the install flag. You
might need administrator privileges for this to work::

   $ sudo python setup.py install
   

Importing data
--------------
Make sure that the run data file is saved in the folder 'runs', and that the run
data file is saved as a .pickle file with proper pickled data structure. Set
the variable :py:data:`dataFile` to the full name of the file, including the
'.pickle'-part.


Setting up run parameters
-------------------------
This can be seen as a complement to the documentation of the module
:py:mod:`PostProcessingNCSM`
(`link <../library/index.html#module-post_processing>`_) and the class
:py:class:`RunParams` (`link <../library/index.html#module-run_params>`_).

Plot settings
*************
Plot settings are controlled through the following variables (rp is short for
RunParams):



    * :py:data:`rp.drawPlot` - Quick and easy way to enable/disable all plots by
      setting this to True/False.

    * :py:data:`rp.plotStyle` - A list containing markup styles used in the
      plots. The program will loop through this list for each consecutive
      figure. The first field specifies the style, for example 'gd--' will be
      green dashed lines with diamond markers. More info on matplotlib plot
      styles can be found `here <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.plot>`_.
      The second field specifies the marker size.
      
    * :py:data:`rp.observables` - A dict containing which observables to handle
      in the post processing, as well as parameter settings. The ones affecting
      plotting are:

    * :py:data:`rp.rcUserParams` - A dict with rc parameters. This is passed
      straight to pl.rcParams.update. A description of rc parameters can be
      found `here <http://matplotlib.sourceforge.net/users/customizing.html#customizing-matplotlib>`_.


Observables settings
********************
Observable settings are set in the :py:data:`rp.observables` dictionary. More
info coming soon.

Other settings
**************
There are some other settings as well. More info coming soon.


Performing fits
---------------
More info soon.
