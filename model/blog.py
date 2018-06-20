import uuid
from model.post import Post
from database import Database
# create a blog object to hold different methods


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    # method for creating a new post
    def new_post(self):
        title = input("Enter Blog title: ")
        content = input("Enter some description: ")

        post = Post(title=title,
                    content=content, author=self.author, blog_id=self.id)

        post.insert_to_mongo()

    # create a method to save data to mongodb
    def save_to_mongo(self):
        Database.insert(collection='blog', data=self.json())

    # return a json structure of the blog
    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    # create a method to get blog from mongo
    def get_posts(self):
        return Post.get_all_posts(self.id)

    # create a method for getting data from mongodb uing an id
    @classmethod
    def from_mongo(cls, id):
        data = Database.find_one(collection='blog', query={'id': id})

        return cls(author=data['author'],
                   title=data['title'],
                   description=data['description'],
                   id=data['id'])
