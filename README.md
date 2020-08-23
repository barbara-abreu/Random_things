# Random things
Just small scripts I sometimes do, along with some scripts I make at my work and other stuff.

### My CV in LATEX

Just the LATEX source code for my CV.

### Thought experiment to show the unbiasedness of the OLS estimator

	thought_experiment.py	
	
Script that performs a single linear regression (using OLS) on several samples,resampled from same dataset. In this way, many  values of b0 (intercept) and b1 (slope/coefficient) are generated and a mean is calculated.When plotting the distributions of the parameters, it is possible to see that the expected value of the parameters are the means of the distribution.

### Scripts for processing text files

	extract_cluster_results.py

Script to process output obtained from g_cluster from the GROMACS package into a more readable/human-friendly format.

### Random phone number generators.
 	phone_number_generator_file.cpp 
	phone_number_generator_file.py

Scripts to generate random mobile phone numbers (from Portugal).
I got this idea when some marketing company called me and told my phone number had been randomly generated.

Did the same script in both python and C++, just to test running speed (and for fun obv). The C++ version is ~10 times faster.




