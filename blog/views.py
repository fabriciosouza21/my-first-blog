from django.shortcuts import render,get_object_or_404,redirect
from .models import post
from django.utils import timezone
from .forms import PostForm

def post_list(request):
    posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts' : posts})


def post_detail(request, pk):
    get_post=get_object_or_404(post, pk=pk)
    return render(request,'blog/post_detail.html',{'post':get_post})

def post_new (request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post_ = form.save(commit=False)
            post_.author = request.user
            post_.published_date = timezone.now()
            post_.save()
            return redirect("post_detail",pk=post_.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_edit.html",{"form":form})  
def post_edit(request, pk):
    post_ = get_object_or_404(post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post_)
        if form.is_valid():
            post_ = form.save(commit=False)
            post_.author = request.user
            post_.published_date = timezone.now()
            post_.save()
            return redirect('post_detail', pk=post_.pk)
    else:
        form = PostForm(instance=post_)
    return render(request, 'blog/post_edit.html', {'form': form})

    
