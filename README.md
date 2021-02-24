# MetFluxCalc

This program aims to calculate velocities of chemical reactions. Given the reactions happening and the components (metabolites) being used, a stoichiometric matrix will be created.
The problem we are trying to solve if of the form : Ax = b, where A is the stoichiometric matrix calculated by the program, and b is the accumulation matrix (balance of the determined fluxes (given by the user in oe of the files)),
The goal is to find x. That is done by doing x = A^(-1) * b. If A is not a squared matrix, the pseudo-inverse will be used.

In order for this program to run correctly, 2 files are needed.
In addition to uploading the code, 2 generic files needed to run the code will also be uploaded.

For output the Program will produce 2/3 files

1 excel file with the stoichiometric matrix
1 txt file with information about the stoichiometric matrix
1 excel file the velocities of the reactions (this file is only created if the rank of the matrix is greater or equal than the number of reactions)
In the case this file is not created, it means that the problem can't be solved. There must be specified more linear independent equations.
If this is the case the txt file will also display an extra information about redundant equations in case they exist.





