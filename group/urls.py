from django.urls import path
from . import views

app_name = 'group'
urlpatterns = [
    path('create/', views.create_group, name='create_group'),
    path('list/', views.group_list, name='group_list'),
    path('<int:group_id>/', views.group_chat, name='group_chat'),
]
