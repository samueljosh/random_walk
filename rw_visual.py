import matplotlib.pyplot as plt 
from random_walk import RandomWalk

# Continua criando novos passeios enquanto o programa estiver ativo

while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Define o tamanho da janela de plotagem
    plt.figure(dpi=128,figsize=(12, 8))

    # Plota os pontos e mostra o gráfico
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=1)
    # Enfatiza o primeiro e o último ponto
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors='none', s=100)

    # Remove os eixos
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()


    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break