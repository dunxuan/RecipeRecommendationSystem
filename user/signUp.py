# import
from argon2 import PasswordHasher
from sql_cmd import sql_query

# import

ph = PasswordHasher()


# 功能:用户注册
# 参数:数据库连接
# 返回:用户uid
def sign_up(db_connect):
    # 输入用户名
    username = input("请输入用户名:")
    # 查询数据库,判断用户名是否存在
    sql = "select * from recipe_recommendation_system.users_base where username = '%s'" % username
    result = sql_query(db_connect, sql)
    # 判断查询结果
    if result:
        # 返回None
        print("用户已存在")
        return -1
    else:
        # 输入密码
        password_hash = ph.hash(input("请输入密码:"))
        # 插入数据库
        sql = "insert into recipe_recommendation_system.users_base(username, password) values('%s','%s')"\
              % (username, password_hash)
        result = sql_query(db_connect, sql)
        # 返回用户uid
        return result[0]
