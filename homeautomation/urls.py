"""homeautomation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
from Manage.views.LightsView import manage_lights
from Manage.views.HomeAssistantView import HomeAssistantView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'Manage/lights', manage_lights),
    url(r'HA/status/([a-z,A-Z,0-9,\.,_]*)$', HomeAssistantView.status),
    url(r'HA/turn_on/([a-z,A-Z,0-9,\.,_]*)$', HomeAssistantView.turn_on),
    url(r'HA/turn_off/([a-z,A-Z,0-9,\.,_]*)$', HomeAssistantView.turn_off),
    url(r'HA/turn_on/([a-z,A-Z,0-9,\.,_]*)/([0-9]{1,3})$', HomeAssistantView.turn_on),
]
