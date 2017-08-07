from gensim.models import word2vec
from gensim import models
import logging

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = models.Word2Vec.load('med250.model.bin')


    tags = []
    with open('tag_721.csv', 'r') as f:
        for tag in f.readlines():
            tags.append(tag.strip())

    i = 0
    while i < len(tags):
        try:
            query = tags[i]
            res = model.most_similar(query, topn=8)
            items = []
            for item in res:
                if item[1] > 0.8:
                    items.append(item[0])

            j = i + 1
            while j < len(tags):
                if tags[j] in items:
                    with open('removed.txt', 'a') as f:
                        f.write("%s-%s\n" % (tags[i], tags[j]))
                    tags.remove(tags[j])
                else:
                    j += 1
            i += 1
        except KeyError:
            tags.remove(tags[i])

    with open('new_tag.csv', 'w') as f:
        for tag in tags:
            f.write(tag+"\n")

if __name__ == "__main__":
    main()
