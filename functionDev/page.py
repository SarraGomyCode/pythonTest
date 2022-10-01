class Page:

    def __init__(self, post):
        self.post = post

    def change_post_by_user(self, new_post):
        self.post = new_post
        print(f"my new post has been published : {self.post}")

    def definition_post(self):
        print(f"new post has been created : {self.post}")

