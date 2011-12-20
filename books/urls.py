import dselector


parser = dselector.Parser()
url = parser.url

urlpatterns = parser.patterns('zaxis.books.views',
    url(r'books/', 'list', {}, 'books_list'),
    url(r'books/{book_id:digits}/', 'view', {}, 'books_view'),
)
