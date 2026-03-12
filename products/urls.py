from django.urls import path
from .import views 
urlpatterns=[
    path('',views.Product_list,name='Product_list'),
    path('<int:id>/',views.product_detail,name='product_detail'),
    path('add-to-cart/<int:id>/',views.add_to_cart,name='cart'),
    path('cart/',views.cart_view,name='cart_view'),
    path('remove/<int:id>/',views.remove_from_cart,name='remove_from_cart'),
    path('increase/<int:id>/',views.increase_quantity),
    path('decrease/<int:id>/',views.decrease_quantity),
    path('checkout/',views.checkout),
]