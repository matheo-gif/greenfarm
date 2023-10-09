from django import forms
from .models import *

class FarmersForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Farmers
        fields = ('username','first_name','other_name', 'address','email','phone_no', 'county', 'sub_county', 'job', 'Social_media', 'password')

class UpdateProfileForm(forms.ModelForm):
    phone_no = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    social_media_handle = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    image = forms.CharField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = Profile
        fields = ['phone_no', 'bio', 'social_media_handle', 'image',]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'social_media_handle', 'image', )
     

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
        
        
class HarvestForm(forms.ModelForm):
    
    class Meta:
        model = Harvest
        fields = "__all__"

class MarketingForm(forms.ModelForm):
    
    class Meta:
        model = FarmMarketing
        fields = "__all__"