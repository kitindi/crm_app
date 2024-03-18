from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path("products/", views.products, name="products"),
   path("products/add/", views.create_product, name="create-product"),
   path("products/delete/<int:pk>", views.delete_product, name="delete-product"),
   path("products/edit/<int:pk>", views.edit_product, name="edit-product"),
   path("products/details/<int:pk>", views.product_details, name="product-details"),
   path("all_customers/", views.all_customers, name="all-customers"),
   path("customer/<int:pk>/", views.customer, name="customer"),
   path("add_customer", views.add_customer, name="add-customer"),
   path("customer/edit/<int:pk>/", views.update_customer, name="edit-customer"),
   path("customer/delete/<int:pk>/", views.delete_customer, name="delete-customer"),
   path("orders/", views.orders, name="orders"),
   path("create_order/<int:pk>", views.create_order, name="create-order"),
   path("order/edit/<int:pk>/", views.update_order, name="edit-order"),
   path("order/delete/<int:pk>/", views.delete_order, name="delete-order"),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
