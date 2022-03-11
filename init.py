# import
import mysql.connector


# import

# 功能：连接recipe_recommendation_system数据库
# 参数：无
# 返回值：数据库连接rrs_connect
def db_init():
    rrs_db_connect = mysql.connector.connect(
        host='127.0.0.1',
        user='rrs_admin',
        password='rrs_admin',
        database='recipe_recommendation_system',
        port=3306
    )
    return rrs_db_connect
