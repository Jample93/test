# 퀴즈1
import random 
station = ('사당', '신도림' , '인천공항')

random.choice (station)
print(random.choice (station) + "행 열차가 들어오고 있습니다.") 

#####랜덤은 내가 했다 개쩐닼ㅋㅋㅋㅋㅋㅋㅋㅋ

station = "사당"
print(station+"행 열차가 들어오고 있습니다.")


# 퀴즈2

from random import *



(randrange(4,29)) #29 미만 이므로 28을 포함시키기 위해서 29로 적음

jample = (randrange(4,29))

print("오프라인 스터디 모임 날짜는 매월" + str(jample) + "일로 선정되었습니다.")
##위에는 내가 한 방식

from random import *

date = randint(4,28)

print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")


# 퀴즈3

#naver , daum , goolge 

#def site(naver, google, daum)



x = ('naver.com')

print(x[0:5])

print(x[0:2])

print(len(x[0:5]))

print(x.count('e'))


print (x[0:3] + str(len(x[0:5])) + str(x.count('e')) + '!' )

y = ('google.com')

print (y[0:3] + str(len(y[0:5])) + str(y.count('e')) + '!' )

z = ('daum')
print (z[0:3] + str(len(z[0:5])) + str(z.count('e')) + '!' )

## 해설

#url = "http://naver.com"
url = "http://google.com"
my_str = url.replace("http://", "")
print(my_str)
my_str = my_str[:my_str.index(".")] #    이 문장은  naver.com 에서 . 이 나오는 시점까지만 출력
print(my_str)
password = my_str[:3]+ str(len(my_str)) + str(my_str.count('e')) +'!'
print("{0}의 비밀번호는 {1}입니다 " .format( url,password))