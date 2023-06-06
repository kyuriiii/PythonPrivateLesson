'''
import math

print(math.floor(3.9))
print(math.ceil(3.14))
print(round(3.14))
print(math.sqrt(9))
from random import randint, uniform

print(randint(1,10))
print(uniform(1,10))


import random

num_list = []
for i in range(4):
    a = random.randint(1,100)
    num_list.append(a)

num_list.sort()
print(num_list)


'''
import random

print("숫자 UP & DOWN GAME START!")
print("-"*20)

rand_num = random.randint(1, 100)
pred_num = int(input('숫자를 입력하세요'))
count = 1 # 입력 시도 횟수

while rand_num != pred_num:
    if ( pred_num > rand_num ):
        print("Down")
    else:
        print("Up")
    pred_num = int(input("숫자를 입력하세요."))
    count += 1

print(count)
print('정답')


