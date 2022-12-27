from scipy.interpolate import interp1d

from .Constants import *
from .Metric_Functions import *
from .Config import *

class TOV_SOLVER:
    def __init__(self,EOS,CP):
        self.EOS= EOS
        self.CP= CP

    def TOV(self,y,r):
        pr, m = y
        P2E, E2P= self.EOS
        min_p,max_p,min_e,max_e= self.CP

        if pr < min_p or pr > max_p:
            return np.array([0.,0.,0.])

        e = P2E(pr)
        
        dpr_dr = -(pr+e)*((m/r**2)+(4*pi*r*pr))*(np.e**(2*Lamda(m,r)))

        dm_dr = (4*pi*r**2)*e

        dpsi_dr = -(1/(pr+e))*(dpr_dr)

        return np.array([dpr_dr, dm_dr, dpsi_dr])

    def TOV_RK4(self,y,psi,r,h):

        k1, l1, m1 = h*self.TOV(y,r)

        y1 = [y[0]+k1/2, y[1]+l1/2]
        k2, l2, m2 = h*self.TOV(y1, r+h/2)

        y2 = [y[0]+k2/2, y[1]+l2/2]
        k3, l3, m3 = h*self.TOV(y2, r+h/2)

        y3 = [y[0]+k3, y[1]+l3]
        k4, l4, m4 = h*self.TOV(y3, r+h)

        pr = y[0] + 1./6*(k1 + 2*k2 + 2*k3 + k4)
        m = y[1] + 1./6*(l1 + 2*l2 + 2*l3 + l4)
        psi = psi + 1./6*(m1 + 2*m2 + 2*m3 + m4)

        y= np.array([pr,m])

        return y, psi

    def TOV_solve(self,eo):
        P2E, E2P= self.EOS
        min_p,max_p,min_e,max_e= self.CP
            
        e0= eo*Mev_per_fm_cube__to__Pa*Pa__to__per_m_square
        rmax = 20000
        r0 = 0.01
        psi_0 = 1

        m0 = ((4/3)*pi*r0**3)*e0
        pr0 = E2P(e0)
        y0 = [pr0, m0]

        yi = [pr0, m0]
        psi_i = psi_0

        mlist = [m0]
        prlist = [pr0]
        rlist = [r0]
        psilist = [psi_0]

        for ri in np.arange(r0+h, rmax, h):
            yi, psi_i = self.TOV_RK4(yi,psi_i,ri,h)
            if yi[0] < min_p:
                break

            rlist.append(ri)
            prlist.append(yi[0])
            mlist.append(yi[1])
            psilist.append(psi_i)

        r_array = np.array(rlist)
        pr_array = np.array(prlist)
        m_array = np.array(mlist)
        psi_array = np.array(psilist)
        e_array = P2E(pr_array)
        
        dpr_dr = np.gradient(pr_array,r_array)
        dpr_de = np.gradient(pr_array,e_array)
        de_dr = np.gradient(e_array,r_array)

        M= m_array[-1]
        R= r_array[-1]

        Psi_bc_R = (np.log(1-(2*M/R)))/2
        Psi_at_R = psi_array[-1]
        change= Psi_bc_R - Psi_at_R 

        psi_array += change
        
        dpsi_dr = np.gradient(psi_array,r_array)
        
        r2m = interp1d(r_array,m_array)
        r2pr = interp1d(r_array,pr_array)
        r2psi = interp1d(r_array,psi_array)
        
        r2dpr_de = interp1d(r_array,dpr_de)
        r2dpr_dr = interp1d(r_array,dpr_dr)
        r2dpsi_dr = interp1d(r_array,dpsi_dr)
        r2de_dr = interp1d(r_array,de_dr)

        riplo = r2m, r2pr, r2psi, r2dpr_de, r2dpr_dr, r2dpsi_dr, r2de_dr
        EOS= P2E, E2P

        return r_array, riplo, EOS