from django.shortcuts import render

# Create your views here.


def parent_info(request):
    return render(request, 'parents/parents.html')
