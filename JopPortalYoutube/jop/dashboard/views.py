from django.shortcuts import render,redirect
from .form import *
from django.contrib import messages
from .models import *
from .filter import *
from django.core.paginator import Paginator
from django.http import JsonResponse
def dashboard(request):
    path = request.get_full_path()
    sort = request.GET.get('sort')
    if sort == "salary":
        filter = JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by("salary"))
    elif sort == "-salary":
        filter = JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by("-salary"))
    elif sort == "title":
            filter = JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by("title"))
    elif sort == "-title":
            filter = JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by("-title"))
    else:
        filter = JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by("-addjob"))
    if 'term' in request.GET:
        filter = JobFilter(request.GET, queryset=Job.objects.filter(title__icontains=request.GET.get('term')))
        titles = list()
        for job in filter.queryset:
            titles.append(job.title)
        return JsonResponse(titles, safe=False)
    page_number = request.GET.get('page',1)
    paginator = Paginator(filter.qs, 3)
    filter_job = paginator.page(page_number)
    context={ 
        'filter':filter,
        'filter_job':filter_job,
        'sort':sort,
        'path':path
    }
    return render(request, "dashboard/dashboard.html",context)


def create_job(request):
    if request.method == "POST":
        form = CreateJobForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.company = request.user.company
            var.save()
            messages.info(request, 'İş İlanınız Başarılı Bir Şekilde Oluşturuldu.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'İş İlanı Oluşturulamadı.')
            return redirect('create_job')
    else:
        form = CreateJobForm()
        context={
            'form':form
        }
        return render(request, 'dashboard/create_job.html', context)

def update_job(request,id):
    job = Job.objects.get(id=id)
    if request.method == "POST":
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.company = request.user.company
            var.save()
            messages.info(request, 'İş İlanınız Başarılı Bir Şekilde Güncellendi.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'İş İlanı Güncellenemedi.')
            return redirect('update_job')
    else:
        form = UpdateJobForm(instance=job)
        context={
            'form':form
        }
        return render(request, 'dashboard/updated_job.html', context)

def job_details(request,id):
    if ApplyJob.objects.filter(user=request.user, job=id).exists():
        has_applited = True
    else:
        has_applited = False
    job = Job.objects.get(id=id)
    context = {
        'job':job,
        'has_applited':has_applited,
    }

    return render(request, 'dashboard/job_details.html', context)

def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context={
        'jobs':jobs
    }
    return render(request, 'dashboard/manage_jobs.html', context)

def applyjob(request,id):
    if request.user.is_authenticated and request.user.is_applicant:
        job = Job.objects.get(id=id)
        if ApplyJob.objects.filter(user=request.user, job=id).exists():
            messages.warning(request, 'Hatalı Giriş')
            return redirect('dashboard')
        else:
            ApplyJob.objects.create(user=request.user,job=job,status="Pending",resume=request.user.resume)
            messages.info(request, 'Başarılı bir şekilde ilana başvuru yaptınız.')
            return redirect('dashboard')
    else:
        messages.info(request, 'Lütfen giriş yapıp öyle devam edin.')
        return redirect('login')
    
def all_applicants(request,id):
    job = Job.objects.get(id=id)
    applicants = job.applyjob_set.all()
    context={
        'job':job,
        'applicants':applicants
    }
    return render(request, 'dashboard/all_applicants.html', context)

def applied_jobs(request):
    jobs = ApplyJob.objects.filter(user=request.user)
    context = {
        'jobs':jobs
    }
    return render(request, 'dashboard/applied_jobs.html', context)