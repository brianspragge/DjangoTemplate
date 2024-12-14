from django.urls import path
from . import views

app_name = 'message'
urlpatterns = [
    path('', views.conversations_list, name='conversations_list'),
    path('conversation/<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),
    path('new/', views.new_conversation, name='new_conversation'),
]
