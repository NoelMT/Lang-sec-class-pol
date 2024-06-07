from flask import Flask, request, jsonify

app = Flask(__name__)

class User:
    def __init__(self, name, role="user"):
        self.name = name
        self.role = role

class Admin:
    def __init__(self, name):
        self.name = name
        self.role = "admin"

users = {
    "alice": User("Alice"),
    "bob": User("Bob")
}

def merge(target, source):
    for key, value in source.items():
        if isinstance(value, dict) and key in target:
            merge(target[key], value)
        else:
            target[key] = value
    return target

@app.route('/update_user', methods=['POST'])
def update_user():
    data = request.json
    username = data.get('username')
    user_config = data.get('config', {})

    if username not in users:
        return jsonify({"error": "User not found"}), 404

    user = users[username]
    user_dict = user.__dict__

    # Vulnerable merge
    merged_config = merge(user_dict, user_config)
    user.__dict__.update(merged_config)


    return jsonify({"username": user.name, "role": user.role})

if __name__ == '__main__':
    app.run(debug=True)
