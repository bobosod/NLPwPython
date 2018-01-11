# 斯瓦迪士核心词列表
from nltk.corpus import swadesh
print(swadesh.fileids())
print(swadesh.words('en'))

# entries()方法中指定一个语言链表来访问多语言中的同源词
fr2en = swadesh.entries(['fr', 'en'])
print(fr2en)