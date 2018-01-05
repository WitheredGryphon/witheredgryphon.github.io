'''
For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)

For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.

This kata is part of the Simple Encryption Series:
Simple Encryption #1 - Alternating Split
Simple Encryption #2 - Index-Difference
Simple Encryption #3 - Turn The Bits Around
Simple Encryption #4 - Qwerty
'''

def decrypt(encrypted_text, n):
    for i in range(0, n):
        str1 = list(map(str, encrypted_text[:len(encrypted_text)//2]))
        str2 = list(map(str, encrypted_text[len(encrypted_text)//2:]))
        c = 0
        if len(str1) > len(str2):
            while str2:
                if i%2 != 0:
                    str2.insert(c, str1[0])
                    del str1[0]
                c += 1
                str1 = ''.join(str1)
                str2 = ''.join(str2)
                encrypted_text = str1 + str2
        else:
            while str1:
                if c%2 != 0:
                    str2.insert(c, str1[0])
                    del str1[0]
                c += 1
            str1 = ''.join(str1)
            str2 = ''.join(str2)
            encrypted_text = str2 + str1
    return encrypted_text


def encrypt(text, n):
    for i in range(0, n):
        str1 = ''.join(list(i for i in text)[1::2])
        str2 = ''.join(list(i for i in text)[::2])
        text = str1 + str2
    return text