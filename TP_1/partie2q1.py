import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser


############## Question 1 ###############

fileIn = "wsj_0010_sample.txt"
fileOut = "wsj_0010_sample.txt.chk.nltk"

# Ouvrir le fichier en lecture seule
file = open(fileIn, "r")
fileO = open(fileOut, "w")
for line in file:
       
    tokens = word_tokenize(line)
    print(tokens)

    tag = nltk.pos_tag(tokens)
    print(tag)
    
    grammar = "Compound: {<DT>?<JJ>*<NN>}"
    # cration des différentes grammaire pour la Q2
    grammar1 = "Compound: {<JJ>*<NN>}"
    grammar2 = "Compound: {<NN>*<NN>}"
    grammar3 = "Compound: {<JJ>?<NN>*<NN>}"
    grammar4 = "Compound: {<JJ>?<JJ>*<NN>}"

    cp  = nltk.RegexpParser(grammar)
    result = cp.parse(tag)
    print(result)
    
    #result.draw()    # It will draw the pattern graphically which can be seen in Noun Phrase chunking 
        
    fileO.write(result)

    # for res in result :
    #     print(res)
    #     # on teste que c'est bien un tuple
    #     if(type(res) is tuple):
    #         fileO.write(res[0]+'\t'+res[1])  
    #         fileO.write('\n')
    #     else :
    #         fileO.write(res)
    #         fileO.write('\n')
fileO.close()
file.close()   