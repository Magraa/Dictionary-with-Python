#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Magra
#
# Created:     23/05/2019
# Copyright:   (c) Magra 2019
# Licence:     Magra Inc.
#-------------------------------------------------------------------------------
# nltk lib for matching words can be use

import json

from difflib import get_close_matches

data = json.load(open("D:\Courses\Python programs\Getting started\Dictionary\data.json"))
#print(type(data))
#print(data["rain"])//magraISIS
def dict(w):

    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0 :
        cnfrm = input(f"Did you mean {get_close_matches(w, data.keys())[0]} Instead of {w} Enter Y for Yes OR N for More Suggestions")
        #cnfrm = input("Did you mean %s Instead of  Enter Y for Yes OR N for No"%get_close_matches(w, data.keys())[0])
        if cnfrm in ["Y", "y"]:
            return data[get_close_matches(w, data.keys())[0]]
        elif cnfrm in ["N", "n"]:
            print("Choose From The Following words,")

            for (i,j) in zip(get_close_matches(w, data.keys()),range(1,4)):
                print(f"for {i} Enter {j}")
            #x = input()
            x = int(input("Enter value for desire Word : "))
            #if x == i:
            if x in [1, 2, 3]:
                #return data[get_close_matches(i, data.keys())]
                return data[get_close_matches(w, data.keys())[x - 1]]
            else:
                return "Invalid Input"
    else:
        return "This Word doesn't Exist\nDouble Check it."

word = input("Enter Word :").lower()

o = dict(word)
if type(o) == list:
    for item in o :
        print(item)








