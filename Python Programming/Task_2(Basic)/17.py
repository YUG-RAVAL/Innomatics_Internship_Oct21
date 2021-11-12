from collections import Counter

n = int(input())
rooms = [int(x) for x in input().split()]
cnt = Counter(rooms)

for k,v in cnt.items():
    if v == 1:
        print(k)
        break