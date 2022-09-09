from django.urls import path
from Custom import views

from .views import registration_view, home, thanks

urlpatterns = [
    path("", views.home, name = "Home"),
    path("register/",views.registration_view, name = "register"),
    path("thanks", views.thanks, name = "thanks")
    
]