# -*- coding:utf-8 -*-
# Author:xieshengsen


with open("DictFile","r",encoding="utf-8") as f:
    City = f.read()
    City = eval(City)      # 将字符串转换为字典形式

Flag = False

while not Flag:
    for i in City:
        print (i)
    choice1 = input("①请选择，按q/Q退出>>>：")

    if choice1 in City:
        while not Flag:
            for i2 in City[choice1]:
                print ("\t",i2)
            choice2 = input("②请选择，按q/Q退出,按b/B返回上一级>>>：")

            if choice2 in City[choice1]:
                while not Flag:
                    for i3 in City[choice1][choice2]:
                        print ("\t\t",i3)
                    choice3 = input("③请选择，按q/Q退出,按b/B返回上一级>>>：")

                    if choice3 in City[choice1][choice2]:
                        while not Flag:
                            for i4 in City[choice1][choice2][choice3]:
                                print ("\t\t\t",i4)
                            choice4 = input("④最后一层，按q/Q退出,按b/B返回上一级>>>：")

                            if choice4 == "b" or choice4 == "B":
                                break
                            elif choice4 == "q" or choice4 == "Q":
                                Flag = True

                    if choice3 == "b" or choice3 == "B":
                        break
                    elif choice3 == "q" or choice3 == "Q":
                        Flag = True

            if choice2 == "b" or choice2 == "B":
                break
            elif choice2 == "q" or choice2 == "Q":
                Flag = True

    if choice1 == "q" or choice1 == "Q":
        Flag = True