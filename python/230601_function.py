'''
a = [1,2,3,4,5]

print(len(a))


def length(b):
    count = 0
    for i in b:
        count +=1
    return count
print(length())
n = input('이름을 입력해주세요')
def test(name):
    return "안녕하세요 " + name
print(test(n))

1. 시간과 요금 입력받기
2. 시간이 15 초과면 시간 * 요금 * 1.5 return
3. 시간이 15 이하면 시간 * 요금 return
4. 출력해라

enter_hour = int(input('주차 시간 : '))
enter_rate = int(input('시간 당 요금 : '))


def parking(hour, rate):
    
    if hour > 15:
        return hour * rate * 1.5
    else:
        return hour * rate
    return (pay)

print(parking(enter_hour, enter_rate))
        '''

x = 'a'
def func():
    x = 'b'
    print('x1 : ' + x)
func()
print('x2 : ' + x)


