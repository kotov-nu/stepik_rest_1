from json import JSONDecodeError

from requests import ConnectTimeout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_408_REQUEST_TIMEOUT, \
    HTTP_500_INTERNAL_SERVER_ERROR

from api.data_retrieval import get_recipients as recipients, get_food_boxes as food_boxes

ERROR_MESSAGE_500 = {"error": "Невалидный ответ"}
ERROR_MESSAGE_408 = {"error": "Сервер не отвечает, попробуйте позже"}
ERROR_MESSAGE_404 = {"error": "Информация по запросу отсутствует"}
ERROR_MESSAGE_400 = {"error": "Неверные данные запроса"}


@api_view(http_method_names=['GET'])
def get_recipients(request: Request) -> Response:
    """ Все получатели. """
    try:
        return Response(recipients())
    except ConnectTimeout:
        return Response(ERROR_MESSAGE_408, status=HTTP_408_REQUEST_TIMEOUT)
    except (JSONDecodeError, TypeError):
        return Response(ERROR_MESSAGE_500, status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(http_method_names=['GET'])
def get_recipient(request: Request, recipient_pk: int) -> Response:
    """ Получатель. """
    try:
        return Response(recipients()[recipient_pk])
    except IndexError:
        return Response(ERROR_MESSAGE_404, status=HTTP_404_NOT_FOUND)


@api_view(http_method_names=['GET'])
def get_food_boxes(request: Request) -> Response:
    """ Все боксы с едой. """
    try:
        if request.query_params:
            min_price = request.query_params.get('min_price')
            min_weight = request.query_params.get('min_weight')
            if min_price and min_weight:
                return Response(ERROR_MESSAGE_400, status=HTTP_400_BAD_REQUEST)
            if not min_price and not min_weight:
                return Response(ERROR_MESSAGE_400, status=HTTP_400_BAD_REQUEST)
            if min_price:
                return Response(food_boxes(min_price=int(min_price)))
            if min_weight:
                return Response(food_boxes(min_weight=int(min_weight)))
        return Response(food_boxes())
    except ConnectTimeout:
        return Response(ERROR_MESSAGE_408, status=HTTP_408_REQUEST_TIMEOUT)
    except (JSONDecodeError, TypeError):
        return Response(ERROR_MESSAGE_500, status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(http_method_names=['GET'])
def get_box(request: Request, box_pk: int) -> Response:
    """ Бокс с едой. """
    try:
        return Response(food_boxes()[box_pk])
    except IndexError:
        return Response(ERROR_MESSAGE_404, status=HTTP_404_NOT_FOUND)
