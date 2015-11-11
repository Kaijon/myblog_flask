import os
from config import config
from flask.ext.script import Manager
from app import create_app


if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    manager = Manager(app)
    manager.run()

