<<<<<<< HEAD
from nltk.corpus import reuters

# 路透社语料库
# 文档分成 90 个主题，按照“训练”和“测试”分为两组。
print(reuters.fileids())
print(reuters.categories())
=======
from nltk.corpus import reuters

# 路透社语料库
# 文档分成 90 个主题，按照“训练”和“测试”分为两组。
print(reuters.fileids())
print(reuters.categories())
>>>>>>> b368d82776e5016ee39e85b5721af5a6925544a1
print(reuters.fileids('barley'))