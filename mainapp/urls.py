from django.urls import path, include
from .views import index, work ,testimonie,profilePic,download_file
urlpatterns = [
    path('',index),
    path('settings/',work,name='portWork'),
    path('testimonialset/',testimonie,name='testimonial'),
    path('profileset/',profilePic,name='profilepic'),
    path('resume/',download_file,name='cv')
]