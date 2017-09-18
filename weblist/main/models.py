# _*_ coding: utf-8 _*_
from sqlalchemy import Column, String, Integer
from weblist import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    email = Column(String(255))
    pw = Column(String(255))

    def __repr__(self):
        return '<User(id={0}, name={1}, email={2})>'.format(self.id, self.name.encode('utf-8'), self.email)
