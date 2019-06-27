from django.conf.urls import url 
from student.views import upload,download,z,simple_upload,contact_upload
from student.views import book_list
from student.views import upload_book,deal_file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
url(r'^upload/$',upload,name='upload'),
url(r'^download/$',download,name='download'),
url(r'^z/$',z,name='mcqs'),
url(r'^res/$',simple_upload,name='fileupload'),
url(r'^upload-csv/$', contact_upload, name='contact_upload'),
url(r'^books/$',book_list,name='book_list'),
url(r'^books/upload/$',upload_book,name='upload_book'),

url(r'^deal/$',deal_file,name='deal_file'),
    #path('login/', login, name='login'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    
