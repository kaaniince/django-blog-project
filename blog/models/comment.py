from django.db import models
from blog.models import ArticlesModel
from blog.abstract_models import DateAbstractModel

class CommentModel(DateAbstractModel):
    writer= models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE,related_name='comment')
    text=models.ForeignKey(ArticlesModel,on_delete=models.CASCADE,related_name='comments')
    comment=models.TextField()

    
    class Meta:
        db_table='comment'
        verbose_name='Comment'
        verbose_name_plural='Comments'
    
    def __str__(self):
        return self.writer.username