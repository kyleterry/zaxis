from django.contrib import admin

from books.models import Book, Author, PublishingCompany, BookType


class BookAdmin(admin.ModelAdmin):

    exclude = ('user',)

    def queryset(self, request):
        if request.user.is_superuser:
            return Book.objects.all()
        return Book.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(PublishingCompany)
admin.site.register(BookType)
