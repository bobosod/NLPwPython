import nltk
from urllib.request import urlopen


# 处理HTML
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()
print(html[:60])

# 清理html
raw = nltk.clean_html(html)
tokens = nltk.word_tokenize(raw)
print(tokens)