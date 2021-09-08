from django.views import generic
from django.shortcuts import render

class TesteView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')