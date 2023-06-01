from rest_framework import serializers
from penny_one.models.userModels import user, user_info

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_info
        fields = '__all__'
