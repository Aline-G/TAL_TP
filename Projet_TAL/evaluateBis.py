#****************************************************************
#
# evaluate.py - the evaluation program.
#
# Author: Yue Zhang
#
# Computing lab, University of Oxford. 2006.11
#
#****************************************************************

#================================================================
#
# Import modules.
#
#================================================================

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "libs")))
import getopt

#================================================================
#
# Main.
#
#================================================================

if __name__ == '__main__':
   #
   # Parse command ......
   #
   opts, args = getopt.getopt(sys.argv[1:], "")
   for opt in opts:
      print(opt)
   if len(args) != 2:
      print(g_sInformation)
      sys.exit(1)
   sCandidate = args[0]
   sReference = args[1]



   #
   # Compare candidate and reference
   #
   nTotalCorrectWords = 0
   nTotalCorrectTags = 0
   nCandidateWords = 0
   nReferenceWords = 0

   first = True


   fileCandidate = open(sCandidate, 'r')

   # Pour chaque ligne du fichier candidat on parcourt le fichier de reference
   # Si la ligne candidate corespond a la ligne de reference alors on incremente les valeurs de mot corectq et de Tag corects
   for line in fileCandidate:
       tupCandidate = line.split("\t")
       wordCandiate = tupCandidate[0]
       TagCandidate = tupCandidate[1].replace("\n","").replace(" ","")
       nCandidateWords = nCandidateWords + 1
       fileRef = open(sReference, 'r')
       for lineRef in fileRef:
           if(first == True):
               nReferenceWords = nReferenceWords+1
           ref = lineRef.replace("\t","").replace(" ","")
           candidat = line.replace("\t","").replace(" ","")
           if (ref == candidat):
               nTotalCorrectWords = nTotalCorrectWords + 1
               nTotalCorrectTags = nTotalCorrectTags + 1
               fileRef.close()
               first = False
               break
           
   fileCandidate.close()
   fileRef.close()






   word_precision = float(nTotalCorrectWords) / float(nCandidateWords)
   word_recall = float(nTotalCorrectWords) / float(nReferenceWords)
   tag_precision = float(nTotalCorrectTags) / float(nCandidateWords)
   tag_recall = float(nTotalCorrectTags) / float(nReferenceWords)
   word_fmeasure = (2 * word_precision * word_recall) / (word_precision + word_recall)
   if tag_precision + tag_recall == 0:
       tag_fmeasure = 0.0
   else:
       tag_fmeasure = (2 * tag_precision * tag_recall) / (tag_precision + tag_recall)



   print("Word precision:", word_precision)
   print("Word recall:", word_recall)

   print("Tag precision:", tag_precision)
   print("Tag recall:", tag_recall)

   print("Word F-measure:", word_fmeasure)
   print("Tag F-measure:", tag_fmeasure)
