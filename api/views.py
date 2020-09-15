from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from api.models import ProductSet, Recipient
from api.serializers import ProductSetSerializer, RecipientSerializer


class ProductSetModelViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = ProductSet.objects.all()
    serializer_class = ProductSetSerializer


class RecipientModelViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class EditRecipientAddressViewSet(ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

    def partial_update(self, request, *args, **kwargs):
        if 'address' not in request:
            return Response('Не указано поле address', status=HTTP_400_BAD_REQUEST)
        if 'id' not in request:
            return Response('Не указано поле id', status=HTTP_400_BAD_REQUEST)
        recipient = get_object_or_404(request['id'])
        serializer = RecipientSerializer(recipient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class EditRecipientSurnameViewSet(ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

    def partial_update(self, request, *args, **kwargs):
        if 'surname' not in request:
            return Response('Не указано поле surname', status=HTTP_400_BAD_REQUEST)
        if 'id' not in request:
            return Response('Не указано поле id', status=HTTP_400_BAD_REQUEST)
        recipient = Recipient.objects.get(id=request['id'])
        serializer = RecipientSerializer(recipient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# from api.data_retrieval import get_recipients as recipients, get_food_boxes as food_boxes
#
# ERROR_MESSAGE_500 = {"error": "Невалидный ответ"}
# ERROR_MESSAGE_408 = {"error": "Сервер не отвечает, попробуйте позже"}
# ERROR_MESSAGE_404 = {"error": "Информация по запросу отсутствует"}
# ERROR_MESSAGE_400 = {"error": "Неверные данные запроса"}
#
#
# @api_view(http_method_names=['GET'])
# def get_recipients(request: Request) -> Response:
#     """ Все получатели. """
#     try:
#         return Response(recipients())
#     except ConnectTimeout:
#         return Response(ERROR_MESSAGE_408, status=HTTP_408_REQUEST_TIMEOUT)
#     except (JSONDecodeError, TypeError):
#         return Response(ERROR_MESSAGE_500, status=HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# @api_view(http_method_names=['GET'])
# def get_recipient(request: Request, recipient_pk: int) -> Response:
#     """ Получатель. """
#     try:
#         return Response(recipients()[recipient_pk])
#     except IndexError:
#         return Response(ERROR_MESSAGE_404, status=HTTP_404_NOT_FOUND)
#
#
# @api_view(http_method_names=['GET'])
# def get_food_boxes(request: Request) -> Response:
#     """ Все боксы с едой. """
#     try:
#         if request.query_params:
#             min_price = request.query_params.get('min_price')
#             min_weight = request.query_params.get('min_weight')
#             if min_price and min_weight:
#                 return Response(ERROR_MESSAGE_400, status=HTTP_400_BAD_REQUEST)
#             if not min_price and not min_weight:
#                 return Response(ERROR_MESSAGE_400, status=HTTP_400_BAD_REQUEST)
#             if min_price:
#                 return Response(food_boxes(min_price=int(min_price)))
#             if min_weight:
#                 return Response(food_boxes(min_weight=int(min_weight)))
#         return Response(food_boxes())
#     except ConnectTimeout:
#         return Response(ERROR_MESSAGE_408, status=HTTP_408_REQUEST_TIMEOUT)
#     except (JSONDecodeError, TypeError):
#         return Response(ERROR_MESSAGE_500, status=HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# @api_view(http_method_names=['GET'])
# def get_box(request: Request, box_pk: int) -> Response:
#     """ Бокс с едой. """
#     try:
#         return Response(food_boxes()[box_pk])
#     except IndexError:
#         return Response(ERROR_MESSAGE_404, status=HTTP_404_NOT_FOUND)
