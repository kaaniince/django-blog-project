from django.db import models
from blog.models import ArticlesModel
class CommentModel(models.Model):
    writer= models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE,related_name='comment')
    text=models.ForeignKey(ArticlesModel,on_delete=models.CASCADE,related_name='comments')
    comment=models.TextField()
    creation_date=models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='comment'
        verbose_name='Comment'
        verbose_name_plural='Comments'
    
    def __str__(self):
        return self.writer.username