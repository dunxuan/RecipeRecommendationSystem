# import
from argon2 import PasswordHasher
from sql_cmd import sql_query

# import

ph = PasswordHasher()


# 功能:用户登陆
# 参数:数据库连接
# 返回:用户uid
def sign_in(sql_connect):
    # 输入用户名、密码
    username = input("请输入用户名:")
    password_hash = ph.hash(input("请输入密码:"))
    # 查询数据库
    sql = "select * from recipe_recommendation_system.users_base where username = '%s' and password = '%s'"\
          % (username, password_hash)
    result = sql_query(sql, sql_connect)
    # 判断查询结果
    if result:
        # 返回用户uid
        return result[0]
    else:
        # 返回None
        print("用户名或密码错误")
        return -1
