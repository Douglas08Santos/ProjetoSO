from inputData import generateMatrix
from makeMatriz import makeMatriz
from calculate import matrixSumSimple
from calculate import matrixMultSimple

#Geração de matriz
def generate(row, col):
	generateMatrix.GenerateMatrix().generateMatrix(row, col)

def readMatriz(filename):
	#maked = makeMatriz.makeMatriz()	
	return list(makeMatriz.MakeMatriz().makeMatrizByCsv(filename))


def simpleSum(matrizA, matrizB):
	return list(matrixSumSimple.SimpleSum().SumMatrix(matrizA, matrizB))

def simpleMult(matrizA, matrizB):
	return list(matrixMultSimple.SimpleMult().multMatrix(matrizA, matrizB))




matrizA = readMatriz("inputData/matriz3x3.csv")
matrizB = readMatriz("inputData/matriz3x3.csv")
matrizR = simpleSum(matrizA, matrizB)
matrizRMult = simpleMult(matrizA, matrizB)
print(matrizA)
print(matrizB)
print(matrizR)
print(matrizRMult)
