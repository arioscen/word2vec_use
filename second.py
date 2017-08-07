# -*- coding: utf-8 -*-

from gensim.models import word2vec
from gensim import models
import logging
import csv
from collections import Counter
import jieba
jieba.load_userdict('dict.txt.big')

tags = None
with open('new_tag.csv','r') as f:
    tags = f.read().split()
def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = models.Word2Vec.load('med250.model.bin')

    with open('p2004_cut.csv','r') as f:
        with open('p2004_tag.csv', 'w') as g:
            row_number = 0
            with open('p2004_cut.csv','r') as h:
                row_number = len(h.readlines())
            row_now = 0
            percent = 1
            for line in csv.reader(f):
                words = jieba.cut(line[1])
                counter_2 = Counter()
                for word in words:
                    counter_1 = Counter()
                    for tag in tags:
                        try:
                            # g.write("%s-%s" % (word, tag))
                            res = model.similarity(word,tag)
                            counter_1[tag] = res
                        except KeyError:
                            pass
                    if len(counter_1) > 0:
                        most_1 = counter_1.most_common(1)[0]
                        if counter_2[most_1[0]] < most_1[1]:
                            counter_2[most_1[0]] = most_1[1]

                row_now += 1
                if row_now / row_number >= percent / 1000:
                    print("completed : " + str(percent / 1000))
                    percent += 1

                if len(counter_2) > 0:
                    most_2 = counter_2.most_common(1)[0]
                    plu_tag = most_2[0]
                    g.write("%s,%s,%s\n" % (line[0], line[1], plu_tag))
		    
if __name__ == "__main__":
    main()


