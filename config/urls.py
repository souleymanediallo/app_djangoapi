
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", include("books.urls")),
    path("auth/", obtain_auth_token, name="api_token_auth"),
    path("movies/", include("movies.urls")),
    #path('api/', include('rest_framework.urls'))
]
