# import
# import

# 功能：输入 numberOfPeople 个人的基本信息
# 参数：无
# 返回值：列表name
def base_information():
    # 输入姓名
    name = input("输入姓名:")
    name = name.strip()
    name = [name]
    # 输入性别(男/女)，输入错误时要求重新输入
    gender = input("输入性别(男/女):")
    while True:  # 判断输入是否正确
        if gender == "男" or gender == "女":
            break
        else:
            gender = input("输入错误，请重新输入性别(男/女):")
    # 输入出生日期(yyyy-mm-dd)
    birth_date = input("输入出生日期(yyyy-mm-dd):")
    birth_date = birth_date.strip()
    name.append(birth_date)
    # 返回列表name
    return name


def setting_information():
    # 输入身高、体重和腰围
    height = input("输入身高(cm):")
    weight = input("输入体重(kg):")
    waist = input("输入腰围(cm):")