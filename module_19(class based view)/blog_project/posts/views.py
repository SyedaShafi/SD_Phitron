from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . forms import PostForm, CommentForm
from . models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator

# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('add_post')
    else:
        post_form = PostForm()
    return render(request, 'add_posts.html', {'form': post_form})


# add post using class based view
@method_decorator(login_required, name = 'dispatch')
class addPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_posts.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def edit_post(request, id):
    post = Post.objects.get(pk = id)
    # print(post.id)
    post_form = PostForm(instance = post)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance = post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('homepage')
    
    return render(request, 'add_posts.html', {'form': post_form})



# update post using class based view
class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'add_posts.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')






@login_required
def delete_post(request, id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect('homepage')


# delete post uisng class based view
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


class DetailPostView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'


        
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
        