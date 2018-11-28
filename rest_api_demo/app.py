import logging.config

import os
from flask import Flask, Blueprint
from rest_api_demo import settings
from rest_api_demo.api.wolf_ssl_api.endpoints.DeviceConnectedEndpoint import ns as device_connected_endpoint
from rest_api_demo.api.wolf_ssl_api.endpoints.DataReceivedEndpoint import ns as data_received_endpoint
from rest_api_demo.api.wolf_ssl_api.endpoints.ConfigureDeviceCertificateIssuanceEndpoint import ns as config_dev_cert_endpoint
from rest_api_demo.api.restplus import api
from rest_api_demo.database import db

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='')
    api.init_app(blueprint)
    api.add_namespace(device_connected_endpoint)
    api.add_namespace(data_received_endpoint)
    api.add_namespace(config_dev_cert_endpoint)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()
