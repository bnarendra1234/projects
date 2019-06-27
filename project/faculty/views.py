from django.shortcuts import render,redirect
from django.http import HttpResponse
from faculty.forms import fdp_conduct_form as fdpcf
from faculty.forms import fdp_attended_form as fdpaf
from faculty.forms import faculty_od as fod
from faculty.forms import download_fdpcf as dfdpcf
from faculty.models import fdp_conduct_form,fdp_attended_form,faculty_od
from faculty.forms import BookForm,nptelform
from faculty.models import book,nptelfaculty
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.
def uploadfdpcf(request):
	if request.method=='POST':
		f=fdpcf(request.POST)
		if f.is_valid():
			c=f.cleaned_data
			m=fdp_conduct_form(empid=c['empid'],fdp_topic=c['fdp_topic'],resource_person=c['resource_person'],pno=c['pno'],venue=c['venue'],email=c['email'],no_of_faculty_participated=c['no_of_faculty_participated'],no_of_days=c['no_of_days'])
			m.save()
			return HttpResponse("<h3>Thank you</h3>")
	else:
		f=fdpcf()
	return render(request,'faculty/uploadfdpcf.html',{'f':f})

def uploadfdpaf(request):
	if request.method=='POST':
		f=fdpaf(request.POST)
		if f.is_valid():
			c=f.cleaned_data
			m=fdp_attended_form(empid=c['empid'],empname=c['empname'],attended_on_topic=c['attended_on_topic'],resource_person=c['resource_person'],venue=c['venue'],no_of_days=c['no_of_days'])
			m.save()
			return HttpResponse("<h3>Thank you</h3>")
	else:
		f=fdpaf()
	return render(request,'faculty/uploadfdpcf.html',{'f':f})

def uploadfod(request):
	if request.method=='POST':
		f=fod(request.POST)
		if f.is_valid():
			c=f.cleaned_data
			m=faculty_od (empid=c['empid'],empname=c['empname'],od_purpose=c['od_purpose'],venue=c['venue'],no_of_days=c['no_of_days'])
			m.save()
			return HttpResponse("<h3>Thank you</h3>")
	else:
		f=fod()
	return render(request,'faculty/uploadfdpcf.html',{'f':f})
def downloadfdpcf(request):
	err="";m=""
	if request.method=='POST':
		s=dfdpcf(request.POST)
		if s.is_valid():
			c=s.cleaned_data
			m=fdp_conduct_form.objects.filter(empid=c['empid'])
			if len(m)==0:
				err="No such number"
	else:
		s=dfdpcf()
	return render(request,'faculty/downloadfdpcf.html',{'f':s,'rs':m,'err':err})
def downloadfdpaf(request):
	err="";m=""
	if request.method=='POST':
		s=dfdpcf(request.POST)
		if s.is_valid():
			c=s.cleaned_data
			m=fdp_attended_form.objects.filter(empid=c['empid'])
			if len(m)==0:
				err="No such number"
	else:
		s=dfdpcf()
	return render(request,'faculty/downloadfdpaf.html',{'f':s,'rs':m,'err':err})
def downloadfod(request):
	err="";m=""
	if request.method=='POST':
		s=dfdpcf(request.POST)
		if s.is_valid():
			c=s.cleaned_data
			m=faculty_od.objects.filter(empid=c['empid'])
			if len(m)==0:
				err="No such number"
	else:
		s=dfdpcf()
	return render(request,'faculty/downloadfod.html',{'f':s,'rs':m,'err':err})
def deletefdpcf(request):
	err="";m=""
	if request.method=='POST':
		s=dfdpcf(request.POST)
		if s.is_valid():
			c=s.cleaned_data
			m=fdp_conduct_form.objects.filter(empid=c['empid'])

			if len(m)==0:
				err="No such number"
			else:
				m.delete()
				return HttpResponse("<h1>deleted successfully</h1>")
	else:
		s=dfdpcf()
	return render(request,'faculty/delete.html',{'f':s,'rs':m,'err':err})
def deletefdpaf(request):
	err="";m=""
	if request.method=='POST':
		s=dfdpcf(request.POST)
		if s.is_valid():
			c=s.cleaned_data
			m=fdp_attended_form.objects.filter(empid=c['empid'])

			if len(m)==0:
				err="No such number"
			else:
				m.delete()
				return HttpResponse("<h1>deleted successfully</h1>")
	else:
		s=dfdpcf()
	return render(request,'faculty/delete.html',{'f':s,'rs':m,'err':err})
def deletefod(request):
	err="";m=""
	if request.method=='POST':
		s=dfdpcf(request.POST)
		if s.is_valid():
			c=s.cleaned_data
			m=faculty_od.objects.filter(empid=c['empid'])

			if len(m)==0:
				err="No such number"
			else:
				m.delete()
				return HttpResponse("<h1>deleted successfully</h1>")
	else:
		s=dfdpcf()
	return render(request,'faculty/delete.html',{'f':s,'rs':m,'err':err})
def book_list(request):
    books=book.objects.all()
    return render(request,'faculty/book_list.html',{'books':books})

def upload_book(request):
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('book_list')
    else:
        form=BookForm()
        return render(request,'faculty/upload_book.html',{'form':form})
def upload_nptel(request):
	
	if request.method=='POST':
		f=nptelform(request.POST,request.FILES)
		if f.is_valid():
			c=f.cleaned_data
			m=nptelfaculty(empid=c['empid'],empname=c['empname'],coursename=c['coursename'],percent=c['percent'])
			m.save()
			return render(request,'faculty/thanku.html')
	else:
		f=nptelform()
	return render(request,'faculty/uploadnptel.html',{'f':f})