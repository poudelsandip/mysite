from blog.models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    return render_to_response('blog/index.html', {}, context_instance=RequestContext(request))

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = post.categories.all()
    return render_to_response('blog/view_post.html', {
        'post': post,
        'categories':categories,
        'post_full_url':request.build_absolute_uri(post.get_absolute_url())
    }, context_instance=RequestContext(request))

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/index.html', {
        'category': category,
        'recent_posts': Post.objects.filter(is_published=True).filter(categories=category).order_by('-published_date')[:5]
    })

#hardcode the slug here, which should always be "about"
def about_blog(request):
    post = get_object_or_404(Post, slug="about")
    return render_to_response('blog/about.html', {'post':post})

