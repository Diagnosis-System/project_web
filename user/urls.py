from django.urls import path
from .views import user_login
urlpatterns = [
    path('', user_login, name='login'),
]
