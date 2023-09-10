from django.shortcuts import render, redirect
from django.contrib import messages
from .form import *
from .models import *
from Appjob.models import *

def update_resume(request):
    if request.user.is_applicant:
        resume = Resume.objects.get(user=request.user)
        if request.method == "POST":
            form = UpdateResumeForm(request.POST, request.FILES, instance=resume)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.has_resume = True
                var.save()
                user.save()
                messages.info(request, "Şirket bilgileriniz başarılı bir şekilde güncellendi.")
                return redirect("dashboard")
            else:
                messages.warning(request, "Hatalı giriş")
        else:
            form = UpdateResumeForm(instance=resume)
            context={"form":form}
            return render(request, "resume/update_resume.html", context)
    else:
        messages.warning(request, "İzinsiz giriş")
        return redirect("dashboard")

def resume_details(request,pk):
    resume = Resume.objects.get(pk=pk)
    context = {"resume":resume}
    return redirect(request, "resume/resume_details.html", context)


