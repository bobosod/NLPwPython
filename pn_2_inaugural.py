<<<<<<< HEAD
import nltk
from nltk.corpus import inaugural
# 就职演说语料库

print(inaugural.fileids())
print([fileid[:4] for fileid in inaugural.fileids()])

cfd = nltk.ConditionalFreqDist((target, fileid[:4]) for fileid in inaugural.fileids() for w in inaugural.words(fileid) for target in ['america', 'citizen'] if w.lower().startswith(target))
=======
import nltk
from nltk.corpus import inaugural
# 就职演说语料库

print(inaugural.fileids())
print([fileid[:4] for fileid in inaugural.fileids()])

cfd = nltk.ConditionalFreqDist((target, fileid[:4]) for fileid in inaugural.fileids() for w in inaugural.words(fileid) for target in ['america', 'citizen'] if w.lower().startswith(target))
>>>>>>> b368d82776e5016ee39e85b5721af5a6925544a1
cfd.plot()