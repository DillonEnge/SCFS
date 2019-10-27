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
vocablist=[
    ['ant', 'hardworking', 'forage'],
    ['dog', 'loyal', 'pander'],
    ['cat', 'independent', 'stalk'],
    ['cow', 'dull', 'loiter'],
    ['pig/boar', 'violent', 'trample'],
    ['chicken', 'wide-eyed', 'chirp'],
    ['bird','vibrant','fly'],
    ['turkey','moody','extend/hold out'],
    ['fish','foul-smelling','swim'],
    ['turtle','secure/protected','protect'],
    ['rabbit','fucund','multiple'],
    ['human','humane/rational','reason/think about'],
    ['sheep','furry/hairy','follow'],
    ['goat','strong-willed','ram'],
    ['camel','reliable','carry'],
    ['llama','dramatic','spit'],
    ['horse','working-class','carry'],
    ['bug/insect','pesky/annoying','bug'],
    ['here','this','return/receive'],
    ['there 2nd person','that 2nd person','give'],
    ['there 3rd person','that 3rd person','throw out/get rid of'],
    ['i','my','flow/lost in thought'],
    ['you','your','discuss'],
    ['they/her/she','their','isolate'],
    ['list','plural/many','count/list off'],
    ['walk','close','walk'],
    ['car','driving distance away','drive/guide'],
    ['ship','far away','fly(plane)/drive(non-car)'],
    ['sky','wide/spacious/open','rain'],
    ['sun','sunny/bright','burn'],
    ['moon/month','alone','record'],
]
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