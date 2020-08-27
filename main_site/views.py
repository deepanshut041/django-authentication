import json

from django.shortcuts import render
from django.views.generic.base import View


class LandingPageView(View):
    def get(self, request):
        return render(request, "landing_page.html")

class AuthPageView(View):
    def get(self, request):
        return render(request, "auth_page.html")