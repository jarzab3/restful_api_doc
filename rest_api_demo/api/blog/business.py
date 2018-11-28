from rest_api_demo.database import db
from rest_api_demo.database.models import Endpoint, Category


def create_api_endpoint(data):
    title = data.get('title')
    body = data.get('body')
    category_id = data.get('category_id')
    category = Category.query.filter(Category.id == category_id).one()
    endpoint = Endpoint(title, body, category)
    db.session.add(endpoint)
    db.session.commit()


def update_endpoint(endpoint_id, data):
    endpoint = Endpoint.query.filter(Endpoint.id == endpoint_id).one()
    endpoint.title = data.get('title')
    endpoint.body = data.get('body')
    category_id = data.get('category_id')
    endpoint.category = Category.query.filter(Category.id == category_id).one()
    db.session.add(endpoint)
    db.session.commit()


def delete_endpoint(endpoint_id):
    endpoint = Endpoint.query.filter(Endpoint.id == endpoint_id).one()
    db.session.delete(endpoint)
    db.session.commit()


def create_category(data):
    name = data.get('name')
    category_id = data.get('id')

    category = Category(name)
    if category_id:
        category.id = category_id

    db.session.add(category)
    db.session.commit()


def update_category(category_id, data):
    category = Category.query.filter(Category.id == category_id).one()
    category.name = data.get('name')
    db.session.add(category)
    db.session.commit()


def delete_category(category_id):
    category = Category.query.filter(Category.id == category_id).one()
    db.session.delete(category)
    db.session.commit()
