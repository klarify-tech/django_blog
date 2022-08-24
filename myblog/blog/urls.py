from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addblog/', views.addBlog, name='addBlog'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogs/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogger/',views.BloggerListView.as_view(), name='blogger'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('blogger/create/', views.BloggerCreate.as_view(), name='blogger-create'),
    path('blogger/<int:pk>/update/', views.BloggerUpdate.as_view(), name='blogger-update'),
    path('blogger/<int:pk>/delete/', views.BloggerDelete.as_view(), name='blogger-delete'),
    path('create/', views.BlogCreate.as_view(), name='blog-create'),
    path('<int:pk>/updateblog/', views.BlogUpdate.as_view(), name='blog-update'),
    path('<int:pk>/deleteblog/', views.BlogDelete.as_view(), name='blog-delete'),
    

]