from django.db.models import Count

from annoying.decorators import render_to

from books.models import Book


@render_to('books/list.html')
def list(request):
    return {'books': Book.objects.filter(user=request.user).annotate(num_authors=Count('authors')).order_by('num_authors')}


@render_to('books/view.html')
def view(request, book_id):
    return {'book': Book.objects.get(pk=book_id)}
