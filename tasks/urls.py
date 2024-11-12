from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('create_task', create_task, name='create_task'),
    path('finish_task/<int:id>', finish_task, name='finish_task'),
    path('restore_task/<int:id>', restore_task, name='restore_task'),
    path('done_tasks', done_tasks, name='done_tasks'),
    path('profile', profile, name='profile'),
    path('edit_task/<int:id>', edit_task, name='edit_task'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('task_details/<int:id>', task_details, name='task_details'),
    path('tasks_dashboard', tasks_dashboard, name='dashboard'),
    path('task_filters', task_filters, name='task_filters'),
    path('search', search_view, name='search')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)