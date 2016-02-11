from django.shortcuts import render
from django.shortcuts import redirect
from isapptoyou.blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.template import RequestContext


from .forms import AddForm
from .models import Blog
# Create your views here.

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()
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


def post_new(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            #post = form.save(commit=False)
            form.author = request.user
            form.published_date = timezone.now()
            post = form.save()
            return redirect('isapptoyou.blog.views.index')
    else:
        form = AddForm()

    return render(request, 'blog/post_edit.html', {'form': form})