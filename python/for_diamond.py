l = int(input("다이아몬드 길이(2~30)를 입력하세요 : "))

for a in range(1, l+1):
    print(" " * (l - a ) + "*" * (2*a-1))

for a in range(l-1, 0, -1):
    print(" " * (l-a) + "*" * (2*a-1))


