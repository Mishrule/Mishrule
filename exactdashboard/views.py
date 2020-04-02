from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, 'exactdashboard/dashboard.html')


def student(request):
    return render(request, 'exactdashboard/student.html')


def student_profile(request):
    return render(request, 'exactdashboard/student_profile.html')


def student_manage(request):
    return render(request, 'exactdashboard/student_manage.html')
