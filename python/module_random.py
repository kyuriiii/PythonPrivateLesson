import random

correct = []
users = []

for i in range(6):
    while True:
        num = random.randint(1, 26)
        if num not in correct:
            correct.append(num)
            break
print(correct)

for i in range(6) :
    while True :
        iNum = int( input("숫자를 입력하세요 : ") )
        
        if iNum not in users :
            if 0 < iNum < 26 :
                users.append( iNum )
                break
            else :
                print( "범위에 없는 숫자입니다." )
        print( "다시 입력하세요." )
print(users)




'''

count = 0
for i in user_inputs :
    if i in correct :
        count += 1

print( "정답 번호 공개!" )
for i in correct :
    print( i, end=" " )
print( "당신의 등수는 ", 7 - count, "등입니다!" )
print( "맞힌 개수 : ", count, "개" )

'''
