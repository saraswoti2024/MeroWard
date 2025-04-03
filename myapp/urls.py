from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("about/",about,name="about"),
    path("services/",services,name="services"),
    path("adminboard/",adminboard,name="adminboard"),
    path("contacts/",contacts,name="contacts"),
    path("appointments/",appointments,name="appointments"),
    #auth
     path("log_in/",log_in,name="log_in"),
     path("register/",register,name="register"),
     path('log_out/',log_out,name="log_out"),
     path('view_app/',view_app,name="view_app"),
     path('emergency/',emergency,name="emergency"),
]
