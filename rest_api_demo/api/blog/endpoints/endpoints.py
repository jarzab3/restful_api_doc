import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.blog.business import create_api_endpoint, update_endpoint, delete_endpoint
from rest_api_demo.api.blog.serializers import blog_post, page_of_blog_posts
from rest_api_demo.api.blog.parsers import pagination_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Endpoint

log = logging.getLogger(__name__)

ns = api.namespace('endpoints', description='Operations related to WolfSSL API endpoint')


@ns.route('/')
class PostsCollection(Resource):

    @api.expect(pagination_arguments)
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


@ns.route('/<int:id>')
@api.response(404, 'Endpoint not found.')
class PostItem(Resource):

    @api.marshal_with(blog_post)
    def get(self, id):
        """
        Returns an API endpoint.
        """
        return Endpoint.query.filter(Endpoint.id == id).one()

    @api.expect(blog_post)  # TODO change it here
    @api.response(204, 'Endpoint successfully updated.')
    def put(self, id):
        """
        Updates an API endpoint.
        """
        data = request.json
        update_endpoint(id, data)
        return None, 204

    @api.response(204, 'Endpoint successfully deleted.')
    def delete(self, id):
        """
        Deletes API endpoint.
        """
        delete_endpoint(id)
        return None, 204


@ns.route('/archive/<int:year>/')
@ns.route('/archive/<int:year>/<int:month>/')
@ns.route('/archive/<int:year>/<int:month>/<int:day>/')
class PostsArchiveCollection(Resource):

    @api.expect(pagination_arguments, validate=True)
    @api.marshal_with(page_of_blog_posts)
    def get(self, year, month=None, day=None):
        """
        Returns list of blog posts from a specified time period.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        start_month = month if month else 1
        end_month = month if month else 12
        start_day = day if day else 1
        end_day = day + 1 if day else 31
        start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month, start_day)
        end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
        posts_query = Endpoint.query.filter(Endpoint.pub_date >= start_date).filter(Endpoint.pub_date <= end_date)

        posts_page = posts_query.paginate(page, per_page, error_out=False)

        return posts_page
