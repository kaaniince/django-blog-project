from django.contrib import admin
from blog.models import CategoryModel,ArticlesModel


admin.site.register(CategoryModel)

class ArticlesAdmin(admin.ModelAdmin):
    search_fields=('header','content')
    list_display=('header','creation_date','edit_date')


admin.site.register(ArticlesModel,ArticlesAdmin)