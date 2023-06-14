from django.shortcuts import render,get_list_or_404,redirect,get_object_or_404
from staff.models import *
from student.form import StudentApplicationForm
from student.models import * 
from staff.form import TeacherForm
from django.shortcuts import render, HttpResponsePermanentRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . models import*
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(login_url='das_login')
def dashboard(request):
    notification= Notification.objects.all()
    context = {'notifications':notification}
    return render(request,'dashboard.html',context)



@login_required(login_url='das_login')
def student_details(request):
    student = StudentApplication.objects.all()
    query = request.GET.get('q')
    if query:
        student = StudentApplication.objects.filter(student_name__icontains = query) | \
                  StudentApplication.objects.filter(email__icontains=query)
    else:
        student = StudentApplication.objects.all()
    return render(request, 'das_student_details.html',{'student':student,'query':query})

@login_required(login_url='das_login')
def search_student():
    return render(request, '/')

@login_required(login_url='das_login')
def new_student(request):
    return render(request,'das_new_student.html')

@login_required(login_url='das_login')
def staff(request):
    staff = Teacher.objects.all()
    query = request.GET.get('q')
    if query:
        staff = Teacher.objects.filter(name__icontains = query) | \
        Teacher.objects.filter(email__icontains = query) 
    else:
        staff = Teacher.objects.all()
    return render(request,'das_staff.html',{'staff':staff,'query':query})

@login_required(login_url='das_login')
def staff_register(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect('staff_register')
        else:
            return render(request,'staff_register.html',{'form':form})
    else:
        form =  TeacherForm()
        return render(request,'staff_register.html',{'form':form})

@login_required(login_url='das_login')
def course_add(request):
    if request.method == "POST":
        course_name = request.POST['course_name']
        course_name = Course.objects.create(course_name=course_name)
        course_name.save()
        return redirect('course_add')
    else:
        return render(request,'course/course_add.html')
    
@login_required(login_url='das_login')
def course_details(request):
    course_details = Course.objects.all()
    return render(request, 'course/course_details.html',{'course_details':course_details})

@login_required(login_url='das_login')
def course_update(request,id):    
    course_details = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course_name = request.POST['course_name']
        course_details.course_name = course_name
        course_details.save()
        return redirect('course_details')
    return render(request, 'course/update_course.html', {'course_details': course_details})

@login_required(login_url='das_login')
def course_delete(request,id):
    course_delete = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course_delete.delete()
        return redirect('course_details')
    return redirect('course_details')

def das_login (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/dashboard_login/das_login.html',{'error_message': 'Invalid credentials!'})
    else:
        return render(request,'accounts/dashboard_login/das_login.html')


def stud_profile(request,pid):
    tab = StudentApplication.objects.filter(id=pid)
    return render(request, 'das_stud_profile.html', {'tab': tab})

def staff_profile(request,sid):
    staff = StudentApplication.objects.filter(id=sid)
    return render(request, 'das_staff_profile.html', {'staff': staff})

def student_delete(request,did):
    tab = StudentApplication.objects.filter(id=did)
    tab.delete()
    return redirect('student_details')

def student_update(request,uid):
    stud=StudentApplication.objects.get(id=uid)
    form=StudentApplicationForm(instance=stud)
    if request.method == 'POST':
        form=StudentApplicationForm(request.POST,request.FILES,instance=stud)
        if form.is_valid():
            form.save()
            return redirect('student_register')
    return render(request,"application.html",{'form':form})


def staff_delete(request,sdid):
    tabl = Teacher.objects.filter(id=sdid)
    tabl.delete()
    return redirect('staff')

def staff_update(request,suid):
    staf=Teacher.objects.get(id=suid)
    form=TeacherForm(instance=staf)
    if request.method == 'POST':
        form=TeacherForm(request.POST,request.FILES,instance=staf)
        if form.is_valid():
            form.save()
            return redirect('staff_register')
    return render(request,"staff_register.html",{'form':form})

