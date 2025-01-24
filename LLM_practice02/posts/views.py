from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    ordering = ['-created_at']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy('posts:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse('accounts:login')}?next={request.path}")

        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect('posts:post_detail', pk=self.object.pk)

        return self.get(request, *args, **kwargs)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy('posts:post_list')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post_list')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    
    def form_valid(self, form):
        self.object.delete()
        return HttpResponseRedirect(self.success_url)


class PostLikeToggleView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        
        if not request.user.is_authenticated:
            login_url = f"{reverse_lazy('accounts:login')}?next={reverse_lazy('posts:post_detail', kwargs={'pk': pk})}"
            return redirect(login_url)

        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return redirect('posts:post_detail', pk=pk)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "posts/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object.post
        return context

    def form_valid(self, form):
        self.object = form.save()
        return redirect('posts:post_detail', pk=self.object.post.pk)

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        try:
            post = self.object.post
            return reverse_lazy('posts:post_detail', kwargs={'pk': post.pk})
        except AttributeError:
            return reverse_lazy('posts:post_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
