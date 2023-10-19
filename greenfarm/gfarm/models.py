from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics",default='avatar.jpg', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    social_media_handle= models.CharField(max_length=300, blank=True, null=True)

    
    def __str__(self):
        return str(self.user)
    
class Contact(models.Model):
    your_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    captured_on = models.DateTimeField(default=datetime.now)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    

    def __str__(self):
        return str(self.your_name)


class Farmers(models.Model):
    username = models.CharField(blank=False, null=False, max_length=100)
    first_name = models.CharField(blank=False, null=False, max_length=100)
    other_name = models.CharField(blank=True, null=True, max_length=100)
    address = models.CharField(blank=True, null=True, max_length=100)
    email = models.CharField(blank=True, null=True, max_length=100)
    phone_no = models.CharField(blank=False, null=False, max_length=100)
    county = models.CharField(blank=False, null=False, max_length=100)
    sub_county = models.CharField(blank=False, null=False, max_length=100)
    job = models.CharField(blank=True, null=True, max_length=100)
    
    
    

    def __str__(self):
        return self.username

VARIETY=(
    ("h614","H614"),
    ("h512","H512"),
    ("h513","H513"),
    ("dh02","DH02"),
    ("dh03","DH03"),
    ("dh04","DH04"),
    ("h624","H624"),
    ("h621","H621"),
    ("h617","H617"),
    ("h614","H614"),
    ("h615","H615"),
    ("h621","H621"),
    ("h614","H614"),
    ("h51515","H515"),
    ("h513","H513"),
    ("hb 3253","PHB 3253"),
    ("phb 30M35","PHB 30M35"),
)


class FarmProduct(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.CharField(max_length=100)
    Maize_Variety = models.CharField(max_length=100, choices=VARIETY)
    description = models.TextField()
    
    

    def __str__(self):
        return self.Maize_Variety


kenyan_regions = (
    ('Central','Central Region'),
    ('Coast','Coast Region'),
    ('Eastern','Eastern Region'),
    ('Nairobi','Nairobi Region'),
    ('North Eastern','North Eastern Region'),
    ('Nyanza','Nyanza Region'),
    ('Rift Valley','Rift Valley Region'),
    ('Western','Western Region')
)

COUNTIES = (
    ('001', 'Mombasa'),
    ('002', 'Kwale'),
    ('003', 'Kilifi'),
    ('004', 'Tana River'),
    ('005', 'Lamu'),
    ('006', 'Taita-Taveta'),
    ('007', 'Garissa'),
    ('008', 'Wajir'),
    ('009', 'Mandera'),
    ('010', 'Marsabit'),
    ('011', 'Isiolo'),
    ('012', 'Meru'),
    ('013', 'Tharaka-Nithi'),
    ('014', 'Embu'),
    ('015', 'Kitui'),
    ('016', 'Machakos'),
    ('017', 'Makueni'),
    ('018', 'Nyandarua'),
    ('019', 'Nyeri'),
    ('020', 'Kirinyaga'),
    ('021', 'Murang\'a'),
    ('022', 'Kiambu'),
    ('023', 'Turkana'),
    ('024', 'West Pokot'),
    ('025', 'Samburu'),
    ('026', 'Trans-Nzoia'),
    ('027', 'Uasin Gishu'),
    ('028', 'Elgeyo-Marakwet'),
    ('029', 'Nandi'),
    ('030', 'Baringo'),
    ('031', 'Laikipia'),
    ('032', 'Nakuru'),
    ('033', 'Narok'),
    ('034', 'Kajiado'),
    ('035', 'Kericho'),
    ('036', 'Bomet'),
    ('037', 'Kakamega'),
    ('038', 'Vihiga'),
    ('039', 'Bungoma'),
    ('040', 'Busia'),
    ('041', 'Siaya'),
    ('042', 'Kisumu'),
    ('043', 'Homa Bay'),
    ('044', 'Migori'),
    ('045', 'Kisii'),
    ('046', 'Nyamira'),
    ('047', 'Nairobi')
)



class Harvest(models.Model):
    id = models.AutoField(primary_key=True)
    Maize = models.ForeignKey(FarmProduct, on_delete=models.CASCADE, default="Maize_Variety")
    land_size = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    region = models.CharField(max_length=20, choices =kenyan_regions,default='Central Region')
    county = models.CharField(max_length=100, choices=COUNTIES, default='mombasa')

    def __str__(self):
        return str(self.id)
PAYMENT = (
    ('M-PESA', 'm-pesa'),
    ('CASH', 'cash'),
    ('CARD', 'visa-card'),
    ('CHEQUE', 'cheque'),
    )

class Post_Sell(models.Model):
    seller = models.ForeignKey(User, on_delete=models. CASCADE, default="username")
    phone_no = PhoneNumberField()
    email= models.EmailField(max_length=200)
    Product = models.CharField(max_length=200)
    paymethod_method = models.CharField(max_length=50, choices=PAYMENT, default='m-pesa')
    quantity_in_kg_or_tonnes  = models.CharField(max_length=50)
    Stoke_costing = models.DecimalField(max_digits=1000000000, decimal_places=2)
    trade_on=models.DateTimeField(default=datetime.now)
    county = models.CharField(max_length=100, choices=COUNTIES, default='mombasa')
    sub_county = models.CharField(blank=False, null=False, max_length=100)

class FarmMarketing(models.Model):
    Maize = models.ForeignKey(FarmProduct, on_delete=models.CASCADE)
    marketing_channel = models.CharField(max_length=50)
    quantity  = models.CharField(max_length=50)
    marketing_cost = models.DecimalField(max_digits=10, decimal_places=2)
    traded_on=models.DateTimeField(default=datetime.now)
    county = models.CharField(max_length=100, choices=COUNTIES, default='mombasa')
    sub_county = models.CharField(blank=False, null=False, max_length=100)

     
    
class Diseases_and_Pest(models.Model):
    Maize_Variety = models.ForeignKey(FarmProduct, on_delete=models.CASCADE)
    desease_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    description = models.TextField(max_length=200)
    posible_solutions = models.TextField(max_length=200)
    county_affected = models.CharField(max_length=100, choices=COUNTIES, default='mombasa')
    
     
     
    