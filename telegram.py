"""
python으로 telegram message 보내기
"""
import requests

# getUpdates를 통해 chat_id 사용
url2='https://api.telegram.org/bot{token}/getUpdates'
response = requests.get(url2)
res_dict = response.json()
#print(res_dict['result']['message']['chat']['id'])

#print(res_dict['result'][0]['message']['chat']['id'])
chat_id=str(res_dict['result'][0]['message']['chat']['id'])
#print(chat_id)
 
token='token'
base_url='https://api.telegram.org/bot'
method='/sendMessage?chat_id='
message='&text=python!'
url = base_url+token+method+chat_id+message
#requests.get('https://api.telegram.org/bot{token}/sendMessage?chat_id=981497753&text=hi!')
requests.get(url)
print(url)


"""
token='token'
base_url='https://api.telegram.org/'
url = f'{base_url}bot{token}/getUpdates'
res=requests.get(url)
res_dict=res.json()
chat_id=res_dict['result'][0]['message']['chat']['id']
msg='자동화'
url = f'{base_url}bot{token}/getMessage?chat_id={chat_id}&text={msg}'
requests.get(url)
"""







