from django.shortcuts import render
from blog.models import ArticlesModel
from django.core.paginator import Paginator
from django.db.models import Q
def homepage(request):
    query=request.GET.get('query')
    articles=ArticlesModel.objects.order_by('-id')
    if query:
        articles=articles.filter(
            Q(header__icontains=query) | Q(content__icontains=query)
        ).distinct()
    
    page=request.GET.get('page')
    paginator=Paginator(articles,1)
    
    return render(request,'pages/homepage.html',context={
        'articles':paginator.get_page(page)
    })