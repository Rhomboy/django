from django.urls import path
from . import views
urlpatterns = [
    #path("", views.starting_page, name="starting-page"),
   # path("posts/", views.posts_page, name="posts-page"),
    path("posts/<slug:slug>", views.PostView.as_view(), name="post-detail"),
    path("all-posts/", views.All_PostsView.as_view(), name="posts-page"),
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("read-later", views.ReadLater.as_view(), name="read-later")

]
