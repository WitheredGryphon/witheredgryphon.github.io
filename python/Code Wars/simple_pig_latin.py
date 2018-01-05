'''
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !
'''

def pig_it(text):
    textArr = text.split()
    for i in textArr:
        if i.isalpha():
            textArr[textArr.index(i)] = ''.join(i[1:] + i[0] + "ay")
    return ' '.join(textArr)