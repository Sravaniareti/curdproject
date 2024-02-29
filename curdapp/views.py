from django.shortcuts import render,redirect
from .models import StudentaData

def index(request):
    data=StudentaData.objects.all()

    return render(request,'index.html',{'data':data})


def studentdata(request):
    if request.method=='GET':
        return render(request,'studentdata.html')

    else:
        StudentaData(
        first_name=request.POST.get('fname'),
        last_name=request.POST.get('lname'),
        contact=request.POST.get('contact'),
        email=request.POST.get('email'),
        date=request.POST.get('date')
        ).save()
        return render(request,'studentdata.html')

def update_studentdata(request,id):
    row=StudentaData.objects.get(id=id)
    return render(request,'update_studentdata.html',{'row':row})

def updated_studentdata(request,id):
    data=StudentaData.objects.get(id=id)
    data.first_name=request.POST.get('fname')
    data.last_name=request.POST.get('lname')
    data.contact=request.POST.get('contact')
    data.email=request.POST.get('email')
    data.date=request.POST.get('date')
    data.save()
    return redirect('index')
def delete_studentdata(request,id):
    data=StudentaData.objects.get(id=id)
    data.delete()
    return redirect('index')
