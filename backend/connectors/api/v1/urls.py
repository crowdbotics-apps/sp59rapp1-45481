from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import testConnector1ViewSet

router = DefaultRouter()
router.register("testconnector1", testConnector1ViewSet, basename="testconnector1")

urlpatterns = [
    path("connectors/", include(router.urls)),
]
