from django.conf.urls import re_path, include, url
from rest_framework import routers
from rest_framework import permissions


from .views.accounts import (UserEmailVerificationAPIView, UserProfileAPIView, UserRegistrationAPIView, 
                           UserLoginView, PasswordResetAPIView, PasswordResetConfirmView)

urlpatterns = [
   url(r'^auth/login/', UserLoginView.as_view(), name='login'),
   url(r'^auth/register/', UserRegistrationAPIView.as_view(), name='regsiter'),
   url(r'^auth/verify/(?P<verification_key>.+)/$', UserEmailVerificationAPIView.as_view(), name='email_verify'),
   url(r'^auth/password_reset/$', PasswordResetAPIView.as_view(), name='password_change'),
   url(r'^auth/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   url(r'^user/profile/$', UserProfileAPIView.as_view(), name='user_profile'),
]