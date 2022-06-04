import json
from difflib import get_close_matches as dl


jf = json.load(open("data1.json"))


x=input("What u want?  :")

def data (d):
    d=d.lower()
    if d in jf:
     return jf [d] 
    elif len( dl (d,jf.keys()) )> 0:
        choise=input("Did you mean %s, Enter (y) for yes & no for (n) :" %dl (d,jf.keys()) [0]);
        if choise== "y" or "Y":
            return jf [dl (d,jf.keys()) [0]]
        elif choise == "n" or "N":
             return "The word does not exist"
        else: 
          return "You entered the wrong choise !"
    else:
        return 'Word is not exist'
    
ans = (data(x))

if  type(ans)==list:
    for i in ans:
        print(i)
else:
    print(ans)