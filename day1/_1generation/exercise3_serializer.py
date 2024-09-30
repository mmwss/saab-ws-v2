"""
Build a custom JSON serializer that allows manually serializing
a user object into a JSON-like string and deserializing it.
"""

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email})"

def custom_serialize_user(user):
    """
    Manually serialize the User object into a JSON-like string.
    """
    # Use AI code completion here to manually construct the JSON-like string
    pass  # Remove this pass statement after completing the code

def custom_deserialize_user(serialized_data):
    """
    Manually deserialize the JSON-like string back into a User object.
    """
    # Use AI code completion here to manually parse the JSON-like string
    pass  # Remove this pass statement after completing the code

# Example usage
if __name__ == "__main__":
    print("Code Generation[3] Custom User Serializer")

    user = User(id=1, name="Alice", email="alice@example.com", age=30)

    serialized_data = custom_serialize_user(user)
    print(f"Custom Serialized User: {serialized_data}")

    deserialized_user = custom_deserialize_user(serialized_data)
    print(f"Custom Deserialized User: {deserialized_user}")
