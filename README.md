# TOV_SOLVER (MOI+TIDAL DEFORMABILITY)
 
 This program calculates the radial pressure pr and total mass m as a function
of radius r in a spherically symmetric, static sphere, in the context of
general relativity. The ODE for the pressure is known as the
Tolman-Oppenheimer-Volkoff (TOV) equation, and the ODE for the
mass-energy comes from performing the Leibniz integral rule on the
definition of m(r) during the TOV derivation. (This is shown in pretty
much every GR book.)

The TOV equation + mass-energy equation lead to 2 ODEs --- one for
m(r) and the other for p(r) --- but in these equations we have a third
variable, the energy density e(r). Thus we close the system by
providing e(r) and an equation of state (EOS). Currently this program
can use only tabulated EOS data. The required form of
such data is:

1.) baryon number density in units of fm^-3 (currently unused)
2.) energy density in units of Mev/fm^3
3.) pressure in units of Mev/fm^3

NS Parameters for maximum and canonical mass is tabulated at the end.
