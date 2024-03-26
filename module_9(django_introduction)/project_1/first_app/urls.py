from django.urls import path
# from .views import contact, home
from . import views

urlpatterns = [
    path("courses/", views.courses),
    path("about/", views.about),
    path("", views.first_app_home)
]
