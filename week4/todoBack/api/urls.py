from django.conf.urls import url
from .views import task_list, task_list_detail

urlpatterns = [
    url('tasks', task_list),
    url('tasks/<int:pk>', task_list_detail),
]