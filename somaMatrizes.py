

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

#Soma de matrizes
def SumMatrix(matrix1, matrix2):
	#Condição para a soma
	#As matrizes devem ser do mesmo tamanho
	#Mesma quantidade de linhas e de colunas
	nRow1 = len(matrix1)
	nColumn1 = len(matrix1[0])
	nRow2 = len(matrix2)
	nColumn2 = len(matrix2[0])

	if (nRow1 == nRow2 and nColumn1 == nColumn2):
		matrixR = makeMatrix(nRow1, nColumn1)
		for i in range(nRow1):
			for j in range(nColumn1):
				matrixR += int(matrix1[i][j]) * int(matrix2[i][j])
	else:
		print("M1[",nRow1," x ", nColumn1,"]\n",
			  "M2[",nRow2," x ", nColumn2,"]\n",
			  "Tamanhos diferentes")