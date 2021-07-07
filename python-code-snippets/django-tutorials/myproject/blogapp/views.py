from django.shortcuts import render
from django.http import HttpResponse
#note . in import means relative path
from .models import Blog

# Create your views here.
def blogs(request):
    count = Blog.objects.count()
    html = f"Total number of blog post: {count}"
    return HttpResponse(html)


def posts(request, index):
    i = int(index)
    blog  = Blog.objects.all()[i]
    title = blog.title
    content = blog.content
    timestamp = blog.timestamp
    
    html = f"""
<h1>{title } | <strong>{ timestamp }</strong></h1>
</hr>
<p>{ content }</p>

            """
    return HttpResponse(html)