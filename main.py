# import

from init import db_init
from user.signIn import sign_in
from user.signUp import sign_up
from menuSelect import menu_sign_in, menu_main


# import

# 参数：无
# 返回值：无
# main
def main():
    # 初始化
    uid = -1
    db_connect = db_init()

    while uid == -1:
        # 要求登录或注册
        user_select = menu_sign_in()
        if user_select == '1':
            # 登录
            uid = sign_in(db_connect)
        elif user_select == '2':
            # 注册
            uid = sign_up(db_connect)

    # 主循环
    while True:
        # 选择菜单
        user_select = menu_main()
        # 根据选择菜单，执行相应操作
        if user_select == '1':
            pass
        elif user_select == '2':
            pass


# main

# RUN
if __name__ == '__main__':
    main()
# RUN
