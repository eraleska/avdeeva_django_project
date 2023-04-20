from django.urls import path
from . import views
urlpatterns = [
    path('', views.notes_home, name='notes_home'),
    path('category', views.category_info, name='category_info'),
]
