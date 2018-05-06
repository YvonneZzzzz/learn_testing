#必须先创建 数据库 ——》 再创建 相对应的 表， 不然执行就会报错 

from pymysql import cursors, connect
# import pymysql.cursors

# 连接MySql数据库
conn = connect ( host = '127.0.0.1',user = 'root',password = 'root123',db = 'guest',charset ='utf8mb4', cursorclass = cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        # 创建sql 语句，并执行
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id, create_time) VALUES ("tom", 1888000, "tom@mail.com", 0, 1, NOW());'
        # sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id) VALUES ("tom", 1888000, "tom@mail.com", 0, 1);'        
        cursor.execute(sql)

    # 提交事物
    conn.commit()

    with conn.cursor() as cursor:
        # 查询添加的嘉宾
        sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql, ('1888000',))
        result = cursor.fetchone()
        print(result)

finally:    
     conn.close()


'''
# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root123', db='guest', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# 通过cursor创建游标
cursor = connection.cursor()

# 创建sql 语句，并执行
sql = "INSERT INTO `sign_guest` (`email`, `password`) VALUES ('huzhiheng@itest.info', '123456')"
cursor.execute(sql)

# 提交SQL
connection.commit()
'''