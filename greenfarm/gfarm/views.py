from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import csv 

from django.views.generic.detail import DetailView





# Views
@login_required
def home(request):
    return render(request, "registration/success.html", {})
 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('homePage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



# Create your views here.
class homePage(TemplateView):
     template_name = "index.html"

class aboutPage(LoginRequiredMixin, ):
     template_name = "NiceAdmin/pages-about.html"

class profilePage(LoginRequiredMixin, CreateView):
     model = Profile
     form_class = ProfileForm
     template_name = "NiceAdmin/users-profile.html"
     
     

     
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = UpdateProfileForm
    template_name = "NiceAdmin/users-profile.html"
    success_url = reverse_lazy('farmerslist')

# ------------
class FarmerCreate(LoginRequiredMixin, CreateView):
     model = Farmers
     form_class = FarmersForm
     template_name = "farmers_form.html"
     success_url = reverse_lazy('farmerslist')

class FarmerListView(LoginRequiredMixin, ListView):
     queryset = Farmers.objects.all()
     context_object_name = "farmer"
     template_name = "NiceAdmin/farmers_list.html"
     
def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    queryset = Farmers.objects.all()  
    writer = csv.writer(response)  
    for Farmer in Farmers:
        writer.writerow([Farmer.username,Farmer.first_name,
                         Farmer.other_name,Farmer.address,email,Farmer.phone_no,
                         county,Farmer.sub_county,Farmer.job])  
    return response

class FarmersDetailsView(LoginRequiredMixin, DetailView):
     model = Farmers
     template_name = "NiceAdmin/tables-general.html"

class FarmersUpdateView(LoginRequiredMixin, UpdateView):
    model = Farmers
    fields = ['username','first_name','other_name', 'address','email','phone_no', 'county', 'sub_county', 'job']
    template_name = "update_farmers_form.html"
    success_url = reverse_lazy('farmerslist')

class FarmersDeleteView(LoginRequiredMixin, DeleteView):
    model = Farmers
    template_name = "delete_form.html"
    success_url = reverse_lazy("farmers")
    
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = BlogPost.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched':searched, 'blogs':blogs})
    else:
        return render(request, "search.html", {})



# ---------

class productCreateView(LoginRequiredMixin, CreateView):
     model =FarmProduct
     form_class = ProductForm
     template_name = "farm_product_form.html"
     success_url = reverse_lazy('product')


class ProductListView(LoginRequiredMixin, ListView):
     queryset = FarmProduct.objects.all()
     context_object_name = "product"
     template_name = "farmproduct_list.html"


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = FarmMarketing
    fields = ['name','description','price', 'quantity']
    template_name = "update_product_form.html"

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = FarmProduct
    template_name = "delete_form.html"
    success_url = reverse_lazy("product")
    
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = FarmProduct.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched':searched, 'blogs':blogs})
    else:
        return render(request, "search.html", {})

    
#-----------------
class DiseaseCreateView(LoginRequiredMixin, CreateView):
     model =Diseases_and_Pest
     form_class = ProductForm
     template_name = "farm_p&diseases_form.html"
     success_url = reverse_lazy('diseases')


class DiseaseListView(LoginRequiredMixin, ListView):
     queryset = Diseases_and_Pest.objects.all()
     context_object_name = "diseases"
     template_name = "p&diseases_list.html"


class DiseaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Diseases_and_Pest
    fields = "__all__"
    template_name = "update_disease_form.html"
    success_url = reverse_lazy("disease")

class DiseaseDeleteView(LoginRequiredMixin, DeleteView):
     model = Diseases_and_Pest
     template_name = "delete_form.html"
     success_url = reverse_lazy("disease")
     
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = Diseases_and_Pest.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched':searched, 'blogs':blogs})
    else:
        return render(request, "search.html", {})

     
#-----------------
 
class HarvestCreateView(LoginRequiredMixin, CreateView):
     model = Harvest
     form_class = HarvestForm
     template_name = "farm_harvest_form.html"
     success_url = reverse_lazy('harvests')


class HarvestListView(LoginRequiredMixin, ListView):
     queryset = Harvest.objects.all()
     context_object_name = "harvet"
     template_name = "farm_harvest_list.html"


class HarvestUpdateView(LoginRequiredMixin, UpdateView):
    model = Harvest
    fields = "__all__"
    template_name = "update_harvest_form.html"

class HarvestDeleteView(LoginRequiredMixin, DeleteView):
     model = Harvest
     template_name = "delete_form.html"
     success_url = reverse_lazy("disease")
     
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = Harvest.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched':searched, 'blogs':blogs})
    else:
        return render(request, "search.html", {})


# ---------------
class FarmMarketingCreateView(LoginRequiredMixin, CreateView):
     model = Post_Sell
     form_class = MarketingForm
     template_name = "market_form.html"
     success_url = reverse_lazy("marketplaces")

class FarmMarketingListView(LoginRequiredMixin, ListView):
     queryset = Post_Sell.objects.all()
     context_object_name = "market"
     template_name = "NiceAdmin/market_list.html"

class FarmMarketingtDeleteView(LoginRequiredMixin, DeleteView):
    model = Post_Sell
    template_name = "delete_form.html"
    success_url = reverse_lazy("marketplaces")


class SellesDetailView(DetailView):
    model = Post_Sell
    template_name = "detail_view.html"
    
    
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = Post_Sell.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched':searched, 'blogs':blogs})
    else:
        return render(request, "search.html", {})



class FarmMarketingUpdateView(LoginRequiredMixin, UpdateView):
    model = Post_Sell
    form_class = MarketingForm
    template_name = "update_market_form.html"
    success_url = reverse_lazy("marketplaces")



     

class contactPage(LoginRequiredMixin, CreateView):
     model = Contact
     form_class = ContactForm
     template_name = "NiceAdmin/contact_form.html"
     success_url = reverse_lazy("contact")

class contactListView(LoginRequiredMixin, ListView):
     queryset = Contact.objects.all()
     context_object_name = "contact"
     template_name = "NiceAdmin/contact_list.html"
     
class contactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    fields = ['your_name','email','subject', 'message']
    template_name = "update_contact_form.html"
    success_url = reverse_lazy("contact")
     
class contactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "delete_form.html"
    success_url = reverse_lazy("contact")
    
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = Contact.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched':searched, 'blogs':blogs})
    else:
        return render(request, "search.html", {})



