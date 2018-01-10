import nltk
print(nltk.corpus.gutenberg.fileids())
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
print(emma.concordance("surprize"))

from nltk.corpus import gutenberg
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
print(int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid)

# 网络和聊天文本
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65], '...')

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(chatroom[123])

