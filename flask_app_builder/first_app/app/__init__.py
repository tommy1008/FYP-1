import os
import logging
from flask import Flask, render_template
from flask_appbuilder import SQLA, AppBuilder, IndexView, BaseView
from sqlalchemy.engine import Engine
from sqlalchemy import event
from .security import MySecurityManager

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, security_manager_class=MySecurityManager)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connesshction_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


@app.route('/')
def index():
    return render_template('index.html',appbuilder=appbuilder)


if __name__ == '__main__':
    app.run()

from app import models, views
