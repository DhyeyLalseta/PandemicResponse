from django.urls import path
from . import views

urlpatterns = [
    # Sets up base url to display home view.
    path('', views.home, name='landing'),
]
