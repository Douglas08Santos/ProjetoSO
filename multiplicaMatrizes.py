
import csv
'''
Referencias:
	http://blog.evaldojunior.com.br/aulas/python/2009/02/08/curso-de-python-aula-12.html
	https://pt.stackoverflow.com/questions/97269/como-ler-um-arquivo-csv-em-python
'''
#

#Cria uma matriz a partir de um arquivo .csv
def makeCsvMatriz(filename):
	matrix = []
	with open(filename, "rb") as fileinput:
		csvFile = csv.reader(fileinput, delimiter=",")
		
		for Row in csvFile:
			matrix.append(Row)
		return matrix

#Retorna uma matriz nula
def makeMatrix(row, column):
	matrix = []
	for i in range(0,Row):
		matrix.append([0]*column)
	return matrix

#Multiplicação de matrizes 
def multiplyMatrix(matrix1, matrix2):
	#Condição para multiplicação
	#Se o #colunas da matrix1 eh igual ao #linhas matrix2 
	nColumnMatrix1 = len(matrix1[0])
	nRowMatrix2 = len(matrix2)
	if (nColumnMatrix1 == nRowMatrix2):
		#Criar uma matriz nula que se tornará a matriz resultante
		matrixR = makeMatrix(nRowMatrix2, nColumnMatrix1)

		#Operação de multiplicação
		for i in range(len(matrix1)):
			for j in range(len(matrix2[0])):
				for k in range(len(matrix2)):
					matrixR += int(matrix1[i][k]) * int(matrix2[k][j])
	else:
		print("Numero de colunas da primeira matriz: ", nColumnMatrix1,
				"\nNumero de linhas da segunda matriz: ", nRowMatrix2,
				"\nElas devem ser iguais")

		
	return matrixR

