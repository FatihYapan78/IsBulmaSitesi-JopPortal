from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .form import *
from company.models import *
from resume.models import *

def register_applicant(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, "Kullanıcı Başarılı bir şekilde oluşturuldu.")
            return redirect("login")
        else:
            messages.info(request,"Hatalı giriş")
            return redirect("register_applicant")
    else:
        form = RegisterUser()
        context={"form":form}
        return render(request, "users/register_applicant.html", context)

def register_recruiter(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request, "Kullanıcı Başarılı bir şekilde oluşturuldu.")
            return redirect("login")
        else:
            messages.info(request,"Hatalı giriş")
            return redirect("register_recruiter")
    else:
        form = RegisterUser()
        context={"form":form}
        return render(request, "users/register_recruiter.html", context)

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.warning(request,"Hatalı giriş")
    
    return render(request, "users/login.html")

def logout_user(request):
    logout(request)
    messages.info(request,"Başaraılı bir şekilde çıkış yapıldı.")
    return redirect("login")