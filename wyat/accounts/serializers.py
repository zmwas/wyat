from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        if user:
            token = Token.objects.create(user=user)
            print token.key
        return user


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
