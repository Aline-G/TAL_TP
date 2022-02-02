
fileIn = "wsj_0010_sample.pos.ref"
fileOut = "wsj_0010_sample.pos.stanford.ref"

# Ouvrir le fichier en lecture seule
file = open(fileIn, "r")
fileO = open(fileOut, "w")

for line in file:
   
    tuples = line.split()
    if tuples:
        fileO.write(tuples[0]+"_"+tuples[1]+" ")
    else:
        fileO.write("\n")

file.close()
fileO.close()
