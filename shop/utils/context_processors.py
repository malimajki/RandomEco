from shop.models import Cart

def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_id=session_id)
    return cart

def cart_context(request):
    cart = get_cart(request)
    total_items = sum(item.quantity for item in cart.items.all())
    total_price = sum(item.quantity * item.product.price for item in cart.items.all())
    return {
        'cart': cart,
        'total_items': total_items,
        'total_price': total_price,
    }