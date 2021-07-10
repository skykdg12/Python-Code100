total = 0
count = 0
limit = int(input("제한 무게 :"))
n = int(input("탑승 인원 :"))

for i in range(n):
    total += int(input('몸무게를 입력해주세요 : '))
    if total <= limit:
        count += 1

print(count)