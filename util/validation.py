from functools import wraps

from flask import request
from voluptuous.error import MultipleInvalid
from util.exceptions import ApiException


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


def validate_params(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            params = request.args
            if not params:
                params = request.get_json(silent=True) or {}
            try:
                schema(params)
            except MultipleInvalid as e:
                raise ApiException('Bad Request: Failed validation.', 400, e.errors)
            return f(*args, **kwargs)
        return wrapper
    return decorator

