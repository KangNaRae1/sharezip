"""sharezip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
import browse.views
import hosting.views
import message.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',browse.views.base, name='base'),
    path('findroom/',browse.views.findroom, name='findroom'),
    path('detail/<int:room_id>',browse.views.detail, name='detail'),
    path('test/', browse.views.test, name='test'),
    
    path('hosting1/', hosting.views.hosting1, name="hosting1"),
    path('create1/', hosting.views.create1, name="create1"),
    path('create2/', hosting.views.create2, name="create2"),
    path('hosting2/', hosting.views.hosting2, name="hosting2"),
    
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    
    path('message/<str:sender>/',message.views.mbox, name="mbox"),
    path('message/<str:sender>/<str:receiver>/',message.views.mdetail, name="mdetail"),
    path('sendMessage/',message.views.sendMessage,name="sendMessage"),
    path('send/<str:receiver>',message.views.new, name='new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

