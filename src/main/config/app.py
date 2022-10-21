from flask import Flask
from flask_cors import CORS

from dotenv import load_dotenv

from src.main.routes.v1 import car_owner_routes_bp

from src.infra.db.sqlalchemy import create_database, DBConnectionHandler

load_dotenv()
create_database(DBConnectionHandler().get_engine())  # Development purpose

app = Flask(__name__)

CORS(app)

app.register_blueprint(car_owner_routes_bp)
