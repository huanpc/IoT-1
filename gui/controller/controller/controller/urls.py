"""controller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from iot_platform import views as iot_platform_view
from sensor import views as sensor_view
from django.views.generic import TemplateView
from iot_platform import views

router = routers.DefaultRouter()
router.register(r'platforms', iot_platform_view.PlatformViewSet)
router.register(r'sensors', sensor_view.SensorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^metrics$', TemplateView.as_view(template_name='index.html')),
    url(r'^xml_query/(?P<time_stamp>[0-9]+)$', views.ajax_get_xml, name='xml_query'),
]
