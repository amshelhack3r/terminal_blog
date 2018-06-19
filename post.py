from database import Database


class Post(object):
    def __init__(self, title, content, blog_id):
        self.title = title
        self.content = content
        self.blog_id = blog_id

    # define a method for inserting data to mongo
    def insert_to_mongo(self):
        Database.insert(collection='posts', data=self.json)

    # define a method to return blog data as a json structure
    def json(self):
        return {
            'title': self.title,
            'content': self.content,
            'blog_id': self.blog_id
        }
    # get a single post from mongo_db

    @staticmethod
    def get_post(id):
        return Database.find_one(
            collection='blog', query={'blog_id': id})

    # get a list of posts from an id
    @staticmethod
    def get_all_posts(id):
        return [x for x in Database.find(collection='blog',
                                         query={'blog_id': id})]
