marksheet=[] 
scorelist=[]

for _ in range(int(input())):
    name = input()
    score = float(input())
    marksheet+=[[name,score]]
    scorelist+=[score]

scorelist = list(dict.fromkeys(scorelist))
b=sorted(scorelist, reverse=True)[1] 

for a,c in marksheet:
    if c==b:
        print(a)