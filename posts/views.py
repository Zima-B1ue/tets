from django.shortcuts import render
from posts.models import Post, Comment


# Create your views here.


def function_hello(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def post_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context = {
            'posts': posts
        }

        return render(request, 'posts/posts.html', context=context)


def post_detail_veiw(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)

        context = {
            'post': post,
            'comments': post.comment_set.all()
        }

        return render(request, 'posts/detail.html', context=context)
