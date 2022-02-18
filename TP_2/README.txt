TP 2
Faire la commande cd TP_2 dans le terminal pour pouvoir éxécuter toutes les commandes suivantes.

Partie I
2b) python .\question2b.py
Les résultats de cette question sont écrits dans le fichier "wsj_0010_sample.pos.stanford.ref"

2c) python evaluate.py wsj_0010_sample.txt.pos.stanford wsj_0010_sample.pos.stanford.ref
Les résultats obtenus correspondent à l'image appelée "resultats_perf_Q2_c.png"

2d) python .\question2d.py
Les résultats de cette question sont écrits dans les fichiers "wsj_0010_sample.txt.pos.univ.stanford" et "wsj_0010_sample.txt.pos.univ.ref"

2e) python evaluate.py wsj_0010_sample.txt.pos.univ.stanford wsj_0010_sample.txt.pos.univ.ref
Les résultats obtenus correspondent à l'image appelée "resultats_perf_Q2_e.png"

2f)



Partie II
2a) java -mx600m -cp stanford-ner.jar:lib*/ edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile ../formal-tst.NE.key.04oct95_small.txt > ../formal-tst.NE.key.04oct95_small.txt.ne.stanford
Les résultats de cette question sont écrits dans le fichier "formal-tst.NE.key.04oct95_small.txt.ne.stanford"

2b) python .\partie2questionb.py


