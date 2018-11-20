from django.shortcuts import render, HttpResponse, redirect
import json

# Create your views here.

def add_to_cart(request):
    product_id = request.POST['product']
    quantity = int(request.POST['quantity'])
    
    
    cart = request.session.get('cart',{})
    cart[product_id] = cart.get(product_id, 0) + quantity
    request.session['cart'] = cart
    
    return HttpResponse(json.dumps(cart))


