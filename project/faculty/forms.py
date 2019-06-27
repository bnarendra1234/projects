from django import forms
from .models import book
class fdp_conduct_form(forms.Form):
     empid=forms.IntegerField()
     fdp_topic=forms.CharField()
     resource_person=forms.CharField()
     pno=forms.IntegerField()
     venue=forms.CharField()
     email=forms.EmailField()
     no_of_faculty_participated=forms.IntegerField()
     no_of_days=forms.IntegerField()
class fdp_attended_form(forms.Form):
     empid=forms.IntegerField()
     empname=forms.CharField()
     attended_on_topic=forms.CharField()
     resource_person=forms.CharField()
     venue=forms.CharField()
     no_of_days=forms.IntegerField()
class faculty_od(forms.Form):
     empid=forms.IntegerField()
     empname=forms.CharField()
     od_purpose=forms.CharField()
     venue=forms.CharField()
     no_of_days=forms.IntegerField()
class download_fdpcf(forms.Form):
     empid=forms.IntegerField()
class BookForm(forms.ModelForm):
     class Meta:
         model=book
         fields={'title','author','pdf'}
class nptelform(forms.Form):
     empid=forms.IntegerField()
     empname=forms.CharField()
     coursename=forms.CharField()
     percent=forms.FloatField()

