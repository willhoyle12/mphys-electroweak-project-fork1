#Plots the data contained in the ROOT files collected by LHC

import numpy as np
import uproot as up
import matplotlib.pyplot as plt

'''Storing LHCb data in 6 numpy arrays'''
with up.open('/tmp/13TeV__2018__magnet_down_data__Z_candidates.root:DecayTree') as file:
    data = file.arrays(["mup_PT", "mup_ETA", "mup_PHI", "mum_PT", "mum_ETA", "mum_PHI"], library="np")
 
'''Plotting the data taken as histograms'''
def histograms():
    hist1 = plt.hist(data["mup_PT"], 100, range=(15000,60000), histtype='step', color='black', label="Positive Muon")
    hist4 = plt.hist(data["mum_PT"], 100, range=(15000,60000), histtype='step', color='red', label="Negative Muon")
    plt.xlim(15000, 60000)
    plt.title('Muon Transverse Momentum')
    plt.xlabel('Transverse Momentum [MeV]')
    plt.ylabel('Counts')
    plt.legend()
    plt.savefig('/home/astro/phuwjf/fork1/transient/Transverse_Momentum.pdf')
    plt.show()
    
    hist2 = plt.hist(data["mup_ETA"], 100, histtype='step', color='black', label="Positive Muon")
    hist5 = plt.hist(data["mum_ETA"], 100, histtype='step', color='red', label="Negative Muon")
    plt.title('Muon Pseudorapidity')
    plt.xlabel('Pseudorapidity')
    plt.ylabel('Counts')
    plt.legend()
    plt.savefig('/home/astro/phuwjf/fork1/transient/Pseudorapidity.pdf')
    plt.show()

    hist3 = plt.hist(data["mup_PHI"], 100, histtype='step', color='black', label="Positive Muon")
    hist6 = plt.hist(data["mum_PHI"], 100, histtype='step', color='red', label="Negative Muon")
    plt.xlim(-np.pi, np.pi)
    plt.title('Muon Polar Angle in the Transverse Plane')
    plt.xlabel(r'$\phi$ (Radians)')
    plt.ylabel('Counts')
    plt.legend()
    plt.savefig('/home/astro/phuwjf/fork1/transient/Polar_Angle.pdf')
    plt.show()

histograms()