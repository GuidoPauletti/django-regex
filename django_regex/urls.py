from django.urls import path
from regexdetector import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.get_email_and_phone, name='get_email_and_phone')
]
