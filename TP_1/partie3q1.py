import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk


############## Question 1 ###############

fileIn = "formal-tst.NE.key.04oct95_sample.txt"
fileOut = "formal-tst.NE.key.04oct95_sample.txt.ne.nltk"

# Ouvrir le fichier en lecture seule
file = open(fileIn, "r")

fileO = open(fileOut, "w")
for line in file:
       
    tokens = word_tokenize(line)
    tag = nltk.pos_tag(tokens)
    namedEnt = nltk.ne_chunk(tag, binary=False)

    for tree in namedEnt.subtrees() :
        if tree.label() == "PERSON":
            for branch in tree:
                b1 = str(branch[0])
                fileO.write(b1+" ")
            fileO.write("PERS")
            fileO.write("\n")
        elif tree.label() == "ORGANIZATION":
            for branch in tree:
                b1 = str(branch[0])
                fileO.write(b1+" ")
            fileO.write("ORG")
            fileO.write("\n")
        elif tree.label() == "LOCATION":
            for branch in tree:
                b1 = str(branch[0])
                fileO.write(b1+" ")
            fileO.write("LOC")
            fileO.write("\n")
        elif tree.label() == "DATE":
            for branch in tree:
                b1 = str(branch[0])
                fileO.write(b1+" ")
            fileO.write("MISC")
            fileO.write("\n")
        elif tree.label() == "TIME":
            for branch in tree:
                b1 = str(branch[0])
                fileO.write(b1+" ")
            fileO.write("MISC")
            fileO.write("\n")
        elif tree.label() == "MONEY":
            for branch in tree:
                b1 = str(branch[0])
                fileO.write(b1+" ")
            fileO.write("MISC")
            fileO.write("\n")
        elif tree.label() == "PERCENT":
            for branch in tree:
                b1 = str(branch[0])
                fileO.write(b1+" ")
            fileO.write("MISC")
            fileO.write("\n")
        elif tree.label() == "FACILITY":
            for branch in tree:
                b1 = str(branch[0])
                fileO.write(b1+" ")
            fileO.write("ORG")
            fileO.write("\n")
        elif tree.label() == "GPE":
            for branch in tree:
                b1 = str(branch[0])
                fileO.write(b1+" ")
            fileO.write("LOC")
            fileO.write("\n")
fileO.close()
file.close()   
