from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""

    quantity=int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """Adjust the quantituy of a specified product in the cart"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

# we can only adjust a quantity if there is already something in the cart.
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop[id]

    request.session['cart'] = cart
    return redirect(request('view_cart'))