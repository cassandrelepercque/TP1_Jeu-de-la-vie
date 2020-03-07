import matplotlib.pyplot as plt
import numpy as np


def afficher_iterations(function, matrix) :
    """Affiche les étapes du jeu de 0 à 9 itérations."""
    plt.figure(figsize=(10, 5))
    plt.title("Itérations de 0 à 9 de Z")
    tableau = list()
    for i in range(10):
        plt.subplot(2, 5, i) #affiche sur 2 lignes et 5 colonnes
        matrice_iteration = function(matrix)
        tableau.append(matrice_iteration) #met les iterations dans la liste
        plt.imshow(tableau[i]) #affiche les figures
        plt.title("Itération" + str(i-1))

