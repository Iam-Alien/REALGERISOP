from django.urls import path 
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="processOrder"),
    path('registration/', views.registration, name="registration"),
    path('confirm/', views.confirm, name="confirm"),
    path('thank_you/', views.thankyou, name="thank_you"),
    path('online/', views.online, name="online"),
   

]