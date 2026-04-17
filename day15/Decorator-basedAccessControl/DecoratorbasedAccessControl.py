users={
    "Ram":"admin",
    "Jenny":"user",
    "guest":"guest"
}

def required_role(role):
    def decorator(func):
        def wrapper(username):
            if users.get(username)==role:
                return func(username)
            else:
                print(f"access denied for {username}")
        return wrapper
    return decorator
@required_role("admin")
def delete_data(username):
    print(f"{username} deleted data")

@required_role("user")
def view_data(username):
    print(f"{username} viewing data")

delete_data("Ram")
delete_data("Jenny")

view_data("Jenny")
view_data("Ram")