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
TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
#   show a single todo item and lets you delete them
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = 'todo%d' % (len(TODOS) + 1)
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


class Hello(Resource):
    def get(self):
        return "Hello, Veerendra!"


api.add_resource(TodoList, '/todos')
api.add_resource(Hello, '/hello')
api.add_resource(Todo, '/todos/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
