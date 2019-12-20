from rest_framework import serializers
from .models import Payment, Product


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("customer_id", "amount")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"