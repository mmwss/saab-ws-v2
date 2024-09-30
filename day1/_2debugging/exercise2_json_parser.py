"""
Debug the program that reads data from a JSON file
but fails when the file does not contain the expected fields.

Example of user in users.json: {
    "name": "Alice",
    "email": "alice@example.com"
}
"""

import json

def read_users(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    users = []
    for user in data:
        users.append({
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'age': user['age']
        })

    return users

# Example usage
if __name__ == '__main__':
    print("Code Debugging[2] JSON Parser")

    users_file = 'data/users.json'
    users = read_users(users_file)

    for user in users:
        print(f"#{user['id']} User: {user['name']}, Email: {user['email']}")
