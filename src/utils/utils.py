from datetime import date, datetime
from decimal import Decimal
import re
from unicodedata import decimal
from flask import jsonify, Response, Request
from src.data.entities import EntityBase


def camel_to_underscore(name: str):
    camel_pattern = re.compile(r'([A-Z])')
    return camel_pattern.sub(lambda x: '_' + x.group(1).lower(), name)


def underscore_to_camel(name: str):
    under_pattern = re.compile(r'_([a-z])')
    return under_pattern.sub(lambda x: x.group(1).upper(), name)


def convert_request_body_to_snakecase(data: dict):
    data_items = data.items()
    data = {}

    for key, value in data_items:
        key_underscore = camel_to_underscore(key)
        data[key_underscore] = value

    return data


def responsify(res: dict | list):
    responsified = dict | list[dict]

    if isinstance(res, dict):
        responsified = responsify_dict(res)

    elif isinstance(res, list):
        responsified = responsify_list(res)

    else:
        message: str
        message = 'You should not be sending anything but a dict or list back from a REST API'

        raise TypeError(message)

    response: Response
    response = jsonify(responsified)

    return response


def responsify_list(iter: list) -> list:
    responsified = [responsify_dict(x) for x in iter]
    responsified = tuple(responsified)

    return responsified


def responsify_dict(obj: dict) -> dict:
    response: dict
    response = {}

    for key, value in obj.items():

        if isinstance(value, (datetime, date)):
            value: datetime | date
            value = value.isoformat()
        
        if isinstance(value, Decimal):
            value: Decimal
            value = float(value)
        
        if isinstance(key, str):
            key = underscore_to_camel(key)

        response[key] = value

    return response


def build_query_string(request: Request):
    query: str
    path: str
    full_path: str

    path = request.path
    full_path = request.full_path

    query = full_path[len(path):]

    return query


def build_query_object(query_string: str):
    obj: dict[str, list]
    obj = {}

    query_string_params: str
    query_string_params = query_string[1:]

    if query_string_params == '':
        return obj

    query_string_params = query_string_params.split('&')
    query_string_param_items = [tuple(x.split('='))
                                for x in query_string_params]

    for key, value in query_string_param_items:
        values = value.split(',')
        
        if key in obj:
            obj[key].extend(values)
        
        else:
            obj[key] = values

    return obj


def clean_query_object(accepted_filter_keys: list[str], query_object: dict):
    filtered_obj: dict
    filtered_obj = {}

    accepted_filter_keys = [x.lower() for x in accepted_filter_keys]

    query_object_items = query_object.items()
    query_object_items = list(query_object_items)

    values: list[str]
    for key, values in query_object_items:

        key = key.lower()

        for index, value in enumerate(values):
            
            if value.isnumeric():
                value = int(value)
            if isinstance(value, str) and value.lower() == 'true':
                value = True
            if isinstance(value, str) and value.lower() == 'false':
                value = False

            values[index] = value

        if key in accepted_filter_keys:
            filtered_obj[key] = values

    return filtered_obj
