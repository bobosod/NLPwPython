from nltk.corpus import udhr
# udh超过 300 种语言的世界人权宣言
print(udhr.fileids())
print([w for w in udhr.words('Greek_Ellinika-UTF8')[:50]])
