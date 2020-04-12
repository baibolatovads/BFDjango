from django.conf.urls import url
from .views import task_list, task_list_detail, TaskListAPIView, TaskListViewSet
from rest_framework.routers import DefaultRouter


"""urlpatterns = [
    url('tasks', TaskListAPIView.as_view()),
    url('tasks/<int:pk>', task_list_detail),
]"""

router = DefaultRouter()
router.register(r'tasks', TaskListViewSet)
urlpatterns = router.urls
