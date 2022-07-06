from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,help_text= "Enter Category ex Marketing")

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    content = models.TextField(help_text=' Start writing your blog here')
    category = models.ManyToManyField('Category',help_text='Select a category')
    comments = models.TextField(help_text='Write your comment here')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)])


class Blogger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio=models.TextField('Write about yourself')

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}' 