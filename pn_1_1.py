<<<<<<< HEAD
from __future__ import division # 确保使用的是浮点除法
import nltk
from nltk.book import *
import matplotlib
print(len(text3))
print(text5.count("lol"))
print(100*text5.count("lol")/len(text5))
print(sent2)
fdist1 = FreqDist(text1)
vocabulary1 = fdist1.keys()
fdist1.plot(50, cumulative=True)
=======
from __future__ import division # 确保使用的是浮点除法
import nltk
from nltk.book import *
import matplotlib
print(len(text3))
print(text5.count("lol"))
print(100*text5.count("lol")/len(text5))
print(sent2)
fdist1 = FreqDist(text1)
vocabulary1 = fdist1.keys()
fdist1.plot(50, cumulative=True)
>>>>>>> b368d82776e5016ee39e85b5721af5a6925544a1
print(fdist1.hapaxes())