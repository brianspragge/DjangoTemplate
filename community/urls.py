from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('create/', views.create_server, name='create_server'),
    path('list/', views.server_list, name='server_list'),
    path('server/<int:server_id>/', views.server_channels, name='server_channels'),
    path('channel/<int:channel_id>/', views.channel_chat, name='channel_chat'),
]
