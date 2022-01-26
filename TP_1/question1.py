import nltk
from nltk.tokenize import word_tokenize


############## Question 1 ###############

fileIn = "wsj_0010_sample.txt"
fileOut = "wsj_0010_sample.txt.pos.nltk"

# Ouvrir le fichier en lecture seule
file = open(fileIn, "r")
fileO = open(fileOut, "w")
for line in file:
    
    text = word_tokenize(line)
   
    tokens_tag = nltk.pos_tag(text)
    
    for pair in tokens_tag :
        fileO.write('\t'.join(pair))  
        fileO.write('\n')
fileO.close()
file.close()   





############## Question 2 ###############
# python evaluate.py wsj_0010_sample.txt.pos.nltk wsj_0010_sample.pos.ref



