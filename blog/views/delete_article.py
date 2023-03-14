from django.contrib.auth.decorators import login_required
from blog.models import ArticlesModel
from django.shortcuts import get_object_or_404,redirect 
@login_required(login_url='/')
def delete_article(request,slug):
    get_object_or_404(ArticlesModel,slug=slug,author=request.user).delete()
    return redirect("my_articles")