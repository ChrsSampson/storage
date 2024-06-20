from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# if this is not lowercase -> flask_migrate cannot find it
def create_app ():

    App = Flask(__name__)


    App.config["port"] = ":5000"
    App.config["debug"] = True
    App.config["template_folder"] = "templates"
    App.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/storage"

    db.init_app(App)

    from pkg.routes.routes import Register_routes
    Register_routes(App, db)

    migrate.init_app(App, db)

    return App