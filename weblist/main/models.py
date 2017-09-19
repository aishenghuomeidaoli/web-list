# _*_ coding: utf-8 _*_
from sqlalchemy import Column, String, Integer
from weblist import Base


class User(Base):
    __tablename__ = 'user' # 定义MySQL数据库中存储用户的表名称

    id = Column(Integer, primary_key=True, autoincrement=True)  # 创建自增的主键

    # 定义三个字段，分别存储用户名称，邮箱，密码
    name = Column(String(255))
    email = Column(String(255))
    pw = Column(String(255))

    # 定义__repr__函数，当获取一个用户实例user，并执行print user时，会调用此函数
    def __repr__(self):
        return '<User(id={0}, name={1}, email={2})>'.\
            format(self.id, self.name.encode('utf-8'), self.email)
