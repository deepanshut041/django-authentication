from django.conf.urls import re_path, include, url
from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'^login/', obtain_jwt_token, name="Login"),
]