from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.TesteView.as_view(), name = 'landing')
]
