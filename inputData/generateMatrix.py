#Gerador de Matrizes
import random
import csv
import sys

'''
TODO:
criar matriz -> OK
adicionar em uma string -> OK
adicionar a string em um aquivo csv -> OK
usar args para configurar o tamanho da matriz -> OK

Para executar:
	python3 generateMatrix.py <numero de linhas> <numero de colunas>

'''
elem = list(range(0, 9))

def generateMatriz(row, col, filename):
	matrizCreated = ""
	for x in range(0,row):
		for y in range(0,col):
			matrizCreated += str(random.choice(elem))
			if y != col-1:
				matrizCreated += ","
		matrizCreated +="\n"

	print(matrizCreated)

	outputfile = open(filename, "w+")
	outputfile.write(matrizCreated)
	outputfile.close()

qtdRow = int(sys.argv[1])
qtdCol = int(sys.argv[2])
outputfile = "matriz"+str(qtdRow) +"x"+ str(qtdCol)+".csv" 
generateMatriz(qtdRow, qtdCol, outputfile)