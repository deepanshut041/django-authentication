from django.conf.urls import url
from django.urls import path, include, re_path

from .views import LandingPageView, AuthPageView

urlpatterns = [
    path('', LandingPageView.as_view()),
    path('auth/', AuthPageView.as_view()),
]