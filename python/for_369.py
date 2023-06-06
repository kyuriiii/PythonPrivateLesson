num = int(input("숫자를 입력해라.")) # 25
count = 0

for i in range(1, num+1):
    # 1. 숫자를 문자로 바꾸고 그 문자를 자를거야 ( 23을 입력했으면 "2" "3" )
    number = str(i) # "23"
    game = list(number) # ["3", "3"]

    for a in range(0, len(game)): # a=1, game[a] = 3
        if "3" == game[a]:
            count += 1
        elif "6" == game[a]:
            count = count+1
        elif "9" == game[a]:
            count = count+1


print( count )


# for ( var i = 1; i < num+1; i++ )
