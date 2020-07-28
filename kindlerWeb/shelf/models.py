from django.db import models, IntegrityError
from django.forms import ModelForm
from taggit.managers import TaggableManager
import isbnlib

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    isbn = models.IntegerField(null=True)
    imageURL = models.URLField(default="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Placeholder_book.svg/792px-Placeholder_book.svg.png")
    exceeded_number_of_clippings = models.IntegerField(default=0)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
    def number_of_clippings(self):
        "Returns number of clippings for this book."
        return len(self.clipping_set.all())
    
    def count_exceeded_number_of_clippings(self):
        self.exceeded_number_of_clippings += 1
        self.save()

    def setMetadata(self):
        try:
            self.isbn = isbnlib.isbn_from_words(f"{self.title+self.author}")
            self.save()
            try:
                self.imageURL = isbnlib.cover(self.isbn)['thumbnail']
                self.save()
            except KeyError as coverError:
                print(f"cover error -> {self.title}")
        except (IndexError, TypeError, UnboundLocalError) as isbnError:
            print(f"isbn error -> {self.title}")

class Clipping(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
    kind_of_clipping_choices = [
        ('Highlight', 'Highlight'),
        ('Note', 'Note'),
        ('Bookmark', 'Bookmark'),
    ]
    kind_of_clipping = models.CharField(
        max_length=10,
        choices=kind_of_clipping_choices,
        default='Highlight',
    )

    location = models.CharField(max_length=20, blank=True)
    message = models.TextField(unique=True, default='')
    starred = models.BooleanField(default=False)
    tags = TaggableManager()

    def __str__(self):
        return self.message

    @classmethod
    def getClippingsFromFile(cls, path_to_file):
        "Create instance of Clipping for every clipping in file."
        from . import kindler
        from timeit import default_timer as timer

        units = kindler.getUnits(path_to_file)
        count, total_number_of_clippings = 0, len(units)
        start = timer()
        repeat_count = 0

        for title, author, kind_of_clipping, location, message in kindler.getUnits(path_to_file):
            count += 1
            print(f"processing clipping {count} of {total_number_of_clippings}. time: {timer()-start}")
            try:
                book = Book.objects.get(title=title)
            except Book.DoesNotExist:
                book = Book.objects.create(title=title, author=author)
                book.setMetadata()
            if '<You have reached the clipping limit for this item>' in message:
                book.count_exceeded_number_of_clippings()
            else:
                try:
                    Clipping(book=book, kind_of_clipping=kind_of_clipping, location=location, message=message).save()
                except IntegrityError: #clipping is not unique.
                    continue
        print(f'processed {total_number_of_clippings} clippings in {timer()-start} seconds.')