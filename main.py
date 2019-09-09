from inputData import generateMatrix
from makeMatriz import makeMatriz
from calculate import matrixSumSimple
from calculate import matrixMultSimple
from calculate import matrixSumThreadProc
from calculate import matrixMultThreadProc
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
	threadSum = matrixSumThreadProc.SumThreadProc(sizeReturn)
	matrizR = list(threadSum.sumThread(matrizA, matrizB))	
	return matrizR
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

inputMatriz = list(range(100, 1600, 100))
if len(sys.argv) == 2:
	mode = sys.argv[1]
	print(mode)	
	avegareTime = []

	for tam in inputMatriz:
		file = "inputData/matriz"+str(tam)+"x"+str(tam)+".csv"
		matrizA = readMatriz(file)
		matrizB = readMatriz(file)
		result = []		
		#print(matrizA)
		#print(matrizB)
		for i in range(1):
			start = time.time()
			matrizR = main(mode, matrizA, matrizB)
			#print(matrizR)
			end = time.time()
			result.append(end - start)
			print(file)
		avegareTime.append(sum(result)/len(result))
		
else:
	print("Ação necessaria")


stringResult = ""
for tam in inputMatriz:
	stringResult += str(tam)+"x"+str(tam)+" "
stringResult += '\n'

for x in avegareTime:
	stringResult += str(round(x, 3))+" "
filename = mode+".txt"
f = open(filename, "w+")
f.write(stringResult)
f.close()

