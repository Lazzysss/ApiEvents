from django.urls import path
from app.views import home, CreateUserView

urlpatterns = [
	path('', home),
    path('auth', CreateUserView.as_view())
]