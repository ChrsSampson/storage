from flask_restful import Resource
from flask import jsonify, request
from pkg.models.user import User
from app import db
from rich import print


# api/users
class User_Handler(Resource):
    def get(self):
        data = User.query.all()
        return jsonify(data)
    
    def post(self):
        body = request.json
        try:
            print(body)
            user = User(
                email=body['email'],
                username=body['username'],
                password=body['password'],
            )
            db.session.add(user)
            db.session.commit()
            return {'status': 201}
        except Exception as err:
            return {"status": 400, "error": str(err._message)}
        


# api/users/<string:user_id>
class User_list_handler(Resource):

    def get(self, user_id:str):
        print(user_id)

        try:
            if user_id == "":
                error = error("ID is required")

            user = User.query.get(user_id)

            return str(user)
        except Exception as err:
            return {"status": 404, "error": str(err)}



