from django.shortcuts import render, redirect
from django.contrib import messages
from .form import *
from .models import *
from Appjob.models import *

def update_company(request):
    if request.user.is_recruiter:
        company = Company.objects.get(user=request.user)
        if request.method == "POST":
            form = UpdateCompanyForm(request.POST, instance=company)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.has_company = True
                var.save()
                user.save()
                messages.info(request, "Şirket bilgileriniz güncellendi.")
                return redirect("dashboard")
            else:
                messages.warning(request, "Bir problem var")
        else:
            form = UpdateCompanyForm(instance=company)
            context ={"form":form}
            return render(request, "company/update_company.html", context)
    else:
        messages.warning(request, "İzin reddedildi")
        return redirect("dashboard")

def company_details(request,pk):
    company = Company.objects.get(pk=pk)
    context={"company":company}
    return render(request, "company/company_details.html", context)


