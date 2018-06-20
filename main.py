from database import Database
from model.blog import Blog
__author__ = 'amshel'

Database.initialize()

blog = Blog(author='samuel', title='learning mongo',
            description='Experience learning Mongo', id ='1')

blog.new_post()

blog.save_to_mongo()

blog_obj = Blog.from_mongo(blog.id)

print(blog.get_posts())


