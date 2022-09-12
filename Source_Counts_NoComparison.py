from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import math
#######################################################
Input_Folder = 'Input/'
Output_Folder = 'Output/'

Name_Catalogue = 'XXL-N_gmrt_out_CorrIRACch1.fits'
Name_Bin_File  = 'Bins_PYTHON.txt'

Flux_Column_Name = 'Total_Flux'

Counts_Frequency    = 1.4   #GHz
Data_Frequency      = 0.61  #GHz
Mean_Spectral_Index = -0.7

Detection_Limit = 350       #uJy (7 Sigma)
#######################################################

print('\n######################################################')
print('Starting the Source_Counts code.')

#Opening bin-info and creating our datapoints from the catalogue
with open(Input_Folder + Name_Bin_File, 'r') as Bins:
    Bins_Data   = np.loadtxt(Bins)
    Left_Edges  = Bins_Data[:,0]
    Right_Edges = Bins_Data[:,1]
    Centres = Bins_Data[:,2]
    
    Catalogue_Data = fits.open(Input_Folder + Name_Catalogue)[1].data
    Flux_Column    = Catalogue_Data[Flux_Column_Name]

    if Counts_Frequency != Data_Frequency:
        print('\n######################################################')
        print('Warning: Flux correction due to different frequencies.')
        print('Counts_Frequency == ', Counts_Frequency, ' GHz')
        print('Data_Frequency   == ', Data_Frequency,   ' GHz')
        print('Using a mean spectral index defined as S~f**(Alpha)')
        print('Alpha            == ', Mean_Spectral_Index)
        print('######################################################\n')        
        Flux_Column = Flux_Column * (Counts_Frequency / Data_Frequency) ** Mean_Spectral_Index

    N_Calculated_Counts = np.zeros(len(Left_Edges))
    N_Calculated_Error = np.zeros(len(Left_Edges))    
    for i in range(len(Left_Edges)):
        Subset = Flux_Column[Flux_Column >= Left_Edges[i]]
        Subset = Subset[Subset < Right_Edges[i]]
        print('Bin ',i , '[', Left_Edges[i], 'to', Right_Edges[i], ']', ' has ', len(Subset), ' sources')
        Bin_Width = Right_Edges[i] - Left_Edges[i]
        N_Calculated_Counts[i] = len(Subset) / Bin_Width / (18.5/((180/np.pi)**2)) #/ 41252.96
        N_Calculated_Counts[i] = N_Calculated_Counts[i] * (Centres[i])**(2.5)

        N_Calculated_Error[i] = (len(Subset))**0.5 / Bin_Width / (18.5/((180/np.pi)**2))
        N_Calculated_Error[i] = N_Calculated_Error[i] * (Centres[i])**(2.5)



#Creating the plot
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_xscale("log", nonposx='clip')
ax.set_yscale("log", nonposy='clip')
plt.errorbar(Centres, N_Calculated_Counts, yerr = N_Calculated_Error, fmt = '+')
ax.axvline(Detection_Limit/10**6,  color = 'red')
plt.xlabel('Flux S')
plt.ylabel('S^(2.5) * dN/dS')
plt.title('Source Counts')
plt.xlim(10**(-5),)
#plt.ylim(,)

plt.savefig(Output_Folder + 'Source_Counts_Plot.png')



#######################################################
#Modification History:
#1) Format of errorbars: fmt = '[color][marker][line]'
#######################################################



