from flask import app
from app.routes.home import home_route
from app.routes.clients import client_route
from app.database.database import db
from app.database.models.client import Client


def configure_all(app):
    configure_routes(app)
    configure_db()
    
def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(client_route, url_prefix="/clients")

def configure_db():
    db.connect()
    db.create_tables([Client])