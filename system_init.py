import kwant
import kwant.continuum
import numpy as np
import supp_functions as sf

W = 1.0
L = 5.0

hamiltonian = """
   ( 0.5 * k_x**2 + 0.5 * k_z**2 + V(x,z,omega_x,omega_y,V0,l_q) -E_F) * kron(sigma_z, sigma_0)
"""
hamiltonian = kwant.continuum.sympify(hamiltonian)

hamright = """
   ( 0.5 * k_x**2 + 0.5 * k_z**2 - E_F) * kron(sigma_z, sigma_0)
   + k_x * kron(sigma_z, sigma_z)
   - k_z * kron(sigma_z, sigma_x)
   + m_x(m0, theta, phi) * kron(sigma_0, sigma_x)
   + m_y(m0, theta, phi) * kron(sigma_0, sigma_y)
   + m_z(m0, theta, phi) * kron(sigma_0, sigma_z)
   + Delta0 * kron(sigma_x, sigma_0)
"""

hamright = kwant.continuum.sympify(hamright)

hamleft = """
   ( 0.5 * k_x**2 + 0.5 * k_z**2 - E_F) * kron(sigma_z, sigma_0)
"""

hamleft = kwant.continuum.sympify(hamleft)

alat= 1/45
template = kwant.continuum.discretize(hamiltonian, grid=alat)
ltemplead = kwant.continuum.discretize(hamleft, grid=alat)
rtemplead = kwant.continuum.discretize(hamright, grid=alat)

def rectangle_shape(site):
    x, y = site.pos
    return -0.5*W < y < 0.5*W and -0.5*L <= x <= 0.5*L

def lead_shape(site):
    x, y = site.pos
    return -0.5*W < y < 0.5*W

syst = kwant.Builder()
syst.fill(template, rectangle_shape, (alat, alat))


l_lead = kwant.Builder(kwant.TranslationalSymmetry([-alat, 0]),
                     conservation_law=np.diag([-2, -1, 1, 2]))

r_lead = kwant.Builder(kwant.TranslationalSymmetry([alat, 0]))

l_lead.fill(ltemplead, lead_shape, (-alat,0))
r_lead.fill(rtemplead, lead_shape, (L+alat,0))

syst.attach_lead(l_lead)
syst.attach_lead(r_lead)

syst = syst.finalized()

def Vprof(x, z, omega_x, omega_y, V0, l_q):        
    
    Usad = -0.5*omega_x**2*(abs(x) - l_q)**2 + 0.5*omega_y**2*z**2
    
    if abs(x) <= l_q:
        gg = V0 + 0.5*(omega_y*z)**2
    elif abs(x) > l_q:
        gg = max([0, V0 + Usad])
    
    return gg

default = dict(E_F=117.5, Delta0=1.0, m0=2.0, theta=0.5, phi=0.0, 
               omega_x=15, omega_y=25, V0=10, l_q=0.2,
               V=Vprof, m_x=sf.mx_homog, m_y=sf.my_homog, m_z=sf.mz_homog)