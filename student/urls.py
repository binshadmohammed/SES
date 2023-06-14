from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_register,name='student_register'),
    path('student_login',views.student_login,name='student_login'),
    path('student_profile',views.student_profile,name='student_profile'),
    path('delete_notifications',views.delete_notifications,name='delete_notifications'),
]