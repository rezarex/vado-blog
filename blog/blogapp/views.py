from django.shortcuts import render
from .forms import BlogForm
from .models import Blog
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    blog = Blog.objects.all()
    context = {'blog':blog}

    return render(request, 'blogapp/index.html', context)

def create_blog(request):
    form = BlogForm()
    context = {'form':form}

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        is_active = request.POST.get('is_active',False)


        blog = Blog()

        blog.title = title
        blog.body = body
        blog.is_active = True if is_active=="on" else False

        blog.save()


        return HttpResponseRedirect(reverse("blog-detail", kwargs={'id': blog.pk}))


    return render(request, 'blogapp/create-blog.html', context)



def blog_detail(request, id):
    return render(request, 'blogapp/blog-detail.html', {})
