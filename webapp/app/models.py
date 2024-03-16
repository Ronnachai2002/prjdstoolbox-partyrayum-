from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images_profile', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    pass1 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Item(models.Model):
    title = models.CharField(max_length=50)
    size = models.CharField(max_length=500)
    description = models.TextField(max_length=255, default='No description')
    material = models.CharField(max_length=50, default='No description')
    price = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True, blank=True, null=True)

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images', null=True, blank=True)

class Cart(models.Model):
    cart = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Detailcart(models.Model):
    itemImages = models.ForeignKey(ItemImage, on_delete=models.CASCADE)
    carts = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  
    material = models.CharField(max_length=50)
    message = models.TextField()
    attachment = models.FileField(upload_to='order_attachments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('รอดำเนินการ', 'รอดำเนินการ'), ('กำลังดำเนินการ', 'กำลังดำเนินการ'), ('ดำเนินการเสร็จสิ้น', 'ดำเนินการเสร็จสิ้น'), ('จัดส่งแล้ว', 'จัดส่งแล้ว'), ('จัดส่งเรียบร้อย', 'จัดส่งเรียบร้อย')])    

    def __str__(self):
        return f"Order {self.id}: {self.name} ({self.get_status_display()})"

class Message(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='payment_slips', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'รอตรวจสอบ'),
        ('verified', 'ชำระเงินเรียบร้อย'),
        ('rejected', 'การชำระเงินถูกปฏิเสธ')
    ], default='pending')
    price = models.DecimalField(max_digits=10, decimal_places=2)  # เพิ่มฟิลด์ราคา





    
