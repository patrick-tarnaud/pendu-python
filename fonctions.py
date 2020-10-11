from random import randint
from donnees import *
import re
import pickle
import os.path


def tirer_mot_aleatoire():
    return mots[randint(0, len(mots) - 1)]


def est_une_lettre(lettre) -> bool:
    return re.match('^[a-zA-Z]$', lettre)


def saisir_lettre() -> str:
    est_lettre = False
    while not est_lettre:
        lettre = input('Quelle lettre choisis tu ? ')
        if not est_une_lettre(lettre):
            print("""Une lettre j'ai dit bordel !""")
            continue
        est_lettre = True
    return lettre.lower()


def calculer_mot_a_afficher(mot_a_trouver: str, lettres: [str]) -> str:
    mot_a_retourner = ''
    for c in mot_a_trouver:
        trouve = False
        for l in lettres:
            if c == l:
                trouve = True
        mot_a_retourner = mot_a_retourner + c if trouve else mot_a_retourner + '*'
    return mot_a_retourner


def calculer_nb_occurences_lettre_dans_mot(mot: str, lettre: str) -> int:
    return mot.count(lettre)


def lire_scores() -> {}:
    if os.path.isfile(FICHIER_SCORE):
        with open(FICHIER_SCORE, 'rb') as file:
            unpic = pickle.Unpickler(file)
            scores = unpic.load()
        return scores
    else:
        return dict()

def sauvegarder_score(prenom: str, score: int):
    # charger les scores pour savoir si ce prenom a déjà un score
    scores = lire_scores()
    scores[prenom] = score
    with open(FICHIER_SCORE, 'wb') as file:
        p = pickle.Pickler(file)
        p.dump(scores)
