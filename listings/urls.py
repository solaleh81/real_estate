
from django.urls import path

from listings import views

urlpatterns = [
    path('', views.listing_list, name="list"),
]
