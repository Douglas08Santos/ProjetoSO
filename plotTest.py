import matplotlib.pyplot as plt 

file = open("simpleSum.txt", 'r')


data = file.read()

file.close()


yEntrada, xTempo = data.split("\n")

yEntrada = yEntrada.split(' ')
xTempo = xTempo.split(' ')
print(len(yEntrada))
print(len(xTempo))
plt.plot(yEntrada, xTempo[0:len(yEntrada)], label = "Soma Sequencial")



'''
# line 1 points 
x1 = [1,2,3] 
y1 = [2,4,1] 
# plotting the line 1 points 
plt.plot(x1, y1, label = "line 1") 

# line 2 points 
x2 = [1,2,3] 
y2 = [4,1,3] 
# plotting the line 2 points 
plt.plot(x2, y2, label = "line 2") 
'''
# naming the x axis 
plt.xlabel('Tamanho das matrizes') 
# naming the y axis 
plt.ylabel('Tempo(em milisegundo)')

# giving a title to my graph 
plt.title('Implementação Sequencial - Soma de matrizes') 

# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 
