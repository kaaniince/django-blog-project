from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class ArticlesModel(models.Model):
    image=models.ImageField(upload_to='text_images')
    header=models.CharField(max_length=50)
    content=RichTextField()
    creation_date=models.DateTimeField(auto_now_add=True)
    edit_date=models.DateTimeField(auto_now=True)
    slug= AutoSlugField(populate_from='header',unique=True)
    categories=models.ManyToManyField(CategoryModel, related_name="article")
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='articles')

    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"
        db_table="Article"
    def __str__(self):
        return self.header