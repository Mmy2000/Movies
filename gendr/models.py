from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify 
from taggit.managers import TaggableManager





class All(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='all/')
    image2 = models.ImageField( upload_to='all/')
    rate = models.FloatField(default=0)
    like = models.ManyToManyField(User , blank=True)
    description = models.TextField(max_length=10000)
    quality = models.CharField(max_length=100)
    age_group = models.CharField(max_length=100)
    category = models.ForeignKey('Category',related_name='all_category',on_delete=models.CASCADE)
    tags = TaggableManager()
    language = models.ForeignKey('Language',related_name='all_category',null=True,blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField( default=timezone.now)
    slug = models.SlugField(null=True,blank=True)
    time = models.CharField( max_length=50)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(All,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("all:all_detail", kwargs={"slug": self.slug})
    


class AllImages(models.Model):
    property = models.ForeignKey(All,related_name='all_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='allimages/')

    def __str__(self):
        return str(self.property)
    

class Category(models.Model):
    name = models.CharField(max_length=60)
    icons = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name

    

class Language(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

