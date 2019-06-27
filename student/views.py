from django.shortcuts import render
import csv,io
from student.forms import st_up_form as suf
from student.forms import st_do_form as sdf
from student.forms import st_rm_form as sef
from student.models import sd
from student.models import up
from student.models import Contact
from django.http import HttpResponse 
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from django.shortcuts import render,redirect
from .forms import BookForm,Deal
from .models import book
#from docx import Document
#import docx
import os
def upload(r):
	if r.method=='POST':
		f=suf(r.POST)
		if f.is_valid():
			c=f.cleaned_data
			m=sd(rno=c['rno'],name=c['name'],phno=c['pno'],email=c['email'])
			m.save()
			return HttpResponse("<h3>Thank You</h3>")
	else:
		f=suf()
	return render(r,'student/upload.html',{'f':f})
 
def download(r):
	err="";m=""
	if r.method=='POST':
		s=sdf(r.POST)
		if s.is_valid():
			c=s.cleaned_data
			m=sd.objects.filter(rno=c['rno'])
			if len(m)==0:
				err="No such Number"
	else:
		s=sdf()
	return render(r,'student/download.html',{'f':s,'rs':m,'err':err})
def z(r):
	err=""
	if r.method=='POST':
		f=sef(r.POST)
		if f.is_valid():
			c=f.cleaned_data
			m=sd.objects.filter(rno=c['rno'])
			if len(m)==0:
				err="No such size"
			else:
				m.delete()
	else:
		f=sef()
	return render(r,'student/mcqs.html',{'f':f,'err':err})
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print(myfile.name)
        print(myfile.size)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'student/fileupload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'student/fileupload.html')

def contact_upload(request):
    template = "student/up.html"

    prompt = {
        'order': "Order of csv should be first_name, last_name, email, ip_address, message"
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This file is not a .csv file")

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Contact.objects.update_or_create(
            first_name=column[0],
            last_name=column[1],
            email=column[2],
            ip_address=column[3],
            message=column[4]
        )

    context = {}
    return render(request, template, context)

# Create your views here.
def book_list(request):
    books=book.objects.all()
    return render(request,'student/book_list.html',{'books':books})

def upload_book(request):
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('book_list')
    else:
        form=BookForm()
        return render(request,'student/upload_book.html',{'form':form})
def deal_file(request):
    wordDoc=''
    if request.method=='POST':
        f=Deal(request.POST,request.FILES)
        myfile=request.POST.get('myfile',False)
        print(myfile.name)

        if f.is_valid():
            f.save()
            c=os.getcwd()
            wordDoc = docx.Document(c+'/new.docx')
            for table in wordDoc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        print(cell.text)
        else:
            f=Deal()
            return render(request,'student/deal_file.html',{'f':f,'wordDoc':wordDoc })