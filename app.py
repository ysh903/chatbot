from flask import Flask
import random
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

# 1. 주문서를 만들고,
# 2. 해당 주문이 들어왔을 때 무엇을 할지 정의

@app.route('/name')
def name():
    return '이승희'

@app.route('/hello/<name>')
def hello(name):
    return f'hello {name}'

@app.route('/square/<int:number>')
def square(number):
    return f'result ={str(number**2)}'

@app.route('/menu')
def menu():
    foods=['바스버거','대우식당','진기와','고갯마루']
    food=random.choice(foods)
    return food

@app.route('/lotto')
def lotto():
    winner=[]
    url="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873"
    response = requests.get(url)
    res_dict=response.json()
    
    for i in range(6):
        result.append(res_dict[f'drwtNo{i+1}'])

    
    result=random.sample(range(1,46),6)

    cnt = len(set(winner)&set(result)) #교집합


    rank = '꽝'
    if cnt ==6:
        rank = '1등'
    if cnt ==5:
        rank = '3등'
    if cnt ==4:
        rank = '4등'
    if cnt ==3:
        rank = '5등'
    #만약 6개 모두 일치하면
    # -> 1등
        
    #만약 5개 모두 일치하면
    # -> 3등
       
    #만약 4개 모두 일치하면
    # -> 4등
       
    #만약 3개 모두 일치하면
    # -> 5등
        
    # sort, sorted(원본 변경 X)
    return str(sorted(result))+rank 
    


