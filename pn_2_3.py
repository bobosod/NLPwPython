import nltk

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)

print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))
print(unusual_words(nltk.corpus.nps_chat.words()))

# 停用词
from nltk.corpus import stopwords
print(stopwords.words('greek'))

# 小练习
puzzle_letters = nltk.FreqDist('egivrvonl')
print([w for w in puzzle_letters])
obligatory = 'r'
wordlist = nltk.corpus.words.words()
print([w for w in wordlist if len(w)>=6
       and obligatory in w
       and nltk.FreqDist(w) <= puzzle_letters])