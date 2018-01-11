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

syllable = ['N', 'IH0', 'K', 'S']
print([word for word, pron in entries if pron[-4:] == syllable])
print([w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n'])

def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]

print([w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']])
print([w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']])