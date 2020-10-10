from random import randint
from donnees import mots
import re


def tirer_mot_aleatoire():
    return mots[randint(0, len(mots) - 1)]


def est_une_lettre(lettre) -> bool:
    return re.match('^[a-zA-Z]$', lettre)

def saisie_lettre()->str:
    est_lettre = False
    while not est_lettre:
        lettre = input('Quelle lettre choisis tu ? ')
        if not est_une_lettre(lettre):
            print("""Une lettre j'ai dit bordel !""")
            continue
        est_lettre = True
    return lettre

def mot_a_afficher(mot_a_trouver: str, lettre : str) -> str:
    mot_a_retourner = ''
    for c in mot_a_trouver:
        if c != lettre:
            mot_a_retourner += '*'
        else:
            mot_a_retourner += lettre
    return mot_a_retourner