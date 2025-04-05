from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",home,name="home"),
    path("about/",about,name="about"),
    path("services/",services,name="services"),
    path("adminboard/",adminboard,name="adminboard"),
    path("contacts/",contacts,name="contacts"),
    path("appointments/",appointments,name="appointments"),
    path("profile_dashboard/",profile_dashboard,name="profile_dashboard"),
    #auth
     path("log_in/",log_in,name="log_in"),
     path("register/",register,name="register"),
     path('log_out/',log_out,name="log_out"),
     path('view_app/',view_app,name="view_app"),
     path('emergency/',emergency,name="emergency"),
    #for forgot password when password is not known end
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = "auth/password_reset.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name = "auth/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "auth/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "auth/password_reset_complete.html"), name='password_reset_complete'),
    #for forgot password when password is not known end
]

