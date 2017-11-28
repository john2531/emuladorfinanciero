from django.shortcuts import render,redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.utils import timezone
from .forms import PostForm
from datetime import datetime
from .models import Post

# Create your views here.

def post_list(request):
    return render_to_response("post_list.html", {
        'time':datetime.now(),
        }, context_instance=RequestContext(request))

def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):

        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post_detail.html', {'post': post})

def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'post_edit.html', {'form': form})

def post_delete(request, pk):
    post = Post.objects.get(pk = pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog.views.post_list')
    return render(request, 'post_delete.html', {'post': post})


def main(request):
	entrada = Post.objects.all().order_by("-published_date")
	paginator = Paginator(entrada,4)

	try: pagina = int(request.GET.get("page","1"))
	except ValueError: pagina = 1
		
	try:
		entrada = paginator.page(pagina)
	except (InvalidPage, EmptyPage):
		entrada = Paginator.page(Paginator.num_pages)

	return render_to_response("post_list.html",dict(post=entrada))

