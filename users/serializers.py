from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'
    def create(self, validated_data):
        print(validated_data)
        user = super().create(validated_data)
        print(user)
        password = user.password
        user.set_password(password)
        user.save()
        # password.save()
        return user

class HJTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['token_message'] = "sparta_time_attack"

        return token

