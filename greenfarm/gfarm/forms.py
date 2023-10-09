from django import forms
from .models import *

class FarmersForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Farmers
        fields = ('username','first_name','other_name', 'address','email','phone_no', 'county', 'sub_county', 'job', 'Social_media', 'password')


class ProfileForm(forms.ModelForm):
    

    class Meta:
        model = Profile
        fields = ('user','image','bio', 'phone_no','social_media_handle')


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('your_name','email','subject', 'message')


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = FarmProduct
        fields = ('Maize_Variety','description','price', 'quantity')

class MarketingForm(forms.ModelForm):
    
    class Meta:
        model = FarmMarketing
        fields = "__all__"