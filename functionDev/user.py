class User:

    def __init__(self, username, password, email, age):

        self.username = username
        self.password = password
        self.email = email
        self.age = age

    def change_user_name(self, new_username):
        self.username = new_username
        print(f"{self.username}")


