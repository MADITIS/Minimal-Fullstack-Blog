from urllib import response
from django.http import HttpRequest


class RequestInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        print("Got request")
        response = self.get_response(request)
        print("Got response")
        return response
