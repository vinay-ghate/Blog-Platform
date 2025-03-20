from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Post
import datetime

# Create your views here.

def index(request):
    return render(request, 'posts.html')

def addPost(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(title=str(title), text=str(content), date=datetime.datetime.now())
        # return HttpResponse(f'Post added: {title} and id is {post.id}')
        return redirect('/posts/')
    else:
        posts = Post.objects.all().values()
        return render(request, 'Addposts.html', {'posts': posts})
    
def getPost(request):
    if request.method == 'GET':
        posts = Post.objects.all().values()
        return render(request, 'posts.html', {'posts': posts[::-1]})
    else:
        return HttpResponse('Invalid request method')


