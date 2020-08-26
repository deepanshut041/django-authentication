from django.http import Http404
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import generics, permissions, status, views
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken

from ..models.accounts import UserProfile
from ..serializers.accounts import (UserRegistrationSerializer, UserLoginSerializer, UserSerializer,
 UserProfileSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer)

User = get_user_model()


class UserRegistrationAPIView(generics.CreateAPIView):
    """
    Endpoint for user registration.
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class UserEmailVerificationAPIView(views.APIView):
    """
    Endpoint for verifying email address.
    """

    permission_classes = (permissions.AllowAny, )

    def get(self, request, verification_key):
        activated_user = self.activate(verification_key)
        if activated_user:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def activate(self, verification_key):
        return UserProfile.objects.activate_user(verification_key)


class UserLoginView(ObtainJSONWebToken):
    """
    Endpoint for user login.
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = UserLoginSerializer


class PasswordResetAPIView(views.APIView):
    """
    Endpoint to send email to user with password reset link.
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = PasswordResetSerializer

    def post(self, request):
        user_profile = self.get_user_profile(request.data.get('email'))
        if user_profile:
            # user_profile.send_password_reset_email(
            #     site=get_current_site(request)
            # )
            return Response(status=status.HTTP_200_OK)

        # Forcing Http status to 200 even if failure to support user privacy.
        # Will show message at frontend like "If the email is valid, you must have received password reset email"
        return Response(status=status.HTTP_200_OK)

    def get_user_profile(self, email):
        try:
            user_profile = UserProfile.objects.get(user__email=email)
        except:
            return None
        return user_profile


class PasswordResetConfirmView(views.APIView):
    """
    Endpoint to change user password.
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            data=request.data,
            context={
                'uidb64': kwargs['uidb64'],
                'token': kwargs['token']
            })

        if serializer.is_valid(raise_exception=True):
            new_password = serializer.validated_data.get('new_password')
            user = serializer.user
            user.set_password(new_password)
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(generics.RetrieveAPIView, generics.UpdateAPIView):
    """
    Endpoint to retrieve user profile.
    """

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = UserProfileSerializer

    def get_object(self):
        try:
            return self.request.user.userprofile
        except UserProfile.DoesNotExist:
            raise Http404