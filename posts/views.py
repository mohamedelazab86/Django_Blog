from django.shortcuts import render,redirect
from .models import Post
from .forms import Postform

# Create your views here.
def post_list(request):
    post_list=Post.objects.all()
    context={'post_list':post_list}
    return render(request,'posts/post_list.html',context)
def post_details(request,pk):
    post=Post.objects.get(id=pk)
    context={'post':post}
    return render(request,'posts/post_detail.html',context)
def create_post(request):
    if request.method=='POST':
        post=Postform(request.POST,request.FILES)
        if post.is_valid():
            my_post=post.save(commit=False)
            my_post.author=request.user
            my_post.save()
            return redirect('/posts/')
    else:
        post=Postform()

    
    context={'post':post}
    return render(request,'posts/create_post.html',context)



def update_post(request,pk):
    post=Post.objects.get(id=pk)
    if request.method=='POST':
        post=Postform(request.POST,request.FILES,instance=post)
        if post.is_valid():
            my_post=post.save(commit=False)
            my_post.author=request.user
            my_post.save()
            return redirect('/posts/')
    else:
        post=Postform(instance=post)
    context={'post':post}
    return render(request,'posts/edit_post.html',context)
def delete_post(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')

