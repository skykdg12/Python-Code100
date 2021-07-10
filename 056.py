nationWidth = {'korea':220877,
                'rusia':17098242,
                'china':9596961,
                'france':543965,
                'japan':377915,
                'england':242900}

w = nationWidth['korea'] # w값 지정
nationWidth.pop('korea') # 기존 값중 korea값 삭제
l = list(nationWidth.items()) # 삭제된 korea값을 제외한 나머지 리스트로 작성
gap = max(nationWidth.values()) # 최대값
item = 0

for i in l: 
    if gap > abs(i[1] - w): # 최대값이 korea값을 제외한 것중 최소값에서 korea값을 뺀 값보다 크다면
        gap = abs(i[1] - w) # 그 값을 최대값으로 함
        item = i 


print(item[0], gap)
