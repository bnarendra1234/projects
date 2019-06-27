from django.db import models
# Create your models here.
class fdp_conduct_form(models.Model):
	empid=models.IntegerField()
	fdp_topic=models.CharField(max_length=100)
	resource_person=models.CharField(max_length=100)
	pno=models.IntegerField()
	venue=models.CharField(max_length=100)
	email=models.EmailField()
	no_of_faculty_participated=models.IntegerField()
	no_of_days=models.IntegerField()
	
class fdp_attended_form(models.Model):
	empid=models.IntegerField()
	empname=models.CharField(max_length=30)
	attended_on_topic=models.CharField(max_length=100)
	resource_person=models.CharField(max_length=100)
	venue=models.CharField(max_length=100)
	no_of_days=models.IntegerField()
    
class faculty_od(models.Model):
	empid=models.IntegerField()
	empname=models.CharField(max_length=30)
	od_purpose=models.CharField(max_length=100)
	venue=models.CharField(max_length=100)
	no_of_days=models.IntegerField()
class book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.title
class nptelfaculty(models.Model):
	empid=models.IntegerField()
	empname=models.CharField(max_length=50)
	coursename=models.CharField(max_length=100)
	percent=models.IntegerField()