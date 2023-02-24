from django.shortcuts import render
from blog.models import Post
# Create your views here.


def blog(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/blog_posts.html', context)

def post_details(request, post_slug):
    selected_post = Post.objects.get(slug=post_slug)
    context = {'post':selected_post}
    return render(request,'blog/post_details.html', context)