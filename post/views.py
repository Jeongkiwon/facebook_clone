from django.views.generic import ListView, TemplateView
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from post.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main.views import LoginRequiredMixin
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.

#--- ListView
def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'post/post.html', context)

def user_detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    posts = Post.objects.filter(owner=user)
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'user_detail.html', context)

def my_post_list(request):
    posts = Post.objects.filter(owner=request.user)
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'post/my_post.html', context)

def user_post_list(request):
    posts = Post.objects.filter(owner=user)
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'post/my_post.html', context)

#--- FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'post/post_search.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content','photo']
    success_url = reverse_lazy('post:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView) :
    model = Post
    fields = ['content', 'photo']
    success_url = reverse_lazy('post:index')

class PostDeleteView(LoginRequiredMixin, DeleteView) :
    model = Post
    success_url = reverse_lazy('post:index')


def comment_create(request, post_pk):
    # 요청 메서드가 POST방식 일 때만 처리
    if request.method == 'POST':
        # Post인스턴스를 가져오거나 404 Response를 돌려줌
        post = get_object_or_404(Post, pk=post_pk)
        # request.POST에서 'content'키의 값을 가져옴
        content = request.POST.get('content')

        # 'content'키가 없었거나 내용이 입력되지 않았을 경우
        if not content:
            # 400(BadRequest)로 응답을 전송
            return HttpResponse('댓글 내용을 입력하세요', status=400)

        # 내용이 전달 된 경우, Comment객체를 생성 및 DB에 저장
        Comment.objects.create(
            post=post,
            # 작성자는 현재 요청의 사용자로 지정
            owner=request.user,
            content=content
        )
        # 정상적으로 Comment가 생성된 후
        # 'post'네임스페이스를 가진 url의 'post_list'이름에 해당하는 뷰로 이동
        return redirect('post:index')

def my_comment_create(request, post_pk):
    # 요청 메서드가 POST방식 일 때만 처리
    if request.method == 'POST':
        # Post인스턴스를 가져오거나 404 Response를 돌려줌
        post = get_object_or_404(Post, pk=post_pk)
        # request.POST에서 'content'키의 값을 가져옴
        content = request.POST.get('content')

        # 'content'키가 없었거나 내용이 입력되지 않았을 경우
        if not content:
            # 400(BadRequest)로 응답을 전송
            return HttpResponse('댓글 내용을 입력하세요', status=400)

        # 내용이 전달 된 경우, Comment객체를 생성 및 DB에 저장
        Comment.objects.create(
            post=post,
            # 작성자는 현재 요청의 사용자로 지정
            owner=request.user,
            content=content
        )
        # 정상적으로 Comment가 생성된 후
        # 'post'네임스페이스를 가진 url의 'post_list'이름에 해당하는 뷰로 이동
        return redirect('post:my_post')