vending_machine = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']

print(f"남은 음료수: {vending_machine}\n")

type = input("사용자 종류를 입력하세요. 1.소비자 2.주인")

if type == '소비자' or type=='1':
    drink = input("마시고 싶은 음료는?")

    if vending_machine.count(drink) == 0:
        print(f"{drink}는 지금 없습니다.")
    else:
        vending_machine.remove(drink)
        print(f"{drink} 드릴게요. 남은 음료수 : {vending_machine}")
        
elif type=="주인" or type=="2":
    todo = input("할 일 선택 : 1.추가 2.삭제")


    if todo=="추가" or todo=="1":
        print(f"남은 음료수 : {vending_machine}")

        drink = input("추가할 음료수를 입력하시오.")
        vending_machine.append(drink)
        vending_machine.sort()
        print(f"추가 완료 남은 음료수 : {vending_machine}")
        
    elif todo=="삭제" or todo=="2":
        print(f"남은 음료수 : {vending_machine}")
        drink = input("삭제할 음료수를 입력하시오.")

        if vending_machine.count(drink) == 0:
            print(f"{drink}는 없습니다.")
        else:
            vending_machine.remove(drink)
            print(f"삭제 완료 남은 음료수 : {vending_machine}")
    else:
        print("잘못 입력하셨습니다.")
else:
    print("잘못 입력하셨습니다.")








    
