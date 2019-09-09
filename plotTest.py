import matplotlib.pyplot as plt 

# naming the x axis 
plt.xlabel('Tamanho das matrizes') 
# naming the y axis 
plt.ylabel('Tempo(em milisegundo)')

# giving a title to my graph 
plt.title('Comparação dos tempos') 

fileTimes = ["simpleSum.txt", "simpleMult.txt", "threadSum.txt", 
"threadMult.txt", "procMult.txt", "procSum.txt"]
for filename in fileTimes:
	file = open(filename, 'r')
	data = file.read()
	file.close()


	yEntrada, xTempo = data.split("\n")

	yEntrada = yEntrada.split(' ')
	xTempo = xTempo.split(' ')
	print(len(yEntrada))
	print(len(xTempo))
	plt.plot(yEntrada, xTempo, label = filename
		[0:-4])
	#plt.legend()
	#plt.show() 

# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 
