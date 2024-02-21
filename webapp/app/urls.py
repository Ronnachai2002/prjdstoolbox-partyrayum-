"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from .views import *
from django.urls import path


urlpatterns = [
    path('' , views.home, name='home'),
    path('signout', views.signout, name='signout'),
    path('registerXlogin', views.registerXlogin, name='registerXlogin'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('upload_profile_image/', upload_profile_image, name='upload_profile_image'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('admin1/', admin1, name='admin1'),
    path('management/', views.management, name='management'),
    path('user_management/', user_management_view, name='user_management'),
    path('products/', products, name='products'),
    path('product/<int:item_id>/', product, name='product'),
    path('productweb/product/<int:item_id>/', product, name='product'),
    path('contag/', contag, name='contag'),
    path('payments/', payments, name='payments'),
    path('add_product/', add_product, name='add_product'),
    path('delete_product_incart/<int:product_id>/', delete_product_incart, name='delete_product_incart'),
    path('add_cart/<int:id>/', add_cart, name='add_cart'),
    path('cart/',cart,name='cart'),
    path('order',order,name='order'),
    path('order2',order2,name='order2'),
    path('order3',order3,name='order3'),
    path('order4',order4,name='order4'),
    path('order5',order5,name='order5'),
    path('order6',order6,name='order6'),
    path('preorder/', views.preorder, name='preorder'),
    path('orders/', views.admin_order_list, name='admin_order_list'),
    path('orders/', views.admin_order_list, name='admin_order_list'),
    path('orders/update/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('orders/view/<int:order_id>/', views.view_order, name='view_order'),
    path('orders/track/<int:order_id>/', views.track_order, name='track_order'),
    path('delete_product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('chat', views.chat, name='chat'),
    path('chat_history/<int:receiver_id>/', views.chat_history, name='chat_history'),
    path('send_message/', views.send_message, name='send_message'),
    path('admin_chat_list', views.admin_chat_list, name='admin_chat'),
    path('admin_chat/<int:id>',views.admin_chat, name='delete_ScoreTopic'),
    path('messages/admin/<int:id>', views.admin_messages, name='latest_messages'),
    path('messages/customer/', views.customer_messages, name='latest_messages'),
    path('payment-tracking/', payment_tracking, name='payment_tracking'),
    path('create_payment/<int:id>', create_payment, name='create_payment'),
    path('send_payment/', send_payment, name='send_payment'),
    path('get_order_payment/<int:id>', get_order_payment, name='get_order_payment'),
    path('payment_slip/', views.payment_slip, name='payment_slip'),
    path('upload_payment_image/', views.upload_payment_image, name='upload_payment_image'),
    path('update_payment_status/', views.update_payment_status, name='update_payment_status'),
    path('delete_payment_image/<int:payment_id>/', views.delete_payment_image, name='delete_payment_image'),

    






]
