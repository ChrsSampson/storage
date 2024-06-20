from pkg.models.user import User
from pkg.models.location import Location
from pkg.models.customer import Customer

def Register_routes(app, db):
    
    @app.route("/api/users")
    def all_users():
        data = User.query.all()
        return str(data)
    
    @app.route("/api/locations")
    def all_locations():
        data = Location.query.all()
        return str(data)
    
    @app.route("/api/customers")
    def all_cusomers():
        data = Customer.query.all()
        return str(data)