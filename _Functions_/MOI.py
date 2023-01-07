from scipy.interpolate import interp1d
from scipy.optimize import toms748 as root

from .Constants import *
from .Config import *

class MOI_SOLVER:
    def __init__(self,TOV_Result):
        r_array, riplo, EOS= TOV_Result
        self.EOS= EOS
        self.r_array= r_array
        self.riplo= riplo
        
    def MOI(self,y,r):
        w, I = y
        P2E, E2P= self.EOS
        r2m, r2pr, r2psi, r2dpr_de, r2dpr_dr, r2dpsi_dr, r2de_dr = self.riplo

        m= r2m(r)
        pr= r2pr(r)
        e= P2E(pr)
        psi= r2psi(r)

        dw_dr = (6/r**4)*((np.e)**psi)*((1-(2*m/r))**(-1/2))*I
        dI_dr = (8*pi*(r**4)/3)*((np.e)**(-psi))*(e+pr)*((1-(2*m/r))**(-1/2))*w

        return np.array([dw_dr, dI_dr])

    def MOI_RK4(self,y,r,h):

        k1, l1 = h*self.MOI(y,r)

        y1 = [y[0]+k1/2, y[1]+l1/2]
        k2, l2 = h*self.MOI(y1, r+h/2)

        y2 = [y[0]+k2/2, y[1]+l2/2]
        k3, l3 = h*self.MOI(y2, r+h/2)

        y3 = [y[0]+k3, y[1]+l3]
        k4, l4 = h*self.MOI(y3, r+h)

        w = y[0] + 1./6*(k1 + 2*k2 + 2*k3 + k4)
        I = y[1] + 1./6*(l1 + 2*l2 + 2*l3 + l4)

        return np.array([w,I])

    def MOI_solve_guess_w0(self,w0):
        r_array= self.r_array
        r2m, r2pr, r2psi, r2dpr_de, r2dpr_dr, r2dpsi_dr, r2de_dr = self.riplo
        
        R= r_array[-1]
        M= r2m(R)
        r0= r_array[0]
        m0= r2m(r0)

        I0 = (2/5)*m0*r0**2

        yi = [w0,I0] 

        for ri in np.arange(r0+h, R-h, h):
            yi= self.MOI_RK4(yi,ri,h)

        W_R= yi[0]
        I_R= yi[1]

        W_R_bc= 1-(2*I_R/R**3)

        diff= W_R_bc-W_R

        I_bar= I_R/(M*R**2)
        M= M*(1/Kg__to__m)*(1/M0)
        I= I_R/Kg__to__m

        return I, I_bar, M, diff

    def Omega(self,w0):
        
        I, I_bar, M, diff= self.MOI_solve_guess_w0(w0)
        
        return diff
    
    def MOI_Solve(self):
        w0= root(self.Omega,0,1)
        
        I, I_bar, M, diff= self.MOI_solve_guess_w0(w0)
        
        return I, I_bar, M