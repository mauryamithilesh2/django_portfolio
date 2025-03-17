from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view ,name="home"),
   
    # path('experience/',views.experience_view ,name="experience"),
   
   
    path('resume/',views.resume_view ,name="resume"),
]
