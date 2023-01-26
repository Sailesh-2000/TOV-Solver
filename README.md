# TOV_SOLVER (MOI+TIDAL DEFORMABILITY)
 
This program computes the M-R profile, Moment of Inertia for slowly rotating star, and Tidal Deformability Parameters. M-R profile is obtained by solving the TOV equation with a given EOS. The EOS must have 3 coloumns with the following data:

1.) baryon number density in units of fm^-3 (currently unused) \
2.) energy density in units of Mev/fm^3 \
3.) pressure in units of Mev/fm^3 

MI is computed by numerically integrating two CDEs obtained from solving Hartle-Throne metric in Einstein field equation. \bar{I} represents the dimensionless moment of inertia ($I/MR^2$). Tidal deformability is computed numerically integrating two CDEs obtained from solving Thorne and Campolattar metric in perturbed Einstein field equation. Radial profile data of mass, pressure, metric function obtained by solving tov is used for calculation of MI and Tidal deformability.

## How to run the programme for your specific tabulated EOS?

Copy & paste your EOS.dat/txt file in the EOS folder. Open TOV_Solver.ipynb. Write the name of your EOS in the path section "Your_Eos.dat". As this code uses multiprocessing for faster computation, assign the values of nc and nc_MR according to no. of cores in your system. Note: (nc * designated_cores) must be around 70. Once everything is set run the whole programme and you will get the NS Parameters along with for parameters for maximum and canonical mass in tabulated form at the end.

## Plots:

[MR-profile.pdf](https://github.com/Sailesh-Ranjan-Mohanty/TOV-Solver/files/10512802/MR-profile.pdf)
[Density-profile.pdf](https://github.com/Sailesh-Ranjan-Mohanty/TOV-Solver/files/10512811/Density-profile.pdf)
[mass-pressure-sound_speed-profile.pdf](https://github.com/Sailesh-Ranjan-Mohanty/TOV-Solver/files/10512813/mass-pressure-sound_speed-profile.pdf)
[MI.pdf](https://github.com/Sailesh-Ranjan-Mohanty/TOV-Solver/files/10512814/MI.pdf)
[Tidal_Deformability.pdf](https://github.com/Sailesh-Ranjan-Mohanty/TOV-Solver/files/10512816/Tidal_Deformability.pdf)
