from collections import OrderedDict

od = OrderedDict()
N = int(input())

for _ in range(N):
    *name, price = input().split()
    name = ' '.join(name)
    if od.get(name):
        od[name] += int(price)
    else:
        od[name] = int(price)

[print(name, price) for name, price in od.items()]
