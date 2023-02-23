from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Calendar(models.Model):
	UserID = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField('Названия календаря', max_length=45)

	def __str__(self):
		return f'{self.UserID.name} ({self.id})'


class Event(models.Model):
	CalendarID = models.ForeignKey(Calendar, on_delete=models.CASCADE)
	UserID = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField('Названия эвента', max_length=45)
	location = models.CharField('Локация', max_length=45)
	start = models.DateTimeField(auto_now_add=timezone.now())
	end = models.DateTimeField(auto_now_add=False)

	def __str__(self):
		return f'{self.CalendarID} {self.id}'


class Invites(models.Model):
	EventsId = models.ForeignKey(Event, on_delete=models.CASCADE)
	UserId = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.EventsId.name} ({self.id})'