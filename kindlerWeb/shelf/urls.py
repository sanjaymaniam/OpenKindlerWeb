"""kindlerWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shelf'

urlpatterns = [
    path('', views.book_list_view, name='bookshelf'),
    path('<int:book_id>/', views.book_view, name='book_view'),
    path('<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('manager/<int:book_id>/<int:clipping_id>/', views.clipping_manager, name='clipping_manager'),
    path('<int:book_id>/<int:clipping_id>/edit/', views.edit_clipping, name='edit_clipping'),
]