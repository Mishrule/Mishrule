from django.shortcuts import render
# from student.forms import StudentRegistration

# Create your views here.


def student(request):
    # form = StudentRegistration()
    return render(request, 'student/student.html', )


def student_profile(request):
    return render(request, 'student/student_profile.html')


def student_manage(request):
    return render(request, 'student/student_manage.html')
