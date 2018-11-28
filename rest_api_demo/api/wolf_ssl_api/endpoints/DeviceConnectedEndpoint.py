import logging

from flask_restplus import Resource

from rest_api_demo.api.wolf_ssl_api.serializers import device_connected
from rest_api_demo.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('device_connected', description="Allows user to register own endpoint to which "
                                                   "wolfssl will be sending 'device_connected' notifications")


@ns.route('')
class DeviceConnectedEndpoint(Resource):

    @api.expect(device_connected, validate=True)
    @api.response(200, 'OK')
    @api.response(201, 'Created')
    @api.response(400, 'Bad Request Payload')
    def post(self):
        """
        Register an notification endpoint for 'device_connected' action
        """
        # TODO implement call to the WolfSSL API
        return "OK", 200

    # @api.marshal_list_with(category)
    @api.expect(device_connected, validate=True)
    @api.response(200, 'OK')
    @api.response(202, 'No Content')
    @api.response(400, 'Bad Request Payload')
    def put(self):
        """
        Update an endpoint `device_connected` in the database
        """
        # TODO implement call to the WolfSSL API
        return "OK", 200

    # @api.expect(device_connected, validate=True)
    @api.response(200, 'OK')
    @api.response(201, 'No Content')
    @api.response(400, 'Bad Request Payload')
    def delete(self):
        """
        Deletes an endpoint `device_connected` from the database
        """
        # TODO implement call to the WolfSSL API
        return "OK", 200
