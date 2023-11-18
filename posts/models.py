from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _


'''
* models .Model
   -  html widget
   - validations
   -  best for database  ()
  
'''
# Create your models here.
class Post(models.Model):                # create table (post)
    title=models.CharField(max_length=100,verbose_name=_('title_post'))
    content=models.TextField(max_length=1000,verbose_name=_('content_post'))
    draft=models.BooleanField(default=True)

    publish_date=models.DateTimeField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField(upload_to='photo')
    tags = TaggableManager()
    category=models.ForeignKey('Category',on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.title
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_author')
    content=models.TextField(max_length=500)
    publish_date=models.DateTimeField(auto_now=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment_post')

    def __str__(self):
        return str(self.post)
    
