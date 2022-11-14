
  
from rest_framework.exceptions import APIException


class UserDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested user does not exist.'


class UserAlreadyExists(APIException):
    status_code = 400
    default_detail = 'This user already exists.'
