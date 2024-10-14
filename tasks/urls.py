from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('create_task', create_task, name='create_task'),
    path('finish_task/<int:id>', finish_task, name='finish_task'),
    path('done_tasks', done_tasks, name='done_tasks'),
    path('edit_task', edit_task, name='edit_task'),
    path('delete_task', delete_task, name='delete_task')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)