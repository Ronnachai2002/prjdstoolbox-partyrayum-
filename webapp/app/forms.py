
from django import forms
from .models import Item, ItemImage, UserProfile

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