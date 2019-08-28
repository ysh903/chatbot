"""
request를 통해 동행복권 api 요청을 보내어
1등 번호를 가져와 파이썬 리스트로 만듦. 
"""

import requests

# 1. requests 통해 요청 보내기
url="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873"
response = requests.get(url)
res_dict=response.json()
print(res_dict)
result = []
# result.append(res_dict['drwtNo1'])


for i in range(6):
    result.append(res_dict[f'drwtNo{i+1}'])
print(result)