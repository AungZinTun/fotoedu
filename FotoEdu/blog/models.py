from django.db import models
from django.utils.text import slugify
import datetime
# Create your models here.
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name=models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return '%s' % self.name


class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=225, blank=True, null=True )
    photo=models.ImageField(upload_to='static/img/', blank=True, null=True)
    time_to_read=models.DurationField(blank=True, null=True)
    description=RichTextUploadingField(blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.SlugField(default='', blank=True)
    created_at=models.DateTimeField(auto_now_add=True )
    updated_at=models.DateTimeField(auto_now=True)

    def save(self):
        self.slug=slugify(self.title)
        super(Post, self).save()
    def __str__(self):
        return '%s' % self.title
