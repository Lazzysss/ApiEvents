from django.shortcuts import render
from django.http import JsonResponse
from app.models import User, Event, Calendar
from rest_framework.decorators import api_view
from app.serializers import UserSerializer, EventSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework import permissions

from .serializers import UserSerializer

@api_view(['GET'])
def home(request):
	user = User.objects.all()
	serializer = UserSerializer(user, many=True)
	event = Event.objects.all()
	serializer = EventSerializer(event, many=True)
	return Response(serializer.data)


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer