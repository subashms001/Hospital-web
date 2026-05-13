"""
URL configuration for learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static  # make dynamic img as static
from django.conf import settings   # make dynamic img as static


urlpatterns = [
    path('',include('learnapp.urls')),
    path('doctiors/',include('doctors.urls')),
    path('labreports/',include('labreports.urls')),
    path('payment/',include('payment.urls')),
    path('admin/', admin.site.urls), 
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  # make dynamic img as static
