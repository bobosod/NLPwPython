from nltk.corpus import reuters

# 路透社语料库
# 文档分成 90 个主题，按照“训练”和“测试”分为两组。
print(reuters.fileids())
print(reuters.categories())
print(reuters.fileids('barley'))