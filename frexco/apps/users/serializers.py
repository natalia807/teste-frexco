from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    login = serializers.CharField()
    dateNasc = serializers.DateField()
   
    class Meta:
        model = User
        fields = ('login', 'dateNasc',)
        read_only_fields = ('login',)

 