from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Max

from shop.utils.context_processors import get_cart
from .models import Product, Category, Review, Order, OrderItem, CartItem


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get("category", "")

    if active_category:
        products = products.filter(category__slug=active_category)
    
    query = request.GET.get("shop_search", "")

    if query:
        products= products.filter(Q(name__icontains=query | Q(descripotion__icontains=query)))

    max_value = Product.objects.aggregate(max_value=Max("price"))["max_value"]

    context = {
        "categories":categories,
        "products":products,
        'active_category':active_category,
        'max_value':max_value
    }

    return render(request, "shop/home.html", context)    

def product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == "POST":
        rating = request.POST.get("rating", 3)
        content = request.Post.get("content", "")

        if content:
            review = Review.objects.filter(created_by=reversed.user, product=product)

            if review.exists():
                review = review.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )

            return redirect('product', slug=slug)

    context = {
        'product': product,
    }
    return render(request, 'a_shop/product.html', context)

def add_to_cart(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    if request.htmx:
        return render (request, "shop/cart-partial.html", {"cart":cart})
    return redirect(request.META.get('HTTP_REFERER','/'))

def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    action = request.POST.get("action")
    if action == "increment":
        cart_item.quantity +=1
        cart_item.save()
    elif action == 'decrement':
        cart_item.quantity -= 1
        if cart_item.quantity <= 0:
            cart_item.delete()
        else:
            cart_item.save()
    elif action == 'delete':
        cart_item.delete()
    return render(request, 'shop/cart-partial.html')

def checkout(request):
    cart = get_cart(request)
    total_price = 0
    if request.method == 'POST':
        order = Order.objects.create(user=request.user if request.user.is_authenticated else None, 
            email = request.POST['email'],
            phone = request.POST['phone'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            street = request.POST['street'],
            city = request.POST['city'],
            zip_code = request.POST['zip'],
            total_price = sum(item.quantity * item.product.price for item in cart.items.all())
        )
        for cart_item in cart.items.all():
            OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
        cart.delete()
        return redirect('shop:home')
    return render(request, 'shop/checkout.html', {'cart': cart})
