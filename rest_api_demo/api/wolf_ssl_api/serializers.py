from flask_restplus import fields
from rest_api_demo.api.restplus import api

blog_post = api.model('Blog post', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a blog post'),
    'title': fields.String(required=True, description='Article title'),
    'body': fields.String(required=True, description='Article content'),
    'pub_date': fields.DateTime,
    'category_id': fields.Integer(attribute='category.id'),
    'category': fields.String(attribute='category.name'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_blog_posts = api.inherit('Page of blog posts', pagination, {
    'items': fields.List(fields.Nested(blog_post))
})

category = api.model('Blog category', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a blog category'),
    'name': fields.String(required=False, description='Category name'),
})

category_with_posts = api.inherit('Blog category with posts', category, {
    'posts': fields.List(fields.Nested(blog_post))
})

data_received = api.model('Data received', {
    'data_received': fields.String(readOnly=True, required=True,
                                   description='Custom endpoint to which notification will be send.'),
})

device_connected = api.model('Device connected', {
    'device_connected': fields.String(readOnly=True, required=True,
                                      description='Custom endpoint to which notification will be send.'),
})

model = api.model('Person', {
    'name': fields.String,
    'age': fields.Integer,
    'boolean': fields.Boolean,
}, mask='{name,age}')

config_cert_issuance = api.model('config_cert_issuance', {
    'device_id': fields.String(readOnly=True, required=True,
                               description='The unique identifier of a device'),
    'enable': fields.Boolean(readOnly=True, required=True,
                             description='Boolean value'),
}, mask='{device_id}')
