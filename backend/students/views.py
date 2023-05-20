from django.shortcuts import render, redirect, HttpResponse
from .forms import StudentRegistrationForm
from .backends import StudentBackend
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from leavemanagement.models import LeaveApplication

from .models import Student
from rest_framework import generics
from .serializers import StudentSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


from leavemanagement.serializers import LeaveSerializer
# Create your views here.


class StudentRegistrationView(generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentLoginView(ObtainAuthToken):
    serializer_class=StudentSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response ({'token': token.key})

class LeaveCreateView(generics.CreateAPIView):
    queryset=LeaveApplication.objects.all()
    serializer_class=LeaveSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class LeaveListAPIView(generics.ListAPIView):
    serializer_class=LeaveSerializer

    def get_queryset(self):
        user=self.request.user
        return LeaveApplication.objects.filter(student=user)


def student_dashboard(request):
    leave_applications = request.user.leave_applications.all()
    return render(request, 'student_dashboard.html', {'leave_applications': leave_applications})




#@login_required
def student_home(request):

    context={
        'username':request.user.username
    }
    return render(request, 'student_home.html', context)



'''def register_student(request):
    if request.method=='POST':
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:student_home')
        
    else:
            form=StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form})
'''
'''class StudentLoginView(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True
    success_url='home/'
'''
'''class StudentLoginView(LoginView):
    authentication_backend = StudentBackend
    template_name = 'student_login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('students:student_dashboard')


class StudentLogoutView(LogoutView):
    template_name='student_logout.html'

    
def apply_leave(request):
    if request.method == 'POST':
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        reason=request.POST['reason']
        student=request.user

        leave_application=LeaveApplication(
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            student=student,
        )
        leave_application.save()
        messages.success(request, 'Leave application submitted successfully.')
        return redirect('students:student_dashboard')
    else:
        return render(request, 'apply_leave.html')

'''