from .models import LeaveApplication
from rest_framework import serializers

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=LeaveApplication
        fields=['start_date', 'end_date', 'reason', 'status', 'student', 'leave_approver']