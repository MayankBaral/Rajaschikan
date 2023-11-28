from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User
from homepage.models import Order

class UserRegister(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2'] 

class UserShipping(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address','city','state','zipcode','contact_number']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']

class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']

class ShippingUpdate(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address','city','state','zipcode','contact_number']