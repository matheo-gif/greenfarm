from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# Create your views here.
class homePage(TemplateView):
     template_name = "index.html"

class aboutPage(TemplateView):
     template_name = "NiceAdmin/pages-contact.html"

class profilePage(TemplateView):
     template_name = "NiceAdmin/users-profile.html"

class contactPage(TemplateView):
     template_name = "NiceAdmin/pages-contact.html"
    