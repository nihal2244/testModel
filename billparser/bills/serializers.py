from rest_framework import serializers
from bills import models


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.User
        fields=['id,','user_name','auth','created_ta']

class billSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Bills
        fields=['id,','user_name','auth','created_at']