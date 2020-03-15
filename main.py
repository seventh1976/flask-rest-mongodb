from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug import generate_password_hash, check_password_hash


# Endpoint for creating new user
@app.route('/add', methods=['POST'])
def add_user():
  pass


# Endpoint to list all user
@app.route('/users')
def users():
  pass


# Endpoint to find a user
@app.route('/user/<id>')
def user(id):
  pass


# Endpoint to update user
@app.route('/update', methods=['PUT'])
def update_user():
  pass


# Endpoint to delete user
@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
  pass


# 404 method to handle not found error
@app.errorhandler(404)
def not_found(error=None):
  message = {
    'status': 404,
    'message': 'Not Found: ' + request.url,
  }
  resp = jsonify(message)
  resp.status_code = 404

  return resp


# Run application
if __name__ == '__main__':
  app.run()
