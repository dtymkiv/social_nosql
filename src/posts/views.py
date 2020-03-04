from django.shortcuts import render

# Create your views here.
from posts.PostService import PostService


def feed(request):
    if request.method == "GET":
        return render(request, 'feed.html', {"posts": PostService.get_all_posts()})
