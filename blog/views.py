from django.core import paginator
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView

def post_list(request) :
    object_list = Post.objects_published.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')

    try :
        posts = paginator.page(page)
    
    except PageNotAnInteger :
        posts = paginator.page(1)

    except EmptyPage :
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts': posts })


def post_detail(request, year, month, day, slug) :
    post = get_object_or_404(Post, status='published', slug=slug, publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'blog/post/detail.html', {'post': post })

class PostListView(ListView) :
    queryset = Post.objects_published.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = 'blog/post/list.html'