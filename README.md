# Random things
Just small scripts I sometimes do, along with some scripts I make at my work and other stuff (the following are ordered by chronological order) .

### Script to extract all the audio files from Fr. Mike's podcast
	basic_scraping.py
Script used to download audio files from Fr. Mike's podcast " The Bible in a year". This script scrapes the webpage of google-podcasts and then downloads the files and renames them.


### Jupyter notebooks with some analyses
	correlations_calpha_rms.ipynb

Notebook in which I calculated the correlation between atomic displacements of C-alpha atoms, using 3D coordinates (RMS-root mean squared).

	PCA_otherdimensions.ipynb
	
I had previously done a PCA analysis on atomic coordinates, with the goal of separating protein conformations that belonged to different proteins states, similarly to a clustering procedure. In this notebook, I choose different combinations of principal components ( beyond PC 1 and PC 2) and analyze the conformational content of those "clusters", also known as basins.

### Script to time my speech therapy exercises
	
	timer.py

It counts 15 periods of 10s each with 3s intervals in between.

### Script to get unique pairs from a list of values

	get_unique_pairs.py

### Script to calculate the factorial of a number in several ways:

	factorial_all_ways.py

Inspired by  [this](https://www.programiz.com/python-programming/examples/factorial-recursion) challenge.

### Script to calculate permutations in binary list

	binary_permutations.py
	
Inspired by [this](https://www.101computing.net/big-o-notation/) page.


### My CV in LATEX

Just the LATEX source code for my CV.

### Thought experiment to show the unbiasedness of the Ordinary Least Squares (OLS) estimator

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




