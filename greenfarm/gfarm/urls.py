from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
     path("", TemplateView.as_view(template_name="index.html")),
     path("about/", TemplateView.as_view(template_name="NiceAdmin/pages-contact.html")),
     path("profile/", TemplateView.as_view(template_name="NiceAdmin/users-profile.html")),
     path("contact/", TemplateView.as_view(template_name="NiceAdmin/pages-contact.html")),
     
]