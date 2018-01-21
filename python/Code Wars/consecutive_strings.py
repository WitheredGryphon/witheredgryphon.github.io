'''
You are given an array strarr of strings and an integer k. 
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
'''

def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0: return ""
    strMax = {'word': "", 'len': 0}
    for i in range(0, len(strarr) - k + 1):
        words = ''.join(strarr[i:i+k])
        strLen = len(words)
        if strLen > strMax['len']:
            strMax['word'] = words
            strMax['len'] = strLen
    return strMax.get('word')