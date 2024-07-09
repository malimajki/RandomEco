from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from PIL import Image, ImageDraw
from io import BytesIO
import qrcode

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        ordering = ("name", )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="upload/", blank=True, null=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.name
    
    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating
        
        if reviews_total > 0:
            return reviews_total / self.reviews.count()
        
        return 0
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"
    

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


##############################  ORDERS  ##############################

class Cart(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Cart ({self.user or self.session_id})"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    def subtotal(self):
        return self.product.price*self.quantity


class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )

    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=12, blank=False, null=False)
    street = models.CharField(max_length=30, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    zip_code = models.CharField(max_length=10, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    total_price = models.IntegerField(blank=True, null=True)
    qr= models.ImageField(upload_to="upload/qr", blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} ({self.email})"
    
    def save(self, *args, **kwargs):
        payment_info = f"SPD*1.0*ACC:CZ1930300000002048017011*RN:MICHAL SANDA*AM:{self.total_price}*CC:CZK*X-VS:245876"
        qrcode_img=qrcode.make(payment_info)
        canvas = Image.new('RGB', (400,400), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code_{self.id}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


    class Meta:
        ordering = ('-created_at',)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.order} - {self.product} x {self.quantity}"
    
    def subtotal(self):
        return self.product.price*self.quantity