"""PS_DIARY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime

AuthenticationForm.current_batch = datetime.today().year - 2

urlpatterns = [
	url('admin/', admin.site.urls),
	url('PS2/', include('PS2.urls')),
    url('dev_page/', include('dev_page.urls')),
    path('', include('django.contrib.auth.urls')),
    url(r'^celery-progress/', include('celery_progress.urls')),
]
