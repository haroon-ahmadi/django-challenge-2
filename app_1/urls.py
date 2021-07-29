from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('book/list', views.book_list, name='book_list'),
]
