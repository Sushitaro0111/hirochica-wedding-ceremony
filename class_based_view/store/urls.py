from django.urls import URLPattern, path

from .views import (
  BookCreateView, BookDeleteView, BookRedirectView, IndexView, BookDetailView,
  BookListView, BookCreateView, BookUpdateView, BookFormView, BookRedirectView
)
from django.views.generic.base import RedirectView, TemplateView

app_name = 'store'

urlpatterns = [
  path('about/', IndexView.as_view(), name='about'),
  path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
  path('celemony_info/', TemplateView.as_view(template_name='celemony_info.html'), name='celemony_info'),
  path('book_detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
  path('book_list/', BookListView.as_view(), name='book_list'),
  path('book_list/<name>', BookListView.as_view(), name='book_list'),
  path('book_add/', BookCreateView.as_view(), name='book_add'),
  path('book_update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
  path('book_delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
  path('book_form/', BookFormView.as_view(), name='book_form'),
  path('google/', RedirectView.as_view(url='https://google.co.jp')),
  path('book_redirect_view/', BookRedirectView.as_view(), name='book_redirect_view'),
  path('book_redirect_view/<int:pk>', BookRedirectView.as_view(), name='book_redirect_view'),
]