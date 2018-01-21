'''
Given an array containing a list of good foods, return a string containing the assertion that any two of the individually good foods are really good when combined.

eg: "You know what's actually really good? Pancakes and relish."

Examples:

Good_foods = ["Ice cream", "Ham", "Relish", "Pancakes", "Ketchup", "Cheese", "Eggs", "Cupcakes", "Sour cream", "Hot chocolate", "Avocado", "Skittles"]

actually_really_good( Good_foods ) #  "You know what's actually really good? Pancakes and relish."

actually_really_good( ['Peanut butter'] ) #  "You know what's actually really good? Peanut butter and more peanut butter."

actually_really_good( [] ) #  "You know what's actually really good? Nothing!"

Notes: 

There are many different valid combinations of 2 foods it doesn't matter which one you choose.
But there should be 2 different foods listed unless there was only one food given in the input array.
Capitalization should be correct, the first given food should be capitalized, but the second should not.
The input array should not be modified by the method. 
'''

def actually_really_good(foods):
    if len(foods) > 1:
        return "You know what's actually really good? " + foods[0].capitalize() + " and " + foods[1].lower() + "."
    elif len(foods) == 1:
        return "You know what's actually really good? " + foods[0].capitalize() + " and more " + foods[0].lower() + "."
    else:
        return "You know what's actually really good? Nothing!"