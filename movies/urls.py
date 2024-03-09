from django.urls import path, include
from . import views
from rest_framework import routers

from .views import MovieView, RatingView, UserView

router = routers.DefaultRouter()
router.register('movies', MovieView)
router.register('ratings', RatingView)
router.register('users', UserView)

urlpatterns = [
    path('api/', include(router.urls)),
]

