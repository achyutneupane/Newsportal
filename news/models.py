from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class MainMenu(models.Model):
    created_at = models.DateField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=0)
    image = models.ImageField(blank=True, upload_to='news')
    description = RichTextField()
    page_visit = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class SubMenu(models.Model):
    created_at = models.DateField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=0)
    image = models.ImageField(blank=True, upload_to='news')
    description = RichTextField()
    page_visit = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Blog(models.Model):
    created_at = models.DateField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE, blank=True)
    sub_menu = models.ForeignKey(SubMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=0)
    image = models.ImageField(blank=True, upload_to='news')
    description = RichTextField()
    page_visit = models.IntegerField(default=0)
    tags = TaggableManager()

    def __str__(self):
        return self.title