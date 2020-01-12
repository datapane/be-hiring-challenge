from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status


def create_http_response_with_attachment(file, content_type, file_name):
    response = HttpResponse(
        file, content_type=content_type
    )
    response['Content-Disposition'] = (
        f'attachment; filename="{file_name}"'
    )

    return response


def create_response_body(**kwargs):
    data = {}
    for k, v in kwargs.items():
        data[k] = v

    return data


def create_success_response(**kwargs):
    data = create_response_body(**kwargs)
    response = Response(
        data=data,
        status=status.HTTP_200_OK
    )

    return response
