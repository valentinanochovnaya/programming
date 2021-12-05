from drf_yasg import openapi
from .models import POSITION_CHOICES


class SwaggerDocDicts:
    FREELANCER_EXAMPLE = {
        "name": "string",
        "email": "string",
        "phone_number": "phone number",
        "availability": 'number',
        "salary": 'number',
        "position": "position"
    }

    FREELANCER_NOT_FOUND_RESPONSE = {
        "status": 404,
        "message": "Freelancer not found"
    }

    FREELANCER_BAD = {
        "status": 400,
        "errors": {
            "field_1": "error_1",
            "field_2": "error_2"
        }
    }

    FREELANCER_CREATE_RESPONSE = {
        "status": 200,
        "message": "Freelancer successfully created",
        "freelancer": FREELANCER_EXAMPLE
    }

    FREELANCER_UPDATE_RESPONSE = {
        "status": 200,
        "message": "Freelancer successfully updated",
        "freelancer": FREELANCER_EXAMPLE
    }

    FREELANCER_DELETE_RESPONSE = {
        "status": 200,
        "message": "Successfully deleted!"
    }

    FREELANCER_INPUT_PARAMETER = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "name": openapi.Schema(type=openapi.TYPE_STRING,
                                   description='Name',
                                   max_length=256),
            "email": openapi.Schema(type=openapi.TYPE_STRING,
                                    description='Email',
                                    max_length=8),
            "phone_number": openapi.Schema(type=openapi.TYPE_STRING,
                                           description='Phone number',
                                           ),
            "availability": openapi.Schema(type=openapi.TYPE_STRING,
                                           description='Availability',
                                           ),
            "salary": openapi.Schema(type=openapi.TYPE_STRING,
                                     description='Salary',
                                     ),
            "position": openapi.Schema(type=openapi.TYPE_STRING,
                                       description="Position",
                                       enum=POSITION_CHOICES,
                                       max_length=64),
        })


class EndpointDocs:
    GET_LIST = {
        "operation_description": "Get list of all Freelancers from database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain list of all freelancers from database",
                examples={
                    "application/json": [
                        SwaggerDocDicts.FREELANCER_EXAMPLE,
                    ]
                }
            ),
        }
    }

    POST = {
        "request_body": SwaggerDocDicts.FREELANCER_INPUT_PARAMETER,
        "operation_description": "Insert new Freelancer into a database",
        "responses": {
            "200": openapi.Response(
                description="Valid freelancer sent -> write to database",
                examples={
                    "application/json": SwaggerDocDicts.FREELANCER_CREATE_RESPONSE
                }
            ),
            "400": openapi.Response(
                description="Invalid freelancer sent -> discard",
                examples={
                    "application/json": SwaggerDocDicts.FREELANCER_BAD
                }
            ),
        }
    }

    GET = {
        "operation_description": "Get Freelancer by id from database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain freelancer from database",
                examples={
                    "application/json": SwaggerDocDicts.FREELANCER_EXAMPLE
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": SwaggerDocDicts.FREELANCER_NOT_FOUND_RESPONSE
                }
            ),
        }
    }

    PUT = {
        "request_body": SwaggerDocDicts.FREELANCER_INPUT_PARAMETER,
        "operation_description": "Edit Freelancer record by ID in database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain freelancer from database",
                examples={
                    "application/json": SwaggerDocDicts.FREELANCER_UPDATE_RESPONSE
                }
            ),
            "400": openapi.Response(
                description="Invalid freelancer sent -> discard",
                examples={
                    "application/json": SwaggerDocDicts.FREELANCER_BAD
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": SwaggerDocDicts.FREELANCER_NOT_FOUND_RESPONSE
                }
            ),
        }
    }

    DELETE = {
        "operation_description": "Delete Freelancer by id from database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain freelancer from database",
                examples={
                    "application/json": SwaggerDocDicts.FREELANCER_DELETE_RESPONSE
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": SwaggerDocDicts.FREELANCER_NOT_FOUND_RESPONSE
                }
            ),
        }
    }
