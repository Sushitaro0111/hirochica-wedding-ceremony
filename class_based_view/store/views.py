from ast import Delete
from datetime import datetime
from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import (
  View, RedirectView
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin

from . import forms
from .models import Books



class IndexView(View):

  def get(self, request, *args, **kwargs):
    book_form = forms.BookForm()
    return render(request, 'about.html', context={
      'book_form': book_form,
    })

  def post(self, request, *args, **kwargs):
    book_form = forms.BookForm(request.POST or None)
    if book_form.is_valid():
      book_form.save()
    return render(request, 'about.html', context={
      'book_form': book_form,
    })

class BookDetailView(DetailView):
  model = Books
  template_name = 'book.html'

class BookListView(ListView):
  model = Books
  template_name = 'book_list.html'
  
  def get_queryset(self):
    qs = super(BookListView, self).get_queryset()
    if 'name' in self.kwargs:
      qs = qs.filter(name__startswith=self.kwargs['name'])
    qs = qs.order_by('description')
    return qs


class BookCreateView(CreateView):
  model = Books
  # fields = ['name', 'type_name', 'description', 'price', 'mail', 'image']
  form_class = forms.BookForm
  template_name = 'book_form.html'

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   # picture_form = forms.PictureUploadForm()
  #   # form_class = forms.BookForm
  #   # context['pictures'] = pictures
  #   # context['picture_form'] = picture_form
  #   return context

  def form_valid(self, form):
    form.instance.create_at = datetime.now()
    form.instance.update_at = datetime.now()
    print(form.cleaned_data)
    return super().form_valid(form)

        #   """仮登録と本登録メールの送信"""
        #   user = forms.PictureUploadForm()
        #   user.is_active = False

        #   image = Image.open(user.picture)
        #   cropped_image = image.crop((x, y, w+x, h+y))
        #   resized_image = cropped_image.resize((800, 600), Image.ANTIALIAS)
        #   resized_image.save(user.image.path)
          
        #   user.save()



        #   picture_form = forms.PictureUploadForm()
        #   print(self.get_object())
        #   book = self.get_object()
        #   picture_form.save(book=book)
        #   return super(BookCreateView, self).form_valid(form)

    # ↓をコメント解除すると動くようになる
    # picture_form = forms.BookForm(request.POST or None, request.FILES or None)
    # if picture_form.is_valid() and request.FILES:
    #   print(self.get_object())
    #   book = self.get_object()
    #   picture_form.save(book=book)
    # return super(BookCreateView, self).form_valid(form)

  # def get_initial(self, **kwargs):
  #   initial = super(BookCreateView, self).get_initial(**kwargs)
  #   initial['name'] = 'sample'
  #   return initial

class BookUpdateView(SuccessMessageMixin, UpdateView):
  template_name = 'book_update.html'
  model = Books
  form_class = forms.BookUpdateForm
  success_message = '更新に成功しました。'

  def get_success_url(self):
    print(self.object)
    return reverse_lazy('store:book_update', kwargs={'pk': self.object.id})

  def get_success_message(self, cleaned_data):
    print(cleaned_data)
    return cleaned_data.get('name') + 'を更新しました。'

  def post(self, request, *args, **kwargs):
    form = forms.BookUpdateForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.FILES:
      print(self.get_object())
      book = self.get_object()
      form.save(book=book)
    return super(BookUpdateView, self).post(request, *args, **kwargs)

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   picture_form = forms.PictureUploadForm()
  #   pictures = Pictures.objects.filter_by_book(book=self.object)
  #   context['pictures'] = pictures
  #   context['picture_form'] = picture_form
  #   return context

  # def post(self, request, *args, **kwargs):
  #   picture_form = forms.PictureUploadForm(request.POST or None, request.FILES or None)
  #   if picture_form.is_valid() and request.FILES:
  #     print(self.get_object())
  #     book = self.get_object()
  #     picture_form.save(book=book)
  #   return super(BookUpdateView, self).post(request, *args, **kwargs)

class BookDeleteView(DeleteView):
  model = Books
  template_name = 'book_delete.html'
  success_url = reverse_lazy('store:book_list')

class BookFormView(FormView):
  # model = Books
  template_name = 'book_form.html'
  form_class=forms.BookForm
  success_url = reverse_lazy('store:book_list')

  def form_valid(self, form):
    if form.is_valid():
      form.save()
      return super(BookFormView, self).form_valid(form)

class BookRedirectView(RedirectView):
  url = 'https://google.co.jp'

  def get_redirect_url(self, *args, **kwargs):
    book = Books.objects.first()
    if 'pk' in kwargs:
        return reverse_lazy('store:book_detail', kwargs={'pk':kwargs['pk']})

    return reverse_lazy('store:book_update', kwargs={'pk': book.pk})

