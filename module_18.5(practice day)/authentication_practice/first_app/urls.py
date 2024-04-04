from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "homepage"),
    path('signup/', views.user_register, name = "user_register"),
    path('profile/', views.profile, name = "profile"),
    path('logout/', views.user_logout, name = "user_logout"),
    path('login/', views.user_login, name = "user_login"),
    path('password_change/', views.password_change, name = "password_change"),
    path('set_password/', views.set_password, name = "set_password"),
]
