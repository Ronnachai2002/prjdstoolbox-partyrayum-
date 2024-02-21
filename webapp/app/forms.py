
from django import forms
from .models import Item, ItemImage, Order, UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'birth_date']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'size', 'description', 'material', 'price']

class ItemImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = ['image']

class PaymentForm(forms.Form):
    order_id = forms.IntegerField(label='เลขคำสั่งซื้อ')
    amount_due = forms.DecimalField(label='จำนวนเงินที่ต้องชำระ')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'category', 'material', 'message', 'attachment']
