import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@127.0.0.1/user_service_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
