from django import forms
from django.forms import ModelForm
from blog.models import Blog
from django.core.exceptions import ValidationError


class addBlogForm(forms.Form):
    title_v = forms.CharField(max_length=15,empty_value="Add Title")
    category_v = forms.CharField(max_length=15)
    content_v = forms.CharField()

    def clean_title_v(self):
        data = self.cleaned_data['title_v']
        return data
    def clean_category_v(self):
        data = self.cleaned_data['category_v']
        return data
    def clean_content_v(self):
        data = self.cleaned_data['content_v']
        return data
    