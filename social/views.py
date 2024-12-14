from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Post, Comment
from .forms import PostForm, CommentForm

@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'social/post_list.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('social:post_list'))
    else:
        form = PostForm()
    return render(request, 'social/create_post.html', {'form': form})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(reverse('social:post_detail', kwargs={'post_id': post_id}))
    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post).order_by('created_at')

    liked = post.likes.filter(id=request.user.id).exists()

    return render(request, 'social/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
        'liked': liked
    })

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(reverse('social:post_detail', kwargs={'post_id': post_id}))
