from django.urls import path
from Products.views import product_view,product_create_view,dynamic_lookup_view,delete_view

app_name='Products';
urlpatterns = [
    path('',product_create_view,name='Create'),
    path('<int:my_id>/',dynamic_lookup_view,name='Product'),
    path('<int:my_id>/delete/',delete_view,name='Delete'),
]