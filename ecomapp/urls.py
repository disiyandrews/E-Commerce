from django.urls import path
from . import views

urlpatterns = [
    # Admin URLs
    path('', views.home, name='home'),
    path('loginn', views.loginn, name='loginn'),
    path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('userdetail/', views.userdetail, name='userdetail'),
    path('logout/', views.logout, name='logout'),
    path('add_category/', views.add_category, name='add_category'),
    path('categoryadd/', views.categoryadd, name='categoryadd'),
    path('prdt/', views.prdt, name='prdt'),
    path('product_add/', views.product_add, name='product_add'),
    path('viewproduct/', views.viewproduct, name='viewproduct'),
    path('userpanel/', views.userpanel, name='userpanel'),
    # path('cart/', views.cart, name='cart'),
    path('category_detail/<int:pk>/', views.category_detail, name='category_detail'),
    path('delete_us/<int:pk>/', views.delete_us, name='delete_us'),
    path('delete_pr/<int:pk>/', views.delete_pr, name='delete_pr'),
    # path('add_cart/<int:pd>/', views.add_cart, name='add_cart'),
    path('cart/', views.cart, name='cart'),
    path('add_cart/<int:pd>/', views.add_cart, name='add_cart'),
    path('remove/<int:ct>/', views.remove, name='remove'),
    path('increment_quantity/<int:pk>/', views.increment_quantity, name='increment_quantity'),
    path('decrement_quantity/<int:pk>/', views.decrement_quantity, name='decrement_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    
    
    

    
]