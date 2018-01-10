import nltk
from nltk.book import *
# 细粒度的选择词
V = set(text1)
long_words = [w for w in V if len(w)>15]
print(sorted(long_words))

fdist5 = FreqDist(text5)
print(sorted(w for w in set(text5) if len(w)>7 and fdist5[w]>7))

# 词语搭配和双连词
fdist1 = FreqDist([len(w) for w in text1])
print([len(w) for w in text1])
print("fdist: ", fdist1)
print(fdist1.keys())
print(fdist1.values())