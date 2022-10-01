from user import User

class Inheritance(User):

    def __init__(self, username, password, email, age, year):
        User.__init__(self, username, password, email, age)
        self.year = year

    def user_definition(self):
        print(f"{self.username}  {self.password}  {self.email}  {self.age}  {self.year}")




