from django import forms
from .models import book

class st_up_form(forms.Form):
	rno=forms.IntegerField()
	name=forms.CharField()
	pno=forms.IntegerField()
	email=forms.EmailField()
	#gender=forms.ChoiceField()
class st_do_form(forms.Form):
	rno=forms.IntegerField()
class st_rm_form(forms.Form):
    rno=forms.IntegerField()
class up_form(forms.Form):
	upload=forms.FileField()


class BookForm(forms.ModelForm):
     class Meta:
         model=book
         fields={'title','author','pdf'}



class Deal(forms.Form):
     title=forms.CharField(max_length=30)
     file=forms.FileField()
