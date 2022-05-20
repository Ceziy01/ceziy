from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('resourcepack', views.rp, name='resourcepack')
]
