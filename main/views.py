from django.views import generic
from django.shortcuts import render

class LandingView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing.html')