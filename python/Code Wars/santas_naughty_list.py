'''
Christmas is comming, and Santa has a long list to go through, 
to find who deserves presents for the big day. 

Go through a list of children, 
and return a list containing every child who appeared on Santa's list. 

Do not add any child more than once. Output should be sorted. For java, use Lists.

Comparison should be case sensitive, and the returned list return only one copy of each name. 
"Sam" and "sam" is allowed, but "sAm" and "sAm" is not.
'''

def find_children(santas_list, children):
    return sorted(set(santas_list).intersection(children))