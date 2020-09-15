from rest_framework.serializers import ModelSerializer

from api.models import ProductSet, Recipient, Order


class ProductSetSerializer(ModelSerializer):
    class Meta:
        model = ProductSet
        fields = '__all__'


class RecipientSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'


class EditRecipientSurnameSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = ['surname']


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class AddressEditionSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['delivery_address']


class StatusEditionSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
