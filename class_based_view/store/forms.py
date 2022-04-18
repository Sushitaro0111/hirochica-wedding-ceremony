from django import forms
from .models import Books
from datetime import datetime
from django.core.files.storage import default_storage


class BookForm(forms.ModelForm):


  class Meta:
    CHOICE =  (
        ('新郎', '新郎'),
        ('新婦', '新婦'),
        ('両方', '両方')
      )
    model = Books
    fields =  ['name', 'type_name', 'description', 'price', 'mail', 'image']
    widgets = {
      'mail': forms.TextInput(attrs={'placeholder': 'example@example.com'}),
      'name':forms.TextInput(attrs={'placeholder': '氏名'}),
      'type_name': forms.RadioSelect(choices=CHOICE)
    }
  
  def save(self, *args, **kwargs):
    obj = super(BookForm, self).save(commit=False)
    obj.create_at = datetime.now()
    obj.update_at = datetime.now()
    obj.save()
    return obj

class BookUpdateForm(forms.ModelForm):
   
  class Meta:
    model = Books
    fields = ['name', 'type_name', 'description', 'price', 'mail', 'image']
    widgets = {
      'name': forms.TextInput(attrs={'placeholder': 'example@xxx.com'})
    }
  
  def save(self):
    upload_file = self.cleaned_data['file']
    file_name = default_storage.save(upload_file.name, upload_file)
    obj = super(BookUpdateForm, self).save(commit=False)
    obj.update_at = datetime.now()
    obj.save()
    return obj

# class PictureUploadForm(forms.ModelForm):
#   picture = forms.FileField(required=False)

#   class Meta:
#     model = Pictures
#     fields = ['picture',]

#   def save(self, *args, **kwargs):
#     obj = super(PictureUploadForm, self).save(commit=False)
#     obj.create_at = datetime.now()
#     obj.update_at = datetime.now()
#     obj.book = kwargs['book']
#     obj.save()
#     return obj

    

class ChkForm(forms.ModelForm):
     model = Books
     labels = ['チェック','複数チェック','ラジオボタン','動的選択肢１','動的選択肢２']
     CHOICE = [
          ('1','選択肢＜１＞'),
          ('2','選択肢＜２＞'),
          ('3','選択肢＜３＞')]
     
     three = forms.MultipleChoiceField(
          label=labels[2],
          required=False,
          disabled=False,
          initial=['2'],
          choices=CHOICE,
          widget=forms.RadioSelect(attrs={
               'id': 'three','class': 'form-check-input'}))
    

  