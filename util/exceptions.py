class ApiException(Exception):
    status = 500

    def __init__(self, message: str, status: int=None, error_list: list=None):
        Exception.__init__(self)
        self.message = message
        self.errors = error_list

        if status is not None:
            self.status = status

    def _error_list(self):
        if self.errors is None:
            return []

        # Cast errors to strings so that there are no problems when trying to jsonify into a response
        return [str(error) for error in self.errors]

    def response(self) -> dict:
        error_message = {
            'status': self.status,
            'message': self.message,
            'errors': self._error_list()
        }

        return error_message


class ResultNotFound(Exception):
    pass


class DBException(Exception):
    pass
