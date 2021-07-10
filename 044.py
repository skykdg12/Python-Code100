n = list(map(int, input())) # map함수를 통해 입력값을 int로 지정하고 list에 저장
result = 0 # 초기 결과값 지정
for i in n: 
    result += i 

print(result)