from flask import Flask

from .main.schema import ms
from .main.models import db

import os

from .main.config import config_by_name
from flask_migrate import Migrate
from .main.bp import exbp



def createApp(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    ms.init_app(app)
    return app


app = createApp('dev')
    
migrate = Migrate(app, db)
app.register_blueprint(exbp)

@app.route('/')
def index():
    return "Selamat Datang"

if __name__ == '__main__':
    app.run()

