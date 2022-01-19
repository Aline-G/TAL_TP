import nltk 


fileIn = open("wsj_0010_sample.txt.pos.nltk", "r")
fileInRef = open("wsj_0010_sample.pos.ref", "r")
fileTag = open("POSTags_PTB_Universal_Linux.txt", "r")
fileOut = open("wsj_0010_sample.txt.pos.univ.nltk","w")
fileOutRef = open("wsj_0010_sample.txt.pos.univ.ref","w")

my_dico = {}

#on crée une sorte de hashmap à partir des tag de reference
for line in fileTag:
    tuples = line.split()
    my_dico[tuples[0]] = tuples[1]
fileTag.close()
    
for l in fileIn:
    tup = l.split()
    fileOut.write(tup[0]+'\t'+my_dico[tup[1]])
    fileOut.write('\n')

for li in fileInRef:
    tup = li.split()
    #tester que le tup existe sinon pb de out of range pour tup[0]
    if tup:
        fileOutRef.write(tup[0]+'\t'+my_dico[tup[1]])
        fileOutRef.write('\n')


fileIn.close()
fileInRef.close()
fileOut.close()
fileOutRef.close()


# python evaluate.py wsj_0010_sample.txt.pos.univ.nltk wsj_0010_sample.txt.pos.univ.ref