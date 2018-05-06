# 创建测试数据 P175



import sys
sys.path.append('../db_fixture')
# from mysql_db import DB
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB


# 创建测试数据
datas = {
    # 发布会数据
    'sign_event':[
        # {'id':1,'name':'红米Pro发布会','`limit`':2000,'status':1,'address':'北京会展中心', 'start_time':'2017-08-20 14:00:00'},
        # {'id':2,'name':'可参加人数为0','`limit`':0,'status':1,'address':'北京会展中心','start_time':'2017-08-20 14:00:00'},
        # {'id':3,'name':'当前状态为0关闭','`limit`':2000,'status':0,'address':'北京会展中心','start_time':'2017-08-20 14:00:00'},
        # {'id':4,'name':'发布会已结束','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2001-08-20 14:00:00'},
        # {'id':5,'name':'小米5发布会','`limit`':2000,'status':1,'address':'北京国家会议中心','start_time':'2017-08-20 14:00:00'},

        {'id':1,'name':'红米Pro发布会','`limit`':2000,'status':1,'address':'北京会展中心', 'creat_time':'2016-08-20 14:00:00', 'start_time':'2017-08-20 14:00:00'},
        {'id':2,'name':'可参加人数为0','`limit`':0,'status':1,'address':'北京会展中心','creat_time':'2016-08-20 14:00:00', 'start_time':'2017-08-20 14:00:00'},
        {'id':3,'name':'当前状态为0关闭','`limit`':2000,'status':0,'address':'北京会展中心','creat_time':'2016-08-20 14:00:00', 'start_time':'2017-08-20 14:00:00'},
        {'id':4,'name':'发布会已结束','`limit`':2000,'status':1,'address':'北京会展中心','creat_time':'2016-08-20 14:00:00', 'start_time':'2001-08-20 14:00:00'},
        {'id':5,'name':'小米5发布会','`limit`':2000,'status':1,'address':'北京国家会议中心','creat_time':'2016-08-20 14:00:00', 'start_time':'2017-08-20 14:00:00'},
    ],
    # 嘉宾表数据
    'sign_guest':[
        # {'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com','sign':0,'event_id':1},
        # {'id':2,'realname':'has sign','phone':13511001101,'email':'sign@mail.com','sign':1,'event_id':1},
        # {'id':3,'realname':'tom','phone':13511001102,'email':'tom@mail.com','sign':0,'event_id':5},

        {'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com','sign':0,'event_id':1, 'creat_time':'2016-08-20 14:00:00'},
        {'id':2,'realname':'has sign','phone':13511001101,'email':'sign@mail.com','sign':1,'event_id':1, 'creat_time':'2016-08-20 14:00:00'},
        {'id':3,'realname':'tom','phone':13511001102,'email':'tom@mail.com','sign':0,'event_id':5, 'creat_time':'2016-08-20 14:00:00'},
    ],
}

# 将测试数据插入表
def init_data():
    '''
    init_data()函数用于读取datas字典中的数据；
    调用DB类中的clear()方法清除表数据；
    循环调用insert()方法插入表数据。
    '''
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


if __name__ == '__main__':
    init_data()