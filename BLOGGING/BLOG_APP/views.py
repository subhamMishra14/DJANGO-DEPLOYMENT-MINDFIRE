from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from BLOG_APP.models import Post,Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from BLOG_APP.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

class AboutView(TemplateView):
    template_name='about.html'

class PostListView(ListView):
    model=Post
    #Now get the post from post table using DJANGO ORM
    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')# - is for desc

class PostDetailView(DetailView):
    model=Post

class CreatePostView(LoginRequiredMixin, CreateView):
#Now we need to implement a methon Login Required...Unless u login you can't create post
#To implement it we need to use another class LOGGING
#THE BELOW ATTRIBUTES ARE REQUIRED FOR
    login_url='/login/'
    redirect_field_name='BLOG_APP/post_detail.html'
    form_class=PostForm
    model=Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='BLOG_APP/post_detail.html'
    form_class=PostForm
    model=Post

class PostDeleteView(DeleteView):
    model=Post
    #where should it will go after u delete
    #But you dont want success url to activate unless you delete it
    #So reverse Lazy comes into picture
    success_url=reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='BLOG_APP/post_list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('create_date')


#-------------------------------------------------------------------------------------------------#
@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'BLOG_APP/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comments,pk=pk)
    comment.approve() #check models.py
    return redirect('post_detail',pk=comment.post.pk)#as comment is linked to a post for redirect we need pk of that post

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comments,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post.pk)
