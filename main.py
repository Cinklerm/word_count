
def count_word(chaine):
    # On vérifie si le paramètre est vide
    if chaine is None:
        return 0
    # On fait le délimitage de la chaine avec split
    # On utilise le délimiteur par défaut pour éviter un cas avec plusieurs délimiteur consecutifs
    # https://python-reference.readthedocs.io/en/latest/docs/str/split.html
    count= len(chaine.split());
    return count
