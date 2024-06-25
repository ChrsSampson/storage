from flask_restful import Api

from pkg.models.user import User
from pkg.models.location import Location
from pkg.models.customer import Customer

from pkg.handlers.userHandler import User_Handler, User_list_handler


def Register_routes(app, db):
    
    api = Api(app)

    api.add_resource(User_Handler, "/api/users")
    api.add_resource(User_list_handler, "/api/users/<string:user_id>")
    
    @app.route("/api/locations")
    def all_locations():
        data = Location.query.all()
        return str(data)
    
    @app.route("/api/customers")
    def all_cusomers():
        data = Customer.query.all()
        return str(data)