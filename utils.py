import matplotlib.pyplot as plt
import numpy as np

def afficher_iterations(function, matrix):
    """Affiche les étapes du je de la vie sur 10 itérations."""
    plt.figure(figsize=(11,5)) #affichage des figures des itérations plus lisible.
    plt.suptitle("Itérations de 0 à 9 de Z") #titre général
    plt.subplot(2, 5, 1)
    matrice_iteration = (np.array(matrix))
    plt.imshow(matrice_iteration)
    plt.title("Itération" + "0")
    for i in range(2, 11):
        plt.subplot(2, 5, i) #affiche sur 2 lignes et 5 colonnes.
        matrice_iteration = function(matrix)
        plt.imshow(matrice_iteration) #affiche les figures.
        plt.title("Itération" + str(i-1)) #titre de chaque figure.
