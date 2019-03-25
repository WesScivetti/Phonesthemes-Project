""" Wesley Scivetti
    Phonestheme Investigation
    Purpose : find phonestheme types in BNC, use word embeddings to calculate semantic cohesion of each
"""
import spacy
from spacy.vocab import Vocab
import nltk
from nltk.corpus.reader.bnc import BNCCorpusReader


bnc_reader = BNCCorpusReader(root="BNC/2554/download/Texts",fileids=r'[A-K]/\w*/\w*\.xml') #reading in all files from BNC
print("1")
allsents = bnc_reader.sents(strip_space=True,stem=False) #creating list of all BNC sentences
initialphonesthemelist = ['bl','cl','cr','dr','fl','gl','gr','sc','sk','scr','sl','sm','sn','sp','spl','spr','squ','st','str','sw','tr','tw','wr','kn']#compiled from Otis and Sagi 2008
finalphonesthemelist = ['ack','am','amp','ap','ash','asp','awl','ick','inge','ip','irl','url','ng','nk','oil','olt','oop','ouch','owl','sk','ump','ust','ign'] #from Otis and Sagi 2008
phonestheme_examples_dictionary = {} #this dictionary will house all examples of phonesthemes. Key is phonestheme str representation, value is list of words as strings
for i in initialphonesthemelist:
    phonestheme_examples_dictionary[i] = []
for j in finalphonesthemelist:
    phonestheme_examples_dictionary[j] = []
for sent in allsents[0:3000]:
    for word in sent:
        newword = word.lower()
        print(newword)
        lenWord = len(newword)
        for phonestheme in initialphonesthemelist:
            #print(phonestheme)

            lenPhon = len(phonestheme)
            print(newword[:(lenPhon)])
            if lenPhon > lenWord:
               print("too short!")
            elif lenPhon <= lenWord:
                if phonestheme == newword[:(lenPhon)]:
                        print("FOUND ONE!!!")
                        if newword not in phonestheme_examples_dictionary[phonestheme]:
                            phonestheme_examples_dictionary[phonestheme].append(newword)

                else:
                    print("not a match!")
       # print("next word!")
   # print("moving on!")

print(phonestheme_examples_dictionary)



nlpsm = spacy.load('en_core_web_sm')

nlplg = spacy.load('en_core_web_lg')

print("MODEL LOADED")

vocab = Vocab(nlplg)
vectorsdictionary = {} #a dictionary with keys as phonesthemes, value is dictionary which uses keys for each example word and value as the corresponding vector


for phonestheme in phonestheme_examples_dictionary:
    vectorsdictionary[phonestheme] = {}
    examplelist = phonestheme_examples_dictionary[phonestheme]
    for word in examplelist:
        processedword = nlplg(word)
        print("word analyzed!")
        if processedword.has_vector == True:
            vectorsdictionary[phonestheme][word] = processedword.vector
            print("vector added!")


print(phonestheme_examples_dictionary['gl'])