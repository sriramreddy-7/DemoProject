from django.shortcuts import render,redirect
from test_app.models import Student
from django.http import HttpResponse

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
    