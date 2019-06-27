from django.conf.urls import url
from faculty.views import uploadfdpcf,uploadfdpaf,uploadfod,downloadfdpcf,downloadfdpaf,downloadfod,upload_nptel,deletefdpcf,deletefdpaf,deletefod
from faculty.views import book_list,upload_book
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
url(r'^uploadfdpcf/$',uploadfdpcf,name='uploadfdpcf'),
url(r'^uploadfdpaf/$',uploadfdpaf,name='uploadfdpaf'),
url(r'^uploadfod/$',uploadfod,name='uploadfod'),
url(r'^downloadfdpcf/$',downloadfdpcf,name='downloadfdpcf'),
url(r'^downloadfdpaf/$',downloadfdpaf,name='downloadfdpaf'),
url(r'^downloadfod/$',downloadfod,name='downloadfod'),
url(r'^deletefdpcf/$',deletefdpcf,name='deletefdpcf'),
url(r'^deletefdpaf/$',deletefdpaf,name='deletefdpaf'),
url(r'^deletefod/$',deletefod,name='deletefod'),
url(r'^books/$',book_list,name='book_list'),
url(r'^books/upload/$',upload_book,name='upload_book'),
url(r'^nptelfaculty/$',upload_nptel,name='upload_nptel')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
