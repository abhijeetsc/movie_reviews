from flask import Flask
from flask_redis import FlaskRedis
from flask_migrate import Migrate
from config import DevConfig, ProdConfig
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
redis_client = FlaskRedis()

def create_app(app_env='dev'):
    movies_app = Flask(__name__)
    if app_env == 'dev':
        movies_app.config.from_object(DevConfig)
    else:
        movies_app.config.from_object(ProdConfig)

    migrate.init_app(movies_app, db)
    redis_client.init_app(movies_app)
    db.init_app(movies_app)

    from app.models import User

    return movies_app


# @movies_app.route('/')
# def index():
#     redis_client.set('visits', redis_client.get('visits') or 0)
#     redis_client.incr('visits')  # Increment the visits count
#     return f"Number of visits: {redis_client.get('visits').decode('utf-8')}"

    # return 'Index Page'

