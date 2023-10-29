
from django.urls import path

from listings import views

urlpatterns = [
    path('', views.listing_list, name="list"),
    path('<int:id>/', views.listing_retrieve, name="listing_retrieve"),

]
