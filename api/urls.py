from django.urls import path
from .views import *

urlpatterns=[
    path('itemList', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('locationList', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
]