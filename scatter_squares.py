import matplotlib.pyplot as plt

#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# plt.scatter(2, 4, s=200)
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
# Define o título do gráfico e nomeia os eixos.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis="both", which="major", labelsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

#plt.show()

# Salve o gráfico em um arquivo automaticamente
plt.savefig('squares_plot.png', bbox_inches='tight')