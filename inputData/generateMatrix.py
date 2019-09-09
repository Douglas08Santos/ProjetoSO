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
class GenerateMatrix(object):
	"""docstring for ClassName"""
	def generateMatrix(self, row=0, col=0):
		elem = list(range(0, 9))
		matrizCreated = ""
		outFilename = "matriz"+str(row) +"x"+ str(col)+".csv" 
		for x in range(0,row):
			for y in range(0,col):
				matrizCreated += str(random.choice(elem))
				if y != col-1:
					matrizCreated += ","
			matrizCreated +="\n"

		#print(matrizCreated)

		output = open(outFilename, "w+")
		output.write(matrizCreated)
		output.close()
		
def main():
	tam = list(range(10, 55, 5))
	generate = GenerateMatrix()
	for i in tam:		
		generate.generateMatrix(i, i)
	'''if len(sys.argv) == 3:
		qtdRow = int(sys.argv[1])
		qtdCol = int(sys.argv[2])
	'''
		
main()