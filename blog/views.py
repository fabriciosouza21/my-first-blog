from django.shortcuts import render,get_object_or_404
from .models import post
from django.utils import timezone

def post_list(request):
    posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts' : posts})

def post_detail(request, pk):
    get_post=get_object_or_404(post, pk=pk)
    return render(request,'blog/post_detail.html',{'post':get_post})