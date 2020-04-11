from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from .views import MyUserViewSet, RegisterUserApiView

urlpatterns = [
    url('login', obtain_jwt_token),
    url('register', RegisterUserApiView.as_view()),
]

router = DefaultRouter()
router.register('auth', MyUserViewSet, basename='auth')

urlpatterns += router.urls
