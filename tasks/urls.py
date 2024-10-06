from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('create_task', create_task, name='create_task')
]