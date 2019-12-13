from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')#first page

def month(request):
    return render(request, 'mainApp/month.html')
