from django.urls import path, include
from . import views
from rest_framework import routers

from .views import MovieView

router = routers.DefaultRouter()
router.register('movies', MovieView)
router.register('ratings', views.RatingView)

urlpatterns = [
    path('api/', include(router.urls)),
]

