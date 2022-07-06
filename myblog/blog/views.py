from django.shortcuts import render
from .models import Category, Blog, Blogger
from django.views import generic
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    num_blogs = Blog.objects.all().count()
    num_bloggers = Blogger.objects.all().count()

    context ={
        'num_blogs':num_blogs,
        'num_bloggers':num_bloggers,
    }

    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blog_list'   # your own name for the list as a template variable
    queryset = Blog.objects.filter()[:5] # Get 5 books containing the title war
    template_name = 'blog/blog_list.html'

class BlogDetailView(generic.DetailView):
    model = Blog
    def book_detail_view(request, primary_key):
        blog = get_object_or_404(Blog, pk=primary_key)
        return render(request, 'catalog/blog_detail.html', context={'blog': blog})
