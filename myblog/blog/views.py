from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Blog, Blogger
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.forms import addBlogForm
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogCreate(CreateView):
    model = Blog
    fields=['title','content','category','blogger','img']

class BlogUpdate(UpdateView):
    model = Blog
    fields =['title','content','category','blogger','img']

class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')

class BloggerCreate(CreateView):
    model = Blogger
    fields = ['first_name', 'last_name', 'bio']
    

class BloggerUpdate(UpdateView):
    model = Blogger
    fields = '__all__' # Not recommended (potential security issue if more fields added)


class BloggerDelete(DeleteView):
    model = Blogger
    success_url = reverse_lazy('blogger')

# Create your views here.
@login_required
def addBlog(request):
    #counting number of records
    pk=Blog.objects.count()+1
    blog_object=Blog(title=" New",pk=pk)
    #blog_object = get_object_or_404(Blog,pk=pk)
    print(blog_object.title)
    #print(blog_object.category)
    form = addBlogForm(request.POST or request.GET)

    if request.method == 'POST' and form.is_valid():
        #print(form)
        blog_object.title = form.cleaned_data['title_v']
        blog_object.content = form.cleaned_data['content_v']
        #blog_object.category = form.cleaned_data['category_v']
        blog_object.save()

        return HttpResponseRedirect(reverse('blogs') )

    else:
        print("In else")
        #form = addBlogForm()

    context = {
        'form': form,
        'blog_object': blog_object,
    }

    return render(request, 'blog/addBlog.html', context) 
#Will implement the edit blog option later





def index(request):
    num_blogs = Blog.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    model = Blog
    paginate_by = 5
    queryset = Blog.objects.filter()

    context ={
        'num_blogs':num_blogs,
        'num_bloggers':num_bloggers,
        'num_visits':num_visits,
        'home_list':queryset
    }

    return render(request, 'index.html', context=context)

def newadmin(request):
    model = Blog
    paginate_by = 5
    blogquery = Blog.objects.filter()
    queryset = Blogger.objects.filter()
    context = {'blog_list':blogquery,'blogger_list':queryset} 
    return render(request,'blog/admin_list.html',context=context)

class AdminView(LoginRequiredMixin,generic.ListView):
    model = Blog
    paginate_by = 5
    context_object_name = 'blogger_list' 
    queryset = Blogger.objects.filter() # Get 5 books containing the title war
    template_name = 'blog/admin_list.html'

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5
    context_object_name = 'blog_list'   # your own name for the list as a template variable
    queryset = Blog.objects.filter() # Get 5 books containing the title war
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
