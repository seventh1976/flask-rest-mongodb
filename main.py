from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash


# Endpoint for creating new user
@app.route('/add', methods=['POST'])
def add_user():
  _json = request.json
  _name = _json['name']
  _email = _json['email']
  _password = _json['pwd']
  # Validate the received values
  if _name and _email and _password and request.method == 'POST':
    # do not save password as a plain text
    _hashed_password = generate_password_hash(_password)
    # save details
    id = mongo.db.user.insert({
      'name': _name,
      'email': _email,
      'pwd': _hashed_password
    })
    resp = jsonify('User added successfully!')
    resp.status_code = 200
    return resp
  else:
    return not_found()


# Endpoint to list all user
@app.route('/users')
def users():
  users = mongo.db.user.find()
  resp = dumps(users)
  return resp


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
