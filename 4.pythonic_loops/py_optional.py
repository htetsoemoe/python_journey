from typing import Optional

# Function Parameters
# The 'email' parameter is optional. If not provided, it defaults to None.
def create_user(name: str, email: Optional[str] = None) -> dict:
    user_data = {"name": name}
    if email is not None: # Check if email was provided
        user_data["email"] = email
    return user_data

user1 = create_user("Alice")
user2 = create_user("John", "john@email.com")

print(f"{user1}, {user2}")