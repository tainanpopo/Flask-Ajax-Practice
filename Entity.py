from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://XXXXX' #若是本地sqlite3:'sqlite:///XXX.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Account(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(15), unique=True)
    Email = db.Column(db.String(50), unique=True)
    Password = db.Column(db.String(80))


if __name__ == '__main__':
    manager.run()
