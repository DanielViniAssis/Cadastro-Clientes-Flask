from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes.home import home_route
from app.routes.clients import client_route
app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(home_route)
app.register_blueprint(client_route, url_prefix="/clients")

db = SQLAlchemy(app)
migrate = Migrate(app, db, command='migrate')

