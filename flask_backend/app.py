from models import db
from flask import Flask


app = Flask(__name__)
# app.config.from_pyfile(config_filename)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["APPLICATION_ROOT"] = "/api/v1"
db.init_app(app)
from routes import *


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
