from inputData import generateMatrix
from makeMatriz import makeMatriz
from calculate import matrixSumSimple
from calculate import matrixMultSimple
from calculate import matrixSumThreadProc
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
	return list(matrixSumSimple.SimpleSum().sumMatrix(matrizA, matrizB))

def theadSum(matrizA, matrizB):
	sizeReturn = len(matrizA)*len(matrizA[0])
	return list(matrixSumThreadProc.SumThreadProc(sizeReturn).sumThread(matrizA, matrizB))
def procSum(matrizA, matrizB):
	sizeReturn = len(matrizA)*len(matrizA[0])
	return list(matrixSumThreadProc.SumThreadProc(sizeReturn).sumProc(matrizA, matrizB))
def threadMult(matrizA, matrizB):
	sizeReturn = len(matrizA)*len(matrizA[0])
	return list(matrixMultThreadProc.MultThreadProc(sizeReturn).multThread(matrizA, matrizB))

def main(mode, matrizA, matrizB):
	matrizR = None
	if(mode == "simpleSum"):
		matrizR = simpleSum(matrizA, matrizB)
	elif(mode == "simpleMult"):
		matrizR = simpleMult(matrizA, matrizB)
	elif(mode == "threadSum"):
		matrizR = theadSum(matrizA, matrizB)
	elif(mode == "procSum"):
		matrizR = procSum(matrizA, matrizB)
	elif(mode == "threadMult"):
		matrizR = threadMult(matrizA, matrizB)
	elif(mode == "procMult"):
		matrizR = procMult(matrizA, matrizB)
	else:
		print("Operações validas:\n'simpleSum'\n'simpleMult'\n'threadSum\n''procSum\n' 'threadMult\n' 'procMult\n'")

	return matrizR
#Entradas para soma sequencial
'''
inputMatriz = ["inputData/matriz100x100.csv", "inputData/matriz250x250.csv", 
"inputData/matriz500x500.csv", "inputData/matriz750x750.csv", "inputData/matriz1000x1000.csv",
"inputData/matriz2500x2500.csv", "inputData/matriz5000x5000.csv", "inputData/matriz7500x7500.csv",
"inputData/matriz10000x10000.csv"]
'''
#Entradas para multiplicação sequencial
'''
inputMatriz = ["inputData/matriz100x100.csv", "inputData/matriz250x250.csv", 
"inputData/matriz500x500.csv", "inputData/matriz750x750.csv", "inputData/matriz1000x1000.csv"]
'''
#Entradas para soma paralela usando thread

inputMatriz = ["inputData/matriz100x100.csv"] 

''', "inputData/matriz250x250.csv", 
"inputData/matriz500x500.csv", "inputData/matriz750x750.csv", "inputData/matriz1000x1000.csv",
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
		

	stringResult = "100x100 250x250 500x500 750x750 1000x1000 2500x2500 5000x5000 7500x7500 10000x10000\n"
	for x in avegareTime:
		stringResult += str(round(x, 3))+" "
	filename = mode+".txt"
	f = open(filename, "w+")
	f.write(stringResult)
	f.close()
else:
	print("Ação necessaria")


