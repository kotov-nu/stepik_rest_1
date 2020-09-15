from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.models import ProductSet, Recipient, Order
from api.serializers import ProductSetSerializer, RecipientSerializer, OrderSerializer, AddressEditionSerializer, \
    StatusEditionSerializer, EditRecipientSurnameSerializer


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
            return Response(serializer.data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class EditRecipientSurnameViewSet(ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

    @action(detail=True, methods=['patch'])
    def edit_surname(self, request):
        if 'surname' not in request:
            return Response('Не указано поле surname', status=HTTP_400_BAD_REQUEST)
        if 'id' not in request:
            return Response('Не указано поле id', status=HTTP_400_BAD_REQUEST)
        recipient = Recipient.objects.get(id=request['id'])
        serializer = EditRecipientSurnameSerializer(recipient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class OrderModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch']
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['order_created_datetime']
    search_fields = ['order_created_datetime']

    @action(detail=True, methods=['patch'])
    def change_delivery_address(self, request):
        if 'address' not in request:
            return Response('Не указано поле address', status=HTTP_400_BAD_REQUEST)
        if 'id' not in request:
            return Response('Не указано поле id', status=HTTP_400_BAD_REQUEST)
        delivery_address = get_object_or_404(request['id'])
        serializer = AddressEditionSerializer(delivery_address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'])
    def change_order_status(self, request):
        if 'status' not in request:
            return Response('Не указано поле status', status=HTTP_400_BAD_REQUEST)
        if 'id' not in request:
            return Response('Не указано поле id', status=HTTP_400_BAD_REQUEST)
        order_status = get_object_or_404(request['id'])
        serializer = StatusEditionSerializer(order_status, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
