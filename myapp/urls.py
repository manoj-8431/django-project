from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('order/', views.order_view, name='order'),
    path('account/', views.account_view, name='account')
]