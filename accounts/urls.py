from django.urls import path
from . import views

urlpatterns = [
   path("", views.home, name="home"),
   path("products/", views.products, name="products"),
   path("customer/<int:pk>/", views.customer, name="customer"),
   path("add_customer", views.add_customer, name="add-customer"),
   path("customer/edit/<int:pk>/", views.update_customer, name="edit-customer"),
   path("customer/delete/<int:pk>/", views.delete_customer, name="delete-customer"),
   path("create_order/", views.create_order, name="create-order"),
   path("order/edit/<int:pk>/", views.update_order, name="edit-order"),
   path("order/delete/<int:pk>/", views.delete_order, name="delete-order"),
   
]
