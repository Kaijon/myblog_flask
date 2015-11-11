import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class ProductConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'data.sqlite')

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development' : DevelopConfig,
    'testing' : TestConfig,
    'product' : ProductConfig,

    'default' : DevelopConfig
}

#if __name__ == '__main__':
#    print basedir
