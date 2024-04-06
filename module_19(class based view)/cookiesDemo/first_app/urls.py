from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='homepage'),
    path('get_cookie/', views.get_cookie, name='cookies'),
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('delete_session/', views.delete_session, name='delete_session'),
    path('delete/', views.delete_cookie, name='delete_cookie'),
]
