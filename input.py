#import
import datetime
#import

#功能：输入 numberOfPeople 个人的基本信息
#参数：无
#返回值：列表name
def baseInformation():
    #输入姓名
    print("输入姓名:", end="")
    name = input()
    name = name.strip()
    name = [name]
    #输入性别(男/女)，输入错误时要求重新输入
    print("输入性别(男/女):", end="")
    gender = input()
    while True:#判断输入是否正确
        if gender == "男" or gender == "女":
            break
        else:
            print("输入错误，请重新输入性别(男/女):",end="")
            gender = input()
    #输入出生日期(yyyy-mm-dd)
    print("输入出生日期(yyyy-mm-dd):", end="")
    birthDate = input()
    birthDate = birthDate.strip()
    name.append(birthDate)
    #返回列表name
    return name