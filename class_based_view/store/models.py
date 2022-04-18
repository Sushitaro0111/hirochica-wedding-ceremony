from ast import Delete
from random import choices
from django import forms
from django.db import models
from django.urls import reverse_lazy

CHOICES_TUPLE = [
    ('新郎', '新郎'),
    ('新婦', '新婦'),
    ('両方', '両方'),
]

# Create your models here.
class BaseModel(models.Model):
  create_at = models.DateTimeField()
  update_at = models.DateTimeField()

  class Meta:
    abstract = True

class Books(BaseModel):

  name = models.CharField(verbose_name="氏名", max_length=255)
  description = models.TextField(verbose_name="メッセージ本文")
  price = models.IntegerField(verbose_name="（仮）")
  type_name = models.TextField(verbose_name="宛先")
  mail = models.EmailField(verbose_name="メールアドレス ※こちらの入力は任意です", null=True, blank=True)
  image = models.ImageField(upload_to='picture/', verbose_name='イメージ画像', null=True, blank=True)

  class Meta:
    db_table = 'books'
    
  def get_absolute_url(self):
    return reverse_lazy('store:book_detail', kwargs={'pk':self.pk})


# class PicturesManager(models.Manager):
#   def filter_by_book(self, book):
#     return self.filter(book=book).all()

# class Pictures(BaseModel):

#   picture = models.FileField(upload_to='picture/')
#   book = models.ForeignKey(
#     'books', on_delete=models.CASCADE
#   )
#   objects = PicturesManager()
