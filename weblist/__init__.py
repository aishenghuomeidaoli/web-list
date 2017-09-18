# _*_ coding: utf-8 _*_
from flask import Flask
from sqlalchemy import create_engine, Column, Integer, DateTime, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from weblist.config import SQL_URL


def create_app():
    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

    from .main import main
    app.register_blueprint(main)

    return app


engine = create_engine(SQL_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()
db = Session()
