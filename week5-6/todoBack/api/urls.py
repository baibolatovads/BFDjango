from django.conf.urls import url
from .views import TaskViewSet, TaskListViewSet
from rest_framework.routers import DefaultRouter


"""urlpatterns = [
    url('tasks', TaskListAPIView.as_view()),
    url('tasks/<int:pk>', task_list_detail),
]"""

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'task_list', TaskListViewSet, basename='task_list')
urlpatterns = router.urls
