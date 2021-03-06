#Retrieving top Nouns and Verbs
#Author: Sanjana Pukalay


#NLTK used for Text Analytics

import os
import nltk
from nltk.corpus import wordnet as wn

#Setting path and reading data from all files in a directory and storing it in a data list

path = "/home/sanjana/Desktop/Demo/"

data = []

for filename in os.listdir(path):
    text_file = open(path + filename,"r")
    file_content = text_file.readlines()
    data.append((filename,file_content))
    text_file.close()

nouns = []
verbs = []

noun_list = []
verb_list = []

noun_lists = []
verb_lists = []

#Extracting tokens from text in the data list

for data_tuple in data:
    for text in data_tuple[1]:
        text.strip()
        text_string = str(text)
        tokens = text_string.split()
        tags = nltk.pos_tag(tokens)

#Performing POS Tagging on data
        
        for tag in tags:
            if tag[1] == "NN":
                nouns.append(tag[0])
            elif tag[1] == "VBD":
                verbs.append(tag[0])

#Extracting top 10 verbs and nouns
                
        frequent_nouns = nltk.FreqDist(nouns)
        common_nouns = frequent_nouns.most_common(10) 
        noun_lists.append(common_nouns)
        
        for noun_tuple in noun_lists:
            noun_list.append(noun_tuple[0])
            
        frequent_verbs = nltk.FreqDist(verbs)
        common_verbs = frequent_verbs.most_common(10)
        verb_lists.append(common_verbs)
        
        for verb_tuple in verb_lists:
            verb_list.append(verb_tuple[0])

print "Nouns: " + str(noun_list)
    
print "Verbs: " + str(verb_list)

eventvalue=[]
valueholder=[]

#Finding WUP Similarity

list1 = noun_list1
list2 = noun_list2

for word1 in list1:
    word1= word1+".n.01"
    word1 = wn.synset(word1)
    for word2 in list2:
        word2= word2+".n.01"
        word2 = wn.synset(word2)
        value=word1.wup_similarity(word2)
        valueholder.append(value)
    z=sum(valueholder)
    eventvalue.append(z)
print(sum(eventvalue))

#Pre-processed data used for construction of Similarity Matrix

