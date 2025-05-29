from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/',views.About_view, name='about'),
    path('blog/',views.blog_view,name='blog')
]