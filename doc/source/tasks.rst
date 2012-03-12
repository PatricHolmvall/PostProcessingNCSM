Tasks
=====
These are some of the tasks that needs to be done.

Task 1
^^^^^^
Output from NCSM runs are parsed with an existing python script and data is
collected into a dictionary structure (described below). Sample dictionaries
will be provided as pickled data. Develop tools to generate the following plots
for selected physics cases and observables:

* :math:`\hbar\Omega`-dependence for different model space truncations
  :math:`N_\mathrm{max}`.

* :math:`N_\mathrm{max}`-dependence for HO frequencies :math:`\hbar\Omega`.
  Possibly plotted as a function of :math:`1/N_\mathrm{max}`.

* Performing constrained fits using various functional forms, e.g.
  :math:`O(N_\mathrm{max},\hbar\Omega) = O_\infty +
  \frac{c_1(\hbar\Omega)}{N_\mathrm{max}} +
  \frac{c_2(\hbar\Omega)}{N_\mathrm{max}^2}`.

* The fit parameters :math:`O_\infty` and :math:`c_1(\hbar\Omega)`,
  :math:`c_2(\hbar\Omega)` are found through a chi-squared fit procedure.

* Producing error bands based on using different ranges of HO frequencies for
  the above fits. Plotting these error bands.

* Summarizing results as a table 


Task 2
^^^^^^
Decide on an appropriate data structure and to be able to generate plots and
extrapolations as outlined above. The current data structure is constructed to
describe ground-state properties. However, there is a need to include different
types of data, e.g.

* State-independent data such as model space dimension

* State-specific properties (such as excitation energy, EM moments, etc) that is
  not necessarily the ground-state. For this we need a state specifier.

* Transitional properties (e.g. transition strengths) for which we need two
  state specifiers.

