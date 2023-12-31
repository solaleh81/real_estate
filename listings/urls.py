
from django.urls import path

from listings import views

urlpatterns = [
    path('', views.listing_list, name="list"),
    path('<int:id>/', views.listing_retrieve, name="listing_retrieve"),
    path('add-listing/', views.listing_create, name="listing_create"),
    path('<int:id>/edit/', views.listing_update, name="listing_update"),
    path('<int:id>/delete/', views.listing_delete, name="listing_delete"),

]
