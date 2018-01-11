from nltk.corpus import wordnet as wn
print(wn.synsets('motorcar'))
print(type(wn.synset('car.n.01').lemma_names))
print(wn.synset('tree.n.01').part_meronyms())
print(wn.synset('walk.v.01').entailments())
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
print(types_of_motorcar[26])
print(wn.synset('baleen_whale.n.01').min_depth())

right = wn.synset('right_whale.n.01')
minke = wn.synset('minke_whale.n.01')
print(right.path_similarity(minke))