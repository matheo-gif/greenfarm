from django.contrib import admin
from .models import *
from django.contrib.auth.models import Permission

admin.site.register(Permission)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Farmers)
admin.site.register(FarmProduct)
admin.site.register(Harvest)
admin.site.register(FarmMarketing)
admin.site.register(Contact)
admin.site.register(Diseases_and_Pest)
admin.site.register(Post_Sell)
admin.site.register(Buyer)