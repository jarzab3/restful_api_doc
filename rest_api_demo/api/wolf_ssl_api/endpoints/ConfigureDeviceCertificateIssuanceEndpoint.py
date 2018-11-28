import logging

from flask_restplus import Resource
from rest_api_demo.api.wolf_ssl_api.serializers import config_cert_issuance
from rest_api_demo.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('configure_device_certificate_issuance', description="Allows user to register own endpoint to which "
                                                                        "wolfssl will be sending "
                                                                        "`data_received` notifications")


@ns.route('')
class DeviceConnectedEndpoint(Resource):

    @api.expect(config_cert_issuance, validate=True)
    @api.response(200, 'OK')
    @api.response(201, 'Created')
    @api.response(400, 'Bad Request Payload')
    def post(self):
        """
        Enable/Disable (by setting 'enable' parameter to true/false) the zero-touch device on-boarding
        """
        # TODO implement call to the WolfSSL API
        return "OK", 200
