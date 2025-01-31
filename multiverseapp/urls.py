from django.urls import path
from . import views
app_name='multiverseapp'

urlpatterns = [
   path('',views.home,name='home'),
   path('designs/',views.designs,name='designs'),
   path('custom/',views.custom,name='custom'),
   path('products/',views.products,name='products'),
   path('about/',views.about,name='about'),



]