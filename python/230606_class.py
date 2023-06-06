class Calculator():
    value = 0
    def __init__(self):
        self.value = 100
    def sub(self, value):
        self.value -= value

class MinLimitCalculator(Calculator):
    def sub(self,value):
        if self.value > value:
            self.value -= value
        else:
            self.value = 0

class MinLimitCalculator2(Calculator):
    def sub(self,value):
        super().sub(value) # 부모의 sub 함수를 실행하겠다
        if self.value < 0:
            self.value = 0

cal = MinLimitCalculator()
cal.sub(20)
print(cal.value)
cal.sub(90)
print(cal.value)

cal2 = MinLimitCalculator2()
cal2.sub(20)
print(cal2.value)
cal2.sub(90)
print(cal2.value)


'''
class Family:
    def __init__(self):
        self.lname = "김"
        
    def getLName(self):
        print(self.lname)
    def getTest(self):
        print('test 함수입니다.')

class Person(Family):
    def __init__(self, name):
        super().__init__()
        self.fname = name
    def getTest(self):
        print('자식의 test 함수')
    def getWholeName(self):
        print(self.lname + self.fname)
        

person1 = Person('규리')
person1.getWholeName()
person1.getTest()
person2 = Person('철수')
person2.getWholeName()

class Supermarket:
    location = ""
    name = ""
    product = []
    customer = 0
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def print_location(self):
        print(self.location)
        
    def change_category(self, product):
        self.product = product

    def show_list(self):
        print(self.product)

    def enter_customer(self):
        self.customer += 1
        
    def show_info(self):
        print('이름 : ', self.name)
        print('위치 : ', self.location)
        print('물품 : ', self.product)
        print('손님수 : ', self.customer)


s1 = Supermarket('은평구','가게1',['커피, 초콜릿'],0)
s1.print_location()
s1.change_category(['물'])
s1.show_list()
s1.enter_customer()
s1.enter_customer()
s1.enter_customer()
s1.enter_customer()
s1.show_info()

class Calc:
    num1 = 0
    num2 = 0
    result = []

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
        self.result = []
    def add(self, a1, b1):
        a = a1 + b1
        self.result.append(a)
        print(a)
    def getResult(self):
        print(self.result)

calc1 = Calc(5, 3)

calc1.add(1,1)
calc1.add(2,2)
calc1.add(3,3)
calc1.getResult()
calc2 = Calc(1,1)

calc2.add(10,10)
calc2.add(20,20)
calc2.add(30,30)
calc2.getResult()

class Movie:
    title = ""
    audience = 0
    count = 0

    def __init__(self, title, audience):
        self.title = title
        self.audience = audience
        Movie.count += 1

movie = Movie("BossBaby", 100)
print(movie.count)
movie2 = Movie("BossBaby2", 200)
print(movie2.count)
print('-----')

print(movie.title)
print(movie.count)
print(movie2.title)
print(movie2.count)
print(Movie.count)

print(id(movie))
print(id(movie2))



class Movie: # 클래스(틀)을 정의
    title = 'BossBaby'
    actor = ''

    def __init__(self, actor2):
        #(2) 클래스를 호출한다 = 생성자를 실행한다. = __init__을 실행한다.
        # (2) 클래스의 함수들은 무조건 self가 있어야 하고
        # (2) 전달받은 값은 actor2라는 변수에 들어온다.
        print('Movie 클래스를 호출했습니다.')
        self.actor = actor2
        # self는 클래스 자체.
        #즉, self.actor는 클래스에 존재하는 필드(클래스의 변수)

    def modify(self, title2):
        self.title = title2
        
    def getActor(self): # (3) 함수 실행
        print(self.actor)

movie1 = Movie('a') # 클래스를 호출한다. 호출하면서 a를 보내 (1)
movie1.getActor() # Movie클래스를 이용해 만들어진 movie1객체.
#그 안의 getActor 함수를 실행(3)

movie2 = Movie('b')
movie2.getActor()

movie2.modify('name')
# movie 클래스를 이용해서 만들어진 movie2 객체에 있는 함수를 실행한다.
print(movie1.title) 
print(movie2.title)

class Car:
    window = 4

    
'''
