from flask import Flask
from flask_restplus import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return "Hello, Veerendra!"


# api.add_resource(TodoList, '/todos')
api.add_resource(Hello, '/hello')
# api.add_resource(Todo, '/todos/<string:todo_id>')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
