# standard models
import os
import json

# external models
from sanic import Sanic
from sanic.response import json as sanic_json
from sanic.exceptions import SanicException
from sanic.request import Request
from sanic_jwt import Initialize, exceptions
from sanic_jwt.decorators import protected

# proprietary models
from logger_setup import setup_logging

SUPPORTED_LOG_LVL = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET']
LOG_LVL = os.environ.get('LOG_LVL') if os.environ.get('LOG_LVL') in SUPPORTED_LOG_LVL else "INFO"
BASE_ROUTE = '/api/v1/'

logger = setup_logging(LOG_LVL)

app = Sanic(name='normalizer')
with open('./my_auth.json', 'r') as json_input:
    Users = json.loads(json_input.read())

async def authenticate(request, *args, **kwargs):
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = Users.get(username)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.get('password'):
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user


Initialize(
    app,
    authenticate=authenticate,
)


@app.exception(Exception)
async def no_details_to_user(request: Request, exception: Exception):
    if isinstance(exception, SanicException):
        return sanic_json({'status_code': exception.status_code, 'msg': str(exception)})
    logger.exception(exception)
    return sanic_json({'status_code': 500, 'msg': str(exception)})


@app.route(BASE_ROUTE + 'norm', methods=['POST'])
@protected()
async def norm(request):
    """
    Returns the stats of all the words we scanned
    :param request: (str) the query params of the GET request - not used here
    :return: (str) a json object with the severs stats
    """
    logger.info("Getting stats")
    normalized = {value.get("name"): v for value in json.loads(request.body)
                  for
                  k, v in value.items() if 'val' in str(k).lower()}
    return sanic_json(normalized)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
