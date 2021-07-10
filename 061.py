data = str(input())
result = data[0] # 반복문 실행되는 동안 문자열 형태로 반환되는 결과들을 담을 변수
count = 0 # 반복되서 나오는 문자 수만큼 카운팅되는 값을 담을 변수

for i in data: 
    if i == result[-1]: # result 변수 마지막 문자와 비교
        count += 1
    else:
        result += str(count) + i # 마지막 글자와 i가 다를 경우 카운팅된 값을 문자열 형태로 result 변수마지막에 추가해주고 i를 마지막 문자로 추가
        count = 1
result += str(count) # 결과들이 담긴 변수에 마지막으로 카운팅된 값을 문자열 형태로 추가

print(result)

