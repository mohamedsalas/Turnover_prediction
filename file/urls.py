from django.urls import path, include
from rest_framework import routers
from .views import UploadViewSet

router = routers.DefaultRouter()
router.register(r'file', UploadViewSet, basename="file")

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
    
    
]