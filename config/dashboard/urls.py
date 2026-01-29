from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('company/<int:pk>/', views.company_detail, name='company_detail'),
    path('set-location/', views.set_current_location, name='set_location'),
    path('facilities/', views.facilities, name='facilities'),
    path('toilets/', views.toilets, name='toilets'),
]
