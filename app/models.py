# -*- coding: utf8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker

from utils import config

username = config.appcfg.get('mysql', 'username')
print username
password = config.appcfg.get('mysql', 'password')
print password

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://'+username+':'+password+'@localhost:3306/doudouSpace')
# 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

def create_user_table():
    print 'start create table'
    connect = engine.connect()
    try:
        result = connect.execute('create table user(userid varchar(32),openid int not null,nickname varchar(100) not null,headimgurl varchar(256) not null,sex int,city varchar(32),country varchar(32),province varchar(32),subscribe_time date,create_at date,update_at date,PRIMARY KEY (userid));')
        result.close()
    except Exception as e:
        print e


def create_user():
    session = DBSession()
