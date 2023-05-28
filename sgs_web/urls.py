from django.urls import path
from sgs_web import views 
# from .views import home
urlpatterns=[
    path('', views.home)
]