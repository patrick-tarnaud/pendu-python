from fonctions import tirer_mot_aleatoire
from donnees import nb_chances_max
from fonctions import *


def jouer():
    prenom = input('Quel est ton prénom ? ')
    print('Bienvenue', prenom.capitalize(), '!')

    nb_essais: int = 0
    est_mot_trouve: bool = False
    mot_a_trouver: str = tirer_mot_aleatoire()
    lettres_bonnes: [str] = []
    lettres_saisies: [str] = []
    mot_a_afficher = '*' * len(mot_a_trouver)

    # tant que l'utilisateur n'a pas trouvé le mot et qu'il n'a pas atteint le nombre max de chances
    while not est_mot_trouve and nb_essais < nb_chances_max:
        print('--Essai n°', nb_essais + 1, ' --')

        if len(lettres_saisies) > 0:
            print('Pour rappel tu as déjà saisi ces lettres {}'.format(lettres_saisies))
            print('Le mot :', mot_a_afficher)
        # saisie de la lettre
        lettre_saisie = saisir_lettre()
        lettres_saisies.append(lettre_saisie)

        nb = calculer_nb_occurences_lettre_dans_mot(mot_a_trouver, lettre_saisie)
        if nb > 0:
            print('Bravo ! La lettre {} est présente {} fois dans le mot à trouver'.format(lettre_saisie, nb))
            lettres_bonnes.append(lettre_saisie)
            mot_a_afficher = calculer_mot_a_afficher(mot_a_trouver, lettres_bonnes)
            print('Le mot obtenu est :', mot_a_afficher)
            # le joueur peut entrer le mot s'il l'a deviné
            mot_saisi = input('Peux tu le deviner maintenant ? Entre le mot (ou Entrée si tu ne sais toujours pas) : ')
            # si mot trouvé alors le joueur a gagné sinon on continue
            if mot_saisi == mot_a_trouver:
                est_mot_trouve = True
            elif len(mot_saisi) > 0:
                print('Et non....')
        else:
            print('Désolé ! La lettre {} n\'est pas présente dans le mot à trouver'.format(lettre_saisie))

        nb_essais += 1

    if est_mot_trouve:
        print('***** Bravo !!! Tu as gagné !*****')
        print('Tu as trouvé le mot en {} essais'.format(nb_essais))

        # score
        score = nb_chances_max - nb_essais
        print('Ton score est de {}'.format(score))
        sauvegarder_score(prenom, score)
    else:
        print('***** Looser tu as perdu ! *****')
        print('Le mot était', mot_a_trouver)

# demande lettre à l'utilisateur

if __name__ == '__main__':
    try:
        jouer()
        # lire_scores()
        # sauvegarder_score('Patrick', 8)
        # sauvegarder_score('Sophie', 10)
        # print(lire_scores())

        # scores = lire_scores()
        # print('scores', scores)
        # print(type(scores))
    except TypeError as e:
        print(e)
