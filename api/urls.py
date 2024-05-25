from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import PumpViewSet

router = routers.DefaultRouter()
router.register("pumps", PumpViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
