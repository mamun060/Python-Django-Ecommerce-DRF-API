from django.shortcuts import redirect , render
from backend.models import Blog , Comment
from backend.forms import CommentForm


def blogs(request):
    allblogs = Blog.objects.select_related('author').all()
    return render(request, 'frontend/blogs.html', {
        'blogs': allblogs
    })

def blog_details(request , slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    comments = Comment.objects.filter(post=blog).order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create a comment but don't commit to the database yet
            comment = comment_form.save(commit=False)
            # Link the comment to the blog post
            comment.post = blog
            # Now save the comment with the associated blog post
            comment.save()
            comment_form = CommentForm()
        
    return render(request, 'frontend/blog-details.html', {
        'blog': blog,
        'comment_form': comment_form,
        'comments': comments,
    })