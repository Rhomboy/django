from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Author, Post, Tag, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse
from .forms import NewComment
class StartingPageView(ListView):
    template_name = "blogs/starting_page.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "latest_posts"
    
    def get_queryset(self):
        query_set =  super().get_queryset()
        data = query_set[:3]
        return data
    
class All_PostsView(ListView):
    template_name = "blogs/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class PostView(View):
      def is_stored_for_later(self, request, post_id):
           stored_posts = request.session.get("stored_posts")
           is_saved_for_later = False
           if stored_posts is not None:
                   is_saved_for_later = post_id in stored_posts
           return is_saved_for_later
      def get(self, request, slug):
           post = Post.objects.get(slug=slug)
           comments = post.comments.all().order_by("-id")
           tags = post.tags.all()
           stored_posts = request.session.get("stored_posts")
       
           comment_form = NewComment()
           return render(request, "blogs/post-detail.html", {"comments": comments, "tags": tags, "post": post, "comment_form": comment_form, "is_saved_for_later": self.is_stored_for_later(request, post.id)})
      def post(self, request, slug):
           post = Post.objects.get(slug=slug)
           new_comment = NewComment(request.POST)
           comments = post.comments.all()
           tags = post.tags.all()
           if new_comment.is_valid():
                comment = new_comment.save(commit=False)
                comment.post = post
                comment.save()
                return HttpResponseRedirect(reverse("post-detail", args=[slug]))
           return render(request, "blogs/post-detail.html", {"comments": comments, "tags": tags, "post": post, "comment_form": new_comment})
class ReadLater(View):
 def get(self, request):
     stored_posts = request.session.get("stored_posts")
     context = {
             
         }
     if stored_posts is None or len(stored_posts) == 0:
         context["posts"] = []
         context["has_posts"] = False
     else:
         posts = Post.objects.filter(id__in=stored_posts)
         context["posts"] = posts
         context["has_posts"] = True
     return render(request, "blogs/stored_posts.html", context)


 
 def post(self, request):
    stored_posts = request.session.get("stored_posts")
    if stored_posts is None:
        stored_posts = []
    post_id = int(request.POST["post_id"])  # Use .get() instead of direct access
    if post_id not in stored_posts:
      stored_posts.append(post_id)
    else:
     stored_posts.remove(post_id)
    request.session["stored_posts"] = stored_posts
    return HttpResponseRedirect("/")

        
          
           
