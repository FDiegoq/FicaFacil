from django.urls import path
from .views import *

urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', exitlogout, name='logout'),
    path('complete_profile', complete_profile, name='complete_profile')
]