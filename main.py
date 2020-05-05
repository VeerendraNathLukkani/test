from flask import Flask
from flask_restplus import reqparse, abort, Api, Resource
from flask_cors import CORS

import socket
print(socket.gethostname())

app = Flask(__name__)
app.config['SERVER_NAME'] = 'veerendra.azurewebsites.net'

# app.config.from_object(__name__)
#
# # enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})
#
api = Api(app)


class Hello(Resource):
    def get(self):
        return "Hello, Veerendra!"


# api.add_resource(TodoList, '/todos')
api.add_resource(Hello, '/hello')
# api.add_resource(Todo, '/todos/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
