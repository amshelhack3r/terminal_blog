from database import Database
from model.blog import Blog


# this creates the run menus to prompt users
class Menu(object):
    def __init__(self):
        self.author = input("Enter author name: ")
        self.blog = None
        if self._has_account():
            print("welcome back {}".format(self.author))
        else:
            self._prompt_for_account()

    # write a method that returns a boolean if the user has an account or not
    def _has_account(self):
        blog = Database.find_one(collection='blog',
                                 query={'author': self.author})

        if blog is not None:
            self.blog = Blog.from_mongo(blog['id'])
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

    # method for asking the user if he/she wants to read or write a blog
    def run_menu(self):
        option = input("Do you want to read(R) or write(W) a blog: ")

        if option == "R" or option == "r":
            self._view_blogs()
            self._read_posts()

            # read the posts
            pass
        elif option == "W" or option == "w":
            # prompt user to create a post
            self.blog.new_post()
            pass
        else:
            print("Thank you for blogging ")

    def _view_blogs(self):
        # get all blogs
        blogs = Database.find(collection='blog', query={})

        # list blogs
        for blog in blogs:
            print("ID {} TITLE {} Author {} \n".format(blog['id'],
                                                       blog['title'],
                                                       blog['author']))

    def _read_posts(self):
        ID = input("Select from blog id the posts you wish to read: ")
        record = Blog.from_mongo(ID)

        posts = record.get_posts()

        for post in posts:
            print("Author {}\n Title {}\n\n{}".format(post['author'],
                                                      post['title'],
                                                      post['content']))
