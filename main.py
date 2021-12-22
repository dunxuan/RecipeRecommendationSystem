# import
from init import init
from input import base_information
from menuSelect import menu_select

# import


# 参数：无
# 返回值：无
# main
def main():
    people = init()
    # 主循环
    while True:
        # 选择菜单
        user_select = menu_select()
        if user_select == '1':
            people.append(base_information())
            print('录入成功')
        elif user_select == '2':
            # code
            pass
        elif user_select == '3':
            # 生成菜谱，后期实现
            # 输出建议食材，暂时替代菜谱输出
            print('建议菜谱：')
            pass
        else:
            print("输入错误，请重新输入")


# main


# RUN
if __name__ == '__main__':
    main()
# RUN
