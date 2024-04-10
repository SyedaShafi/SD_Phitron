"""
URL configuration for car_sale_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from cars.views import profile
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "homepage"),
    path('profile/', profile, name = "profile"),
    path('sort_by_category/<int:id>', views.home, name = "sort_category"),
    path('change_password/', views.password_change, name = "change_password"),
    path('set_password/', views.set_password, name = "set_password"),
    path('signup/', views.register, name = "register"),
    path('login/', views.UserLoginView.as_view(), name = "user_login"),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),
    path('car/', include('cars.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)