from django.contrib import admin
from blog.models import (CategoryModel,ArticlesModel,CommentModel,ContactModel)


admin.site.register(CategoryModel)

class ArticlesAdmin(admin.ModelAdmin):
    search_fields=('header','content')
    list_display=('header','creation_date','edit_date')


admin.site.register(ArticlesModel,ArticlesAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('writer','creation_date','edit_date')
    search_fields=('writer__username',)

admin.site.register(CommentModel,CommentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('email','creation_date','edit_date')
    search_fields=('email',)

admin.site.register(ContactModel,ContactAdmin)