from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from products.models import Product
import json

# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    
    
    cart_items = []

    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
       
        
        cart_items.append({
            'id': product.id,
            'name': product.name,
            'brand': product.brand,
            'sku': product.sku,
            'description': product.description,
            'image': product.image,
            'price': product.price,
            'stock': product.stock,
            'quantity': quantity,
            'total': product.price * quantity,
          
        })    
        
    cart_total =0
    for item in cart_items:
        cart_total += item['total']
    
    return render(request, "checkout/checkout.html", {'cart_items': cart_items, 'cart_total': cart_total})
    
    
    