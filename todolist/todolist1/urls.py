from django.urls import path
from . import views

urlpatterns = [
    path('todolist', views.index, name="index"),
    path('todoAdd', views.todoAdd, name="todoAdd"),

]