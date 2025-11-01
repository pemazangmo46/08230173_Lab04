from django.urls import path  # Import Django's path function for URL mapping
from . import views  # Import views from the current app directory

urlpatterns = [
    path('', views.index, name='index'),  # Root URL (homepage) displays the Learning Journey page
    path('aboutMe/', views.about_me, name='about_me'),  # URL for the About Me page
]
