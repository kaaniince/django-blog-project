
from django.urls import path
from blog.views import contact, homepage,category,my_articles,detail,add_article,update_article,delete_article

urlpatterns = [ 
    path('',homepage,name='homepage'),
    path('iletisim',contact,name='contact'),
    path('category/<slug:categorySlug>',category,name="category"),
    path('my_articles',my_articles,name="my_articles"),
    path('add_article',add_article,name="add_article"),
    path('detail/<slug:slug>',detail,name="detail"),
    path('delete_article/<slug:slug>',delete_article,name="delete_article"),
    path('update_article/<slug:slug>',update_article,name="update_article"),
    
]
