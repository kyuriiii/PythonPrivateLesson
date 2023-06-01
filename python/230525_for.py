'''
list = [1,2,3,4,5]

for i in list:
    print(i)

a = input("숫자를 입력해라.")

b=0

for i in range(1,int(a)+1):
    b = b+i

print(f"결과는 {b}")

# b = 0+1
# b = 1+2
# b = 3+3
# b = 3+4


a = int(input("몇 초 후에 발사할까요?"))

for i in range(a,0,-1):
    print(f"{i}초")
print('발사')
    
a = int(input("몇 단을 출력할까요?"))

for i in range(1, 10):
    print(f"{a} * {i} = {a*i}")



for x in range(1,4): # 1 2 3 
    for y in range(1,3):# 1 2 
        print(f"{x} * {y} = {x*y}")

# 1 2 3 1 2 

a = 1
while a < 10:
    a = a + 1
    if a == 5:
        continue
    print(a)

a = int(input("몇 줄을 출력할까요?"))

for i in range(1, a+1):
    print('*'*i)

    

for i in range(1,a+1):
    print(' '*(a-i) + '*'*i)


    

for i in range(1, a+1):
    print(" "*(a-i) + '*'*(2*i-1))
a = input('여러 개의 숫자를 입력해주세요.')
b = a.split()

array = []

for c in b:
    array.append(int(c))
print(array)

maxValue = max(array)
minValue = min(array)
print("가장 큰 값 : ", maxValue)
print("가장 작은 값 : ", minValue)

array.remove(maxValue)
array.remove(minValue)
print(array)

average = sum(array) / len(array)
print("평균 : ",average)

''' 


sum = 0
for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    sum = sum + i
print(f"결과는 {sum}")




