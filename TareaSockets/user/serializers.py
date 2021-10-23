from rest_framework import serializers
from .models import user_homework

class User(serializers.ModelSerializer):
    class Meta:
        model = user_homework
        fields = '__all__'




