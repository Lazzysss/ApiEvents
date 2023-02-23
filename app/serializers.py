from rest_framework import serializers
from django.utils import timezone
from app.models import User, Event, Calendar
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=45)


class EventSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=45)
	location = serializers.CharField(max_length=45)
	start = serializers.DateTimeField()
	end = serializers.DateTimeField()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", )
#a 
