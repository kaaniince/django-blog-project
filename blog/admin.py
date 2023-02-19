from django.contrib import admin
from blog.models import (CategoryModel,ArticlesModel,CommentModel,ContactModel)


admin.site.register(CategoryModel)

@admin.register(ArticlesModel)

class ArticlesAdmin(admin.ModelAdmin):
    search_fields=('header','content')
    list_display=('header','creation_date','edit_date')


@admin.register(CommentModel)

class CommentAdmin(admin.ModelAdmin):
    list_display=('writer','creation_date','edit_date')
    search_fields=('writer__username',)

@admin.register(ContactModel)

class ContactAdmin(admin.ModelAdmin):
    list_display=('email','creation_date','edit_date')
    search_fields=('email',)

