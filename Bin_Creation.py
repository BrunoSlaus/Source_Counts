from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

#######################################################
Input_Folder   = 'Input/'
Name_Catalogue = 'XXL-N_gmrt_out_CorrIRACch1.fits'

Flux_Column_Name = 'Total_Flux'
Counts_Frequency    = 1.4   #GHz
Data_Frequency      = 0.61  #GHz
Mean_Spectral_Index = -0.7

Name_Bin_File    = 'Bins_PYTHON.txt'
N_Bins = 20
#######################################################

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

Flux_Min = np.amin(Flux_Column)
Flux_Max = np.amax(Flux_Column)
print('Minimum flux value == ', Flux_Min)
print('Maximum flux value == ', Flux_Max)

Range_x    = np.linspace(start=np.log10(Flux_Min), stop=np.log10(Flux_Max), num=2*N_Bins+1)
Left_Edges  = 10 ** (Range_x[0:-1:2])
Centres     = 10 ** (Range_x[1::2])
Right_Edges = 10 ** (Range_x[2::2])
print('Centres of bins: ', Centres)
print('Numer of Left Edges  :', len(Left_Edges))
print('Numer of Centres     :', len(Centres))
print('Numer of Right Edges :', len(Right_Edges))

Bin_Data = np.column_stack([Left_Edges, Right_Edges, Centres])

with open(Input_Folder + Name_Bin_File, 'w') as Bins:
    Bins.write('#Left_Edge\t\tRight_Edge\t\tCentre\n')
    np.savetxt(Bins, Bin_Data)

'''
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
for line in Left_Edges:
    ax.axvline(line,  color = 'black',  label='Left Bin Edge')
for line in Right_Edges:
    ax.axvline(line,  color = 'red',    label='Right Bin Edge')
for line in Centres:
    ax.axvline(line,  color = 'orange', label='Centre of Bin')    
ax.set_xscale("log", nonposx='clip')
ax.set_yscale("log", nonposy='clip')
ax.legend()
plt.title('Bin Visualisation')
plt.show()
'''
#######################################################
#Modification History:
#1) Plotter is now deactivated. 

#######################################################











