from django.shortcuts import render
from django.http import HttpResponse
from .models import Clipping, Book
from .forms import ClippingForm, BookForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse


def book_list_view(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'book_list_page.html', context=context)


def book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    clippings = book.clipping_set.all()
    context = {'book': book, 'clippings': clippings}
    return render(request, 'book_view.html', context=context)


def edit_clipping(request, book_id, clipping_id):
    clipping = get_object_or_404(Clipping, id=clipping_id)
    form = ClippingForm(instance=clipping)
    if request.method == 'POST':
        form = ClippingForm(request.POST, instance=clipping)
        if form.is_valid():
            form.save()
            return redirect(reverse('shelf:book_view', args=(book_id, )))
    context = {'clipping': clipping, 'form': form}
    return render(request, 'edit_clipping_form.html', context)


def clipping_manager(request, book_id, clipping_id):
    if request.method == 'POST':
            clipping = get_object_or_404(Clipping, id=clipping_id)
            if 'delete-button' in request.POST:
                clipping.delete()
                # instead of redirecting, just update the same page
                return redirect(reverse('shelf:book_view', args=(book_id, )))
            elif 'star-button' in request.POST:
                clipping.starred = not clipping.starred
                clipping.save()
                return redirect(reverse('shelf:book_view', args=(book_id, )))
            elif 'edit-button' in request.POST:
                return redirect(reverse('shelf:edit_clipping', args=(book_id, clipping_id, )))


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=Book)
        if form.is_valid():
            form.save()
            return redirect(reverse('shelf:book_view', args=(book_id, )))
    context = {'book': book, 'form': form}
    return render(request, 'book_form.html', context=context)


def delete_book(request, book_id):
    return HttpResponse(f"You're trying to delete book #{book_id}")
