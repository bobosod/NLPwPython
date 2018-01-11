import nltk
entries = nltk.corpus.cmudict.entries()
print(len(entries))
for entry in entries[39943:39951]:
    print(entry)

for word, pron in entries:
    if len(pron) == 3:
        ph1, ph2, ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print(word, ph2)