# import all libraries
import numpy as np
from numpy.linalg import matrix_rank
from numpy import linalg as LA
import re
import pandas as pd
import openpyxl
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import ctypes
import sys


###
### Designed and Coded By Andre Duarte
### Some Internet Sites were consulted, mainly:
### https://stackoverflow.com/questions/28816627/how-to-find-linearly-independent-rows-from-a-matrix
### https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
###


def LI_vecs(dim,M, file_out):
    LI=[M[0]]
    file_out.write('\n\n\nIn this order, the irrelevant Reactions are:\n')
    for i in range(dim):
        tmp=[]
        for r in LI:
            tmp.append(r)
        tmp.append(M[i])                #set tmp=LI+[M[i]]
        if matrix_rank(tmp)>len(LI):    #test if M[i] is linearly independent from all (row) vectors in LI
            LI.append(M[i])           #note that matrix_rank does not need to take in a square matrix
        elif i !=0:
            file_out.write('Equation Number {}\n'.format(i+1))

    return LI



# Python program to convert a list to string
# Function to convert
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1


def onclick(args):
    if args == 4:
        sys.exit()

    if args == 1:
        root = tk.Tk()
        root.withdraw()
        global in_path
        in_path = filedialog.askopenfilename()
        global control1
        control1 = 1

    if args == 2:
        root = tk.Tk()
        root.withdraw()
        global out_folder
        out_folder = filedialog.askdirectory()
        global control2
        control2 = 1

    if args == 5:
        root = tk.Tk()
        root.withdraw()
        global accum_matrix
        accum_matrix = filedialog.askopenfilename()
        global control3
        control3 = 1




    if args == 3:

        if(control1 != 1 or control2 != 1 or control3 !=1):
            ctypes.windll.user32.MessageBoxW(0, "You first need to specify the files to use and the output folder!", "Warning",1)

        elif(control1 == 1 and control2 == 1 and control3 ==1):
            a = []
            f = open(in_path, "r")
            numero_equacoes = f.readline()
            numero_equacoes = re.findall(r"[-+]?\d*\.\d+|\d+", numero_equacoes)
            numero_equacoes = int(listToString(numero_equacoes))
            f.close()

            # Using for loop
            count = 0
            check_componentes = 0
            componentes = []

            # Abrir Ficheiro, Descobrir nome de todos os componentes que estão nas equações e criar vetor com isso
            with open(in_path) as fp:
                for line in fp:
                    a = line.strip()
                    if a == 'End of Components':
                        break
                    if a == 'Components':
                        check_componentes = 1
                    elif check_componentes == 1:
                        count += 1
                        componentes.append(a)
            fp.close()

            # Criar matriz das reacoes e array com nome dos componentes para depois saber onde indexar na matriz
            nome_componentes = np.array(componentes)
            matriz_reacoes = np.zeros([numero_equacoes, len(nome_componentes)], dtype=float)
            count = 0
            check_componentes = 0
            reacoes = []

            with open(in_path) as fp:
                for line in fp:
                    a = line.strip()
                    if a == 'Reac':
                        check_componentes = 1
                    elif check_componentes == 1:
                        count += 1
                        reacoes.append(a)
            fp.close()

            reacoes = np.array(reacoes)

            # Ciclo de Preencher matriz
            i = 0
            for i in range(len(reacoes)):
                # Avaliar reacao a reacao
                x = reacoes[i].split("=", 1)
                # Dividir em parte esquerda e direita do igual
                parte_esquerda = x[0]
                parte_direita = x[1]
                # Perceber quantos componentes existem na parte esquerda e direita. Len destes resultados é isso
                quantos_componentes_esquerda = ([pos for pos, char in enumerate(parte_esquerda) if char == '+'])
                quantos_componentes_direita = ([pos for pos, char in enumerate(parte_direita) if char == '+'])
                parte_esquerda_splitted = parte_esquerda.split("+", len(quantos_componentes_esquerda))
                parte_direita_splitted = parte_direita.split("+", len(quantos_componentes_direita))
                j = 0
                for j in range(len(parte_esquerda_splitted)):
                    k = 0
                    for k in range(len(nome_componentes)):
                        indice = 0
                        if re.search(r'\b{}\b'.format(nome_componentes[k]), parte_esquerda_splitted[j]):
                            indice = k
                            # Descobrir o coeficiente que multiplica pelo componente
                            # #tem de ser coeficiente 0, porque se o composto tiver numeros no nome ele dá varios resultados
                            find_coeficiente = re.findall(r"[-+]?\d*\.\d+|\d+", parte_esquerda_splitted[j])
                            matriz_reacoes[i, indice] = -1 * float(find_coeficiente[0])

                j = 0
                for j in range(len(parte_direita_splitted)):
                    k = 0
                    for k in range(len(nome_componentes)):
                        indice = 0
                        if re.search(r'\b{}\b'.format(nome_componentes[k]), parte_direita_splitted[j]):
                            indice = k
                            # Descobrir o coeficiente que multiplica pelo componente
                            # #tem de ser coeficente[0], porque se o composto tiver numeros no nome ele dá varios resultados
                            find_coeficiente = re.findall(r"[-+]?\d*\.\d+|\d+", parte_direita_splitted[j])
                            matriz_reacoes[i, indice] = float(find_coeficiente[0])

            dataframe_linhas = []
            aux = 0
            for aux in range(numero_equacoes):
                dataframe_linhas.append('X{}'.format(aux+1))
            df1 = pd.DataFrame(matriz_reacoes, columns=nome_componentes, index= dataframe_linhas)
            df1 = df1.transpose()
            file_out = open(out_folder+'/dados_matriz.txt', "w")
            arr = df1.to_numpy()

            A = arr[:, 0:]

            # Matriz A tem, Linhas os Compostos, Nas colunas as Equações
            file_out.write('The Rank of Matrix A = {}\n'.format(matrix_rank(A)))
            file_out.write('The Number of Reactions = {}\n'.format(len(reacoes)))
            file_out.write('The condition Number of A = {}\n'.format(LA.cond(A)))


            file_out.write('Number of Equations = {}\n'.format(len(nome_componentes)))

            if matrix_rank(A) != len(nome_componentes):
                S = -1
                file_out.write('Matrix doenst have inverse\n')
            else:
                S = 1
                file_out.write('Matrix with possible inverse\n')


            accum_matrix = pd.read_csv(accum_matrix, sep=';', index_col= 0, header=0)
            nomes_colunas_final = accum_matrix.columns
            accum_matrix = accum_matrix.to_numpy()


            if(matrix_rank(A) >= len(reacoes)):
                Pseudo_Inv = np.linalg.pinv(A)
                vetor_final = np.matmul(Pseudo_Inv, accum_matrix)
                df2 = pd.DataFrame(vetor_final, columns=nomes_colunas_final, index=dataframe_linhas)
                df2.to_excel(out_folder + '/matriz_velocidades.xlsx', index=True, header=True, startcol=1, startrow=1)
            else:
                A = np.transpose(A)
                file_out.write('\n\n\n\nThis Problem does not have solution and there might be reactions that are redundant')
                file_out.write('\nIf so, they are presented below\n')
                A = LI_vecs(len(A),A, file_out)


            file_out.close()
            df1.to_excel(out_folder+'/matriz_estequeometrica.xlsx', index=True, header=True, startcol= 1, startrow= 1)
            ctypes.windll.user32.MessageBoxW(0, "Please Check the Output Files!", "Finished", 1)
            # sys.exit()



