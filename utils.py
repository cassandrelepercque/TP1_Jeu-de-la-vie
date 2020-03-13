import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def afficher_iterations(function, matrix):
    """Affiche les étapes du je de la vie sur 10 itérations."""
    plt.figure(figsize=(11,5)) #affichage des figures des itérations plus lisible.
    plt.subplot(2, 5, 1)
    matrice_iteration = (np.array(matrix))
    plt.imshow(matrice_iteration)
    plt.title("Itération" + "0")
    for i in range(2, 11):
        plt.subplot(2, 5, i) #affiche sur 2 lignes et 5 colonnes.
        matrice_iteration = function(matrix)
        plt.imshow(matrice_iteration) #affiche les figures.
        plt.title("Itération" + str(i-1)) #titre de chaque figure.


def video(matrix, jeu_np, iterations):
    case = plt.matshow(matrix)

    def animate(i):
        case.set_array(jeu_np(np.array(matrix), i))
        return(case)
    anim = animation.FuncAnimation(plt.figure(), animate, frames = iterations)
    return(anim)