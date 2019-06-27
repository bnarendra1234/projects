from django.db import models


class sd(models.Model):
	rno=models.IntegerField()
	name=models.CharField(max_length=30)
	phno=models.IntegerField()
	email=models.EmailField()

class td(models.Model):
	rno=models.IntegerField()
	name=models.CharField(max_length=30)
	pno=models.IntegerField()
	email=models.EmailField()
'''class foo(models.Model):
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)'''
class up(models.Model):
	upload = models.FileField(upload_to='uploads/')

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    ip_address = models.GenericIPAddressField(null=True)
    message = models.TextField()

    def __str__(self):
        return {f  : "{self.first_name} {self.last_name}"}
class book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.title


















'''class DealModel(models.Model):
    title=models.CharField(max_length=30)
    pdf=models.FileField()
'''