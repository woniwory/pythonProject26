n = int(input())
tmp= 0
result = 0
tip = []


for _ in range(n):
    tip.append(int(input()))

tip = sorted(tip, reverse=True)

for i in range(len(tip)):
    tmp = tip[i] - ( (i+1) -1)
    if tmp < 0:
        tmp = 0
    result += tmp

print(result)