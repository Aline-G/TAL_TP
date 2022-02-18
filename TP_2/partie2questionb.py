
# Faire une sorte de hasmap on le remplit en parcourant le texte
# la clé de la hashmap est le nom de l'entité nommée
# un fois le tableau rempli avec toutes les données on les écrit proprement dans un fichier texte

fileIn = "formal-tst.NE.key.04oct95_small.txt.ne.stanford"
fileOut = "res_partie2_question2b"

def createhash(fileIn, fileOut):
    fileI = open(fileIn,'r')
    fileO = open(fileOut,'w')

    my_dico = {}
    compteur = 0
    for line in fileI:
        tuples = line.split()
        for token in tuples:
            #compte le nombre de mots dans le texte
            compteur = compteur+1
            checkTag = 0
            word = ''
            etiquette = ""
            # séparer le mot de son étiquette
            for letter in token:
                if(letter == "/"):
                    checkTag = 1
                if(checkTag == 1 and letter != "/"):
                    etiquette = etiquette + letter
                if(letter != "/" and checkTag == 0):
                    word = word + letter
            # On vérifie que le mot existe déjà dans le dico
            if(word in my_dico):
                my_dico[word] = [etiquette, my_dico[word][1]+1, my_dico[word][1]+1]
                
            else:
                my_dico[word] = [etiquette, 1, 1]
    fileI.close()
    # Pensez à diviser la "Proportion dans le texte" par le compteur
    print(my_dico)
    #ecrire dans le fichier texte fileO le dictionnare
    



createhash(fileIn, fileOut)



