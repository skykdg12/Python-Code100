data = input().split(' ')
data = [int(i) for i in data]

def sol(l):
    l = sorted(l)
    for i in range(len(l) -1 ):
        if l[i]+1 != l[i+1]:
            return 'NO'
    return 'YES'

print(sol(data))