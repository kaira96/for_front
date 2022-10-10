from django.forms import ValidationError
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
            'is_stockman',
            'is_accountant',
            'password'
        )
        # read_only_fields = (
        #     'is_stockman',
        #     'is_accountant',
        # )

        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self, attrs):
        if attrs.get('is_stockman') and attrs.get('is_accountant'):
            raise ValidationError('Пользователь не может быть одновременно сотрудником склада и бухгалтером.')

        return attrs

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
