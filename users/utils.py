from rest_framework_jwt.utils import jwt_payload_handler


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username,
        # Add any other user-related data you want to include in the response
    }
