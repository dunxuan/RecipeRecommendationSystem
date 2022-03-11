# 功能:sql查询
# 参数:sql连接、sql语句
# 返回:sql查询结果
def sql_query(db_connect, sql):
    db_cursor = db_connect.cursor()
    # 执行sql语句
    db_cursor.execute(sql)
    # 获取查询结果
    result = db_cursor.fetchone()
    return result
