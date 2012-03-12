Dictionary
==========
Description of the current dictionary structure, as well as the new structure
that is intended to be implemented soon.

Future dictionary structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Class description

Current dictionary structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'allruns' dictionary structure:
      ncsmrun = gs_obs, where ncsmrun is the tuple that identifies a physics
      case  (za, int) gs_obs are the observables in a dictionary structure


1. ncsm run identifier tuple:


ncsmrun = (za, hams, trans), where
          za is a tuple (Z,A) where Z, A are integers
          hams = hamiltonian (eg 'cdb') [string]
          trans is a tuple (trans_name,coeff) where trans_name describes which
          transformation is used. ('srg','lz' or 'bare') and coeff is a
          related coefficient.
          (In the case of SRG: coeff is the value of Lambda)


2. gs_obs = dictionary with observables (see below)
      "e" = energy:
             list of tuples (hw,nmax,e) [float, int, float]
             where
             hw = HO frequency [float]
             nmax = Nmax, model space cutoff [int]
             e = binding energy in MeV [float]
      "mu" = magnetic dipole moment:
             list of tuples (hw,nmax,mu) [float, int, float]
      "q" = electric quadrupole moment:
             list of tuples (hw,nmax,q) [float, int, float]
      "rn","rp","rc" = radii 
             rn=point-neutron, rp=point-proton,
             rc=charge rms radius:
             list of tuples (hw,nmax,r) [float, int, float]
             
      General (not state-specific) properties:
      
      "dimgs" = list of tuples (nmax, nlj, nljm, dim) [integers]
              with dimension info for the Mz,Pi=J, Pi (gs) case.
               
      "files" = List of filenames [strings] from which the output
                has been collected (this key is not used in the
                output from antextract() but rather updated in
                the calling routine)

Other dictionaries used in this (or related) module: 'state' dictionary
structure:

      "jj" = 2*J [int]
      
      "pi" = parity [int] (0=+, 1=-)
      
      "tt" = 2*T [int]
      
      "n" = state number with given J,pi [int] (=1 per default for gs)

