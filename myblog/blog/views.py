from django.shortcuts import render
from .models import Category, Blog, Blogger
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    num_blogs = Blog.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    #user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')
    #user.first_name = 'Test'
    #user.last_name = 'User'
    #user.save()

    context ={
        'num_blogs':num_blogs,
        'num_bloggers':num_bloggers,
        'num_visits':num_visits,
    }

    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = Blog
    #paginate_by = 2
    context_object_name = 'blog_list'   # your own name for the list as a template variable
    queryset = Blog.objects.filter()[:5] # Get 5 books containing the title war
    template_name = 'blog/blog_list.html'

class BloggerListView(generic.ListView):
    model = Blogger
    #paginate_by =10
    context_object_name = 'blogger_list'
    queryset = Blogger.objects.filter()
    template_name ='blogger/blogger_list.html'

class BlogDetailView(generic.DetailView):
    model = Blog
    def blog_detail_view(request, primary_key):
        blog = get_object_or_404(Blog, pk=primary_key)
        return render(request, 'blog/blog_detail.html', context={'blog': blog})

class BloggerDetailView(generic.DetailView):
    model = Blogger
    template_name ='blogger/blogger_detail.html'
    def blogger_detail_view(request, primary_key):
        blogger = get_object_or_404(Blogger, pk=primary_key)
        return render(request, 'blogger/blogger_detail.html', context={'blogger': blogger})
