from django.contrib import admin
from django.urls import include, path

from .views import TaskDetail, TaskList, create_task, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/tasks/', TaskList.as_view()),
    path('api/tasks/<int:pk>/', TaskDetail.as_view()),
    path('api/tasks/create/', create_task),
]
