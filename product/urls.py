from django.contrib import admin  
from django.urls import path  
from product import views
from product.models import Product  
from django.views.generic import TemplateView 
from django.views.generic import ListView

urlpatterns = [
    path('product/', views.product),  
    path('show/',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy), 
    path('getjson', views.getjson), 
    path('raw_sql/', views.raw_sql),
    path('api/get_products/', views.get_products, name="get-products"),
    path('api/pay/', views.PaymentView.as_view(), name="pay"),
    path('generic_views/example1', views.ExampleStaticView.as_view(), name="example1"),
    #same above can be written as following
    path('generic_views/example2', TemplateView.as_view(template_name='generic_templates/static.html')),
    path('generic_views/example3', ListView.as_view(template_name='generic_templates/generic_products.html', 
    model = Product, context_object_name = "product_objects")),
]  