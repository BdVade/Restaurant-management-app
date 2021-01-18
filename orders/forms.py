from .models import Order
from django import forms
from userss.models import User

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['details',]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['type']

class OrderFulfillForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['fulfilled']


