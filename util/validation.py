from functools import wraps

from flask import request
from voluptuous.error import MultipleInvalid


def validate_payload(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            payload = request.get_json(silent=True)

            try:
                schema(payload)
            except MultipleInvalid:
                return {"message": 'Bad Request: Failed validation.', "error code": 400}, 400

            kwargs['payload'] = payload
            return f(*args, **kwargs)
        return wrapper
    return decorator
