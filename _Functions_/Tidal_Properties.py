from .Constants import *
from .Metric_Functions import *
from .Config import *

class Tidal_SOLVER:
    def __init__(self,TOV_Result):
        r_array, riplo, EOS = TOV_Result
        self.EOS= EOS
        self.r_array= r_array
        self.riplo= riplo
        
    def Love(self,y,r):
        beta, H = y
        P2E, E2P= self.EOS
        r2m, r2pr, r2psi, r2dpr_de, r2dpr_dr, r2dpsi_dr, r2de_dr = self.riplo
        
        pr = r2pr(r)
        m = r2m(r)
        e = P2E(pr)
        dpr_de = r2dpr_de(r)
        dpsi_dr = r2dpsi_dr(r)

        lam = 2*Lamda(m,r)

        A= (2/r) + ((np.e)**(lam))*(((2*m/(r**2))) + (4*pi*r)*(pr-e))
        B= ((4*pi*(np.e**(lam)))*(4*e + 8*pr + ((e+pr)/(dpr_de))*(1+dpr_de))) - ((6*(np.e**(lam)))/(r**2)) - (2*dpsi_dr)**2

        dbeta_dr = -(A*beta + B*H)    
        dH_dr= beta

        return np.array([dbeta_dr, dH_dr])

    def Love_RK4(self,y,r,h):

        k1, l1 = h*self.Love(y,r)

        y1 = [y[0]+k1/2, y[1]+l1/2]
        k2, l2 = h*self.Love(y1, r+h/2)

        y2 = [y[0]+k2/2, y[1]+l2/2]
        k3, l3 = h*self.Love(y2, r+h/2)

        y3 = [y[0]+k3, y[1]+l3]
        k4, l4 = h*self.Love(y3, r+h)

        beta = y[0] + 1./6*(k1 + 2*k2 + 2*k3 + k4)
        H = y[1] + 1./6*(l1 + 2*l2 + 2*l3 + l4)

        return np.array([beta,H])

    def Love_solve(self):
        r_array= self.r_array
        r2m, r2pr, r2psi, r2dpr_de, r2dpr_dr, r2dpsi_dr, r2de_dr = self.riplo
        
        R= r_array[-1]
        M= r2m(R)
        r0= r_array[0]
        beta0 = 2*r0
        H0 = r0**2

        yi = [beta0,H0] 

        for ri in np.arange(r0+h, R-h, h):
            yi= self.Love_RK4(yi,ri,h)

        Beta= yi[0]
        H= yi[1]

        y= (R*Beta)/H

        C= M/R

        t1= (8/5)*(C**5)*((1-2*C)**2)*((2*C*(y-1))-y+2)
        t2= 2*C*((4*(y+1)*C**4) + (2*(3*y-2)*C**3) - (2*(11*y-13)*C**2) + (3*(5*y-8)*C) - (3*(y-2)))
        t3= (3*(1-2*C)**2)*(2*C*(y-1)-y+2)*np.log(1-2*C)

        k2=  t1/(t2+t3)

        l = (2*k2)/(3*(C**5))

        M = M*(1/Kg__to__m)*(1/M0)

        return M, k2, l, C