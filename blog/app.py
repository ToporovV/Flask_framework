from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blog.articles.views import article
from blog.auth.views import auth
from blog.user.views import user


db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hu!g9)!#t2b8pczjr&g_^=pmf75=y9ws4_%1yh$znmh(&lni5!'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .models import User
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)
