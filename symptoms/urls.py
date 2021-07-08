from django.urls import path
from . import views

app_name = 'symptoms'

urlpatterns = [
    
    #symptoms view
    path('',views.Symname,name ="Symname")
    
]

