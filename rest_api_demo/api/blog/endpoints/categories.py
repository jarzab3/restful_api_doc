import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.restplus import api
from rest_api_demo.api.blog.parsers import pagination_arguments
from rest_api_demo.api.blog.parsers import test_arguments

from rest_api_demo.database.models import Endpoint
from rest_api_demo.api.blog.serializers import blog_post, page_of_blog_posts

log = logging.getLogger(__name__)

ns = api.namespace('register_notification_endpoint', description='Allows user to register own endpoint to which '
                                                                 'wolfssl will be sending specific notifications')

from rest_api_demo.api.blog.business import create_api_endpoint, update_endpoint, delete_endpoint

@ns.route('/')
class CategoryCollection(Resource):
    # @api.marshal_list_with(category)
    # def get(self):
    #     """
    #     Returns list of API categories.
    #     """
    #     categories = Category.query.all()
    #     return categories
    #
    # @api.response(201, 'Category successfully created.')
    # @api.expect(category)
    # def post(self):
    #     """
    #     Creates a new API category.
    #     """
    #     data = request.json
    #     create_category(data)
    #     return None, 201

    # @api.response(201, 'Category successfully created.')
    # @api.expect(category, validate=False)
    # def post(self):
    #     """
    #     Updates a new API category.
    #     """
    #     data = request.json
    #     create_category(data)
    # return None, 201

    @api.expect(test_arguments)
    @api.marshal_with(page_of_blog_posts)  # TODO Change it here
    def get(self):
        """
        Returns list of API Endpoints.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        endpoints_query = Endpoint.query
        endpoints_page = endpoints_query.paginate(page, per_page, error_out=False)

        return endpoints_page

    @api.expect(blog_post)
    def endpoint(self):
        """
        Creates a new API endpoint.
        """
        create_api_endpoint(request.json)
        return None, 201

#
# @ns.route('/<int:id>')
# @api.response(404, 'Category not found.')
# class CategoryItem(Resource):
#
#     @api.marshal_with(category_with_posts)
#     def get(self, id):
#         """
#         Returns a category with a list of endpoints.
#         """
#         return Category.query.filter(Category.id == id).one()
#
#     @api.expect(category)
#     @api.response(204, 'Category successfully updated.')
#     def put(self, id):
#         """
#         Updates an API category.
#
#         Use this method to change the name of an API category.
#
#         * Send a JSON object with the new name in the request body.
#
#         ```
#         {
#           "name": "New Category Name"
#         }
#         ```
#
#         * Specify the ID of the category to modify in the request URL path.
#         """
#         data = request.json
#         update_category(id, data)
#         return None, 204
#
#     @api.response(204, 'Category successfully deleted.')
#     def delete(self, id):
#         """
#         Deletes an API category.
#         """
#         delete_category(id)
#         return None, 204
