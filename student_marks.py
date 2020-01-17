# marksheet=[] 
# scorelist=[]
# m=[]
d={}
for _ in range(int(input())):
    name = input()
    score = float(input())
    # m+=[name]
    d[name]=score
    # marksheet+=[[name,score]]
    # scorelist+=[score]
# print(d)
d_sorted={k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
# print(d_sorted)
prev=-1
name_list=[]
ind=0
# print(d_sorted)
for i,j in d_sorted.items():
    if prev==-1:
        prev=j
    elif  ind==0 and prev<j:
        name_list.append(i)
        ind+=1
        prev=j
    elif ind==0 and prev==j:
        # name_list.append(i)
        # ind+=1
        continue
    elif prev==j and ind==1:
        name_list.append(i)
        # ind+=1
    elif prev<j and ind==1:
        break

    # elif ind==2:
    #     break
    
# print(name_list)
    # if jprev:
    #     name_list.append(i)
    #     prev=j
    # else:
    #     break
for i in sorted(name_list):
    print(i)
# print(scorelist)
# scorelist = list(dict.fromkeys(scorelist))
# b=sorted(scorelist, reverse=True)[1] 
# print(scorelist)



# same_name=[]
# for a,c in marksheet:
#     if c==b:
#         same_name+=[a]

# if len(same_name) > 1:
#         same_name = sorted(same_name)
#         #same_name.sort()
#         for name in same_name:
#             print(name)