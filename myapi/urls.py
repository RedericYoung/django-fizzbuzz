from django.urls import path, re_path
from rest_framework import routers
from .views import (
    FizzBuzzList,
    detail
)

urlpatterns = [
    path('', FizzBuzzList.as_view()),
    path('/<int:id>', detail, name = 'view_record'),  
]