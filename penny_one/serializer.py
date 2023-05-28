from rest_framework import serializers
from penny_one.models import user, user_info, ewallet, recovery_codes, ewallet_transaction, points, points_transaction,\
                            reward, order, order_items, products, food, drink


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_info
        fields = '__all__'

class EwalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ewallet
        fields = '__all__'

class RecoveryCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = recovery_codes
        fields = '__all__'


class EwalletTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ewallet_transaction
        fields = '__all__'

class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = points
        fields = '__all__'


class PointsTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = points_transaction
        fields = '__all__'


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = reward
        fields = '__all__'


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

