"""
URL configuration for decentralized_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .home.views import dashboard, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((
        [
            path('', dashboard, name='dashboard'),
            path('search/', search, name='search'),
        ],
        'home'  # app_name for this set of URLs
    ), namespace='home')),
    path('user_auth/', include('user_auth.urls', namespace='user_auth')),
    path('mail/', include('mail.urls', namespace='mail')),
    path('group/', include('group.urls', namespace='group')),
    path('community/', include('community.urls', namespace='community')),
    path('social/', include('social.urls', namespace='social')),
    path('message/', include('message.urls', namespace='message')),
]
