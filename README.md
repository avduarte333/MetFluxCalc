# MetFluxCalc

This program aims to calculate velocities of chemical reactions. Given the reactions happening and the components (metabolites) being used, a stoichiometric matrix will be created.
The problem we are trying to solve if of the form : Ax = b, where A is the stoichiometric matrix calculated by the program, and b is the accumulation matrix (balance of the determined fluxes (given by the user in oe of the files)),
The goal is to find x. That is done by doing x = A^(-1) * b. If A is not a squared matrix, the pseudo-inverse will be used.

In order for this program to run correctly, 2 files are needed.
In addition to uploading the code, 2 generic files needed to run the code will also be uploaded, in case the following explanation is not very clear.

1 text file that indicates the number of reactions happening, the name of the components and the reactions itself.
The file should have this shape:
------------------------------------------------
y (Number of Reactions)
Components
Glc
GAP
G6P
PEP
Pyr
F6P
ATP
FBP
DHAP
.
.
.
End of Components
Reac
1 Glc + 1 PEP = 1 G6P + 1 Pyr 
1 G6P = 1 F6P 
1 F6P + 1 ATP = 1 FBP 
1 FBP = 1 DHAP + 1 GAP
.
.
.
---------------------------------------------
1 csv file that has the information about the output of the reactions and has the the following shape:
---------------------------------------------
;XXXX;YYYY;......... (#this column names are given by the user, and the number of columns can be anything)
Glc;1;0;.....
GAP;2;0;.....
G6P;3;0;.....
PEP;4;0;.....
Pyr;5;0;.....
F6P;6;0;.....
ATP;7;0;.....
FBP;8;0;.....
DHAP;9;0;.....
.
.
.
--------------------------------------------
(Insert as many as the user wants, keeping in mind that the components that appear in the rows of this file must be the components also specified on the txt file.)

----------------------------------------
For output the Program will produce 2/3 files

1 excel file with the stoichiometric matrix
1 txt file with information about the stoichiometric matrix
1 excel file the velocities of the reactions (this file is only created if the rank of the matrix is greater or equal than the number of reactions)
In the case this file is not created, it means that the problem can't be solved. There must be specified more linear independent equations.
If this is the case the txt file will also display an extra information about redundant equations in case they exist.





