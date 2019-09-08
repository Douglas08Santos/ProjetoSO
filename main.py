from inputData import generateMatrix
from makeMatriz import makeMatriz
from calculate import matrixSumSimple
from calculate import matrixMultSimple
import sys
import time

#Geração de matriz
def generate(row, col):
	generateMatrix.GenerateMatrix().generateMatrix(row, col)

def readMatriz(filename):
	#maked = makeMatriz.makeMatriz()	
	return list(makeMatriz.MakeMatriz().makeMatrizByCsv(filename))

def simpleMult(matrizA, matrizB):
	return list(matrixMultSimple.SimpleMult().multMatrix(matrizA, matrizB))

def simpleSum(matrizA, matrizB):
	return list(matrixSumSimple.SimpleSum().SumMatrix(matrizA, matrizB))

def main(mode, matrizA, matrizB):
	matrizR = None
	if(mode == "simpleSum"):
		matrizR = simpleSum(matrizA, matrizB)
	elif(mode == "simpleMult"):
		matrizR = simpleMult(matrizA, matrizB)
	else:
		print("Operações validas:\n'simpleSum' ou 'simpleMult'")

	return matrizR
#Teste sequencial
inputMatriz = ["inputData/matriz100x100.csv", "inputData/matriz250x250.csv", 
"inputData/matriz500x500.csv"]
''', "inputData/matriz750x750.csv", "inputData/matriz1000x1000.csv",
"inputData/matriz2500x2500.csv", "inputData/matriz5000x5000.csv", "inputData/matriz7500x7500.csv",
"inputData/matriz10000x10000.csv"]'''




if len(sys.argv) == 2:
	mode = sys.argv[1]
	print(mode)
	avegareTime = []

	for inputData in inputMatriz:
		matrizA = readMatriz(inputData)
		matrizB = readMatriz(inputData)
		result = []		
		#print(matrizA)
		#print(matrizB)
		for i in range(5):
			start = time.time()
			matrizR = main(mode, matrizA, matrizB)
			#print(matrizR)
			end = time.time()
			result.append(end - start)
		print(inputData)
		avegareTime.append(sum(result)/len(result))
		

	stringResult = "100x100 250x250 500x500\n"# 750x750 1000x1000 2500x2500 5000x5000 7500x7500 10000x10000\n"
	for x in avegareTime:
		stringResult += str(round(x, 3))+" "
	filename = mode+".txt"
	f = open(filename, "w+")
	f.write(stringResult)
	f.close()
else:
	print("Ação necessaria")


