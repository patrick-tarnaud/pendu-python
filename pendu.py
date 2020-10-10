from fonctions import tirer_mot_aleatoire
from donnees import nb_chances_max
from fonctions import *

def jouer():
    prenom = input('Quel est ton prénom ? ')
    print('Bienvenue', prenom.capitalize(), '!')

    nb_essais = 0
    mot_trouve = False
    mot_a_afficher= '*' * nb_chances_max

    # tant que l'utilisateur n'a pas trouvé le mot et qu'il n'a pas atteint le nombre max de chances
    while not mot_trouve and nb_essais < nb_chances_max:
        # gestion de la saisie de la lettre
        lettre = saisie_lettre()
        # afficher la lettre saisi dans le mot
        # mot_a_afficher =



# demande lettre à l'utilisateur

if __name__ == '__main__':
    try:
        # jouer()
        print(mot_a_afficher('pangolin', 'n'))
    except TypeError as e:
        print(e)

