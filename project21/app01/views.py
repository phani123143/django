from django.shortcuts import render
from app01.models import Employee

# Create your views here.

def showIndex(request):
    return render(request,'index.html')

def registerPage(request):
    return render(request,'register.html')

def loginPage(request):
    return render(request,'index.html')

def saveDetails(request):
    idno=request.POST.get('idno')
    name=request.POST.get('name')
    contact=request.POST.get('contact')
    salary=request.POST.get('salary')
    username=request.POST.get('username')
    password=request.POST.get('password')
    emp=Employee(idno=idno,name=name,contact=contact,salary=salary,username=username,password=password)
    emp.save()
    return render(request,'register.html',{'message':'Registered Details Successfully'})

def loginchuck(request):
    uname=request.POST.get('username')
    upass=request.POST.get('password')
    result=Employee.objects.filter(username=uname,password=upass)
    if result:
        print('valid')
        result=Employee.objects.get(username=uname)
        return render(request,'welcome.html',{'emp':result})
    else:
        print('In-Valid')
        return render(request,'index.html',{'message':'Invalid User'})

def viewProfile(request):
    username=request.GET.get('uname')
    result=Employee.objects.get(username=username)
    return render(request,'welcome.html',{'profile':result,'emp':result})

def deleteProfile(request):
    username=request.GET.get('uname')
    result=Employee.objects.get(username=username)
    return render(request,'welcome.html',{'delete':result,'emp':result})

def delete(request):
    options=request.POST.get('a')
    username=request.POST.get('uname')
    if options == 'Yes':
        Employee.objects.filter(username=username).delete()
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def updateProfile(request):
    username=request.GET.get('uname')
    result=Employee.objects.get(username=username)
    return render(request,'welcome.html',{'update':result,'emp':result})

def updateDetails(request):
    idno=request.POST.get('idno')
    name=request.POST.get('name')
    contact=request.POST.get('contact')
    salary=request.POST.get('salary')
    username=request.POST.get('username')
    password=request.POST.get('password')
    e=Employee(idno=idno,name=name,contact=contact,salary=salary,username=username,password=password)
    e.save()
    return render(request,'welcome.html',{'profile':e,'emp':e})
