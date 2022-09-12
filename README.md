# Source_Counts
Code that creates source counts for a catalogue, with or without comparison to other surveys.

This code creates the source counts for a given catalogue. There are two versions of the code.
One version compares the resulting source counts with the literature and the other does not. The
table containing literature data should be provided in the Input folder.

In order for the codes to work you need to put them together in one folder. In that same folder you should create the "Input" folder containing the input data. You should also create the "Output" folder as well. The names of these folders should be exactly as stated.

The code also requires the info concerning the bins. You can write it manually or use the "bin-creation" code given in this repository.

The repository contains:

 1)   Source_Counts.py : This is the main code for SC creation.

 2)   Source_Counts_NoComparison.py : This is the main code for SC creation without a need for comparison data. (Use this first.)

 3)   Bin_Creation.py : Code for bin creation.
