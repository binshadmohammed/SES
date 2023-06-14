
from django.shortcuts import render,HttpResponsePermanentRedirect,redirect
from . models import *
from .form import StudentApplicationForm
from django.views import View
from datetime import datetime
from .models import StudentApplication,Notification
from django.utils import timezone
def student_register(request):
    delete_notifications()
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            # form.save()
            
            student_application = form.save()
            current_time = datetime.now()
            notification = Notification(student=student_application,time=current_time)
            notification.save()
            return HttpResponsePermanentRedirect('/')
        else:
            return render(request,'application.html',{'form':form})
    else:
        form = StudentApplicationForm()
        return render(request,'application.html',{'form':form})

def delete_notifications():
    two_day_ago = timezone.now() - timezone.timedelta(days=2)
    Notification.objects.filter(time__lt=two_day_ago).delete()
    
def student_login(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None and user.is_superuser:
    #         login(request, user)
    #         return redirect('dashboard')
    #     else:
    #         return render(request, 'profile/st_profile.html',{'error_message': 'Invalid credentials!'})
    # else:
    return render(request, 'profile/st_profile.html')


class RegisterForm:
    pass


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})

def student_profile(request):
    return render(request, 'student_profile.html')