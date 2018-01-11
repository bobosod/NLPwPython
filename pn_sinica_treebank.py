<<<<<<< HEAD
import nltk
from nltk.corpus import sinica_treebank
# Sinica（中央研究院）提供的繁体中文语料库
print(sinica_treebank.words())
sinica_treebank.parsed_sents()[33].draw()

sinica_text=nltk.Text(sinica_treebank.words())
=======
import nltk
from nltk.corpus import sinica_treebank
# Sinica（中央研究院）提供的繁体中文语料库
print(sinica_treebank.words())
sinica_treebank.parsed_sents()[33].draw()

sinica_text=nltk.Text(sinica_treebank.words())
>>>>>>> b368d82776e5016ee39e85b5721af5a6925544a1
print(sinica_text.concordance('我'))