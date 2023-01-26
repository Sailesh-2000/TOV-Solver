# TOV_SOLVER (MOI+TIDAL DEFORMABILITY)
 
This program computes the M-R profile, Moment of Inertia for slowly rotating star, and Tidal Deformability Parameters. M-R profile is obtained by solving the TOV equation with a given EOS. The EOS must have 3 coloumns with the following data:

1.) baryon number density in units of fm^-3 (currently unused) \
2.) energy density in units of Mev/fm^3 \
3.) pressure in units of Mev/fm^3 

MI is computed by numerically integrating two CDEs obtained from solving Hartle-Throne metric in Einstein field equation. \bar{I} represents the dimensionless moment of inertia ($I/MR^2$). Tidal deformability is computed numerically integrating two CDEs obtained from solving Thorne and Campolattar metric in perturbed Einstein field equation. Radial profile data of mass, pressure, metric function obtained by solving tov is used for calculation of MI and Tidal deformability.

## How to run the programme for your specific tabulated EOS?

Copy & paste your EOS.dat/txt file in the EOS folder. Open TOV_Solver.ipynb. Write the name of your EOS in the path section "Your_Eos.dat". As this code uses multiprocessing for faster computation, assign the values of nc and nc_MR according to no. of cores in your system. Note: (nc * designated_cores) must be around 70. Once everything is set run the whole programme and you will get the NS Parameters along with for parameters for maximum and canonical mass in tabulated form at the end.

## Plots:
![MR-profile](https://user-images.githubusercontent.com/105746092/214935216-a0ec73f3-b32a-441a-b673-e82e4c4997b8.png) \
![Density-profile](https://user-images.githubusercontent.com/105746092/214935201-bad50352-fa86-4d3c-bf0a-4d04580010a6.png) \
![mass-pressure-sound_speed-profile](https://user-images.githubusercontent.com/105746092/214935207-734dc4f7-8203-44be-b415-b5ab2bd8de7f.png) \
![MI](https://user-images.githubusercontent.com/105746092/214935212-be363251-f820-437a-9346-4d46745d8c64.png) \
![Tidal_Deformability](https://user-images.githubusercontent.com/105746092/214935223-0e7e2103-db25-48f9-a155-71ee2b08f058.png)
