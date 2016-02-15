from django.shortcuts import render
from django.shortcuts import redirect
from isapptoyou.blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.template import RequestContext


from .forms import AddBlogForm, AddGoalForm
from .models import Blog, Goal
# Create your views here.

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all(),
        'goals': Goal.objects.all()
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)
    })

def view_goal(request, slug):   
    return render_to_response('view_goal.html', {
        'goal': get_object_or_404(Goal, slug=slug)
    })

def post_new(request):
    if request.method == 'POST':
        form = AddBlogForm(request.POST)
        if form.is_valid():
            #post = form.save(commit=False)
            form.author = request.user
            form.published_date = timezone.now()
            post = form.save()
            return redirect('isapptoyou.blog.views.index')
    else:
        form = AddBlogForm()

    return render(request, 'blog/edit_post.html', {'form': form})

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = AddBlogForm(request.POST, instance=post)
        if form.is_valid():
            #post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('isapptoyou.blog.views.view_post', pk=post.pk)
    else:
        form = AddBlogForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

def edit_goal(request):
    if request.method == 'POST':
        form = AddGoalForm(request.POST)
        if form.is_valid():
            #post = form.save(commit=False)
            post = form.save()
            return redirect('isapptoyou.blog.views.index')
    else:
        form = AddGoalForm()

    return render(request, 'blog/edit_goal.html', {'form': form})