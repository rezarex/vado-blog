from django.shortcuts import render

def index(request):
    return render(request, 'blogapp/index.html')

def create_blog(request):
    return render(request, 'blogapp/create-blog')
