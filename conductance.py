import kwant
import numpy as np
import h5py
from system_init import syst, default
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Calculate conductance and save to hdf5 or just plot from files.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p', '--plot', type=bool, default=False, help='Just plot the result from hdf5 files.')
parser.add_argument('-f', '--file', type=str, default='conductance.h5', help='HDF5 file to read.')
args = parser.parse_args()

def andreev_conductance(s):
    '''Calculate the Andreev conductance from the scattering matrix.
    The formula is G = N_e - Tr(S^dagger_ee S_ee) + Tr(S^dagger_he S_he)
    where S_ee is the submatrix of the scattering matrix that connects the
    electrons and S_he is the submatrix that connects the holes.
    
    Parameters:
    s: scattering matrix
    
    Returns:
    G: Andreev conductance
    '''
    R_ee_top = np.concatenate((s.submatrix((0,0),(0,0)),s.submatrix((0,0),(0,1))), axis=1)
    R_ee_bot = np.concatenate((s.submatrix((0,1),(0,0)),s.submatrix((0,1),(0,1))), axis=1)
    R_ee = np.concatenate((R_ee_top,R_ee_bot), axis=0)
    
    R_he_top = np.concatenate((s.submatrix((0,2),(0,0)),s.submatrix((0,2),(0,1))), axis=1)
    R_he_bot = np.concatenate((s.submatrix((0,3),(0,0)),s.submatrix((0,3),(0,1))), axis=1)
    R_he = np.concatenate((R_he_top,R_he_bot), axis=0)
    
    N_electrons = len(R_ee)
    trans_ee = np.trace( np.conj(R_ee.T) @ R_ee)
    trans_he = np.trace( np.conj(R_he.T) @ R_he)
    return N_electrons -trans_ee.real + trans_he.real


nvolts = 50    #number of points in the Voltage array
FerE = np.array([5, 18.5, 42, 74.5, 116.5])    # array of Fermi Energy points
Darr = np.array([0.5,3])     # array of superconducting gap parameter points
Gs = []   # empty list for the conductance results

# Calculate the conductance
if not args.plot:
    for ferE in FerE:
        Gs.append([])
        volarr = np.linspace(0, ferE, nvolts)
        for D0 in Darr:
            Gs[-1].append([])
            for vv in volarr:
                default['V0'] = vv
                default['Delta0'] = D0
                default['E_F'] = ferE
                smat = kwant.smatrix(syst, energy=0.0, params=default)
                c = andreev_conductance(smat)
                Gs[-1][-1].append(c)
        
        Gsarr = np.array(Gs[-1]) 
        
# Save the data
    with h5py.File('conductance.h5', 'w') as f:
        for i, ferE in enumerate(FerE):
            f.create_group(str(ferE))
            for j, D0 in enumerate(Darr):
                f[str(ferE)].create_dataset(str(D0), data=np.array(Gs[i][j]))
                f[str(ferE)].attrs['m0'] = default.get('m0')
                f[str(ferE)].attrs['E_F'] = ferE
                f[str(ferE)].attrs['theta'] = default.get('theta')
                f[str(ferE)].attrs['phi'] = default.get('phi')
                f[str(ferE)].attrs['Delta0'] = D0
                f[str(ferE)].attrs['V0'] = np.linspace(0, ferE, nvolts)

# Read the data and plot
if args.plot:
    with h5py.File(args.file, 'r') as f:
        for i in f.keys():
            for j in f[i].keys():
                Gsarr = np.array(f[i][j])
                plt.plot(f[i].attrs['E_F']*np.ones(len(f[i].attrs['V0'])) - f[i].attrs['V0'], Gsarr, '-', label=r'$\Delta_0=$'+str.format('{:.2f}',f[i].attrs['Delta0']))
            rttl = r'$m_0=$'+str.format('{:.1f}',f[i].attrs['m0'])+\
            r'$,\,E_F=$'+str.format('{:.1f}',f[i].attrs['E_F'])+\
            r'$,\,\theta/\pi=$'+str.format('{:.2f}',f[i].attrs['theta'])+\
            r'$,\,\phi/\pi=$'+str.format('{:.2f}',f[i].attrs['phi'])
            plt.ylabel("G [$e^2/h$]", fontsize=12, labelpad=-2)
            plt.xlabel(r"$E_F - V_{QPC}\,[E_{SO}]$", fontsize=12, labelpad=-2)
            plt.yticks(np.linspace(0,16,9))
            plt.legend(frameon=False)
            plt.title(rttl)
            plt.savefig('conductance_'+str.format('{:.1f}',f[i].attrs['E_F'])+'.png', dpi=300)
            plt.show()