control1 = 0
control2 = 0
control3 = 0


root = tk.Tk()
root.title("GUI Button")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 500
window_height = 400
x = ((screen_width)*0.5) - window_width*0.5
y = ((screen_height)*0.5) - window_height*1
root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

#First Step, Create Element
btn1 = tk.Button(root, text = "Input File", command=lambda:onclick(1))
btn2 = tk.Button(root, text = "Output Folder (for the Excel File)", command=lambda:onclick(2))
btn3 = tk.Button(root, text = "Run Program", command=lambda:onclick(3))
btn4 = tk.Button(root, text = "End Program", command=lambda:onclick(4))
btn5 = tk.Button(root, text = "Array / Accumulation Matrix", command=lambda:onclick(5))

btn1.place(relx=0.05, rely=0.1, anchor=W)
btn2.place(relx=0.05, rely=0.2, anchor=W)
btn3.place(relx=0.05, rely=0.4, anchor=W)
btn4.place(relx=0.85, rely=0.1, anchor=CENTER)
btn5.place(relx=0.05, rely=0.3, anchor=W)

T = tk.Text(root, height=3, width=44)
T.pack()
quote = "In case of doubt read README.txt\nWork done by André Duarte\nData Science and Engeneering Student At IST"
T.insert(tk.END, quote)
T.place(relx=0.05, rely=0.7, anchor=W)
root.mainloop()


