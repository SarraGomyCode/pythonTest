from user import User
from page import Page
from inheritance import Inheritance


user_test_one = Inheritance("sarra", "1234", "sarra@gmail.com", "29","2019")
user_test_one.user_definition()

new_post = Page("hi guys, please to check my new post")
new_post.definition_post()
new_post_second = Page("new post")
new_post_second.change_post_by_user("new_post_test")

y = User("sarra","1234", "sarra@gmail.com","29")
print(y.username)
y.change_user_name("monir")

