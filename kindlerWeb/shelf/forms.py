from django.forms import ModelForm
from shelf.models import Clipping, Book

class ClippingForm(ModelForm):
    class Meta:
        model = Clipping
        fields = ['message', 'kind_of_clipping', 'location', 'starred', ]

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'rating', 'isbn', 'imageURL']