from rest_framework import serializers
from .models import PurchaseOrder


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        
    def validate(self, data):
        order_date = data.get('order_date')
        delivery_date = data.get('delivery_date')

        if order_date >= delivery_date:
            raise serializers.ValidationError("Order date must be before delivery date")

        return data