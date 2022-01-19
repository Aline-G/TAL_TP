import nltk
from nltk.tokenize import word_tokenize
import numpy as np

############## Question 1 ###############

fileIn = "wsj_0010_sample.txt"
fileOut = "wsj_0010_sample.txt.pos.nltk"

# Ouvrir le fichier en lecture seule
file = open(fileIn, "r")
for line in file:
    
    text = word_tokenize(line)
   
    tokens_tag = nltk.pos_tag(text)
       
file.close()

fileO = open(fileOut, "w")
for pair in tokens_tag :
    for elt in pair:
        fileO.write(elt+'\t')
        
    fileO.write('\n')
fileO.close()



############## Question 2 ###############
# python evaluate.py wsj_0010_sample.txt.pos.nltk wsj_0010_sample.pos.ref



