from django.urls import path
from . import views

app_name = 'mail'
urlpatterns = [
    path('send/', views.send_email, name='send_email'),
    path('inbox/', views.inbox, name='inbox'),
]
