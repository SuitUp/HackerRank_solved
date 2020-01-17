n = int(input())
tmp = {}
unique = 0

for i in range(n):
    word = input()
    if word not in tmp:
        tmp[word] = 1
        unique += 1
        
    else:
        tmp[word] += 1

print(unique)

for i in tmp:
    print(tmp[i], end=" ")