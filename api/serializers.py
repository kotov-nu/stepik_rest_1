from rest_framework.serializers import ModelSerializer

from api.models import ProductSet, Recipient, Order


class ProductSetSerializer(ModelSerializer):
    class Meta:
        model = ProductSet
        fields = [
            'id',
            'title',
            'description',
        ]


class RecipientSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = [
            'id',
            'surname',
            'name',
            'patronymic',
            'phone_number',
            'delivery_address',
        ]


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'order_created_datetime',
            'delivery_datetime',
            'recipient',
            'product_set',
            'status',
        ]
