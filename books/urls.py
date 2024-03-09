from django.urls import path, include
from . import views
from rest_framework import routers

from .views import BookView

router = routers.DefaultRouter()
router.register('books', BookView)

urlpatterns = [
    path('api/', include(router.urls)),

]