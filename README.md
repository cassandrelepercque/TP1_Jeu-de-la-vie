# Jeu de la vie

Le jeu de la vie est un automate cellulaire imaginé par *John Horthon Conway* en 1970.
Le "jeu" est en faite un jeu à zéro joueur, car son évolution est déterminée par son état initial et ne nécessite aucune intervention de la part d'un humain.

## Règles

- **Naissance** : Toute cellule morte ayant exactement 3 voisins devient une cellule vivante.
- **Equilibre** : Toute cellule vivante avec 2 ou 3 voisins reste vivante à la génération suivante.
- **Etouffement** : Toute cellule vivante ayant 4 voisins vivants meurt à la génération suivante.
- **Isolement** : Toute cellule vivante ayant 0 ou 1 voisin vivant décède à la génération suivante.
