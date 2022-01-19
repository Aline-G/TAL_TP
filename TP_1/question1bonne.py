import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser


file_in = "wsj_0010_sample.txt"
file_out = "wsj_0010_sample.txt.pos.nltk"


print("file_in :" , file_in, "& file_out :", file_out)

f1 = open(file_in, "r")
f2 = open(file_out, "w") 
line_pos_tag = []
for line in f1 :
    line_pos_tag = pos_tag((word_tokenize(line)))
    for word in line_pos_tag : 
        f2.write('\t'.join(word))
        f2.write('\n')