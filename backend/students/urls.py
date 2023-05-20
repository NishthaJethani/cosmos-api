from django.urls import path
from .views import StudentRegistrationView, StudentLoginView, LeaveCreateView, LeaveListAPIView
app_name = 'students'

urlpatterns=[
    path('register_student/', StudentRegistrationView.as_view(), name="register_student"),
    #path('student_home/', views.student_home, name='student_home'),
    path('student_login/', StudentLoginView.as_view(), name='student_login'),
    #path('student_logout/', views.StudentLogoutView.as_view(), name='student_logout'),
    path('apply_leave/', LeaveCreateView.as_view(), name='apply_leave'),
    path('leave/list/', LeaveListAPIView.as_view(), name= 'leave_list'),
    #path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
]