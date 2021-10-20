
from django.contrib import admin
from django.urls import path, include
import train
from django_ML_API.views import align,hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(("train.urls", "train"), namespace="train")),
    path('', hello),
    path('align/', align),
   # path(r"", include(("file.urls", "file"), namespace="file")),
    path(r"", include(("train.urls", "train"), namespace="train"))

]
