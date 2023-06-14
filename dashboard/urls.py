from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('student_details',views.student_details,name='student_details'),
    path('new_student',views.new_student,name='new_student'),
    path('staff',views.staff,name='staff'),
    path('staff_register',views.staff_register,name='staff_register'),
    path('search_student',views.search_student,name = 'search_student'),
    path('course_add',views.course_add,name='course_add'),
    path('course_details',views.course_details,name = 'course_details'),
    path('course_update/<int:id>/',views.course_update,name = 'course_update'),
    path('course_delete/<int:id>/',views.course_delete,name='course_delete'),
    path('das_login',views.das_login,name='das_login'),
    path('stud_profile/<int:pid>/', views.stud_profile, name='stud_profile'),
    path('staff_profile/<int:sid>/', views.staff_profile, name='staff_profile'),
    path('student_delete/<int:did>/', views.student_delete, name='student_delete'),
    path('student_update/<int:uid>/', views.student_update, name='student_update'),
    path('staff_delete/<int:sdid>/', views.staff_delete, name='staff_delete'),
    path('staff_update/<int:suid>/', views.staff_update, name='staff_update')
]