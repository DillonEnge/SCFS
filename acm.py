import random, json
alphabet={
    'vowels' : [
        ['i','i'],
        ['u','u'], 
        ['ɛ','e'], 
        ['ɑ','a'], 
        ['o','o']
    ], 
    'consonants' : [
        ['p', 'p'], 
        ['b', 'b'], 
        ['t', 't'], 
        ['d', 'd'], 
        ['k', 'k'], 
        ['g', 'g'], 
        ['n', 'n'], 
        ['m', 'm'], 
        ['ɾ', 'r'], 
        ['s', 's'], 
        ['st', 'st'], 
        ['sp', 'sp'], 
        ['sk', 'sk'], 
        ['z', 'z'], 
        ['ʃ', 'sh'], 
        ['ʒ', 'zh'], 
        ['h', 'h'], 
        ['t͡s', 'ts'], 
        ['t͡ʃ', 'ch'], 
        ['d͡z', 'dz'], 
        ['d͡ʒ', 'j']
    ]
}
with open('vocablist.json') as f:
    vocablist=json.load(f)
dictionary={}
for words in vocablist:
    x=random.choice(alphabet['consonants'])[1]+random.choice(alphabet['vowels'])[1]+random.choice(alphabet['consonants'])[1]
    dictionary[words[0]]= x
    dictionary[words[1]]= x+'i'
    dictionary[words[2]]= x+'on'

for vals in sorted(dictionary.items(),key=lambda x: x[1]):
    print("%s: %s" % (vals[1],vals[0]))