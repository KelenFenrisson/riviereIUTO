# coding=utf-8
# construit une nouvelle grille hexagonale.
# Cette grille contiendra nbLig lignes, nbCol colonnes.
# si paire est à True la grille sera paire sinon elle sera impaire
# valeur sera la valeur par défaut stockée dans chaque case de la grille

def GrilleHexa(nbLig, nbCol, paire=True, valeur=None):
    grille = None

    if type(nbCol) is int and type(nbLig) is int and type(paire) is bool:
        grille = {"nombre de lignes": nbLig, "nombre de colonnes": nbCol, "paire": paire}

        for x in range(grille["nombre de lignes"]):
            for y in range(grille["nombre de colonnes"]):
                if grille["paire"]:
                    if x%2 == y%2:
                        grille[(x,y)]=valeur
                else:
                    if not x%2 == y%2:
                        grille[(x,y)]=valeur

    return grille


# retourne le nombre de lignes de la grille
def getNbLigGH(grille):
    return grille["nombre de lignes"]


# retourne le nombre de colonnes de la grille
def getNbColGH(grille):
    return grille["nombre de colonnes"]


# indique si la grille est paire ou impaire
def estPaireGH(grille):
    return grille["paire"]


# vérifie si une position est bien une position de la grille
# par exemple si la grille est paire, lig vaut 2 et col vaut 3
# la fonction retourne False car il n'y a pas de colonne 3 dans une ligne
# de numéro paire d'une grille paire
def estPosGH(grille, lig, col):
    estPos = False
    if (lig, col) in grille:
        estPos = True
    return estPos


# retourne la valeur qui se trouve dans la grille à la ligne lig, colonne col
def getValGH(grille, lig, col):
    if estPosGH(grille, lig, col):
        return grille[(lig,col)]


# met la valeur val dans la grille à la la ligne lig, colonne col
def setValGH(grille, lig, col, val):
    if estPosGH(grille, lig, col):
        grille[(lig,col)] = val

# retourne un couple d'entier qui indique de combien de ligne et de combien
# de colonnes il faut se déplacer pour aller dans une direction.
# par exemple si direction vaut 'S' le retour sera (2,0) car pour se déplacer
# vers le sud, on ne change pas de colonne par contre on passe 2 lignes
# Si la direction est 'NE' le resultat sera (-1,1) car pour aller dans cette direction
# il faut remonter d'une ligne et aller une colonne vers la droite
# Cette fonction vous sera utile pour la fonction suivante.
def incDirectionGH(direction):
    d_direction = {'N': (-2, 0),
                   'S': (2, 0),
                   'NE': (-1, 1),
                   'NO': (-1, -1),
                   'SE': (1, 1),
                   'SO': (1, -1),
                   'X': (0,0)}

    return d_direction.get(direction, None)


# permet de retourner la liste des n valeurs qui se trouvent dans la grille
# dans une direction donnée à partir de la position lig,col
# si il y a moins n celulles dans la grille dans la direction données on retourne
# toutes le cellules trouvées
def getNProchainsGH(grille, lig, col, direction, n=3):
    liste_NProchains = []

    vx, vy = incDirectionGH(direction)

   # On regarde le prochain pas
    lig += vx
    col += vy

    for i in range(n):
        x_a_i_pas = lig + vx * i
        y_a_i_pas = col + vy * i

        if (estPosGH(grille, x_a_i_pas, y_a_i_pas)):
            valeur = grille[(x_a_i_pas,y_a_i_pas)]
            liste_NProchains.append(valeur)
    return liste_NProchains


# fonction d'initiation d'une grille avec des caractères pour faire des tests
# la grille doit être créée
def initAlphaGH(grille):
    possibles = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    nbLig = getNbLigGH(grille)
    nbCol = getNbColGH(grille)
    if estPaireGH(grille):
        dec = 0
    else:
        dec = 1
    k = 0
    for i in range(nbLig):
        for j in range(dec, nbCol, 2):
            setValGH(grille, i, j, possibles[k])
            k = (k + 1) % len(possibles)
        dec = (dec + 1) % 2


# affichage en mode texte d'une grille hexagonale
def afficheGH(grille):
    nbLig = getNbLigGH(grille)
    nbCol = getNbColGH(grille)
    if estPaireGH(grille):
        print(" ", end='')
        debut = 0
    else:
        debut = 1
        print("   ", end='')
    for j in range(debut, nbCol, 2):
        print("_   ", end='')
    print()

    c1 = c2 = ' '
    for i in range(nbLig):
        if debut == 1:
            print(c1 + '_', end='')
        prem = ''
        for j in range(debut, nbCol, 2):
            print(prem + '/' + str(getValGH(grille, i, j)) + '\\', end='')
            prem = '_'
        if j != nbCol - 1:
            print('_' + c2)
        else:
            print()
        c1 = '\\'
        c2 = '/'
        debut = (debut + 1) % 2
    if debut == 1:
        print('\\', end='')
        debut = 0
    else:
        print('  \\', end='')
        debut = 1
    for j in range(debut, getNbColGH(grille) - 2, 2):
        print('_/ \\', end='')
    print('_/')


# tests-------------------------------------------------
if __name__ == '__main__':

    print('TEST des fonctions de grille.py : ')
    l_grille=[GrilleHexa(10,10,True), GrilleHexa(10,10,False), GrilleHexa(9,10, True), GrilleHexa(9,10, False), GrilleHexa(10,9, True),GrilleHexa(10,9, False)]
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')
    for even_grid in l_grille:
        even_grid = GrilleHexa(10, 10, True, None)
        initAlphaGH(even_grid)
        afficheGH(even_grid)

        print('getNbLigGH() : ', getNbLigGH(even_grid))
        print('getNbColGH() : ', getNbColGH(even_grid))
        print('estPaireGH() : ', estPaireGH(even_grid))

        for x in range(getNbLigGH(even_grid)):
            for y in range(getNbColGH(even_grid)):
                print('________________________________________________________________________________ ')
                print('COORDS : ', (x, y))
                print('estPosGH() : ', estPosGH(even_grid, x, y))
                print('getValGH() : ', getValGH(even_grid, x, y))

                for dir in ['N', 'S', 'O', 'E', 'NE', 'NO', 'SE', 'SO', 'X']:
                    print('incDirectionGH() : ', incDirectionGH(dir), 'direction : ', dir)
                    print('getNPProchains() : ', getNProchainsGH(even_grid, x, y, dir))

                print('setValGH() : ', setValGH(even_grid, x, y, "$"))
                print('POST SET getValGH() : ', getValGH(even_grid, x, y))

        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ')
