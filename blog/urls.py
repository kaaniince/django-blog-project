
from django.urls import path
from blog.views import contact, homepage

urlpatterns = [ 
    path('',homepage),
    path('iletisim',contact),
]
