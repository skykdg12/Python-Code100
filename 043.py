a = input()
b = []

while a:
    b.append(str(a % 2))
    a = int(a / 2)
    
print(b)
b.reverse()
print(b)
print(''.join(b))