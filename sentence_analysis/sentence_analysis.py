# Sentence Analysis Tool
'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
'''

sentence = input("Please enter your sentence for analysis: ")
analysis = {'lower': 0, 'upper': 0, 'puncs': 0, 'chars': 0}

for i in range(0, len(sentence)):
    if sentence[i].islower():
        analysis['lower'] += 1
    elif sentence[i].isupper():
        analysis['upper'] += 1
    elif sentence[i].isspace():
        i
    else:
        analysis['puncs'] += 1

analysis['chars'] = analysis['lower'] + analysis['upper'] + analysis['puncs']
print('Lower case: ' + str(analysis['lower']))
print('Upper case: ' + str(analysis['upper']))
print('Punctuation: ' + str(analysis['puncs']))
print('Total chars: ' + str(analysis['chars']))
