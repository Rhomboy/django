from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    def __str__(self):
      return self.caption
  #  featured_posts = models.
class Author(models.Model):
 first_name = models.CharField(max_length=100)
 last_name = models.CharField(max_length=100)
 email_address = models.EmailField(max_length=30)
 def get_fullname(self):
   return f"{self.first_name} {self.last_name}"
 def __str__(self):
   return self.get_fullname()
class Post(models.Model):
 profile_pic = models.ImageField(upload_to="posts", null=True)
 title = models.CharField(max_length=100)
 excerpt = models.CharField(max_length=200) # some words describing the post
 slug = models.SlugField(unique=True)
 date = models.DateField(auto_now=True)
 content = models.TextField(validators=[MinLengthValidator(10)])
 author = models.ForeignKey(Author, on_delete=models.SET_NULL, null = True, related_name="posts")
 tags = models.ManyToManyField(Tag, related_name="tags")
 def __str__(self):
   return f"{self.title}"
class Comment(models.Model):
  writer = models.CharField(max_length=40)
  content = models.CharField(max_length=100)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

      
