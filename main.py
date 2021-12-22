#IMPORT

#IMPORT



#MAIN
def main:
    people = init()
    #主循环
    while True:
        #选择菜单
        user_select = menuSelect()
        if user_select == '1':
            people.append(baseInformation())
            print('录入成功')
        elif user_select == '2':
            #code
            pass
        elif user_select == '3':
            #生成菜谱，后期实现
            #输出建议食材，暂时替代菜谱输出
            print(datetime.datetime.now().strftime('%Y年%m月%d日 推荐菜谱:'))
            print('  - 早餐')
            #code
            pass
            print('  - 午餐')
            #code
            pass
            print('  - 晚餐')
            #code
            pass
        else:
            print("输入错误，请重新输入")
#MAIN



#RUN
if __name__ == '__main__':
    main()
#RUN