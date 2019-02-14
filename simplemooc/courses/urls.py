from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<slug>[\w_-]+)/', views.details, name='details')
]
