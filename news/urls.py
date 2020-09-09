from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog/<slug>', views.blog, name='blog'),
    path('details', views.details, name='details'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('main-menu-details/<name>', views.mainmenudetails, name='main-menu-details'),
    path('sub-menu-details/<name>', views.submenudetails, name='sub-menu-details'),
]
