"""
应用配置文件
"""
import os


class Config:
    """应用配置"""
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
