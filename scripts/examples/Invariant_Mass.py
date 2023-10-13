#Finding the dimuon invariant mass from the Z boson decay data

import numpy as np
import uproot as up
import matplotlib.pyplot as plt

'''Store muon kinematic data in 6 numpy arrays'''
with up.open('/tmp/13TeV__2018__magnet_down_data__Z_candidates.root:DecayTree') as file:
    data = file.arrays(["mup_PT", "mup_ETA", "mup_PHI", "mum_PT", "mum_ETA", "mum_PHI"], library="np")
    
m_u = 105.6583755 #muon mass in MeV (According to Wikipedia)

'''Function for converting the muon data into it's cartesian momentum components and energy'''
def convert_coordinates(PT, ETA, PHI):
    P_x = PT*np.cos(PHI)
    P_y = PT*np.sin(PHI)
    P_z = PT*np.sinh(ETA)
    E = np.sqrt(P_x**2 + P_y**2 + P_z**2 + m_u**2)
    return E, P_x, P_y, P_z

'''store the co-ordinate transformed data as variables'''
Positive_cartesian = convert_coordinates(data["mup_PT"], data["mup_ETA"], data["mup_PHI"])
Negative_cartesian = convert_coordinates(data["mum_PT"], data["mum_ETA"], data["mum_PHI"])

'''calculating the invariant mass of the Z boson'''
def invariant_mass(Positive_cartesian_vals, Negative_cartesian_vals):
    Masses = []
    #calculate the dot product of the momentum 3-vectors
    dot_product = np.multiply(Positive_cartesian_vals[1], Negative_cartesian_vals[1]) \
    + np.multiply(Positive_cartesian_vals[2], Negative_cartesian_vals[2]) \
    + np.multiply(Positive_cartesian_vals[3], Negative_cartesian_vals[3])
    for i in range(len(Positive_cartesian_vals[0])): #loop over all events calculating the invariant mass
        M = np.sqrt(2*(Positive_cartesian_vals[0][i]*Negative_cartesian_vals[0][i] - dot_product[i] + m_u**2))
        Masses.append(M) #store invariant mass results to an array
    return Masses
    
'''Plot the invariant mass as a histogram'''
Z_mass = invariant_mass(Positive_cartesian, Negative_cartesian)
plt.hist(Z_mass, 250, range=(50000, 110000), histtype='step', color='black')
plt.xlim(50000, 110000)
plt.title('Dimuon Invariant Mass from Z Boson Decays')
plt.xlabel('Invariant Mass [MeV]')
plt.ylabel('Counts')
plt.savefig('/home/astro/phuwjf/fork1/transient/Invariant_Mass.pdf')
plt.show()
