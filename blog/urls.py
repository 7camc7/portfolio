from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]

