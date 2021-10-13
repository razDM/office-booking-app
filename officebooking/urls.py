"""officebooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from officebooking.views import homepage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view),
    path('offices/', include('offices.urls')),
    path('zones/', include('zones.urls')),
    path('floors/', include('floors.urls')),
    path('users/', include('users.urls'))]
    # path('offices/', include(('offices.urls','offices'),namespace='offices')),
    # path('zones/', include(('zones.urls','zones'),namespace='zones')),
    # path('floors/', include(('floors.urls','floors'),namespace='floors')),
    # path('users/', include(('users.urls','users'),namespace='users'))
