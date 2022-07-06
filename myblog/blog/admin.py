from django.contrib import admin

from .models import Blog, Blogger,Category

# Register your models here.
admin.site.register(Blog)
admin.site.register(Blogger)
admin.site.register(Category)
