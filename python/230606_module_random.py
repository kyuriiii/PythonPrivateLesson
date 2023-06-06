# 1. 사용자 입력을 다 받고 비교한다.
# 2, 입력을 받으면서 비교한다.
import random

# 랜덤 로또 정답
correct = []
for i in range(6):
    while True:
        num = random.randint(1,26)
        if num not in correct:
            correct.append(num)
            break
# 사용자 입력
users = []
for i in range(6):
    while True:
        a = int(input('숫자를 입력하세요'))

        if a not in users:
            if 0 < a < 26:
                users.append(a)
                break
            else:
                print('범위가 틀렸습니다.')
        print('다시 입력하세요.')
    # 중복된 숫자를 입력하면?
    # 1~26 이외의 숫자를 입력하면?

cnt=0
for i in users:
    if i in correct:
        cnt += 1

print(correct)
print('맞힌 개수 : ', cnt, "개")













        
