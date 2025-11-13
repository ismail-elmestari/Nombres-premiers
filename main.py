"""
Ce module contient des fonctions pour tester si un
nombre est premier
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):

    """""
    Verifie qu un nombre est premier et retourne true le cas échéant, retourne false sinon

    """

    premier=True
    n=2
    if p<2 :
        return False

    while n<=sqrt(p) :
        if p%n==0 :
            premier=False
            break
        n+=1

    return premier

#### Fonction principale


def main():

    """
    Teste la fonction isprime sur [0; 100]
    """


    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
