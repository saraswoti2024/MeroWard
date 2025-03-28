from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("about/",about,name="about"),
    path("services/",services,name="services"),
    path("news/",news,name="news"),
    path("events/",events,name="events"),
    path("dashboard/",dashboard,name="dashboard"),
    path("adminboard/",adminboard,name="adminboard"),
    path("contacts/",contacts,name="contacts"),

    #auth
     path("log_in/",log_in,name="log_in"),
     path("register/",register,name="register"),


]
