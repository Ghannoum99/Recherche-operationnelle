"""
%    Projet Recherche opérationnelle : Programmation dynamique

%    Auteur : Jihad GHANNOUM

%    ISTY | IATIC 4 | 2021-2022

%   fonction : Knapsack_DP

%   But de fonction : cette fonction permet de résoudre le problème
%   du sac à dos en appliquant le principe de programmation dynamique.

%   Entrees :
%   b : capacité du sac à dos
%   a : tableau représentant les poids des objets
%   c : tableau représentant la valeur d'un objet
%   n : nombre d'objets

%   Sortie :
%   T[n][b] : la solution optimale

"""


def knapsack_DP(b, a, c, n):
    # Declaration d'un tableau T 2D
    T = [[0 for x in range(b + 1)] for x in range(n + 1)]

    # Construire le tableau T de bas en haut "manière ascendante"
    for i in range(n + 1):
        for j in range(b + 1):

            if i == 0 or j == 0:
                T[i][j] = 0

            elif j >= a[i - 1]:
                T[i][j] = max(c[i - 1] + T[i - 1][j - a[i - 1]], T[i - 1][j])

            else:
                T[i][j] = T[i - 1][j]

    return T[n][b]


# fonction main
if __name__ == '__main__':
    # capacité du sac = 12
    b = 12
    # poids des objets
    a = [5, 2, 4, 5, 3]
    # valeurs des objets
    c = [75, 90, 70, 75, 80]

    res_opt = knapsack_DP(b, a, c, 5)

    # affichage de la solution optimale
    print("la solution optimale est ", end = "")
    print(res_opt)

