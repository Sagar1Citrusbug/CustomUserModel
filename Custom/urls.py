from django.urls import path
from Custom import views
from Custom.forms import forgetpass


from .views import registration_view, home, log_in,logout, changepassword, logged, forgetpassword, reset

urlpatterns = [
    path("", views.home, name = "Home"),
    path("register/",views.registration_view, name = "register"),
    path("thanks/", views.thanks, name = "thanks"),
    path("login/", views.log_in, name="login"),
    path('logout/', views.logout, name = "logout"),
    path("changepassword/", views.changepassword, name  = "changepassword"),
    path("loggedout/", views.logged, name  = "loggedout"),
    path("forgetpass/", views.forgetpassword, name = "forgetpass"),
    path("reset/<int:pk>", views.reset, name = "Resset")
    
]