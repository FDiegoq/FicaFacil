from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', exitlogout, name='logout'),
    path('complete_profile', complete_profile, name='complete_profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)