from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from django.views import View
from .models import Post,Answer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .form import PostForm, AnswerForm
# Create your views here.




class PostListView(View):
    
    def get(self,request):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'index.html', context)
    
 
 
    
class GetPostAnswerView(View):
    
    def get(self,request,id):
        
        anserws= Answer.objects.filter(post_id=id).order_by('-id')
        posts = Post.objects.all()
        context = {
            'posts': posts,
            'selected_post_id': int(id),
            'anserws':anserws
        }
        return render(request, 'index.html', context)    


@method_decorator(login_required, name='dispatch')    
class CreatePost(CreateView):
    
    model = Post
    form_class = PostForm  
    template_name = 'create_post.html'
    
    success_url = '/'  # Redirect to post list after successful creation
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request  # Pass the request to the form's __init__
        return kwargs
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user here before saving
        return super().form_valid(form)
    
    
     
@method_decorator(login_required, name='dispatch')    
class AddPostAnswerView(CreateView):
    
    model = Answer
    form_class = AnswerForm  
    template_name = 'add_answer.html'
    
    success_url = '/'  
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request  
        return kwargs
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        post_id=Post.objects.get(id=self.kwargs['post_id'])
        form.instance.post = post_id   # Set the post  here before saving
        return super().form_valid(form)    
    
    def get_context_data(self, **kwargs):
        
        data=super().get_context_data(**kwargs)
        post_id=Post.objects.get(id=self.kwargs['post_id'])
        data['post_id']=post_id
        return data
        
        
