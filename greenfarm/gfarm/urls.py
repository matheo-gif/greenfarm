from . import views
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
     path("homepage/", TemplateView.as_view(template_name="index.html")),
     path('register/', views.register, name='register'),
     path("about/", TemplateView.as_view(template_name="NiceAdmin/pages-about.html")),
     path("profile/", TemplateView.as_view(template_name="NiceAdmin/users-profile.html")),
     path("contact/", TemplateView.as_view(template_name="NiceAdmin/pages-contact.html")),
     path("faq/", TemplateView.as_view(template_name="NiceAdmin/pages-faq.html")),

     path("addfarmer/", FarmerCreate.as_view() ),
     path("farmerslist/", FarmerListView.as_view(), name="farmers" ),
     path('farmers/<str:pk>/', FarmersDetailsView.as_view()),
     path('farmers/delete/<str:pk>/', FarmersDeleteView.as_view(), name="farmer-delete"),
     path('farmers/update/<str:pk>/', FarmersUpdateView.as_view(), name="farmer-update"),
     path('farmerslist/csv',views.getfile),  
     
     
     path("add_market_place/", FarmMarketingCreateView.as_view(), name="add_market_place"),
     path("market/", FarmMarketingListView.as_view(), name="marketplaces"),
     path('market/delete/<str:pk>/', FarmMarketingtDeleteView.as_view(), name='delete_market'),
     path('market/update/<str:pk>/', FarmMarketingUpdateView.as_view(), name='update_market'),
     path('market/detail/<str:pk>/', SellesDetailView.as_view(), name='detail_market'),

     path("add_product/",productCreateView.as_view(), name="add_farm_product"),
     path("product/", ProductListView.as_view(), name="product"),
     path('product/delete/<str:pk>/', ProductDeleteView.as_view(), name="product-delete"),
     path('product/update/<str:pk>/', ProductUpdateView.as_view(), name="product-update"),
     
     path("add_diseases/",DiseaseCreateView.as_view(), name="add_farm_product"),
     path("", DiseaseListView.as_view(), name="disease"),
     path('disease/delete/<str:pk>/', DiseaseDeleteView.as_view(), name="disease-delete"),
     path('disease/update/<str:pk>/', DiseaseUpdateView.as_view(), name="disease-update"),
     
     path("add_harvests/",HarvestCreateView.as_view(), name="add_farm_harvest"),
     path("harvests/", HarvestListView.as_view(), name="harvests"),
     path('harvests/delete/<str:pk>/', HarvestDeleteView.as_view(), name="harvests-delete"),
     path('harvests/update/<str:pk>/', HarvestUpdateView.as_view(), name="harvests-update"),

     path("contact/", contactListView.as_view(), name="contact-info"),
     path("add_contact/",contactPage.as_view()),
     path('contact/delete/<str:pk>/', contactDeleteView.as_view(), name="contact-delete"),
     path('contact/update/<str:pk>/', contactUpdateView.as_view(), name="contact-update"),

     path("planting/", PlantingListView.as_view(), name="planting-info"),
     path("add_planting/", PlantingRecordsPage.as_view()),
     path('planting/delete/<str:pk>/', PlantingDeleteView.as_view(), name="planting-delete"),
     path('planting/update/<str:pk>/', PlantingRecordsUpdateView.as_view(), name="planting-update"),

     path("buyer/", BuyerView.as_view(), name="buyer-info"),
     path("add_buyer/", BuyerPage.as_view(), name="add-buyer"),
     path('buyer/delete/<str:pk>/', BuyerDeleteView.as_view(), name="buyer-delete"),
     path('buyer/update/<str:pk>/', BuyerUpdateView.as_view(), name="buyer-update"),
     
]