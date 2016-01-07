from rest_framework.routers import DefaultRouter

from .viewsets.users import UserViewSet


# Ember does POST to /projects (not /projects/), so we need this:
router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
