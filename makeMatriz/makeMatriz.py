import csv

class MakeMatriz(object):
	
	#Cria uma matriz a partir de um arquivo .csv
	def makeMatrizByCsv(self, filename):
		matrix = []
		with open(filename, "rt", encoding="UTF-8") as fileinput:
			csvFile = csv.reader(fileinput, delimiter=",")

			for row in csvFile:
				matrix.append(row)

			return matrix

	#Retorna uma matriz nula
	def makeNullMatrix(self, row, column):
		matrix = []
		for i in range(0,row):
			matrix.append([0]*column)
		return matrix
		