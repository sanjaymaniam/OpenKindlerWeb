from django.contrib import admin
from .models import Clipping, Book

     
class ClippingAdmin(admin.ModelAdmin):
    list_display= ('id', 'message', 'book', 'location', 'starred', 'kind_of_clipping')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'number_of_clippings', 'exceeded_number_of_clippings', 'rating', 'isbn', 'imageURL')
    
admin.site.register(Clipping, ClippingAdmin)
admin.site.register(Book, BookAdmin)