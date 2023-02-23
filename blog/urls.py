
from django.urls import path
from blog.views import contact, homepage,category,my_articles

urlpatterns = [ 
    path('',homepage,name='homepage'),
    path('iletisim',contact,name='contact'),
    path('category/<slug:categorySlug>',category,name="category"),
    path('my_articles',my_articles,name="my_articles"),
]
