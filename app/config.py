import os


class Config:
    '''Parent configuration class'''
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_HOST = os.getenv('DB_HOST')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    SECRET_KEY = os.getenv('SECRET_KEY')


class Development(Config):
    '''Configuration for development environment'''
    DEBUG = True
    TESTING = False


class Testing(Config):
    '''Configuration for testing environment'''
    DEBUG = True
    TESTING = True
    DB_NAME = os.getenv('DB_TEST_NAME')


class Production(Config):
    '''Configuration for production environment'''
    DEBUG = False


app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}
