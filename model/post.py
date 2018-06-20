import uuid
import datetime
from database import Database


class Post(object):
    def __init__(self, title, content, author, blog_id, id=None,
                 date=datetime.datetime.utcnow()):
        self.title = title
        self.content = content
        self.blog_id = blog_id
        self.created_date = date
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id

    # define a method for inserting data to mongo
    def insert_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    # define a method to return blog data as a json structure
    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'date': self.created_date
        }

    # get a single post from mongo_db
    @staticmethod
    def get_post_by_id(_id):
        return Database.find_one(
            collection='posts', query={'id': _id})

    # get a list of posts from an id
    @staticmethod
    def get_all_posts(_id):
        return [x for x in Database.find(collection='posts',
                                         query={'blog_id': _id})]
