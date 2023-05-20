from django.urls import path
from .views import WardenRegistrationView, WardenLoginView, LeaveApprovalView, LeaveListAPIView
app_name = 'wardens'


urlpatterns=[
    path("register_warden/", WardenRegistrationView.as_view(), name="register_warden"),
    path('approve_leave/<int:leave_id>/', LeaveApprovalView.as_view(), name='approve_leave'),
    #path('warden_dashboard/', views.warden_dashboard, name='warden_dashboard'),
    #path("warden_home/", views.warden_home, name='warden_home'),
    path('warden_login/', WardenLoginView.as_view(), name='warden_login'),
    #path('warden_logout/', views.WardenLogoutView.as_view(), name='warden_logout'),
    path('leaves/', LeaveListAPIView.as_view(), name='leaves_list'),
]