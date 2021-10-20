from django.urls import path, include
from rest_framework import routers
#from .views import TrainViewSet
from .views import post
#router = routers.DefaultRouter()
#router.register(r'train', TrainViewSet, basename="train")

# Wire up our API using automatic URL routing.
urlpatterns = [
    #path('', views.TrainViewSet.apiOverview, name="api-overview"),
    #path('',views.home),
    #path('train/', views.TrainViewSet.modelCreate, name="train"),
    path("kkk",post)
    
]