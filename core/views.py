from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def admin(request):
    return render(request, 'admin-page.html', {})