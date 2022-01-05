# Gender Bias In Text Example
MALE = 'male'
FEMALE = 'female'
UNKNOWN = 'unknown'
BOTH = 'both'

MALE_WORDS = set([
    'guy', 'spokesman', 'chairman', "men's", 'men', 'him', "he's", 'his',
    'boy', 'boyfriend', 'boyfriends', 'boys', 'brother', "brother's", 'dad',
    'dads', 'dude', 'father', 'fathers', 'fiance', 'gentleman', 'gentlemen', 'god',
    'grandfather', 'grandpa', 'grandson', 'groom', 'he', 'himself', 'husband', 'husbands', 
    'king', 'male', 'man', 'mr', 'nephew', 'nephews', 'priest', 'prince', 'son', 'sons', 'uncle',
    'uncles', 'waiter', 'widower', 'widowers'
])

FEMALE_WORDS = set([
    'heroine', 'spokeswoman', 'chairwoman', "women's", 'actress', 'women',
    "she's", 'her', 'aunt', 'aunts', 'bride', 'daughter', 'daughters', 'female', 
    'fiance', 'girl', 'girlfriend', 'girlfriends', 'girls', 'goddess', 
    'granddaughter', 'grandma', 'grandmother', 'herself', 'ladies', 'lady',
    'mom', 'moms', 'mother', 'mothers', 'mrs', 'ms', 'niece', 'nieces',
    'priestess', 'princess', 'queens', 'she', 'sister', 'sisters', 'waitress',
    'widow', 'widows', 'wife', 'wives', 'woman'
])


from collections import Counter
import nltk

def genderize(words):
    ''' words is List '''
    # intersection() returns a set that contains the items that exist in both set x and set y
    mwlen = len(MALE_WORDS.intersection(words))
    fwlen = len(FEMALE_WORDS.intersection(words))

    if mwlen > 0 and fwlen == 0:
        return MALE
    elif mwlen == 0 and fwlen > 0:
        return FEMALE
    elif mwlen > 0 and fwlen > 0:
        return BOTH
    else:
        return UNKNOWN

def count_gender(sentences):
    ''' sentences is List too '''
    sents = Counter()
    words = Counter()

    for sentence in sentences:
        gender = genderize(sentence)
        sents[gender] += 1
        words[gender] += len(sentence)
    
    return sents, words

def parse_gender(text):
    ''' text = .txt file (not sure what other filetypes will work) '''
    sentences = [
        [word.lower() for word in nltk.word_tokenize(sentence)]
        for sentence in nltk.sent_tokenize(text)
    ]

    sents, words = count_gender(sentences)
    total = sum(words.values())

    for gender, count in words.items():
        
        pcent = (count / total) * 100
        nsents = sents[gender]

        print(f"{pcent}% {gender} ({nsents} sentences)")

##########################################################################
from sys import argv

script, filename = argv

target = open(filename)
article = target.read()

parse_gender(article)
