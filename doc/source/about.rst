About 
=====
Some background and problem description.

No Core Shell Model
^^^^^^^^^^^^^^^^^^^
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
:math:`\hbar\Omega`
and for different model-space cutoffs :math:`N_\mathrm{max}`.

The results display a pseudo-dependence on the HO frequency that is due to
approximations made in the low-energy renormalization scheme of the nuclear
Hamiltonian. However, the formalism guarantees that this dependence will
disappear as the model space approaches the infinite Hilbert space, i.e.
:math:`N_\mathrm{max} \to \infty`.

This feature can be employed by collecting results for several
:math:`N_\mathrm{max}`-sequences obtained at various values of
:math:`\hbar\Omega` and performing a constrained fit. This means that a
particular form of the extrapolation function is chosen and that all sequences
have the same asymptotic value, which is found through a chi-squared best fit.

