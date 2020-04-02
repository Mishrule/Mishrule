from django.shortcuts import render

# Create your views here.


def staff_Registration(request):
    return render(request, 'staff/staff_registration.html')


def staff_Profile(request):
    return render(request, 'staff/staff_profile.html')


def staff_Management(request):
    return render(request, 'staff/staff_management.html')
