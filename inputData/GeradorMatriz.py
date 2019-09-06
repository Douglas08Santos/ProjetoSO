#Gerador de Matrizes
import random
import csv

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
qtdRow = 3
qtdCol = 3
outputfile = "matriz"+str(qtdRow) +"x"+ str(qtdCol)+".csv" 
generateMatriz(qtdRow, qtdCol, outputfile)