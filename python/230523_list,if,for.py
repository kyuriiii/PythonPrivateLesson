'''
# 02_다양한 자료형 실습1
rainbow=['red','orange','yellow','green','blue','indigo','purple']

print('(1) ',end='')
print(rainbow[2])
print('(2) ',end='')
rainbow.sort()
print(rainbow)
print('(3) ',end='')
rainbow.append('pink')
print(rainbow)
print('(4) ',end='')
del rainbow[3:]
print(rainbow)


t = (1,2,3)
print(t)


a = {'name':'kim', 'name':'lee'}
print('name' in a ) # yes
print('age' in a)# no
# True False : boolean 자료형

name='1'
print('안녕 {name}')

print(f'안녕{name}')

ulist = [1,2,3,4,5,6,7,8,9,10]
print("홀수:", list[1:len(list)])
print("홀수:", list[1:len(list):2])
'''


list = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']

a = input('마시고 싶은 음료? ')

if list.count(a) == 0:
    print(a +'는 지금 없네요')
else:
    print(a +'드릴게요')
