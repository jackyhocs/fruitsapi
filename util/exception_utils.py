import traceback

from flask import jsonify, Blueprint
from flask_restful import Api
from util.exceptions import ApiException

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(ApiException)
def handle_error(error: 'ApiException'):
    return jsonify(error.response()), error.status


@errors.app_errorhandler(Exception)
def handle_unexpected_errors(error):
    traceback.print_exc()

    error_message = {
        'status': 500,
        'message': 'Internal Server Error'
    }

    return jsonify(error_message), 500


class ApiCustomErrorHandler(Api):
    """Custom Api class"""

    def handle_error(self, e):
        """Override the default flask-restful Api class to delegate error handling to flask"""
        self.blueprint.handle_exception(e)
