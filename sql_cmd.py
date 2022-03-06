# 功能:sql查询
# 参数:sql语句、sql连接
# 返回:sql查询结果
def sql_query(sql, sql_connect):
    # 执行sql语句
    sql_connect.cursor.execute(sql)
    # 获取查询结果
    result = sql_connect.cursor.fetchone()
    return result
