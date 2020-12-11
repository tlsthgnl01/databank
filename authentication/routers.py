from rest_framework import routers

from authentication import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', views.UserViewSet)
