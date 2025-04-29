# Initialisation des compteurs
longueur = 0
mots = 0
voyelles = 0

# Lire la phrase
phrase = input("Entrez une phrase qui se termine par un point : ")

# Vérification que la phrase se termine bien par un point
if phrase[-1] != '.':
    print("Erreur : la phrase doit se terminer par un point.")
else:
    # Parcourir chaque caractère
    for i in range(len(phrase)):
        caractere = phrase[i]
        
        # Incrémenter la longueur
        longueur += 1
        
        # Vérifier si le caractère est une voyelle
        if caractere.lower() in 'aeiouy':
            voyelles += 1
        
        # Vérifier si le caractère est un espace (indiquant un nouveau mot)
        if caractere == ' ':
            mots += 1
    
    # Ajouter 1 mot de plus, car le nombre de mots = nombre d'espaces + 1
    mots += 1

    # Afficher les résultats
    print("Longueur de la phrase :", longueur)
    print("Nombre de mots :", mots)
    print("Nombre de voyelles :", voyelles)
