a = input().split()
b = input().split()
c = []
count = 0

for i, j in zip(a, b):
    if count % 2 == 0:
        c.append([i, j])
    else:
        c.append([j, i])
    count += 1

print(c)