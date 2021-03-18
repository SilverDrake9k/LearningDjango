from django.urls import path
from . import views # . means the current directory

#name is blog-home to avoid duplicates across apps 
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
#path can be regex. But not needed.
