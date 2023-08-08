from django.contrib import admin
from django.urls import path
from Appjob.views import *
from dashboard.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", dashboard,name="dashboard"),
    path("login", login_user,name="login"),
    path("logout", logout_user,name="logout"),
    path("register_applicant", register_applicant,name="register_applicant"),
    path("register_recruiter", register_recruiter,name="register_recruiter"),
]
