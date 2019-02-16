import os


class Config:
    '''Parent configuration class'''
    DB_URL = os.getenv('DB_URL')
    # # DB_USER = os.getenv('DB_USER')
    # # DB_HOST = os.getenv('DB_HOST')
    # # DB_PASSWORD = os.getenv('DB_PASSWORD')
    # SECRET_KEY = os.getenv('SECRET_KEY')


class Development(Config):
    '''Configuration for development environment'''
    DEBUG = True
    TESTING = False


class Testing(Config):
    '''Configuration for testing environment'''
    DEBUG = True
    TESTING = True
    DB_URL = os.getenv('DB_URL')


class Production(Config):
    '''Configuration for production environment'''
    DEBUG = False


app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development,
    # "DB_URL": os.getenv('DB_URL')
    # "TEST_DB_URL": os.getenv('DATABASE_TEST_URL')

}
