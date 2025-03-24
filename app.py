from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate a database
users_db = [
    {"id": 1, "name": "Ariana", "lastname": "Grande", "age": 32},
    {"id": 2, "name": "Taylor", "lastname": "Swift", "age": 34}
]

# Find user by ID
def find_user_by_id(user_id):
    return next((user for user in users_db if user["id"] == user_id), None)

# Route to GET the user by ID
@app.route("/user", methods=["GET"])
def get_user():
    user_id = request.args.get("id", type=int)
    if user_id is None:
        return jsonify({"message": "Inform your id"}), 400
    
    user = find_user_by_id(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    
    return jsonify(user)

# Route to insert user into 
@app.route("/user", methods=["POST"])
def insert_user():
    data = request.json
    if not data.get("name") or not data.get("lastname") or not data.get("age"):
        return jsonify({"message": "Missing required fields"}), 400
    
    new_id = max(user["id"] for user in users_db) + 1 if users_db else 1
    new_user = {
        "id": new_id,
        "name": data["name"],
        "lastname": data["lastname"],
        "age": data["age"]
    }
    users_db.append(new_user)
    return jsonify({"message": "User created", "user": new_user}), 201


# Route to UPDATE the user by the ID
@app.route("/user", methods=["PUT"])
def update_user():
    user_id = request.args.get("id", type=int)
    if user_id is None:
        return jsonify({"message": "Inform your ID"}), 400
    
    user = find_user_by_id(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    
    data = request.json
    user.update({key: data[key] for key in data if key in user})
    return jsonify({"message": "User updated", "user": user})

# Route to DELETE the ubser by the ID
@app.route("/user", methods=["DELETE"])
def delete_user():
    user_id = request.args.get("id", type=int)
    if user_id is None:
        return jsonify({"message": "Inform your id"}), 400
    
    global users_db
    users_db = [user for user in users_db if user["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
