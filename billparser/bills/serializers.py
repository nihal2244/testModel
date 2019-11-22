from rest_framework import serializers
from bills import models


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.User
        fields=['id','userName','auth','createdAt']

class billSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Bills
        fields=['id','user_id','invoice','vender','buyer','bill_date','bill_items','bill_path','digitized']