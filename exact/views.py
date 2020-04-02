from django.shortcuts import render

# Create your views here.


def assign_exeat(request):
    return render(request, 'exact/exeat.html')


def view_exeat(request):
    return render(request, 'exact/view_exeat.html')


def manage_exeat(request):
    return render(request, 'exact/manage_exeat.html')
