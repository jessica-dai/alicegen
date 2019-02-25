import nltk
from nltk.corpus import treebank
from nltk.tokenize import word_tokenize
import random

base = []

with open("input.txt") as f:
    for line in f:
        # remove image captions
        if (line[0] != " " or line[2] == " "):
            base.append(line) # 333 lines in my input alice


gen = nltk.text.ContextIndex([word.lower() for word in treebank.words()])
ignore = [',','!','.', ';', '\'', '?', "\'\'", '``', '`', '\"\"', "*", "*t*-1"]
newfile = open('output.txt', 'w') 

for i in range(len(base)):
    tokenized = word_tokenize(base[i])
    for j in range(len(tokenized)):
        if (tokenized[j] not in ignore):
            newfile.write(" ")

            n_to_gen = min(20, int(i/13) + 3) # randomness increases over the course of the text

            replacements = (gen.similar_words(tokenized[j], n_to_gen)) # generate similar words

            # clean replacements
            for alt in replacements:
                if alt in ignore:
                    replacements.remove(alt)
            
            random.shuffle(replacements) # shuffle replacements

            freq = j % (max(1, 5 - int(i/10))) # only replace some words

            if (len(replacements) > 0 and (freq == 0)):
                newfile.write(replacements[0])
            else:
                newfile.write(tokenized[j])
        else:
            newfile.write(tokenized[j])

    newfile.write('\n')

newfile.close()