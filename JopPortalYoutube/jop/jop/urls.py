from django.contrib import admin
from django.urls import path
from Appjob.views import *
from dashboard.views import *
from company.views import *
from resume.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", dashboard,name="dashboard"),
    path("login", login_user,name="login"),
    path("logout", logout_user,name="logout"),
    path("register_applicant", register_applicant,name="register_applicant"),
    path("register_recruiter", register_recruiter,name="register_recruiter"),
    path("update_company", update_company,name="update_company"),
    path("company_details/<int:pk>", company_details,name="company_details"),
    path("update_resume", update_resume,name="update_resume"),
    path("resume_details/<int:pk>", resume_details,name="resume_details"),
    path("create_job/", create_job,name="create_job"),
    path("update_job/<int:pk>", update_job,name="update_job"),
    path("job_details/<int:id>", job_details,name="job_details"),
    path("manage_jobs/", manage_jobs,name="manage_jobs"),
    path("applyjob/<int:id>", applyjob,name="applyjob"),
    path("all_applicants/<int:id>", all_applicants,name="all_applicants"),
]
