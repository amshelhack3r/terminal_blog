from database import Database
from model.blog import Blog


# this creates the run menus to prompt users
class Menu(object):
    def __init__(self):
        self.author = input("Enter author name: ")
        self.blog = None
        if self._has_account():
            print("welclome back {}".format(self.author))
        else:
            self._prompt_for_account()

    # write a method that returns a boolean if the user has an account or not
    def _has_account(self):
        blog = Database.find_one(collection='blog',
                                 query={'author': self.author})

        if blog is not None:
            self.blog = blog
            return True
        else:
            return False

    # wrte a method to prompt user to create an account
    def _prompt_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.author,
                    title=title,
                    description=description)

        blog.save_to_mongo()
        self.blog = blog
