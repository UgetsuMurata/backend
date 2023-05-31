from rest_framework import serializers
from penny_one.models.orderModels import order, order_items, products, food, drink

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_items
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = '__all__'

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = drink
        fields = '__all__'
