from rest_framework.response import Response


class _Response(Response):
    def __init__(self, data=None, status=None, message=None, **kwargs):
        response = {
            'status': "ok" if status in [200, 201, 204] else "error",
            'message': message,
            'data': data
        }

        super().__init__(data=response, status=status, **kwargs)