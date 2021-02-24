# MetFluxCalc

This program aims to calculate the metabolic flux distribution for any metabolic reaction network model, according to (1).
The problem we are trying to solve is of the form: AX = B, where A is the stoichiometric matrix calculated by the program, and B is the accumulations matrix (balance of the determined fluxes for any given condition). The goal is to find X, which is carried out doing X = A^(-1) * B. If A is not a squared matrix, the pseudo-inverse will be used.
In order for this program to run correctly, two input files are needed: A file with the metabolic model and the list of metabolites in order to create the corresponding stoichiometric matrix (*.txt), and a second file (*.csv) to input the accumulations matrix. As output, the Program will produce two or three files:
i)	An MSExcel file with the stoichiometric matrix,
ii)	A *.txt file with mathematical properties of the stoichiometric matrix, and finally
iii)	An MSExcel file with the calculated flux distributions.
The file described in iii) is only created if the rank of the matrix is greater or equal than the number of the metabolic reactions present in the model. In the case that this file is not created, it means that the problem cannot be solved, and the metabolic model has to be changed by either grouping or adding extra biochemical reactions. The *.txt output file will display an extra information about redundant equations in case they exist.
It is suggested that in addition to download the code, the two generic files (generic_model1.txt and accumulation_generic1.csv) needed for the program to run should also be downloaded in order to check its format. When running the program the name of the output file produced is similar to the input file (e.g. ****.x*»»»).
The program was developed using python 3.7
Reference:
1.	Vallino JJ, Stephanopoulos G. 2000. Metabolic flux distributions in Corynebacterium glutamicum during growth and lysine overproduction. Reprinted from Biotechnology and Bioengineering, Vol. 41, Pp 633-646 (1993) [classical article]. Biotechnol Bioeng 67:872-885.

