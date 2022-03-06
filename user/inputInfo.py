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
    gender = gender.strip()
    name.append(gender)
    # 输入出生日期(yyyy-mm-dd)
    birth_date = input("输入出生日期(yyyy-mm-dd):")
    birth_date = birth_date.strip()
    name.append(birth_date)
    # 返回列表name
    return name


# 功能：输入健康信息
# 参数：无
# 返回值：列表health
def health_information():
    # 输入身高
    height = input("输入身高(cm):")
    height = height.strip()
    # 输入体重
    weight = input("输入体重(kg):")
    weight = weight.strip()
    # 输入腰围
    waist_line = input("输入腰围(cm):")
    waist_line = waist_line.strip()
    #
    return [height, weight, waist_line]
