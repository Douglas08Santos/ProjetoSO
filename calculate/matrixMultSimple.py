from makeMatriz import makeMatriz

class SimpleMult(object):
	"""docstring for multiplyThreadAndProcess"""
	#Multiplicação de matrizes 
	def multMatrix(self, matrix1, matrix2):
		#Condição para multiplicação
		#Se o #colunas da matrix1 eh igual ao #linhas matrix2
		nRowMatrix1 = len(matrix1)
		nColumnMatrix1 = len(matrix1[0])
		nRowMatrix2 = len(matrix2)
		nColumnMatrix2 = len(matrix2[0])
		if (nColumnMatrix1 == nRowMatrix2):
			#Criar uma matriz nula que se tornará a matriz resultante
			matrixR = list(makeMatriz.MakeMatriz().makeNullMatrix(nRowMatrix1, nColumnMatrix2))

			#Operação de multiplicação
			for i in range(nRowMatrix1):
				for j in range(nColumnMatrix2):
					for k in range(nRowMatrix2):
						matrixR[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
		else:
			print("Numero de colunas da primeira matriz: ", nColumnMatrix1,
					"\nNumero de linhas da segunda matriz: ", nRowMatrix2,
					"\nElas devem ser iguais")

			
		return matrixR

		
