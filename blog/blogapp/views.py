from django.shortcuts import render
from .forms import BlogForm
from .models import Blog
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def get_showing_blogs(request, blog):
    
    if request.GET and request.GET.get('filter'):
        if request.GET.get('filter')=='active':
            return blog.filter(is_active=True)
        if request.GET.get('filter')=='inactive':
            return blog.filter(is_active=False)
    return blog


def index(request):
    #blog = Blog.objects.all()
    blog = Blog.objects.filter(owner = request.user)


    #filter querysets
    active_count = blog.filter(is_active = True).count()
    inactive_count = blog.filter(is_active = False).count()
    total_count = blog.count()
    #context = {'blog':[]} #--simulate no content
    context = {
        'blog':get_showing_blogs(request, blog),
          'active_count':active_count,
            'inactive_count':inactive_count,
            'total_count':total_count,
            }

    return render(request, 'blogapp/index.html', context)

@login_required
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
        blog.owner = request.user
        blog.save()

        messages.add_message(request, messages.SUCCESS, "Blog Created Successfully" )

        return HttpResponseRedirect(reverse("blog-detail", kwargs={'id': blog.pk}))


    return render(request, 'blogapp/create-blog.html', context)



def blog_detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    context = {'blog' : blog}

    return render(request, 'blogapp/blog-detail.html', context)


def blog_delete(request, id):
    blog = get_object_or_404(Blog, pk=id)
    context = {'blog' : blog}

    if request.method == 'POST':
        blog.delete()
        messages.add_message(request, messages.SUCCESS, "Blog Deleted Successfully" )
        return HttpResponseRedirect(reverse('home'))


    return render(request, 'blogapp/blog-delete.html', context)


def blog_edit(request, id):
    blog = get_object_or_404(Blog, pk=id)
    form = BlogForm(instance=blog)
    context = {'blog' : blog, 'form':form}

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        is_active = request.POST.get('is_active',False)

        blog.title = title
        blog.body = body
        blog.is_active = True if is_active=="on" else False

        blog.save()

        messages.add_message(request, messages.SUCCESS, "Blog Updated Successfully" )

        return HttpResponseRedirect(reverse("blog-detail", kwargs={'id': blog.pk}))
    
    return render(request, 'blogapp/blog-edit.html', context)

