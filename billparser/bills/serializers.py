from rest_framework import serializers
from bills import models


class EndUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.

class InternalUserSerializer(serializers.ModelSerializer):
    pass