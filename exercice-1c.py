if __name__ == '__main__':
    # On commence avec 10 caracteres
    a = 10
    # une boucle dans laquelle on imprime une ligne
    while a > 0:
        # Boucle variable pour imprimer les caractere d'une ligne
        for b in range(0, a):
            print("*", end="")
        a = a - 1
        # On cree une ligne vide comme ca on peut passer a la prochaine ligne
        print("")
