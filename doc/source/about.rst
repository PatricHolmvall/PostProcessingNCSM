About
=====

Note, the mathematical formulas on this page might take a while to render.

No Core Shell Model
-------------------

Background
^^^^^^^^^^
The ab initio no-core shell model (NCSM) is a many-body framework for
calculating properties of light nuclei using realistic nuclear Hamiltonians.
It is a configuration-interaction method meaning that the energy eigenvalues
and eigenstates are obtained in an exact-diagonalization scheme with truncated
many-body basis spaces. A specific aim of the NCSM campaign is to use the
region of light nuclei as a benchmark for testing modern low-energy nuclear
interactions. 

Problem
^^^^^^^
Observables (such as ground-state and excitation energies, electromagnetic
moments, transition strengths, etc) are calculated using different Hamiltonians
and for various isotopes. For each such physics case we can compute the
observables for different choices of the harmonic-oscillator (HO) frequency
.. math:: \hbar\Omega
and for different model-space cutoffs
.. math:: N_\mathrm{max}

The results display a pseudo-dependence on the HO frequency that is due to
approximations made in the low-energy renormalization scheme of the nuclear
Hamiltonian. However, the formalism guarantees that this dependence will
disappear as the model space approaches the infinite Hilbert space, i.e.
.. math:: N_\mathrm{max} \to \infty.

This feature can be employed by collecting results for several
.. math:: N_\mathrm{max}-\mathrm{sequences}
obtained at various values of
.. math:: \hbar\Omega
and performing a constrained fit. This means that a particular form of the
extrapolation function is chosen and that all sequences have the same
asymptotic value, which is found through a chi-squared best fit.

Task
^^^^
Output from NCSM runs are parsed with an existing python script and data is
collected into a dictionary structure (described below). Sample dictionaries
will be provided as pickled data. 

Output from NCSM runs are parsed with an existing python script and data is
collected into a dictionary structure (described below). Sample dictionaries
will be provided as pickled data.

Task 1: develop tools to generate the following plots for selected physics cases
and observables:

    * \hbar\Omega-dependence for different model space truncations
    N_\mathrm{max}.
    * N_\mathrm{max}-dependence for HO frequencies \hbar\Omega. Possibly plotted
    as a function of 1/N_\mathrm{max}.
    * Performing constrained fits using various functional forms. E.g.
    O(N_\mathrm{max},\hbar\Omega) = O_\infty +
    \frac{c_1(\hbar\Omega)}{N_\mathrm{max}} +
    \frac{c_2(\hbar\Omega)}{N_\mathrm{max}^2}.
    * The fit parameters O_\infty and c_1(\hbar\Omega), c_2(\hbar\Omega)
    are found through a chi-squared fit procedure.
    * Producing error bands based on using different ranges of HO frequencies
    for the above fits. Plotting these error bands.
    * Summarizing results as a table 

The current data structure (see below) is constructed to describe ground-state
properties. However, there is a need to include different types of data, e.g.

    State-independent data such as model space dimension
    State-specific properties (such as excitation energy, EM moments, etc) that
    is not necessarily the ground-state. For this we need a state specifier.
    Transitional properties (e.g. transition strengths) for which we need two
    state specifiers. 

Task 2: decide on an appropriate data structure and to be able to generate plots
and extrapolations as outlined above.

Sample data
^^^^^^^^^^^
* Download
:download:`pickle file <http://dl.dropbox.com/u/5988069/z4a10.pickle>`.
* Start python and load the pickle file into a dictionary:
>> pf=open('z4a10.pickle','r')
>> import pickle
>> allruns=pickle.load(pf)


Current dictionary structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ----'allruns' dictionary structure:
#       ncsmrun = gs_obs, where (see above)
#               ncsmrun is the tuple that identifies a physics case  (za, int)
#               gs_obs are the observables in a dictionary structure
#
# -----
# 1. ncsm run identifier tuple:
# ncsmrun = (za, hams, trans), where
#           za is a tuple (Z,A) where Z, A are integers
#           hams = hamiltonian (eg 'cdb') [string]
#           trans is a tuple (trans_name,coeff) where trans_name describes which
#           transformation is used. ('srg','lz' or 'bare') and coeff is a
#           related coefficient.
#           (In the case of SRG: coeff is the value of Lambda)
# 2. gs_obs = dictionary with observables (see below)
#       "e" = energy:
#              list of tuples (hw,nmax,e) [float, int, float]
#              where
#              hw = HO frequency [float]
#              nmax = Nmax, model space cutoff [int]
#              e = binding energy in MeV [float]
#       "mu" = magnetic dipole moment:
#              list of tuples (hw,nmax,mu) [float, int, float]
#       "q" = electric quadrupole moment:
#              list of tuples (hw,nmax,q) [float, int, float]
#       "rn","rp","rc" = radii 
#              rn=point-neutron, rp=point-proton,
#              rc=charge rms radius:
#              list of tuples (hw,nmax,r) [float, int, float]
#       ----
#       General (not state-specific) properties
#       "dimgs" = list of tuples (nmax, nlj, nljm, dim) [integers]
#               with dimension info for the Mz,Pi=J, Pi (gs) case. 
#       "files" = List of filenames [strings] from which the output
#                 has been collected (this key is not used in the
#                 output from antextract() but rather updated in
#                 the calling routine)
#
# Other dictionaries used in this (or related) module:
# ----'state' dictionary structure:
#       "jj" = 2*J [int]
#       "pi" = parity [int] (0=+, 1=-)
#       "tt" = 2*T [int]
#       "n" = state number with given J,pi [int] (=1 per default for gs)
#
#-----------------------------------
