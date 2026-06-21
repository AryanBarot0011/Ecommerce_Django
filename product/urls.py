from django.urls import path , include
from . import views

urlpatterns = [
    path('product/',views.product_list,name="product_list"),
    path('product/details/',views.product_details,name="product_details"),
]