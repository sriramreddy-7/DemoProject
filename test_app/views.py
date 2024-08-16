from django.shortcuts import render,redirect
from test_app.models import Student,Jobs
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
# Create your views here.


def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        htno=request.POST.get('htno')
        year=request.POST.get('year')
        branch=request.POST.get('branch')
        std=Student.objects.create(name=name,hallticket_no=htno,year=year,branch=branch)
        std.save()
        # except:
        #     return HttpResponse("<h1>500 Data Storing Error</h1>")
        print(name,htno,year,branch)
        return redirect('index')
    student_data=Student.objects.all()
    # print(type(student_data))
    context={
            'student_data':student_data,
        }
    return render(request, 'index.html',context)

def update(request,id):
    std=Student.objects.get(pk=id)
    context={
        "std":std,
    }
    if request.method=="POST":
        name=request.POST.get('name')
        htno=request.POST.get('htno')
        year=request.POST.get('year')
        branch=request.POST.get('branch')
        std.name=name
        std.hallticket_no=htno
        std.year=year
        std.branch=branch
        std.save()
        return redirect('index')
    return render(request,'update_data.html',context)


def delete(request,id):
    std=Student.objects.get(pk=id)
    std.delete()
    return redirect('index')
    
    
def index2(request):
    return render(request, 'index2.html')


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("<h1>Invalid Credentials</h1>")
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def user_signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.create_user(username=username,password=password)
        user.save()
        return redirect('login')
    return render(request,'signup.html')



def post_job(request):
    if request.method=="POST":
        job_title=request.POST.get('job_title')
        job_description=request.POST.get('job_description')
        job_location=request.POST.get('job_location')
        job_salary=request.POST.get('job_salary')
        job_type=request.POST.get('job_type')
        job_url=request.POST.get('job_url')
        job=Jobs.objects.create(job_title=job_title,job_description=job_description,job_location=job_location,job_salary=job_salary,job_type=job_type,link=job_url)
        job.save()
        print(type(job))
        return redirect('post_job')
    jobs=Jobs.objects.all()
    context={
        'jobs':jobs,
    }
    return render(request,'post_job.html',context)