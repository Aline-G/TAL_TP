
fileIn = open("wsj_0010_sample.txt.pos.stanford", "r")
fileInRef = open("wsj_0010_sample.pos.stanford.ref", "r")
fileTag = open("POSTags_PTB_Universal.txt", "r")
fileOut = open("wsj_0010_sample.txt.pos.univ.stanford","w")
fileOutRef = open("wsj_0010_sample.txt.pos.univ.ref","w")


my_dico = {}

#on crée un dictionnaire à partir des tag de reference
for line in fileTag:
    tuples = line.split()
    my_dico[tuples[0]] = tuples[1]
fileTag.close()

def traitement(fileI, fileO, dico):
    checkTag = 0
    w = ''
    for l in fileI:
        tup = l.split()
        for word in tup:
            for letter in word:
                print(letter)
                if(letter == "_"):
                    fileO.write("\t")
                    checkTag = 1
                if(checkTag == 1 and letter != "_"):
                    w = w+letter
                if(letter != "_" and checkTag == 0):
                    fileO.write(letter)
            fileO.write(" "+dico[w]+" ")
            fileO.write('\n')
            checkTag = 0
            w = ''
    fileI.close()
    fileO.close()

traitement(fileIn, fileOut, my_dico)
traitement(fileInRef,fileOutRef, my_dico)

