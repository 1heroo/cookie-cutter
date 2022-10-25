from django.shortcuts import render
from blog.models import Category, Post, Comment
from .forms import CommentForm
from django.views.generic import ListView, FormView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse


class BlogListView(ListView):
    model = Post
    template_name: str = "blog_index.html"
    context_object_name = 'posts'


class BlogCategoryView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog_category.html'


    def get_queryset(self):
        return Post.objects.filter(categories__name__contains=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context


class BlogDetailView(FormView, DetailView):
    model = Post
    form_class = CommentForm
    template_name = "blog_detail.html"
    pk_url_kwarg: str = 'pk'

    def post(self, request, pk, *args, **kwargs):
        form = CommentForm(request.POST)
        post = self.get_object()
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        post = self.get_object()
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=post)
        context['post'] = post
        return context


    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.kwargs['pk']})
