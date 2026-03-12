from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Cart,Order
# Create your views here.
def Product_list(request):
    products=Product.objects.all()
    return render(request,'products.html',{'products':products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    Cart.objects.create(product=product,quantity=1)
    return redirect('Product_list')

def cart_view(request):
    cart_items=Cart.objects.all()
    total_price=0
    for item in cart_items:
        total_price+=item.product.price*item.quantity
    return render(request,'cart.html',{'cart_items': cart_items,'total_price':total_price})


def remove_from_cart(request,id):
    cart_item=Cart.objects.get(id=id)
    cart_item.delete()
    return redirect('cart_view')


def increase_quantity(request,id):
    cart_item=Cart.objects.get(id=id)
    cart_item.quantity+=1
    cart_item.save()
    return redirect('cart_view')

def decrease_quantity(request,id):
    cart_item=Cart.objects.get(id=id)
    if cart_item >1:
         cart_item.quantity-=1
         cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_view')

def checkout(request):
    cart_items=Cart.objects.all()
    for item in cart_items:
        Order.objects.create(
            product=item.product,
            quantity=item.quantity,
            total_price=item.product.price*item.quantity
        )
    cart_items.delete()
    return render(request,'checkout.html')
