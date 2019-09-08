from makeMatriz import makeMatriz

class SimpleSum(object):
	"""docstring for SimpleSum"""
	#Soma de matrizes
	def sumMatrix(self, matrix1, matrix2):
		#Condição para a soma
		#As matrizes devem ser do mesmo tamanho
		#Mesma quantidade de linhas e de colunas
		nRow1 = len(list(matrix1))
		nColumn1 = len(list(matrix1[0]))
		nRow2 = len(list(matrix2))
		nColumn2 = len(list(matrix2[0]))
		#Verifica se atende a condição para se realizar
		if (nRow1 == nRow2 and nColumn1 == nColumn2):
			matrixR = list(makeMatriz.MakeMatriz().makeNullMatrix(nRow1, nColumn1))
			for i in range(nRow1):
				for j in range(nColumn1):
					matrixR[i][j] += int(matrix1[i][j]) + int(matrix2[i][j])
			return matrixR
		else:
			print("M1[",nRow1," x ", nColumn1,"]\n",
				  "M2[",nRow2," x ", nColumn2,"]\n",
				  "Tamanhos diferentes")
			return None