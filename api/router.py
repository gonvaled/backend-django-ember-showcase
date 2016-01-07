from rest_framework.routers import DefaultRouter

from .viewsets.users import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
